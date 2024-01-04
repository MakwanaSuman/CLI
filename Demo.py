import csv
import hashlib
import click

@click.group
def mycommands():
    print("executing")
    pass

@click.command()
@click.option('--name', prompt='Enter your name', help='Your name to be added')
def hello(name):
    click.echo(f"hello {name}")

@click.command()
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option('-n', '--name', prompt='Enter name', help='The name of to do')
@click.option('-d', '--desc', prompt='Describe', help='Enter Description')
def add_intofile(name, desc, todofile):
    filename = todofile if todofile is not None else "myfile.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc}\n")

@click.command()
@click.argument('idx', type=int, required=True)
def delete_todo(idx):
    with open("myfile.txt", "r") as f:
        todo_list = f.read().splitlines()

    if 0 <= idx < len(todo_list):
        todo_list.pop(idx)

        with open("myfile.txt", "w") as f:
            f.write("\n".join(todo_list))
            f.write("\n")
    else:
        click.echo(f"Index {idx} is out of range.")

@click.command()
@click.argument("todofile", type=click.Path(exists=True), required=False)
def list_todos(todofile):
    filename = todofile if todofile is not None else "myfile.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()

    for idx, todo in enumerate(todo_list):
        print(f"({idx}) - {todo}")

@click.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False), required=False)
@click.option('-o', '--output-file', type=click.Path(), default='hashed_data.csv', help='Output CSV file')
@click.option('-c', '--column-index', type=int, help='Index of the column to hash (zero-based index)')
def hash_csv(input_file, output_file, column_index):
    # If input_file is not provided
    if not input_file:
        input_file = click.prompt('Enter the input CSV file path', type=click.Path(exists=True, dir_okay=False))

    # If column_index is not provided2
    if column_index is None:
        column_index = click.prompt('Enter the index of the column to hash (zero-based index)', type=int)

    # Read data from the input CSV file and compute SHA-256 
    hashed_data = []
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if column_index < len(row):
                original_data = row[column_index]
                hashed_value = hashlib.sha256(original_data.encode()).hexdigest()
                # hashed_data.append({'original_data': original_data, 'hashed_value': hashed_value})
                click.echo(f'Original Data: {original_data}, Hashed Value: {hashed_value}')
            else:
                click.echo(f"Invalid column index. The CSV row does not have a column at index {column_index}.")

    # # Write the original and hashed data to a new CSV file
    # with open(output_file, 'w', newline='') as csvfile:
    #     fieldnames = ['original_data', 'hashed_value']
    #     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     csvwriter.writeheader()
    #     csvwriter.writerows(hashed_data)


mycommands.add_command(hello)
mycommands.add_command(add_intofile)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)
mycommands.add_command(hash_csv)


if __name__ == '__main__':
    mycommands()


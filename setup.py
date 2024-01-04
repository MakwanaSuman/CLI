# from setuptools import setup, find_packages

# setup(
#     name='Demo',
#     version='1.0',
#     packages=find_packages(),
#     install_requires =[
#         'click'
#         ],
#     entry_points={
#         'console_scripts': [
#             'Demo = Demo:mycommands',
#         ],
#     },
# )

from setuptools import setup, find_packages

setup(
    name='your-cli-tool',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your-cli-command=yourmodule:cli_function',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Description of your CLI tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-cli-tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)


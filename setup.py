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
    name='Demo',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'Demo=Demo:mycommands',
        ],
    },
    author='Test',
    author_email='yl@logicode.in',
    description='Description of your CLI tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MakwanaSuman/CLI/tree/main',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)


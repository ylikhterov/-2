from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='my-todo',
    version='1.0',
    packages=['my_todo'],
    entry_points={
        'console_scripts':
            ['my-todo=my_todo.my_todo:main']
        }
)
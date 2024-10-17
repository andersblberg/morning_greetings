from setuptools import setup, find_packages

"""
Setup configuration for the Morning Greetings package.

Defines the package metadata, dependencies, and entry points for easy installation.

Attributes:
    name (str): The package name.
    version (str): The version of the package.
    packages (list): A list of all Python import packages that should be included.
    install_requires (list): A list of packages that are required for this package to work.
    entry_points (dict): Console scripts for running the main functionality.
    description (str): A brief description of the package.
    author (str): The name of the package author.
    author_email (str): The email of the package author.
    url (str): URL for the package repository.
    long_description (str): A detailed description of the package.
    long_description_content_type (str): The format of the long description.
    classifiers (list): A list of classifiers that provide metadata about the package.
    python_requires (str): The required Python version.
"""

setup(
    name='morning_greetings',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'schedule',  # For scheduling daily greetings
        're',        # Regular expressions for email validation
    ],
    entry_points={
        'console_scripts': [
            'morning_greetings = main:main',
        ],
    },
    description='A package to send personalized "Good Morning" messages',
    author='Anders Blomberg',
    author_email='s339872@oslomet.no',
    url='https://github.com/andersblberg/morning_greetings',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

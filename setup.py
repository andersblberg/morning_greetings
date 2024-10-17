from setuptools import setup, find_packages

setup(
    name='morning_greetings',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
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

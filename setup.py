from setuptools import setup, find_packages

setup(
    name='quote_generation_api',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'quote_generation_api = app:main'
        ]
    },
)
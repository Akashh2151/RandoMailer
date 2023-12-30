# setup.py

from setuptools import setup, find_packages

setup(
    name='RandoMailer',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Akash Desai',
    author_email='Akashh2151@gmail.com', 
    description='A package for generating random emails',
    long_description=(
        'RandoMailer is a Python package designed for creating random email addresses. '
        'It is a versatile tool suitable for various applications, from testing to data anonymization.'
        '\n\n'
        'Key Features:'
        '\n- Efficient and secure random email generation.'
        '\n- Lightweight and easy to integrate into Python projects.'
        '\n- Suitable for testing and data generation tasks.'
        '\n- Customizable options for email format.'
        '\n\n'
        'Installation:'
        '\n```bash'
        '\npip install RandoMailer'
        '\n```'
        '\n\n'
        'Get started today and enhance your Python projects with RandoMailer!'
    ),
    url='https://github.com/yourusername/RandoMailer',
    project_urls={
        'Source Code': 'https://github.com/Akashh2151/RandoMailer',
        'Bug Tracker': 'https://github.com/Akashh2151/RandoMailer/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='random email generator testing development',
)

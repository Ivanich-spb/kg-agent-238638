from setuptools import setup, find_packages

setup(
    name='kg_agent',
    version='0.1.0',
    description='Skeleton implementation of KG-Agent: an autonomous agent framework for reasoning over KGs',
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.10',
    install_requires=[
        'torch>=2.0.0',
        'transformers>=4.30.0',
        'networkx>=3.0',
        'rdflib>=6.0.0'
    ],
)

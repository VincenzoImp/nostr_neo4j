from setuptools import setup, find_packages

setup(
    name='nostr_neo4j',
    version='0.1',
    packages=find_packages(['nostr_neo4j']),
    description='Nostr Neo4j Library',
    author='VincenzoImp',
    author_email='',
    url='https://github.com/VincenzoImp/nostr_neo4j',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
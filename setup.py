from setuptools import setup

# TODO(auberon): Handle distribution of model files
# TODO(auberon): pyproject.toml

setup(
    name='collage_dna',
    version='0.0.4',
    description='A deep learning framework for identifying naturally selected patterns of codon preference within a species',
    url='https://github.com/wilburnlab/collage',
    author='Wilburn Lab',
    license='MIT',
    packages=['collage'],
    install_requires=['numpy'] # TODO(auberon): make requirements looser

)
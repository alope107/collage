'''
collage

A deep learning framework for identifying naturally selected patterns of codon preference within a species.
'''

__version__ = '0.0.4'
__author__ = 'Wilburn Lab'

try:
    import torch
except ModuleNotFoundError:
    raise ModuleNotFoundError('collage depends on PyTorch. Please install the appropriate version for your system. You can finkd instructions here: https://pytorch.org/get-started/locally/')
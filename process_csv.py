#!/usr/bin/python3
import os, glob

def get_header(file):
    """Get header from file."""
    with open(file, 'r') as fh:
        header = fh.readline().strip()

    return header

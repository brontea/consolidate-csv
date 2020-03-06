#!/usr/bin/python3
import os, glob, json

def get_header(file):
    """Get header from file."""
    with open(file, 'r') as fh:
        header = fh.readline().strip()

    return header

def get_unique_headers(pattern="*.csv"):
    """Get unique headers from pattern files"""
    unique_headers = {}
    for file in glob.glob(pattern):
        header = get_header(file)
        if header not in unique_headers:
            unique_headers[header] = []
        unique_headers[header].append(file)

    return unique_headers

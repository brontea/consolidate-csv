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

def write_consolidated_data(unique_headers, group_name="group", suffix=".txt"):
    """Write consolidated data in groups of files."""
    groups_count = 0
    for header, files in unique_headers.items():
        groups_count += 1
        with open(group_name + "_" + str(groups_count) + suffix, 'w') as group_fh:
            group_fh.write(header + "\n")
            for file in files:
                with open(file, 'r') as current_file:
                    first_line = current_file.readline()
                    rest_of_the_lines = current_file.readlines()
                group_fh.writelines(rest_of_the_lines)

unique_headers = get_unique_headers()
write_consolidated_data(unique_headers)

#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py
Author: "Sahil Sherzai"
Semester: "Fall 2024"

Description:
This script provides a visual representation of memory usage on a Linux system.
It can display the total system memory usage or the memory usage of specific
processes when a program name is provided. The script uses the `/proc` file
system to extract memory-related information and `argparse` for command-line
argument parsing.


import argparse
import os, sys

def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """
    Convert memory size from KiB to a human-readable format.
    """
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes) - 1:
        result /= 1024
        suf_count += 1
    return f"{result:.{decimal_places}f} {suffixes[suf_count]}"

def get_total_mem() -> int:
    """
    Get the total system memory in KiB.
    """
    # Example value in KiB (e.g., 16 GiB = 16 * 1024 * 1024 KiB)
    return 16 * 1024 * 1024

def get_used_mem() -> int:
    """
    Get the used system memory in KiB.
    """
    # Example value in KiB (e.g., 8 GiB = 8 * 1024 * 1024 KiB)
    return 8 * 1024 * 1024

def percent_to_graph(percentage: float, length: int = 50) -> str:
    """
    Convert a percentage to a graphical bar representation.
    """
    bar_length = int(percentage * length)
    return '█' * bar_length + '-' * (length - bar_length)

if __name__ == "__main__":
    total_mem = get_total_mem()
    used_mem = get_used_mem()
    used_percent = used_mem / total_mem

    bar = percent_to_graph(used_percent, 50)
    print(f"Memory         [{bar}| {used_percent * 100:.0f}%] {bytes_to_human_r(used_mem)}/{bytes_to_human_r(total_mem)}")

#!/usr/bin/env python3
"""a function named index_range that takes two integer arguments"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a
    start index and an end index"""
    upper_bound = page * page_size
    rtuple = (upper_bound - page_size, upper_bound)
    return rtuple

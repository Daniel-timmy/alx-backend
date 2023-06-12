#!/usr/bin/env python3
"""Server class module"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a
    start index and an end index"""
    upper_bound = page * page_size
    rtuple = (upper_bound - page_size, upper_bound)
    return rtuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value pairs
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        rlist = self.get_page(page, page_size)
        data = self.dataset()
        rlen = math.ceil(len(data) / page_size)
        start, end = index_range(page, page_size)
        prev_page = 0
        next_page = 0
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page > rlen:
            next_page = None
        else:
            next_page = page + 1

        return {"page_size": len(rlist),
                'page': page,
                'data': rlist,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': rlen
                }

#!/usr/bin/env python3
'''
    Simple pagination.
'''
import csv
import math
from typing import List


def index_range(page, page_size):
    '''
        Returns the range of indexes for a given page.
    '''
    start_index = (page - 1) * page_size
    end_index = page * page_size

    indices = tuple([start_index, end_index])
    return indices


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:  # sourcery skip: identity-comprehension
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            Returns a page of data.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()

        if self.dataset() is None:
            return []

        indexRange = index_range(page, page_size)
        return self.dataset()[indexRange[0]:indexRange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dictionary
        """
        keys = ["page_size", "page", "data", "next_page", "prev_page", "total_pages"]

        # Initialize dictionary with keys and None as values
        empty_dict = {key: None for key in keys}
        ranges = index_range(page, page_size)
        data_set = self.dataset()

        empty_dict["page_size"] = page_size
        empty_dict["page"] = page
        empty_dict["prev_page"] = ranges[0] - 1
        empty_dict["next_page"] = ranges[1] + 1
        empty_dict["total_pages"] = (len(data_set) + page_size - 1) // page_size
        empty_dict["data"] = self.get_page(page, page_size)

        return empty_dict

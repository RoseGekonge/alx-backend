#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        returns a dictionary
        """
        keys = ["index", "data", "page_size", "next_index"]
        hyper_dict = {key: None for key in keys}

        assert (index - 1) % page_size == 0
        #assert next_index == index

        hyper_dict["index"] = index
        hyper_dict["next_index"] = hyper_dict["index"] + page_size
        hyper_dict["page_size"] = page_size
        dataset = self.dataset()[index:(index + page_size)]
        hyper_dict["data"] = dataset

        return hyper_dict

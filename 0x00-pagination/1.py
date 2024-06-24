#!/usr/bin/env python3
import csv
import math
from typing import List

"""
pagging
"""


def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = page * page_size

    indices = tuple([start_index, end_index])
    return indices


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = 'Popular_Baby_Names.csv'
    def __init__(self):
        self.__dataset = None
        self.data = []
        self.a_list = []
        self.load_data()

    def load_data(self):
        with open(self.DATA_FILE, mode='r') as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)
            r = 0
            k = 0
            characters = ["Year of Birth", "Gender", "Ethnicity", "Child\'s First Name", "Count", "Rank"]
            for row in csv_reader:
                self.data.append(row)
            while k < len(self.data):
                while r < len(characters):
                    self.a_list.append(row[characters[r]])
                    r += 1
                k += 1

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
        list_of_rows = []
        i = 0
        k = 0
        characters = ["Year of Birth", "Gender", "Ethnicity", "Child\'s First Name", "Count", "Rank"]
        assert page > 0
        assert page_size > 0
        indices = index_range(page, page_size)
        i += indices[0]
        if page * page_size < len(self.data):
            for i in self.data:
                while k < len(characters):
                    list_of_rows.append(i[characters[k]])
                    k += 1
        return list_of_rows

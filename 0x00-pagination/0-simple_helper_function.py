#!/usr/bin/env python3
"""
pagging
"""


def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = page * page_size

    indices = tuple([start_index, end_index])
    return indices

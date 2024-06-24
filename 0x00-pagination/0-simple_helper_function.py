#!/usr/bin/env python3
"""
pagging
"""


def index_range(page, page_size):
    """
    find the index ranges.

    Args:
        page: current page number
        page_size: data per page

    Return:
        tuple of the ranges.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    indices = tuple([start_index, end_index])
    return indices

"""Utility functions."""

__author__ = "730402799"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read file as csv rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of the csv line by line
    for row in csv_reader:
        result.append(row)
    # Close files when we're done
    return result  


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new table with only the first N rows of data."""
    for x in column_table:
        if N > len(column_table[x]):
            N = len(column_table[x])
    shorter_table: dict[str, list[str]] = {}
    for x in column_table:
        i: int = 0
        super_list: list[str] = []
        while i < N:
            super_list.append(column_table[x][i])
            i += 1
        shorter_table[x] = super_list
    return shorter_table


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for x in column_names:
        result[x] = column_table[x]
    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table that concatenates two previous tables."""
    result: dict[str, list[str]] = {}
    for x in column_table_1:
        result[x] = column_table_1[x]
    for y in column_table_2:
        if y in column_table_1:
            i: int = 0
            while i < len(column_table_2[y]):
                column_table_1[y].append(column_table_2[y][i])
                i += 1
            result[y] = column_table_1[y]
        else:
            result[y] = column_table_2[y]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of each value appearing in a list."""
    result: dict[str, int] = {}
    for x in values:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


def integerify(counts: dict[str, int]) -> dict[int, int]:
    """Converts keys of a str-int dictionary from type str to type int."""
    result: dict[int, int] = {}
    for x in counts:
        result[int(x)] = counts[x]
    return result
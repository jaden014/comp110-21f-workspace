"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union
# from _typeshed import SupportsDivMod

__author__ = "730402799"


class Simpy:
    """Utility class for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initializing a Simpy."""
        self.values = values

    def __str__(self) -> str:
        """Showing Simpy as a str."""
        return f"Simpy({self.values})"

    def fill(self, filler: float, number: int) -> None:
        """Fill a Simpy with one float."""
        result: list[float] = []
        i: int = 0
        while i < number:
            result.append(filler)
            i += 1
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Define a Simpy with a range."""
        assert step != 0
        result: list[float] = []
        if step > 0.0:
            while start < stop:
                result.append(start)
                start += step
        if step < 0.0:
            while start > stop:
                result.append(start)
                start += step
        self.values = result

    def sum(self) -> float:
        """Deliver the sum of a Simpy."""
        sum: float = 0.0
        for x in self.values:
            sum += x
        return sum

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds two Simpys or Simpy and float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes one Simpy to the power of another or a float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Mask of 2 Simpys or Simpy and float for ==."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Mask of 2 Simpys or Simpy and float for >."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation or filter with mask."""
        if isinstance(rhs, int):
            result: float = 0.0
            result = self.values[rhs]
            return result
        if isinstance(rhs, list): 
            assert len(self.values) == len(rhs)
            resulty: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    resulty.values.append(self.values[i])
                i += 1
            return resulty
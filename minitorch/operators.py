"""
Collection of the core mathematical operators used throughout the code base.
"""

import math
from typing import Callable, Iterable

# ## Task 0.1
#
# Implementation of a prelude of elementary functions.


def is_close(num1: float, num2: float) -> bool:
    return abs(num1 - num2) < 1e-2 


def mul(num1: float, num2: float) -> float:
    return num1 * num2


def max(num1: float, num2: float) -> float:
    return num1 if num1 > num2 else num2


def add(num1: float, num2: float) -> float:
    return num1 + num2


def neg(num1: float) -> float:
    return - num1


def id(num: float) -> float:
    return num


def inv(num: float) -> float:
    return 1.0 / num


def relu(num: float) -> float:
    return num if num > 0 else 0.0


def relu_back(num1: float, num2: float) -> float:
    return num2 if num1 > 0 else 0.0


def lt(num1: float, num2: float) -> float:
    return float(num1 < num2)


def eq(num1: float, num2: float) -> float:
    return float(num1 == num2)


def sigmoid(num: float) -> float:
    return 1.0/(1.0 + math.exp(-num)) if num >=0 else math.exp(num)/(1.0 + math.exp(num))


def log(num: float) -> float:
    return math.log(num + 1e-6)


def exp(num: float) -> float:
    return math.exp(num)


def log_back(num: float) -> float:
    return 1.0 / num


def inv_back(num: float) -> float:
    return - 1.0 / (num ** 2)


# ## Task 0.3

# Small practice library of elementary higher-order functions.


def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """
    Higher-order map.

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: Function from one value to one value.

    Returns:
        A function that takes a list, applies `fn` to each element, and returns a
         new list
    """
    raise NotImplementedError("Need to include this file from past assignment.")


def negList(ls: Iterable[float]) -> Iterable[float]:
    "Use `map` and `neg` to negate each element in `ls`"
    raise NotImplementedError("Need to include this file from past assignment.")


def zipWith(
    fn: Callable[[float, float], float]
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """
    Higher-order zipwith (or map2).

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
        fn: combine two values

    Returns:
        Function that takes two equally sized lists `ls1` and `ls2`, produce a new list by
         applying fn(x, y) on each pair of elements.

    """
    raise NotImplementedError("Need to include this file from past assignment.")


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    "Add the elements of `ls1` and `ls2` using `zipWith` and `add`"
    raise NotImplementedError("Need to include this file from past assignment.")


def reduce(
    fn: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""
    Higher-order reduce.

    Args:
        fn: combine two values
        start: start value $x_0$

    Returns:
        Function that takes a list `ls` of elements
         $x_1 \ldots x_n$ and computes the reduction :math:`fn(x_3, fn(x_2,
         fn(x_1, x_0)))`
    """
    raise NotImplementedError("Need to include this file from past assignment.")


def sum(ls: Iterable[float]) -> float:
    "Sum up a list using `reduce` and `add`."
    raise NotImplementedError("Need to include this file from past assignment.")


def prod(ls: Iterable[float]) -> float:
    "Product of a list using `reduce` and `mul`."
    raise NotImplementedError("Need to include this file from past assignment.")

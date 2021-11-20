# Statistics library

import math

from typing import List
from collections import Counter

from linear_algebra import dot, sum_of_squares


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    """if len(x) is odd then median is the middle element"""
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of two middle elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    assert len(v) != 0
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: List[float], p: float) -> float:
    """Returns p-th percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


def mode(xs: List[float]) -> List[float]:
    """Returns a list since there may be more than one mode"""
    counts = Counter(xs)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Translate xs b subtracting its mean
       so the result has mean of 0"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from mean"""
    assert len(xs) >= 2, "variance requires at least two elements"
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """Square root of variance"""
    return math.sqrt(variance(xs))


def interquantile_range(xs: List[float]) -> float:
    """Retuns difference between 75%-ile and 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "x and y must be the same length"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

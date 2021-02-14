import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    arr = A
    start_idx = 0
    end_idx = len(arr) - 1

    def is_even(num):
        return num % 2 == 0

    def is_odd(num):
        return num % 2 != 0

    while start_idx < end_idx:
        if is_odd(arr[start_idx]) and is_even(arr[end_idx]):
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
            start_idx += 1
            end_idx -= 1
        else:
            if is_even(arr[start_idx]):
                start_idx += 1
            if is_odd(arr[end_idx]):
                end_idx -= 1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))

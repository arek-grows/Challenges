# The Golomb sequence is uniquely defined by the following rules:
#
#     All terms are positive integers.
#     No term is smaller than any previous term.
#     The nth term is equal to the total number of times that the integer n appears within the sequence.
#
# Write a function that returns the first n terms of the Golomb sequence as a list.
# Examples
#
# golomb(1) ➞ [1]
#
# golomb(8) ➞ [1, 2, 2, 3, 3, 4, 4, 4]
#
# golomb(10) ➞ [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]
#
# 1 appears once; 2 appears twice; 3 appears twice; 4 appears 3 times; 5 will appear 3 times in the full sequence, etc.
# Notes
#
#     The tests will consist of random inputs between 1 and 1000 inclusive.
#     If stuck, see resources tab for more information and hints.
from random import randint
import numpy.testing as npt


def golomb(n):
    end_list = []
    for x in range(1, n + 1):
        end_list.append(x)
        if len(end_list) == n:
            return end_list
        while end_list[x - 1] != end_list.count(x):
            end_list.append(x)
            if len(end_list) == n:
                return end_list


def golomb_check(lst, n):
    return lst == sorted(lst) and lst[0] > 0 and all(lst[i - 1] == lst.count(i) for i in range(1, lst[-1])) and len(
        lst) == n


for i in range(10):
    n = randint(1, 1000)
    npt.assert_equal(golomb_check(golomb(n), n), True)

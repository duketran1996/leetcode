'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''
#!/usr/bin/python3
import unittest
from typing import List


InputOne = [-4, -1, 0, 3, 10]
OutputOne = [0, 1, 9, 16, 100]

InputTwo = [-7, -3, 2, 3, 11]
OutputTwo = [4, 9, 9, 49, 121]


class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(sortedSquares(InputOne), OutputOne)

    def test_two(self):
        self.assertEqual(sortedSquares(InputTwo), OutputTwo)


def sortedSquares(A: List[int]) -> List[int]:
    for i in range(len(A)):
        A[i] = A[i] * A[i]

    A.sort()

    return A


if __name__ == "__main__":
    unittest.main()

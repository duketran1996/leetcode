'''
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
'''
#!/usr/bin/python3
import unittest
from typing import List


InputOne = [12, 345, 2, 6, 7896]
OutputOne = 2

InputTwo = [555, 901, 482, 1771]
OutputTwo = 1


class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(findNumbers(InputOne), OutputOne)

    def test_two(self):
        self.assertEqual(findNumbers(InputTwo), OutputTwo)


def findNumbers(nums: List[int]) -> int:
    count = 0
    for val in nums:
        if len(str(val)) % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    unittest.main()

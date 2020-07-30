'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
#!/usr/bin/python3
import unittest
from typing import List


InputOne = [1,1,0,1,1,1]
OutputOne = 3

InputTwo = [0]
OutputTwo = 0

InputThree = [1]
OutputThree = 1

InputFour = [0,0]
OutputFour = 0

InputFive = [1,0]
OutputFive = 1

class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(findMaxConsecutiveOnes(InputOne), OutputOne)

    def test_two(self):
        self.assertEqual(findMaxConsecutiveOnes(InputTwo), OutputTwo)

    def test_three(self):
        self.assertEqual(findMaxConsecutiveOnes(InputThree), OutputThree)

    def test_four(self):
        self.assertEqual(findMaxConsecutiveOnes(InputFour), OutputFour)

    def test_five(self):
        self.assertEqual(findMaxConsecutiveOnes(InputFive), OutputFive)


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = 0
    temp = 0

    for val in nums:
        if val == 1:
            count += 1
            if count > temp:
                temp = count
        else:
            count = 0
        
    return temp


if __name__ == "__main__":
    unittest.main()

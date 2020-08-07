'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''
#!/usr/bin/python3
import unittest
from typing import List


InputOneOne = [1, 2, 3, 0, 0, 0]
InputOneTwo = [2, 5, 6]
OutputOne = [1, 2, 2, 3, 5, 6]

InputTwoOne = [1, 0]
InputTwoTwo = [2]
OutputTwo = [1, 2]

InputThreeOne = [2, 0]
InputThreeTwo = [1]
OutputThree = [1, 2]

InputFourOne = [1, 2, 3, 0, 0, 0]
InputFourTwo = [4, 5, 6]
OutputFour = [1, 2, 3, 4, 5, 6]


class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(merge(InputOneOne, len(InputOneTwo),
                               InputOneTwo, len(InputOneTwo)), OutputOne)

    # def test_two(self):
    #     self.assertEqual(merge(InputTwoOne, len(InputTwoTwo),
    #                            InputTwoTwo, len(InputTwoTwo)), OutputTwo)

    # def test_three(self):
    #     self.assertEqual(merge(InputThreeOne, len(InputThreeTwo),
    #                            InputThreeTwo, len(InputThreeTwo)), OutputThree)

    # def test_four(self):
    #     self.assertEqual(merge(InputFourOne, len(InputFourTwo),
    #                            InputFourTwo, len(InputFourTwo)), OutputFour)


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1

    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]

    return nums1


if __name__ == "__main__":
    unittest.main()

'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''
#!/usr/bin/python3
import unittest
from typing import List


InputOne = [1, 0, 2, 3, 0, 4, 5, 0]
OutputOne = [1, 0, 0, 2, 3, 0, 0, 4]

InputTwo = [1, 2, 3]
OutputTwo = [1, 2, 3]


class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(duplicateZeros(InputOne), OutputOne)

    def test_two(self):
        self.assertEqual(duplicateZeros(InputTwo), OutputTwo)


def duplicateZeros(arr: List[int]) -> None:
    flag = True
    for i in range(len(arr)):
        if arr[i] == 0 and flag:
            for j in range(len(arr)-1, i, -1):
                arr[j] = arr[j-1]
            flag = False
        else:
            flag = True

    return arr


if __name__ == "__main__":
    unittest.main()

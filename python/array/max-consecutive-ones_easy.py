'''
Problem questions
'''
#!/usr/bin/python3
import unittest


input = "Hello World!"
output = "HELLO WORLD!"


class TestMethods(unittest.TestCase):

    def test_one(self):
        self.assertEqual(main(), output)


def main():
    output = input.upper()
    return output


if __name__ == "__main__":
    unittest.main()

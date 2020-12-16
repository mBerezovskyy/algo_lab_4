from unittest import TestCase
from solution import Solution


class Test(TestCase):
    def test_case_1(self):
        solution = Solution()
        data = solution.read_file('test_cases/wchain1')
        longest = solution.longest_words_chain(data)
        self.assertEqual(longest, 6)

    def test_case_2(self):
        solution = Solution()
        data = solution.read_file('test_cases/wchain2')
        longest = solution.longest_words_chain(data)
        self.assertEqual(longest, 4)

    def test_case_3(self):
        solution = Solution()
        data = solution.read_file('test_cases/wchain3')
        longest = solution.longest_words_chain(data)
        self.assertEqual(longest, 1)

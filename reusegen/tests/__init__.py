#

from unittest import TestCase

from reusegen import reuse


class TestReuseGen(TestCase):
    def setUp(self):
        gen = (i * i for i in range(10))
        self.reused = reuse(gen)
        self.expected = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    def test_it_works(self):
        for _i in range(10):
            self.assertEqual(list(self.reused), self.expected)

    def test_not_exhuasted_gen(self):
        for i in range(10):
            for j, val in zip(range(i + 1), self.reused):
                self.assertEqual(val, self.expected[j])


class TestReuseFunc(TestCase):
    def test_it_works(self):
        @reuse
        def fib(n):
            a, b = 0, 1
            for i in range(n):
                yield b
                a, b = b, a + b

        fib10 = fib(10)
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for _i in range(10):
            for i, val in enumerate(fib10):
                self.assertEqual(val, expected[i])

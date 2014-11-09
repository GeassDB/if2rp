#!/usr/bin/env python3
import random
import unittest
import if2rp

class test_infix2rp(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(1000))
        self.syms = "()+-*/^"

    def test_exp1(self):
        self.assertEqual(if2rp.infix2rp("11+22-33*44"), "11 22 + 33 44 * -")
    def test_exp2(self):
        self.assertEqual(if2rp.infix2rp("1+(2-3)*4"), "1 2 3 - 4 * +")
    def test_exp3(self):
        self.assertEqual(if2rp.infix2rp("(1-2*3)/4*5^6"), "1 2 3 * - 4 / 5 6 ^ *")

    def test_empty(self):
        with self.assertRaises(EOFError):
            if2rp.infix2rp("")

    def test_illegal1(self):
        with self.assertRaises(if2rp.IllegalExprError):
            if2rp.infix2rp("&&&")
    def test_illegal2(self):
        with self.assertRaises(if2rp.IllegalExprError):
            if2rp.infix2rp("1)")
    def test_illegal3(self):
        with self.assertRaises(if2rp.IllegalExprError):
            if2rp.infix2rp("(1")
    def test_illegal4(self):
        with self.assertRaises(if2rp.IllegalExprError):
            if2rp.infix2rp("1+")
    def test_illegal5(self):
        with self.assertRaises(if2rp.IllegalExprError):
            if2rp.infix2rp("1++1")

if __name__ == '__main__':
    unittest.main()

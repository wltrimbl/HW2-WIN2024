#!/bin/bash

import unittest, re
from gradescope_utils.autograder_utils.decorators import weight, number
from subprocess import PIPE, Popen
from os.path import exists

import pa1

class TestFlights(unittest.TestCase):
    def setUp(self):
        flights = []
        with open("flights.csv") as f:
            for line in f:
                flights.append(line)

    @weight(0)
    @number("1")
    def test_lint_gt8(self):
        '''Test exist pa1.py'''
        self.assertEqual( exists("pa1.py"), True, "pa1.py file does not exist.")
    @weight(1)
    @number("2")
    def test_inputok(self):
        '''Run pylint'''
        clean = clean_data(flights)
        self.assertEqual(  'CARDIOID', flights[-1][3], 
              "Last line does not match expectation.")
    @weight(1)
    @number("3")
    def test_inputlineok(self):
        '''Run pylint'''
        clean = clean_data(flights)
        self.assertEqual(  ('KBOS', 'KLAX', '2347', 'CARDIOID'), flights[-1], 
              "Last line does not match expectation.")


#!/usr/bin/python3
"""module"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class testCommand(unittest.TestCase):
    """Command test"""

    def test_quit(self):
        """test for quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        stdo = f.getvalue()
        self.assertEqual(stdo, "")

    def test_EOF(self):
        """test for EOF [CTRL + D] command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        stdo = f.getvalue()
        self.assertEqual(stdo, "\n")


if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3
"""Unittests for testing console output."""

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models


class TestConsole(unittest.TestCase):
    """class for testing the output of the console."""

    all_objects = models.storage.all()

    def test_docs(self):
        """Testing the documentation of each function."""
        functions = ["all", "create", "destroy", "quit", "show", "update"]
        docs = ["Prints all objects with the class name provided.\n",
                "Creates a new instance.\n",
                "Deletes an instance based on class name and id.\n",
                "Exits the command interpeter.\n",
                "Shows information about created instance by id.\n",
                ("Update instance by class name and id"
                    "\nby adding or updating attributes.\n")
                ]
        with patch('sys.stdout', new=StringIO()) as output:
            for i in range(len(functions)):
                HBNBCommand().onecmd(f"help {functions[i]}")
                out_val = output.getvalue()
                self.assertEqual(out_val, docs[i])
                output.truncate(0)
                output.seek(0)

    def test_create(self):
        """Tests the create command."""
        old_num = len(models.storage.all())
        tests = ["", "Model"]
        outputs = ["** class name missing **\n",
                   "** class doesn't exist **\n"]
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            new_num = len(models.storage.all())
            self.assertEqual(new_num, old_num + 1)
            for i in range(2):
                output.truncate(0)
                output.seek(0)
                HBNBCommand().onecmd(f"create {tests[i]}")
                out_val = output.getvalue()
                self.assertEqual(out_val, outputs[i])

    def test_all(self):
        """Tests all command."""
        objects = [str(v) for k, v in self.all_objects.items()]
        some_objects = [str(v) for k, v in self.all_objects.items()
                        if k.startswith("User")]
        tests = ["", "Model", "User"]
        outputs = [f"{objects}\n", "** class doesn't exist **\n",
                   f"{some_objects}\n"]
        with patch('sys.stdout', new=StringIO()) as output:
            for i in range(3):
                output.truncate(0)
                output.seek(0)
                HBNBCommand().onecmd(f"all {tests[i]}")
                out_val = output.getvalue()
                self.assertEqual(out_val, outputs[i])

#!/usr/bin/python3
"""unittest module for the console"""


import unittest
import os
import json
import pycodestyle
import io
from io import StringIO
from unittest.mock import patch

console = __import__("console.py")
HBNBCommand = console.HBNBCommand
base = __import__("models/base_model.py")
BaseModel = base.BaseModel
user = __import__("models/user.py")
User = user.User
place = __import__("models/place.py")
Place = place.Place
state = __import__("models/state.py")
State = state.State
city = __import__("models/city.py")
City = city.City
amenity = __import__("models/amenity.py")
Amenity = amenity.Amenity
review = __import__("models/review.py")
Review = review.Review
filestorage = __import__("models/engine/file_storage.py")
FileStorage = filestorage.FileStorage


class TestCommand(unittest.TestCase):
    """Class that tests the console"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup.
        Temporarily rename any existing file.json.
        Reset FileStorage objects dictionnary.
        Create an instance of the command interpreter.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown.
        Restore original file.json.
        Delete the test HBNBCommand instance.
        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

        def setUp(self):
            """Reset FileStorage objects dictionnary."""
            FileStorage._FileStorage__objects = {}

        def tearDown(self):
            """Delete any created file.json"""
            try:
                os.remove("file.json")
            except IOError:
                pass

        def test_pep8(self):
            """test PEP8 styling"""
            style = pep8.StyleGuide(quiet=True)
            p = style.check_files(["console.py"])
            self.assertEqual(p.total_errors, 0, "fix Pep8")

        def test_docstrings(self):
            """check for docstrings."""
            self.assertIsNotNone(HBNBCommand.__doc__)
            self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
            self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
            self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
            self.assertIsNotNone(HBNBCommand.do_create.__doc__)
            self.assertIsNotNone(HBNBCommand.do_show.__doc__)
            self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
            self.assertIsNotNone(HBNBCommand.do_all.__doc__)
            self.assertIsNotNone(HBNBCommand.do_update.__doc__)
            self.assertIsNotNone(HBNBCommand.default.__doc__)

        def test_create(self):
            """Test create command inpout"""
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("create")
                self.assertEqual(
                    "** class name missing **\n", f.getvalue())
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("create asdfsfsd")
                self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd('create User email="x@.com" password="234"')
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("all User")
                self.assertEqual(
                    "[[User]", f.getvalue()[:7])


if __name__ == "__main__":
    unittest.main()


"""
test_base_classes.py

Unit tests for Root and Verb base classes

@copyright Bandwidth Inc.
"""
import unittest

from bandwidth.model.bxml.root import Root
from bandwidth.model.bxml.verb import Verb


class TestBaseClasses(unittest.TestCase):
    
    def setUp(self): 
        self.root = Root(tag="TestRoot")
        self.verb1 = Verb(tag="TestVerb1", content="test")
        self.verb2 = Verb(tag="TestVerb2")
        self.verb3 = Verb(tag="TestVerb3")
    
    def test_root(self):
        self.root.add_verb(self.verb1)
        self.root.add_verb(self.verb2)
        
        expected_bxml = "<?xml version='1.0' encoding='utf8'?>\n<TestRoot><TestVerb1>test</TestVerb1><TestVerb2 /></TestRoot>"
        assert(type(self.root[0]) == Verb)
        assert(len(self.root) == 2)
        assert(expected_bxml == self.root.to_bxml())
    
    def test_verb(self):
        self.verb3.add_verb(self.verb1)

        expected_bxml = "<TestVerb3><TestVerb1>test</TestVerb1></TestVerb3>"
        assert(type(self.verb3[0]) == Verb)
        assert(len(self.verb3) == 1)
        assert(expected_bxml == self.verb3.to_bxml())


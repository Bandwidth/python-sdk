
"""
test_base_classes.py

Unit tests for Root and Verb base classes

@copyright Bandwidth Inc.
"""
import pytest
import unittest

from bandwidth.models.bxml import Root, Verb, NestableVerb


class TestBaseClasses(unittest.TestCase):

    def setUp(self):
        self.root = Root(tag="TestRoot")
        self.verb1 = Verb(tag="TestVerb1", content="test")
        self.verb2 = Verb(tag="TestVerb2")
        self.nestable_verb = NestableVerb(tag="TestNestableVerb")

    def test_root(self):
        self.root.add_verb(self.verb1)
        self.root.add_verb(self.verb2)

        expected_bxml = "<?xml version='1.0' encoding='UTF-8'?>\n<TestRoot><TestVerb1>test</TestVerb1><TestVerb2 /></TestRoot>"
        assert type(self.root[0]) == Verb
        assert len(self.root) == 2
        assert expected_bxml == self.root.to_bxml()

    def test_nestable_verb(self):
        self.nestable_verb.add_verb(self.verb1)

        expected_bxml = "<TestNestableVerb><TestVerb1>test</TestVerb1></TestNestableVerb>"
        assert type(self.nestable_verb[0]) == Verb
        assert len(self.nestable_verb) == 1
        assert expected_bxml == self.nestable_verb.to_bxml()

    def test_adding_verbs_to_root_during_creation(self):
        self.root2 = Root(tag="TestRoot2", nested_verbs=[self.verb1, self.verb2])

        assert len(self.root2) == 2

    def test_adding_verbs_to_terminal_verb(self):
        with pytest.raises(AttributeError):
            self.terminal_verb.add_verb(self.verb1)

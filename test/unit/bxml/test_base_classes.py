
"""
test_base_classes.py

Unit tests for Root and Verb base classes

@copyright Bandwidth Inc.
"""
from bandwidth.model.bxml.root import Root
from bandwidth.model.bxml.verb import Verb

class TestBaseClasses:
    def __init__(self): 
        self.root = Root(tag="TestRoot")
        self.verb1 = Verb(tag="TestVerb1")
        self.verb2 = Verb(tag="TestVerb2")

import pytest
from .bigImit import *

def test_pytest():
    assert 1 == 1

def test_big():
    assert bigInit.debug() == 1


import pytest

from fonctions import moy, facto

def test_moy():
    assert moy(1, 2) == 1.5
    assert moy(2, 5) == 3.5


def test_facto():
    assert facto(2)==2
    assert facto(3)==6
    
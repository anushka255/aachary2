from aachary2.example import hello
from aachary2.example import add
from aachary2.example import multiply


def test_hello():
    assert hello() is None


def test_add():
    assert add(1, 2) == 3
    assert add("hello", " world") == "hello world"


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply("hello ", 3) == "hello hello hello "


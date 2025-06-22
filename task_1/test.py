from task_1.solution import strict


@strict
def int_add(a: int, b: int) -> int:
    return a + b


@strict
def str_example(name: str) -> str:
    return f"Hello, {name}!"


@strict
def float_multiply(a: float, b: float) -> float:
    return a * b


@strict
def bool_example(flag: bool) -> bool:
    return not flag


@strict
def str_concat(a: str, b: str) -> str:
    return a + b


def test_add_correct():
    assert int_add(2, 3) == 5


def test_greet_correct():
    assert str_example("Alice") == "Hello, Alice!"


def test_float_multiply():
    assert float_multiply(2.5, 4.0) == 10.0


def test_bool_example():
    assert bool_example(True) == False


def test_type_error():
    import pytest
    with pytest.raises(TypeError):
        int_add(1, "bad")

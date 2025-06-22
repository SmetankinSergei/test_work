from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args):
        items = list(zip(args, func.__annotations__.items()))
        for item in items:
            argument = item[0]
            expected_type = item[1][1]
            if not isinstance(argument, expected_type):
                raise TypeError(
                    f"Argument: {argument}, type {type(argument)}, must be {expected_type}"
                )
        return func(*args)
    return wrapper

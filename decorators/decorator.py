"""
This module contains a decorator for counting method calls and storing the counts in a file.
"""
import os
import logging


def method_calls_counter(func):
    """
    A decorator that registers and writes to a file the number of method calls.
    """

    def wrapper(*args, **kwargs):
        try:
            with open("file.txt", "r", encoding='utf-8') as file:
                read_file = file.read()
                method_calls = dict(eval(read_file))  # pylint: disable=eval-used
        except (FileNotFoundError, SyntaxError):
            method_calls = {}

        method_name = func.__name__
        if method_name in method_calls:
            method_calls[method_name] += 1
        else:
            method_calls[method_name] = 1

        with open("file.txt", "w", encoding='utf-8') as file:
            file.write(str(method_calls))
        return func(*args, **kwargs)

    return wrapper


def result_to_file_decorator(cls):
    """
    Декоратор, що створює файл, який називається НазваКласу_назва_методу,
    і в нього записується результат виклику методу.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            filename = f"{cls}_{func.__name__}.txt"

            if os.path.exists(filename):
                with open(filename, "a", encoding='utf-8') as second_file_decorator:
                    second_file_decorator.write(str(result) + "\n")
            else:
                with open(filename, "w", encoding='utf-8') as second_file_decorator:
                    second_file_decorator.write(str(result) + "\n")

            return result

        return wrapper

    return decorator


def logged(exception, mode):
    """A decorator that logs exceptions raised by the decorated function.
        Args:
            exception (Exception): The type of exception to be caught and logged.
            mode (str): The logging mode. Can be either "console" or "file".
        Returns:
            function: The decorated function."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as error:
                if mode == "console":
                    logging.basicConfig(format='%(levelname)s - %(message)s')
                    logging.error(error.message)
                elif mode == "file":
                    logging.basicConfig(filename='app.log', filemode='w',
                                        format='%(levelname)s - %(message)s')
                    logging.error(error.message)
            return None

        return wrapper

    return decorator

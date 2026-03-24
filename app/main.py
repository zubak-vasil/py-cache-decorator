from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        key = args

        if key in results:
            print("Getting from cache")
            return results[key]

        print("Calculating new result")
        result = func(*args)
        results[key] = result
        return result

    return wrapper

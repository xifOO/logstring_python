from typing import List, Optional


def multiply_elements(lst: List[float], multiplier: Optional[float] = None) -> List[float]:
    if multiplier is None:
        multiplier = 2
    return [x * multiplier for x in lst]


multiply_lambda = lambda lst, multiplier=2: [x * multiplier for x in lst]

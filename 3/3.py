from typing import Union, List

def function_name(search: str, status: bool, *args: list, **kwargs: dict) -> Union[List[int], str]:
    result = []
    result_2 = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f" {i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += (" Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")

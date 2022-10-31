from dataclasses import dataclass
from typing import List


@dataclass
class Statistic:
    length: int
    if_construction_amount: int
    for_construction_amount: int
    while_construction_amount: int
    recursive_call_amount: int

    def __str__(self):
        return f'\t\tcode length: {self.length} lines\n' \
               f'\t\tconstructions amounts:\n' \
               f'\t\t\tif: {self.if_construction_amount}\n' \
               f'\t\t\tfor: {self.for_construction_amount}\n' \
               f'\t\t\twhile: {self.while_construction_amount}\n' \
               f'\t\t\trecursive call: {self.recursive_call_amount}\n' \



def get_statistics(function_name: str, code: List[str]) -> Statistic:
    length = get_length(code)
    if_constr = get_construction_amount("if", code)
    for_constr = get_construction_amount("for", code)
    while_constr = get_construction_amount("while", code)
    recursive_call_constr = get_construction_amount(f" {function_name}(", code)
    return Statistic(length, if_constr, for_constr, while_constr, recursive_call_constr)


def get_length(code: List[str]):
    return len(code)


def get_construction_amount(construction: str, code: List[str]):
    return len(list(filter(lambda x: x.__contains__(construction), code)))


class Method:
    def __init__(self, name: str, args: List[str], return_type: str, comment: str, code: List[str]):
        self.name = name
        self.args = args
        self.return_type = return_type
        self.comment = comment
        self.statistics = get_statistics(name, code)
        self.code = code

    def __str__(self):
        return f'name: {self.name}\n' \
               f'args: {self.args}\n' \
               f'return type: {self.return_type}\n' \
               f'comment: {self.comment}\n' \
               f'statistic:\n{self.statistics}'

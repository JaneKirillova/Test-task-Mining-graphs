import re
from typing import List
from method import Method

def get_file_methods(file):
    with open(file, "r") as f:
        data = f.read()
    data = data.split("\n")
    return get_methods(data)


def get_methods(lines: List[str]):
    current_ind = 0
    regex_for_func = r"^[\n\t\s]*[private|public|protected]? *function "
    methods = []
    while current_ind < len(lines):
        line = lines[current_ind]
        current_ind += 1
        if bool(re.match(regex_for_func, line)):
            name = get_function_name(line)
            args = get_arguments(line)
            comment = get_comments(lines, current_ind - 1)
            return_type = get_return_type(line)
            try:
                body, end_id = get_function_body(lines, current_ind)
                methods.append(Method(name, args, return_type, comment, body))
            # we can not guarantee that files in repositories are always correct
            # so if some methods in file are not correct we just skip them
            except:
                continue
    return methods


def get_function_name(line):
    parts = line.split()
    index = parts.index('function')
    return parts[index + 1].split('(')[0]


def get_function_body(lines: List[str], body_start):
    body = [lines[body_start]]
    balance = 1
    body_start += 1
    while balance != 0:
        cur_line = lines[body_start]
        if cur_line.__contains__("{"):
            balance += 1
        elif cur_line.__contains__("}"):
            balance -= 1
        body.append(cur_line)
        body_start += 1
    return body, body_start


def get_comments(lines: List[str], function_start):
    comment = []
    if function_start == 0 or not lines[function_start - 1].endswith("*/"):
        return ""
    function_start -= 1
    comment_regex = r"^[\n\t\s]*/\*\*"
    while function_start >= 0:
        cur_line = lines[function_start]
        comment.append(cur_line)
        if bool(re.match(comment_regex, cur_line)):
            break
        function_start -= 1
    return "\n".join(comment[::-1])


def get_arguments(func_def: str):
    open_br = func_def.find('(')
    close_br = func_def.find(')')
    args = func_def[open_br + 1: close_br]
    args = args.split(", ")
    if args.__contains__(''):
        args.remove('')
    return args

def get_return_type(line: str):
    parts = line.split("):")
    if len(parts) == 1:
        return ""
    return parts[1].split('{')[0].split()[0]

from typing import Dict

from .innerBlock import InnerBlock


class IfTag(InnerBlock):
    def __init__(self, arg_name: str, ret_val: str = None):
        super().__init__()
        self.arg_name = arg_name
        self.ret_val = ret_val

    def __call__(self, arguments: Dict[str, str]) -> str:
        return self.ret_val \
            if (self.arg_name in arguments and arguments[self.arg_name]) \
            else ''


class IfNotTag(IfTag):
    def __call__(self, arguments: Dict[str, str]):
        return self.ret_val \
            if not(self.arg_name in arguments and arguments[self.arg_name]) \
            else ''

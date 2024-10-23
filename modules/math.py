# _*_ coding: utf8 _*_

import logging
import traceback


class Math:
    def __init__(self, _display):
        self.display_ = _display

    def calc(self, _expression: str):
        _operators = {"*", "-", "+"}
        _parsed_expression = []
        _calculus = ""
        
        for x in _operators:
            if x in _expression:
                _parsed_expression = _expression.split(x)
                _calculus = x

        try:
            _result: int
            _numerator = int(_parsed_expression[0])
            _denominator = int(_parsed_expression[1])

            match _calculus:
                case "*":
                    _result = _numerator * _denominator
                case "-":
                    _result = _numerator - _denominator
                case "+":
                    _result = _numerator + _denominator
                case _:
                    raise IndexError("Insuficient values in the" \
                                    "current expression.")
        except Exception as _exc:
            logging.error(traceback.format_exc(_exc))
        else:
            self.print_result(str(_result))

    def print_result(self, _result:str):
        self.display_.clear_frame()
        self.display_.update_string(_result)

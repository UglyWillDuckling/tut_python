#!/usr/bin/env python3


ONE = 1
IS_ZERO = lambda x: x == 0
SUB1 = lambda x: x - 1
MULT = lambda x: lambda y: x * y
IF = lambda cond: lambda t_func: lambda f_func: t_func(None) if cond else f_func(None)



fact = lamba n : (
    IF(
        IS_ZERO(n)
    )(
        lambda _: ONE
    )(
        lambda _: MULT(n)( fact(SUB1(n)) )
    )

print(
    fact(6)
)

'''This easing function library is translated from https://github.com/ai/easings.net/blob/master/src/easings/easingsFunctions.ts and a cubic Bezier curve has been added. 

Function ID reference table: 
0: easeLinear
1: easeInSine
2: easeOutSine
3: easeInOutSine
4: easeInQuad
5: easeOutQuad
6: easeInOutQuad
7: easeInCubic
8: easeOutCubic
9: easeInOutCubic
10: easeInQuart
11: easeOutQuart
12: easeInOutQuart
13: easeInQuint
14: easeOutQuint
15: easeInOutQuint
16: easeInExpo
17: easeOutExpo
18: easeInOutExpo
19: easeInCric
20: easeOutCric
21: easeInOutCric
22: easeInBack
23: easeOutBack
24: easeInOutBack
25: easeInElastic
26: easeOutElastic
27: easeInOutElastic
28: easeInBounce
29: easeOutBounce
30: easeInOutBounce
31: easeBezier'''

import math

_SQRT = math.sqrt
_SIN = math.sin
_COS = math.cos

_PI = 3.14159265
_HALF_PI = 1.57079633

_C1 = 1.70158
_C2 = _C1 * 1.525
_C3 = _C1 + 1
_C4 = (2 * _PI) / 3
_C5 = (2 * _PI) / 4.5
_N1 = 7.5625
_D1 = 2.75

_EASING_TYPE_MAP = {
    'easeLinear': 0,
    'easeInSine': 1,
    'easeOutSine': 2,
    'easeInOutSine': 3,
    'easeInQuad': 4,
    'easeOutQuad': 5,
    'easeInOutQuad': 6,
    'easeInCubic': 7,
    'easeOutCubic': 8,
    'easeInOutCubic': 9,
    'easeInQuart': 10,
    'easeOutQuart': 11,
    'easeInOutQuart': 12,
    'easeInQuint': 13,
    'easeOutQuint': 14,
    'easeInOutQuint': 15,
    'easeInExpo': 16,
    'easeOutExpo': 17,
    'easeInOutExpo': 18,
    'easeInCric': 19,
    'easeOutCric': 20,
    'easeInOutCric': 21,
    'easeInBack': 22,
    'easeOutBack': 23,
    'easeInOutBack': 24,
    'easeInElastic': 25,
    'easeOutElastic': 26,
    'easeInOutElastic': 27,
    'easeInBounce': 28,
    'easeOutBounce': 29,
    'easeInOutBounce': 30,
    'easeBezier': 31
}

def easeLinear(x):
    return x

def easeInSine(x):
    return 1 - _COS(x * _HALF_PI)

def easeOutSine(x):
    return _SIN(x * _HALF_PI)

def easeInOutSine(x):
    return -(_COS(_PI * x) - 1) / 2

def easeInQuad(x):
    return x * x

def easeOutQuad(x):
    return 1 - (1 - x) * (1 - x)

def easeInOutQuad(x):
    if x < 0.5:
        return 2 * x * x 
    else: 
        return 1 - pow(-2 * x + 2, 2) / 2

def easeInCubic(x):
    return x ** 3

def easeOutCubic(x):
    return 1 - pow(1 - x, 3)

def easeInOutCubic(x):
    if x < 0.5:
        return 4 * x * x * x
    else:
        return 1 - pow(-2 * x + 2, 3) / 2

def easeInQuart(x):
    return x ** 4

def easeOutQuart(x):
    return 1 - pow(1 - x, 4)

def easeInOutQuart(x):
    if x < 0.5:
        return 8 * x * x * x * x
    else:
        return 1 - pow(-2 * x + 2, 4) / 2

def easeInQuint(x):
    return x ** 5

def easeOutQuint(x):
    return 1 - pow(1 - x, 5)

def easeInOutQuint(x):
    if x < 0.5:
        return 16 * x * x * x * x * x
    else:
        return 1 - pow(-2 * x + 2, 5) / 2

def easeInExpo(x):
    if x == 0:
        return 0
    return pow(2, 10 * x - 10)

def easeOutExpo(x):
    if x == 1:
        return 1
    return 1 - pow(2, -10 * x)

def easeInOutExpo(x):
    if x == 0 or x == 1:
        return x
    if x < 0.5:
        return pow(2, 20 * x - 10) / 2
    else: 
        return (2 - pow(2, -20 * x + 10)) / 2

def easeInCric(x):
    return 1 - _SQRT(1 - pow(x, 2))

def easeOutCric(x):
    return _SQRT(1 - pow(x - 1, 2))

def easeInOutCric(x):
    if x < 0.5:
        return (1 - _SQRT(1 - pow(2 * x, 2))) / 2
    else:
        return (_SQRT(1 - pow(-2 * x + 2, 2)) + 1) / 2

def easeInBack(x):
    return _C3 * x * x * x - _C1 * x * x

def easeOutBack(x):
    return 1 + _C3 * pow(x - 1, 3) + _C1 * pow(x - 1, 2)

def easeInOutBack(x):
    if x < 0.5:
        return (pow(2 * x, 2) * ((_C2 + 1) * 2 * x - _C2)) / 2
    else:
        return (pow(2 * x - 2, 2) * ((_C2 + 1) * (x * 2 - 2) + _C2) + 2) / 2

def easeInElastic(x):
    if x == 0 or x == 1:
        return x
    return -pow(2, 10 * x - 10) * _SIN((x * 10 - 10.75) * _C4)

def easeOutElastic(x):
    if x == 0 or x == 1:
        return x
    return pow(2, -10 * x) * _SIN((x * 10 - 0.75) * _C4) + 1

def easeInOutElastic(x):
    if x == 0 or x == 1:
        return x
    if x < 0.5:
        return -(pow(2, 20 * x - 10) * _SIN((20 * x - 11.125) * _C5)) / 2
    else:
        return (pow(2, -20 * x + 10) * _SIN((20 * x - 11.125) * _C5)) / 2 + 1

def easeInBounce(x):
    return 1 - easeOutBounce(x)

def easeOutBounce(x):
    if x < 1 / _D1:
        return _N1 * x * x
    elif x < 2 / _D1:
        return _N1 * (x - 1.5 / _D1) * (x - 1.5 / _D1) + 0.75
    elif (x < 2.5 / _D1):
        return _N1 * (x - 2.25 / _D1) * (x - 2.25 / _D1) + 0.9375
    else:
        return _N1 * (x - 2.625 / _D1) * (x - 2.625 / _D1) + 0.984375

def easeInOutBounce(x):
    if x < 0.5:
        return (1 - easeOutBounce(1 - 2 * x)) / 2
    else:
        return (1 + easeOutBounce(2 * x - 1)) / 2

def easeBezier(x):
    return (3 * x - 2 * pow(x, 2)) * x

def easeBezierV1(c1, c2, c3, c4, x):
    o = 1 - x
    return (
        (((pow(o, 3)) * c1) + ((pow(o, 2) * 3.0 * x) * c2)
        + ((x * x) * ((o) * 3.0) * c3))
        + ((x * x * x) * c4)
    )

_FUNC_LIST = [
    easeLinear,
    easeInSine,
    easeOutSine,
    easeInOutSine,
    easeInQuad,
    easeOutQuad,
    easeInOutQuad,
    easeInCubic,
    easeOutCubic,
    easeInOutCubic,
    easeInQuart,
    easeOutQuart,
    easeInOutQuart,
    easeInQuint,
    easeOutQuint,
    easeInOutQuint,
    easeInExpo,
    easeOutExpo,
    easeInOutExpo,
    easeInCric,
    easeOutCric,
    easeInOutCric,
    easeInBack,
    easeOutBack,
    easeInOutBack,
    easeInElastic,
    easeOutElastic,
    easeInOutElastic,
    easeInBounce,
    easeOutBounce,
    easeInOutBounce,
    easeBezier
]

def calculate(a, b, t, e):
    """Easing calculation function

    Args:
        a (float): The starting value of the range.
        b (float): The ending value of the range.
        t (float): The current time or position in the duration of the transition. It is a normalized value between 0 and 1.
        e (int|string): The type of easing function to use for the transition. 
        
    Returns:
        float: The eased value at time t, between a and b.
    """    
    if isinstance(e, str):
        e = _EASING_TYPE_MAP[e]
    return a + (b - a) * _FUNC_LIST[e](t)

from math import sin, pi

__author__ = "Masoud Sadrnezhaad"


def simpson(function, start, end, intervals):
    """
    Integrate sin function on a given period using Simpson 1/ 3 method.
    :param function:
    :param start:
    :param end:
    :param intervals:
    :return:
    """
    if intervals % 2:
        return "Number of intervals must be an even number."
    elif intervals == 0:
        return "Number of intervals could not be zero."

    h = float(end - start) / intervals
    integral = float(function(start))
    start = float(start)

    if intervals == 2:
        integral += 4 * function(start + h) + function(end)
    else:
        start += h
        for i in range(0, intervals // 2):
            integral += 4 * function(start) + 2 * function(start + h)
            start += 2 * h
        integral -= function(end)

    integral *= (h / 3)
    return integral


print(simpson(sin, 0, pi, 4))

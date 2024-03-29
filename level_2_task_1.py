"""
Read.me
=====

Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power.
Huge space stations with doomsday devices take even more power.
To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface.
But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels.
You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not take down all
of the panels at once if you can help it, since they do help power the space station and all!

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining
the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output
of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output
levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for
example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found
by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5])
 will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level
whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but
you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive
output of the multiple of their power values). The final products may be very large, so give the solution as a string
representation of the number.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([2, 0, 2, 2, 0])
Output:
    8

Input:
solution.solution([-2, -3, 4, -5])
Output:
    60
"""


def solution(xs):
    # If there is only one element, return it.
    if len(xs) == 1:
        result = xs[0]
        return str(result)

    # 1. Filtering positive numbers.
    positive_numbers = []

    for num in xs:
        if num > 0 and num <= 1000:
            positive_numbers.append(num)
    # print("Positive numbers: ", positive_numbers)

    # 2. Filtering negative numbers, removing the odd number.

    negative_numbers = []
    for num in xs:
        if num < 0 and num >= -1000:
            negative_numbers.append(num)

    if len(negative_numbers) % 2 != 0:
        # print('Max number:', max(negative_numbers))
        negative_numbers.remove(max(negative_numbers))
    # print('Negative numbers:', negative_numbers)

    # Multiply all the elements in the list

    numbers_to_multiply = negative_numbers + positive_numbers

    if numbers_to_multiply == []:
        return str(0)

    result = list_multiply(numbers_to_multiply)
    # print("Result: ", result)

    return str(result)


def list_multiply(list_to_multiply):
    count = 1
    for num in list_to_multiply:
        count *= num
    return count


# Test cases
# print(solution([2, 0, 2, 2, 0]))
# print(solution([-2, -3, 4, -5]))
# print(solution([-2, -3, 4, -5, -1, -1, -1, -1]))
# print(solution([-2, -3, -4, -5, 1001, -1001, 1000, -1000]))
#
# print(solution([-2]))
# print(solution([2]))
#
# print(solution([0, 0, 0, 0]))



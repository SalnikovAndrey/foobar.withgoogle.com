"""
Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42",
and other "good" numbers have been lording it over the poor minions who are stuck
with more boring IDs. To quell the unrest, Commander Lambda has tasked you with
reassigning everyone new random IDs based on a Completely Foolproof Scheme.

Commander Lambda has concatenated the prime numbers in 
a single long string: "2357111317192329...". Now every minion must draw a number from a hat.
That number is the starting index in that string of primes, and the minion's new ID number
will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function solution(n)
which takes in the starting index n of Lambda's string of all primes,
and returns the next five digits in the string.
Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

-- Python cases --
Input: solution.solution(0)
Output: 23571

Input: solution.solution(3)
Output: 71113
"""

def solution(i):
    n = 0
    prime_numbers = ""
    while len(prime_numbers) < i + 5:
        if is_prime(n):
            prime_numbers += str(n)
        n += 1
    return prime_numbers[i:i + 5]


def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(1, x):
        if x % i == 0 and i != 1:
            return False
    return True

# Test cases
# print(solution(6))
# print(solution(3))
# print(solution(0))
# print(solution(1))
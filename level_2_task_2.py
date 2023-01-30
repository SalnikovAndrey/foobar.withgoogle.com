"""
Read.me

Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired
 spectacularly. The Commander had been improving the structure of the ion flux converter tree, but something went
 terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others
 had their position labels blasted off. Commander Lambda is having her henchmen rebuild the ion flux converter tree by
 hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label
them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order of
that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

   7
 3   6
1 2 4 5

Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive
integers representing different flux converters - which returns a list of integers p where each element in p is the
label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For
example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect
binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root,
h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with
the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain
at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(3, [7, 3, 5, 1])
Output:
    -1,7,6,3

Input:
solution.solution(5, [19, 14, 28])
Output:
    21,15,29

"""
# from pprint import pprint

def solution(h, q):
    root_node = node_count = (2 ** h - 1)

    traverse_postorder = [i for i in range(1, root_node + 1)]
    leaf_count = 2 ** (h - 1)
    # print(f"Leaf count is: {leaf_count}")

    root_map = tree_builder(h)


    results = []

    for conv in q:
        if conv >= root_node:
            results.append(-1)
        elif conv < root_node:
            results.append(root_map[conv])

    # print("Results: ", results)

    return results


def tree_builder(h):
    root_node = node_count = (2 ** h - 1)

    traverse_postorder = [i for i in range(1, root_node + 1)]
    leaf_count = 2 ** (h - 1)
    # print(f"Leaf count is: {leaf_count}")
    # print(traverse_postorder)
    tree = {}

    for i in range(1, h + 1):
        tree[i] = []

    # print(tree)

    count = 0
    level = 1
    level_length = leaf_count

    for num in traverse_postorder:
        count += 1
        # print(f"Count: {count}")
        # print(f"Number: {num}")
        # print(f"Level: {level}")
        # print(f"Level_length: {level_length}")
        # print("tree[level]", len(tree[level]))

        if len(tree[level]) == level_length:
            level += 1
            level_length = int(level_length / 2)
            count = 1

        if num == root_node:
            tree[h] += [num]
            break
        if count == 1:
            tree[level] += [num]
            # traverse_postorder.remove(num)
        elif count == 2:
            tree[level] += [num]
            # traverse_postorder.remove(num)
        elif count == 3:
            tree[level + 1] += [num]
            # traverse_postorder.remove(num)
            count = 0
        # print(tree)
        # traverse_postorder.remove(num)

    # tree is a perfect tree with a given height
    # pprint(tree)

    root_map = {} # {child: parent}

    count = 0
    for lev in range(2, h + 1):
        # print("Level: ", lev)
        index = -1
        for item in tree[lev]:
            # print("Item: ", item)
            index += 1
            # print(tree[lev - 1][index])
            key = tree[lev - 1][index]
            root_map[key] = item
            index += 1
            # print(tree[lev - 1][index])
            key = tree[lev - 1][index]
            root_map[key] = item


    # pprint(root_map)
    return root_map

# print(solution(5, [7, 77, 5, 9]))

print(tree_builder(1))

print(solution(2, [7, 3, 5, 1]))

print(solution(5, [19, 14, 28]))
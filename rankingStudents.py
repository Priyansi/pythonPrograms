#!python3
import itertools as it

GREATER_THAN = '>'
NEWLINE = '\n'


def relation(A, B):
    if all([a > b for a, b in zip(A, B)]):
        return ">"
    elif all([a < b for a, b in zip(A, B)]):
        return "<"
    return "#"


def read_file(FILENAME):
    roll_marks = {}
    with open(FILENAME, 'r') as f:
        for line in f.readlines():
            roll, *marks = line.split()
            roll_marks[roll] = [int(mark) for mark in marks]
    return roll_marks


def all_relations(FILENAME):
    roll_marks = read_file(FILENAME)
    rolls = roll_marks.keys()
    rels = set()
    for roll1, roll2 in it.combinations(rolls, 2):
        rel = relation(roll_marks[roll1], roll_marks[roll2])
        if rel == ">":
            rels.add(roll1 + roll2)
        elif rel == "<":
            rels.add(roll2 + roll1)
    return rels


def all_removables(rels):
    def is_removable(first, middle, second):
        return first + middle in rels and middle + second in rels

    firsts = set([rel[0] for rel in rels])
    seconds = set([rel[1] for rel in rels])
    both = firsts & seconds
    return set(first+second for first in firsts for second in seconds if first + second in rels for middle in both if is_removable(first, middle, second))


def start_middle_end_rels(minimal):
    firsts = [rel[0] for rel in minimal]
    seconds = [rel[1] for rel in minimal]
    start_rels, end_rels, middle_rels = list(), list(), list()
    for rel in minimal:
        if rel[0] in seconds and rel[1] in firsts:
            middle_rels.append(rel)
        else:
            if rel[0] not in seconds:
                start_rels.append(rel)
            if rel[1] not in firsts:
                end_rels.append(rel)
    return start_rels, middle_rels, end_rels


def remove_common_start_end_rels(orders, start_rels, end_rels):
    for rel in start_rels:
        for x in end_rels:
            if rel[1] == x[0]:
                orders.append(rel+x[1])
                start_rels.remove(rel)
    return orders, start_rels, end_rels


def remove_same_start_end_rels(orders, start_rels, end_rels):
    for rel in start_rels:
        if rel in end_rels:
            orders.append(rel)
            start_rels.remove(rel)
            end_rels.remove(rel)
    return orders, start_rels, end_rels


def make_partial_orders(orders, start_rels, middle_rels, end_rels):
    def find_next_rel(rel):
        for middle_rel in middle_rels:
            if rel[-1] == middle_rel[0]:
                return middle_rel

    firsts_of_end_orders = [end_rel[0] for end_rel in end_rels]
    for rel in start_rels:
        partial_order = rel
        next_rel = find_next_rel(rel)
        while next_rel[1] not in firsts_of_end_orders:
            partial_order += next_rel[1]
            next_rel = find_next_rel(next_rel)
        end_order = end_rels[firsts_of_end_orders.index(next_rel[1])]
        orders.append(partial_order+end_order)
    return orders


def partial_orders(FILENAME):
    rels = all_relations(FILENAME)
    minimal = rels ^ all_removables(rels)
    orders = []
    start_rels, middle_rels, end_rels = start_middle_end_rels(minimal)
    orders, start_rels, end_rels = remove_same_start_end_rels(
        orders, start_rels, end_rels)
    orders, start_rels, end_rels = remove_common_start_end_rels(
        orders, start_rels, end_rels)
    return NEWLINE.join(GREATER_THAN.join(roll for roll in partial_order) for partial_order in make_partial_orders(orders, start_rels, middle_rels, end_rels))


print(partial_orders('roll_and_marks.txt'))

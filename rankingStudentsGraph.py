#!python3
import itertools as it
import os


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


def generate_graph(FILENAME):
    rels = all_relations(FILENAME)
    minimal = rels ^ all_removables(rels)
    with open("partial_orders.dot", "w") as f:
        print("digraph partial_orders {", file=f)
        for relation in minimal:
            print("\t%s -> %s;" % (relation[0], relation[1]), file=f)
        print("}", file=f)

    os.system("dot -T png -o partial_orders.png partial_orders.dot")


if __name__ == "__main__":
    generate_graph('roll_and_marks.txt')

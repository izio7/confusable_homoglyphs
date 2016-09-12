# -*- coding: utf-8 -*-
import pickle

try:
    with open('categories.pkl', 'r') as file:
        categories_data = pickle.load(file)
except IOError:
    try:
        from generate_categories import generate
        categories_data = generate()
    except:
        raise Exception('Datafile not found, datafile generation failed!')


def aliases_categories(chr):
    l = 0
    r = len(categories_data['code_points_ranges']) - 1
    c = ord(chr)

    # binary search
    while r >= l:
        m = (l + r) // 2
        if c < categories_data['code_points_ranges'][m][0]:
            r = m - 1
        elif c > categories_data['code_points_ranges'][m][1]:
            l = m + 1
        else:
            return (
                categories_data['iso_15924_aliases'][categories_data['code_points_ranges'][m][2]],
                categories_data['categories'][categories_data['code_points_ranges'][m][3]])
    return 'Unknown', 'Zzzz'


def alias(chr):
    a, _ = aliases_categories(chr)
    return a


def category(chr):
    _, a = aliases_categories(chr)
    return a


def unique_aliases(string):
    cats = [alias(c) for c in string]
    return set(cats)

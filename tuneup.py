#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Justin Miller after going thru the 3/24 demo"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        p = cProfile.Profile()
        p.enable()
        result = func(*args, **kwargs)
        p.disable()
        ps = pstats.Stats(p).strip_dirs().sort_stats("cumulative")
        ps.print_stats(10)
        return result
    return inner

def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns title if it is within movies list"""
    return title in movies

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies.sort()
    duplicates = [m1 for m1, m2 in zip(movies[1:], movies[:-1]) if m1 == m2]
    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie, movies):
    #         duplicates.append(movie)

    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt="find_duplicate_movies('movies.txt')",
        setup='from __main__ import find_duplicate_movies'
        )
    runs_per_repeat = 5
    num_repeats = 7
    result = t.repeat(repeat=num_repeats, number=runs_per_repeat)
    best_time = min(result) / float(runs_per_repeat)
    print("Best time across {} repeats of {} runs per repeat: {} sec".format(num_repeats, runs_per_repeat, best_time))


def main():
    """Computes a list of duplicate movie entries"""
    # timeit_helper()
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()

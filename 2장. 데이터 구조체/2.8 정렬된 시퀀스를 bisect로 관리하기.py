import bisect
import random
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    # if sys.argv[-1] == 'left':
    #     bisect_fn = bisect.bisect_left
    # else:
    #     bisect_fn = bisect.bisect_right
    
    print('DEMO :', bisect.bisect_right.__name__)
    print('haystack->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect.bisect_right)

    print('-'*70)

    print('DEMO :', bisect.bisect_left.__name__)
    print('left')
    demo(bisect.bisect_left)

    print('-'*70)

    def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]
    
    grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(grades)

    ############################
    print('-'*70)
    SIZE = 7
    random.seed(1729)
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        print('%2d -> '% new_item, my_list)
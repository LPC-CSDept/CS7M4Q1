
from functools import reduce
import pandas as pd


def makeList():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    return students


def printList(students):
    for student in students:
        for k, v in student.items():
            print(f'{k} -> {v}', end='\t')
        print()


def scorebySubject(students):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def findStudents(students):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def getAvgList(students):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    # (1) makeList
    students = makeList()
    # (2) printList
    printList(students)
    # (3) scorebySubject
    retval = scorebySubject(students)
    for k, v in retval.items():
        print(f'{k} -> {v}', end='\t')
    print()
    # (4) findStudents
    retval = findStudents(students)
    printList(retval)
    # (5) getAvgList
    retval = getAvgList(students)
    print(retval)


if __name__ == '__main__':
    main()

import main
import io
import sys
import re
import math
import types


def test_main_1():

    main.main()
    students = main.makeList()
    main.printList(students)
    assert len(students) == 5


def test_main_2():
    students = main.makeList()
    ret = main.scorebySubject(students)
    assert len(ret) == 4
    assert sum(ret['1st']) == 490
    assert sum(ret['2nd']) == 430
    assert sum(ret['3rd']) == 400
    assert sum(ret['4th']) == 400


def test_main_3():
    students = main.makeList()
    ret = main.findStudents(students)
    assert len(ret) == 3
    assert ret[0]['id'] == 1003
    assert ret[1]['id'] == 1004
    assert ret[2]['id'] == 1005


def test_main_4():
    students = main.makeList()
    ret = main.getAvgList(students)
    assert len(ret) == 5
    assert ret[0] == 77.5
    assert ret[1] == 82.5
    assert ret[4] == 87.5

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..utils import cached_property, environ_property

print("invoke student, begin process function")

def getSex():
    return 'M'

class Student(object):

    @cached_property
    def sex(self):
        # calculate something important here
        return getSex()

def test_cache_property():
    st = Student()
    print(dir(st))
    sex = st.sex
    print(sex)

class Test(object):
    environ = {'sex': 'M'}
    #sex_val成员是读写描述符
    sex_val = environ_property('sex')

def test_enviroment_property():
    test = Test()
    print(test.sex_val)
    test.sex_val = 'F'


def start_cache():
    test_cache_property()
    test_enviroment_property()


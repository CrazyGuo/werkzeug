#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..contrib.sessions import _urandom, generate_key
from ..contrib.sessions import ModificationTrackingDict
from ..contrib.sessions import FilesystemSessionStore

def test_function():
    #测试随机函数得到的随机数
    val_random = _urandom()
    print(val_random)
    #生成session_id的生成函数
    session_id = generate_key()
    print(session_id)
    #每个session_id的长度都为40
    session_len = len(session_id)
    print(session_len)

class SimpleSlots(object):
    __slots__ = ('name',)

    def __init__(self, name=" "):
        self.name = name

def test_ModificationTrackingDict():
    mdict = ModificationTrackingDict({'name': 'Matthew'})
    val = mdict.get('name', None)
    print(val)
    #__slots__中不存在sex属性名，以下竟然不报错
    mdict.sex = 'M'
    #属性改变，触发回调函数
    mdict['sex'] = 'F'
    #非字典形式的slots类
    simple_slot = SimpleSlots(name="Guo Jing")
    #设置了非slots中之外的属性，程序报错
    try:
        simple_slot.sex = 'M'
    except Exception as e:
        print(e)
    #两者产生差异的原因是是否存在__dict__属性
    print(dir(mdict))
    print(dir(simple_slot))

def test_filestore_session():
    store = FilesystemSessionStore("C:\Works")
    session_obj = store.new()
    print(session_obj)
    session_obj['foo'] = [1, 2, 3]
    print(session_obj)
    session_dic = dict(session_obj)
    print(session_dic)
    store.save(session_obj)
    #根据sid获取保存在文件中的对象
    file_session= store.get(session_obj.sid)
    print(file_session['foo'])
    #获取文件下的所有sid
    all_list = store.list()
    print(all_list)

def start_session_app():
    test_function()
    test_ModificationTrackingDict()
    test_filestore_session()
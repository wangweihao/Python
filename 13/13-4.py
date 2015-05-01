#!/usr/bin/env python
#coding:UTF-8

import shelve

class user_db(object):
    #用户登录名，密码及时间戳(上次登录) (name:[passwd, time])
    user_info = {}
    #resource
    resource = []

    def __init__(self, data):
        try:
            isinstance(data, str)
        except (ValueError, TypeError):
            data = str(data)
        
        #读取数据库的数据
        p = shelve.open(data)
        for name in p.keys():
            self.user_info[name] = p[name]
            pass
        p.close()

    def __del__(self):
        p = shelve.open('data')
        for ever_user in self.user_info.keys():
            p[ever_user] = self.user_info[ever_user]
        p.close()

    def Enter(self):
        nm = raw_input('name:')
        pw = raw_input('passward:')
        if self.user_info[nm] == pw:
            print 'Enter success!'
        else:
            print 'Enter error!'

    def Register(self):
        nm = raw_input('name:')
        pw = raw_input('passward:')
        opw = raw_input('once passward:')
        if pw == opw:
            self.user_info[nm] = pw
        else:
            print 'input error! try again!'


if __name__ == '__main__':
    db = user_db('data')
    db.Enter()

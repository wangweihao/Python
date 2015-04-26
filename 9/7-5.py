#!/usr/bin/env python
#coding:UTF-8

import time

db = []
tp = {}

#[{name:password}, tima]
#[name:[password, time]]

def GetNowTime():
    #time.strftime('%H-%M-%S')
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def newuser():
    prompt = 'login desired: '
    while True:
        flag = False
        name = raw_input(prompt)
        for i in range(len(db)):
            #gain {name:pwd} and try newname in map?
            temp = db[i][0]
            if name in temp:
                flag = True
                break
        if flag == False:
            break
        else:
            print 'this name have exist, please try again'


    pwd = raw_input('passwd: ')
    time = GetNowTime()
    tuple = ({name:pwd}, time)
    db.append(tuple)

def olduser():
    while True:
        index = 0
        while True:
            flag = False
            name = raw_input('login:')
            for i in range(len(db)):
                temp = db[i][0]
                if name in temp:
                    flag = True
                    index = i
                    break
            if flag == True:
                break
            else:
                print 'name error, please input again'
        pwd = raw_input('passwd:')
        passwd = db[index][0].get(name)
        if passwd == pwd:
            print 'welcome back', name
            print 'You already logged in at %s' % db[index][1]
        else:
            print 'login incorrect'
        break

def manager():
    prompt = """
 (D)elete user
 (S)how all user
 (Q)uit

 Enter choice: """
    while 1:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except (EOFError, KeyboardInterrupt):
            choice = 'q'
        print '\n You picked:[%s] ' % choice
        if choice not in 'dsq':
            print 'invaild option ,try again'
        elif choice == 'q':
            break
        elif choice == 's':
            for i in range(len(db)):
                print db[i][0].values(),
        elif choice == 'd':
            delet = raw_input('input want delete user:')
            for i in range(len(db)):
                if delet in db[i][0]:
                    print 'delete %s' % delet
                    del db[i]
                    break


def showmenu():
    prompt = """
 (N)ew User Login
 (E)xisting User Login
 (Q)uit
 (M)anager

 Enter choice: """

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\n You picked:[%s]' % choice
            if choice not in 'neqm':
                print 'invaild option ,try again'
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()
        if choice == 'm':
            manager()


if __name__ == '__main__':
    showmenu()

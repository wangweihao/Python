#!/usr/bin/env python
#coding:UTF-8

prompt = """
1.save
2.draw
3.lend
4.loan
5.cancel

   Enter:"""

my_db = [100, 20, 200000]

def showmenu():
    while 1:
        choice = input(prompt)
        if choice == 1:
            new_mony = input('save mony:')
            my_db[0] = new_mony
        elif choice == 2:
            draw_mony = input('load mony:')
            my_db[0] -= draw_mony
        elif choice == 3:
            lend_mony = input('lend mony:')
            my_db[0] += lend_mony
        elif choice == 4:
            loan_mony = input('loan_mony:')
            my_db[0] += loan_mony
            my_db[2] -= loan_mony
        elif choice == 5:
            



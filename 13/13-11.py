#!/usr/bin/env python
#coding:UTF-8


class Cart(object):
    stuff = []
    def __init__(self, obj):
        self.stuff = obj

    def add(self, obj):
        self.stuff.push(obj)

    def pull(self, obj):
        self.stuff.remove(obj)

    def Show(self):
        for one in self.stuff:
            print one

class Item(object):
    def __init__(self, nm, num, price):
        self.name = nm
        self.num = num
        self.price = price

    def __str__(self):
        return 'name:%s,num:%d,price:%.2f' %(self.name, self.num, self.price)

class User(object):
    cart = []
    def __init__(self, obj):
        self.cart = obj

    def add(self, obj):
        self.cart.push(obj)

    def pull(self, obj):
        self.cart.remove(obj)

    def Show(self):
        for c in self.cart:
            print c.Show()


if __name__ == '__main__':
    item1 = Item('a', 10, 1.1)
    print 'item---------------------'
    print item1
    item2 = Item('b', 20, 2.2)
    item3 = Item('c', 30, 3.3)
    item4 = Item('d', 40, 4.4)
    cart1 = Cart([item1, item2])
    print 'cart---------------------'
    cart1.Show()
    cart2 = Cart([item3, item4])
    user = User([cart1, cart2])
    print 'user---------------------'
    user.Show()



#!/usr/bin/python
from ipython_genutils import encoding

import analyze
import global_constants
import cluster


def main():
    #
    key_list = global_constants.init()
    #
    # fruit = analyze.createAPIConnection(
    #     key_list['example_pic_URL'],
    #     key_list['subscription_key']
    # )
    # # print len(list3)
    # word = fruit[0].encode('ascii', 'ignore')+" "
    # list=[]
    # list.append(word.title())
    # print("mystring is :"+str(list) )
    # # list = ['Pear']
    # analyze.findByKeyword(list )

    # print analyze.makelistofingredients()
    cluster.clustering()


main()

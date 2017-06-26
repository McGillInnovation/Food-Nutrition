#!/usr/bin/python

import analyze
import global_constants

def main():

    key_list = global_constants.init()

    analyze.createAPIConnection(
    #     key_list['example_pic_URL'],
    #     key_list['subscription_key']
    )
    # list3 = ["Organic", "Spelt", "Berries"]
    # print len(list3)
    #
    # analyze.findByKeyword(list3)

main()

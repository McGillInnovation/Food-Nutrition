#!/usr/bin/python

import analyze
import global_constants

def main():

    key_list = global_constants.init()

    analyze.createAPIConnection(
        key_list['example_pic_URL'],
        key_list['subscription_key']
    )

main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


word_dict = {'car': '車'}


def main():

    for key_word in word_dict.keys():
        print ('What is the Japanese word for ' + key_word)
        guessword = input()

        if guessword == word_dict[key_word]:
            print ('correct')
        else:
            print ('incorrect')



main()
    #TODO get input from user

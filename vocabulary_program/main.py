#!/usr/bin/env python
# -*- coding: utf-8 -*-


word_dict = {'car': '車'}


def main():

    for key_word in word_dict.keys():
        print('What is the Japanese word for: {}'.format(key_word))
        guessword = input()

        if guessword == word_dict[key_word]:
            print('Correct! The Japanese word for {} is: {}'.format(key_word, word_dict[key_word]))
        else:
            print ('incorrect')



main()

#TODO score user
#TODO add timer
#TODO continue midway in the test
#TODO load dictionary
#TODO if user guessed wrong, try again

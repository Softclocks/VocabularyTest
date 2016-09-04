#!/usr/bin/env python
# -*- coding: utf-8 -*-


word_dict = {'car': '車', 'fish': 'sakana'}

def main():
    score = 0
    for key_word in word_dict.keys():
        print('What is the Japanese word for: {}'.format(key_word))
        while True:
            guessword = input()

            if guessword == word_dict[key_word]:
                score += calculate_score(word_length=len(word_dict[key_word]))
                print('Correct! The Japanese word for {} is: {}'.format(key_word, word_dict[key_word]))
                print('Your current score is {}'.format(score))
                break

            else:
                print('Incorrect, {} is not the Japanese word for {} '.format(guessword, key_word))

def calculate_score(word_length):
    return word_length ** 2

main()

# TODO add timer
# TODO continue midway in the test
# TODO load dictionary
# TODO allowing user to choose between dictionaries

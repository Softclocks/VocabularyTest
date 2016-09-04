#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def main():
    score = 0
    for key_word in word_dict.keys():
        print('What is the Japanese word for: {}'.format(key_word))
        while True:
            guessword = input()

            if guessword == word_dict[key_word]:
                score += calculate_score(len(word_dict[key_word]))
                print('Correct! The Japanese word for {} is: {}\nYour current score is {}'
                      .format(key_word, word_dict[key_word], score))
                break

            else:
                print('Incorrect, {} is not the Japanese word for {} '.format(guessword, key_word))

def calculate_score(word_length=1):
    return word_length ** 2

def load_dictionary(file_path):
    return json.load(open(file_path))

word_dict = load_dictionary('C:/Users/Admin/PycharmProjects/VocabularyTest/dict.json')
main()

# TODO add timer
# TODO continue midway in the test
# TODO load dictionary
# TODO allowing user to choose between dictionaries

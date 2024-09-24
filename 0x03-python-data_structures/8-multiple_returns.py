#!/usr/bin/python3

def multiple_returns(sentence):

    size = len(sentence)
    if size != 0:
        first_ch = sentence[0]
    else:
        first_ch = "None"
    return (size, first_ch)

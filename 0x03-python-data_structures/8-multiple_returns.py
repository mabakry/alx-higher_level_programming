#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first = None
    else:
        first = sentence[0]

    t = (len(sentence), first)
    return (t)

import unittest
from program import charCount,panagram,avg


def testsame():
    ret = charCount("aa")
    assert ret=={"a":2}

def testMultiple():
    ret = charCount("aabbbcccc")
    assert ret=={"a":2,"b":3,"c":4}


def testEmpty():
    ret = charCount("")
    assert ret=={}    


def test1():
    ret = panagram("the quick brown fox jumps over a lazy dog")
    assert ret == True


def test2():
    ret = panagram("the quick brown fox jumped over a lazy dog")
    assert ret == False

def test_avg_pos():
    ret = avg([1,2,3,6])
    assert ret == 3

def test_avg_neg():
    ret = avg([-3,-4,-6,-7])
    assert ret ==-5


def test_avg_empty():
    ret = avg([])    
    assert ret == None




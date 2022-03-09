import string
def charCount(word):
    d = {}

    for character in word:

        if character in d:
            d[character] += 1
        else:
            d[character] = 1
    return d


def panagram(s):
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True    


def avg(data):
    sum=0
    if len(data)<=0:
        return None
    
    for i in data:
        sum = sum+i
    return sum/len(data)  

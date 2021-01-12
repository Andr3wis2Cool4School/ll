def findTheDifference(s, t):
    all = s + t
    list_all = list(all)
    diff = 0
    for i in list_all:
        diff ^= ord(i)
    return chr(diff)


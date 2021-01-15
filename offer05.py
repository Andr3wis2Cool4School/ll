def replaceSpace(s):
    res = list()
    for i in s:
        if i == ' ':
            res.append('%20')
        else:
            res.append(i)

    return ''.join(res)

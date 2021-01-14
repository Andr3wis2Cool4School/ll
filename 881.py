def numRescueBoats(people, limit):
    if people is None or len(people) == 0:
        return 0
    people.sort()
    # 对撞指针
    i = 0
    j = len(people)-1
    res = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1 
        j -= 1 
        res += 1
    return res 


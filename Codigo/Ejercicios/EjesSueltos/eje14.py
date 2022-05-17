#Eje 14

def dictdiff(dic1,dic2):
    dic0 = {}
    for key in dic1:
        if dic1.get(key) != dic2.get(key):
            dic0[key] = [dic1.get(key), dic2.get(key)]
    for key in dic2:
        if dic2.get(key) != dic1.get(key):
            dic0[key] = [dic1.get(key), dic2.get(key)]

    print(dic0)


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}

d5 = {'a': 1, 'b': 2, 'd': 4}

dictdiff(d1,d5)

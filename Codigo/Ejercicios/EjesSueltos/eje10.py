#Eje 10
import operator

def alfabetizar(diccionario):
    print(sorted(diccionario,key=operator.itemgetter('last' , 'first')))


PEOPLE = [{'first': 'Reuven', 'last': 'Lerner'},
{'first': 'Donald', 'last': 'Trump'},
{'first': 'Vladimir', 'last': 'Putin'},
{'first': 'Álvaro', 'last': 'Raso'},
{'first': 'Jose', 'last': 'Lopez'}]

alfabetizar(PEOPLE)
#Eje 9

def dic(*diccionario):
    print(diccionario)
    total = {}
    for x in diccionario:
        total.update(x)

    print(total)



color_code = dict([('RED', 100), ('GREEN', 200), ('BLUE', 110)])
goals_by_player = {"Erling Haaland": 27, "Leo Messi": 29, "Cristiano Ronaldo": 31,"Robert Lewandowski": 45, "Kylian Mbappe": 20}
urjc_world_coordinates = dict(lat=40.335913308819116, lon=-3.8732171058654785)
color_code2 = dict([('RED', 10001), ('GREEN', 20001), ('BLUE', 11001)])

dic(color_code,goals_by_player,urjc_world_coordinates,color_code2)
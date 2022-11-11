def transforma_base(t): 
    lista1 = [] 
    lista2 = []
    lista3 = []
    dic = {}
    for i in range(len(t)):
        if t[i]['nivel'] == 'facil':
            lista1.append(t[i])
            dic['facil'] = lista1
        if t[i]['nivel'] == 'medio':
            lista2.append(t[i])
            dic['medio'] = lista2
        if t[i]['nivel'] == 'dificil':
            lista3.append(t[i])
            dic['dificil'] = lista3
    return dic
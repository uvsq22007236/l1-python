def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    res = []
    while True:
        res.append (n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else :
            n = 3 * n + 1
    return res 

print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max +1):
        syracuse(i)

        return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    cpt = 0
    while True:
        if n == 1:
            break
        cpt += 1
        if n % 2 == 0:
            n = n // 2
        else :
            n = 3 * n + 1
    return cpt

print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1, n_max +1)]
    

print(tempsVolListe(100))
# Fonction qui retourne le nombre de chiffres
def Nb_Chiffres(n):
    return len(str(n))


# Fonction qui vérifie si nb est un nombre de Keith
def Keith(nb):

    k = Nb_Chiffres(nb)

    if k < 2:
        return False

    # récupérer les chiffres du nombre
    suite = []

    for chiffre in str(nb):
        suite.append(int(chiffre))


    terme = 0

    while terme < nb:

        # somme des k derniers termes
        somme = 0

        for i in range(k):
            somme += suite[len(suite)-k+i]


        terme = somme

        # ajouter le nouveau terme
        suite.append(terme)


    return terme == nb
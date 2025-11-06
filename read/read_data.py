import csv 


def list_film_csv():
    list_film = []
    fichier = open("data/movies.csv", "r")
    filmCSV = csv.reader(fichier,delimiter=",")
    for line in filmCSV:
        if not line:  # ligne vide
            continue
        list_film.append([line[0],line[1],line[2],line[3],line[4]])
    fichier.close()
    return list_film      

def recherche_film_par_titre(list_film,film_recherche):
    for film in list_film:
        if film[1] == film_recherche:
            return film[0]

def recherche_film_par_age_requis(list_film,age):
     for film in list_film:
         if film[4].isdigit():
            if int(film[4]) <= age :
                print(film[1])

def rechercher_film_par_genre(list_film,genre):
    for film in list_film:
        if film[3] == genre :
                print(film[1])

def recherche_film_par_année(list_film,debut,fin):
    for film in list_film:
        if film[2].isdigit():
            if int(film[2]) > debut and int(film[2]) < fin :
                print(film[1])     


def menu_recherche():
    print("1. Rechercher un film par titre : ")
    print("2. Rechercher un film par age requis : ")
    print("3. Rechercher un film par genre : ")
    print("4. Rechercher un film par annee : ")
    print("5. Sortir : ")
    choix = input("Tapez votre choix")
    match choix :
        case "1":
            titre = input("Saisissez votre titre : ")
            print(recherche_film_par_titre(list_film_csv(),titre))
        case "2":
            choix = int(input("Saisir l'age requis : "))
            recherche_film_par_age_requis(list_film_csv(),choix)
        case "3":
            choix = input("Saisir le genre : ")
            rechercher_film_par_genre(list_film_csv(),choix)
        case "4":
            debut = int(input("Saisir l'année de debut : "))
            fin = int(input("Saisir l'année de fin : "))
            recherche_film_par_année(list_film_csv(),debut,fin)
        case "5":
            return False

while menu_recherche():
    pass

                  
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



def menu_recherche():
    print("1. Rechercher un film par titre : ")
    print("2. Rechercher un film par age requis : ")
    print("3. Rechercher un film par genre : ")
    choix = input("Tapez votre choix")
    match choix :
        case "1":
            print(recherche_film_par_titre(list_film_csv(),"Parasite"))
        case "2":
            choix = int(input("Saisir l'age requis : "))
            recherche_film_par_age_requis(list_film_csv(),choix)
        case "3":
            choix = input("Saisir le genre : ")
            rechercher_film_par_genre(list_film_csv(),choix)

menu_recherche()
                  
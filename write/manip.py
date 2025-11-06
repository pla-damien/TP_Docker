from models.Movie import Movie
from exeptions.InvalidAgeLimitException import InvalidAgeLimitException
import csv
import os

list_film = [] 
def menu():
    print("Que voulez vous faire : ")
    print("1. Ajouter")
    print("2.Modifier")
    print("3.Supprimer")
    print("0.Sortir")
    choix = input("Saisissez votre choix : ")
    return choix



def saisie_film():
    titre = input("Titre : ")
    annee_production = input("Année : ")
    genre = input("Genre : ")
    age_limite = input("Age limite : ")
    id2 = int(Movie.recup_id(read_csv()))
    id2 +=1
    film = Movie(id2,titre,annee_production,genre,age_limite)
    return film
   
def write_csv(film:Movie):
    fichier = open("data/movies.csv", "at")
    filmCSV = csv.writer(fichier,delimiter=",")
    filmCSV.writerow([film.id,film.titre,film.annee_production,film.genre,film.age_limite])
    fichier.close()

def afficher_film():
    list_film = read_csv()
    for film in list_film:
        print(film.id,film.titre,film.annee_production,film.genre,film.age_limite)
    print("Quel film voulez vous selectionner ? ")
    choix = int(input(print("Tapez son id : ")))
    return choix
    
def read_csv():
    list_film = []
    fichier = open("data/movies.csv", "r")
    filmCSV = csv.reader(fichier,delimiter=",")
    for line in filmCSV:
        if not line:  # ligne vide
            continue
        list_film.append(Movie(line[0],line[1],line[2],line[3],line[4]))
    fichier.close()
    return list_film        


def menu_update_film(id:int):
    list_film = []
    list_film = read_csv()
    print("Quelle information souhaité vous modfier?")
    choix = input(print("1.Titre","2.Année","3.Genre","4.Age"))
    match choix:
        case "1":
            list_film[id].titre = input("Tapez le nouveau titre")
        case "2":
            list_film[id].Annee_production = input("Tapez la nouvelle année")   
        case "3":
            list_film[id].genre = input("Tapez le nouveau genre")
        case "4":
            list_film[id].age_limite = input("Tapez le nouveau age limite")
    update_movie_csv(list_film)

def update_movie_csv(list_film):
    open("data/movies.csv", "w").close()
    fichier = open("data/movies.csv", "a",newline='')
    filmCSV = csv.writer(fichier,delimiter=",")
    id = 1
    for film in list_film:
        filmCSV.writerow([id,film.titre,film.annee_production,film.genre,film.age_limite])
        id +=1
    fichier.close()

def delete_movie():
    list_film = read_csv()
    choix =afficher_film()
    list_film.pop(choix-1)
    update_movie_csv(list_film)





while True :
    choix = menu()
    match choix:
        case "1":
            try:
                film = saisie_film()
                write_csv(film)
            except InvalidAgeLimitException as e:
                print(e)
            else:
                print("Saisie OK : ")
        case "2":
            id = afficher_film()
            menu_update_film(id)
        case "3":
            delete_movie()
        case "0":
            break

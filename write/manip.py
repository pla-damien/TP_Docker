from models.Movie import Movie
from exeptions.InvalidAgeLimitException import InvalidAgeLimitException
import csv


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
    verif_age(age_limite)
    film = Movie(Movie.id,titre,annee_production,genre,age_limite)
    return film

def verif_age(age):
    if age.isalnum() == False:
        raise InvalidAgeLimitException()


def write_csv(film:Movie):
    fichier = open("data/movies.csv","wt",newline=";")
    filmCSV = csv.writer(fichier,delimiter=";")
    filmCSV.writerow([film.titre,film.annee_production,film.genre,film.age_limite])
    fichier.close()






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
            pass
        case "0":
            break

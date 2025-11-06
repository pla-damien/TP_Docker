# 🎬 Gestionnaire de Films (Python CLI)

Ce projet est une petite application **en ligne de commande** permettant de **gérer une base de données de films** à l’aide d’un fichier CSV.  
Elle permet d’**ajouter**, **modifier**, **supprimer** et **afficher** des films enregistrés localement.

---

## 🧩 Fonctionnalités

- 📥 **Ajouter** un film (titre, année, genre, âge limite)
- ✏️ **Modifier** les informations d’un film existant
- ❌ **Supprimer** un film
- 📃 **Afficher** la liste des films
- 💾 Sauvegarde automatique dans un fichier CSV (`data/movies.csv`)

---

## 🧱 Structure du projet

```
project/
├── data/
│   └── movies.csv
├── exeptions/
│   └── InvalidAgeLimitException.py
├── models/
│   └── Movie.py
├── main.py   ← (le fichier contenant le code du programme)
└── README.md
```

---

## ⚙️ Installation et exécution

1. **Cloner le dépôt** ou copier les fichiers localement :
   ```bash
   git clone https://github.com/ton-repo/gestion-films.git
   cd gestion-films
   ```

2. **Créer les dossiers nécessaires** :
   ```bash
   mkdir data
   touch data/movies.csv
   ```

3. **Lancer le programme** :
   ```bash
   python main.py
   ```

---

## 🧠 Utilisation

### Menu principal
Lors de l’exécution, un menu s’affiche :

```
Que voulez-vous faire :
1. Ajouter
2. Modifier
3. Supprimer
0. Sortir
```

- **1 : Ajouter** → Permet d’ajouter un film avec son titre, année, genre et âge limite  
- **2 : Modifier** → Affiche la liste des films et permet de modifier une information spécifique  
- **3 : Supprimer** → Supprime un film de la base  
- **0 : Sortir** → Ferme le programme  

---

## 🗂️ Format du fichier CSV

Le fichier `data/movies.csv` contient les films enregistrés au format :

```
id,titre,annee_production,genre,age_limite
1,Inception,2010,SF,12
2,Gladiator,2000,Action,16
```

---

## 🧱 Classes utilisées

### `Movie` (dans `models/Movie.py`)
Représente un film avec les attributs :
- `id` : identifiant unique
- `titre` : titre du film
- `annee_production` : année de sortie
- `genre` : type de film
- `age_limite` : âge minimal requis pour le visionner

---

## 🚨 Gestion des exceptions

Le programme utilise une exception personnalisée :

### `InvalidAgeLimitException`
Située dans `exeptions/InvalidAgeLimitException.py`, elle est levée si la limite d’âge saisie n’est pas valide (par exemple : non numérique ou négative).

---

## 🧰 Fonctions principales

| Fonction | Description |
|-----------|--------------|
| `menu()` | Affiche le menu principal et retourne le choix de l’utilisateur |
| `saisie_film()` | Saisie des informations d’un film et création d’un objet `Movie` |
| `write_csv(film)` | Ajoute un film dans le fichier CSV |
| `read_csv()` | Lit la liste des films à partir du fichier CSV |
| `afficher_film()` | Affiche tous les films et retourne l’ID choisi |
| `menu_update_film(id)` | Permet de modifier un film à partir de son ID |
| `update_movie_csv(list_film)` | Met à jour le fichier CSV complet |
| `delete_movie()` | Supprime un film à partir de son ID |

---

## 🧪 Exemple d’exécution

```
Que voulez vous faire :
1. Ajouter
2. Modifier
3. Supprimer
0. Sortir
Saisissez votre choix : 1

Titre : Matrix
Année : 1999
Genre : Science-fiction
Age limite : 12

Saisie OK :
```

---

## 🧼 Améliorations possibles

- Vérification de la validité des champs (année, âge limite, etc.)
- Gestion d’erreurs plus fine (fichier manquant, saisie invalide)
- Interface graphique (Tkinter, PyQt…)
- Persistance en base de données (SQLite, PostgreSQL…)

---

## 🧑‍💻 Auteur

**Nom :** Damien PLA 
**Projet :** Gestionnaire de films Python  
**Licence :** Libre / Open Source

---

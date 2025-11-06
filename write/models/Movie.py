class Movie() :
    id = 31
    def __init__(self,id:int,titre:str,anne_production:int,genre:str,age_limite:int):
        self.id = id 
        self.titre = titre
        self.annee_prodution = anne_production
        self.genre = genre
        self.age_limite = age_limite
        id = id + 1

    def __str__(self):
        print(f"le film {self.titre}est du genre {self.genre} et est sortie en {self.annee_prodution}. Il faut avoir {self.age_limite} pour le voir")
    
    @classmethod
    def recup_id():
        return id 
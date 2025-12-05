class Voiture:
    def __init__(self, immatriculation, marque:str, proprietaire:str, abonnement:str)->None:
        self.immat = immatriculation
        self.marque = marque
        self.proprio = proprietaire
        self.sub = abonnement

    def __str__(self)->str:
        return f"Le propriétaire est {self.proprio}, immatriculé au {self.immat} de marque {self.marque}. Est-il abonné ? {self.sub}"

    def releve_immatriculation(self):
        return self.immat

    def nom_proprio(self):
        return self.proprio

    def constructeur(self):
        return self.marque

    def abonner(self):
        if self.sub == "Oui" or self.sub == "oui":
            return True
        else:
            return False


class Parking:
    
    def __init__ (self, etages:int, places, reserver_sub)->None:
        self.etage = etages
        self.place = places
        self.reserver_sub = reserver_sub
    
    def __str__(self)->str:
        return f"Le parking possède {self.etage} étages avec {self.place} places, dont {self.reserver_sub} réservées aux abonnés."
    
    def places_dispo(self):
        lst = []
        for i in range(self.etage):
            floor = f"{i}"
            for j in range(self.place):
                if j < 10:
                    pla = f"0{j}"
                    lst.append(floor+pla)
                else:
                    pla = f"{j}"
                    lst.append(floor+pla)
        return lst

    def place_libre_occuper(self, voiture:Voiture):
            for i in range(len(self.places_dispo())):
                if self.places_dispo()[i] == voiture.releve_immatriculation():
                    return f"La place {self.places_dispo()[i]} est occupée par la voiture immatriculée {voiture.releve_immatriculation()}."
            return f"La voiture immatriculée {voiture.releve_immatriculation()} n'a pas de place attribuée."
        
    def attribuer_place(self, voiture:Voiture):
        for i in range(len(self.places_dispo())):
            if self.places_dispo()[i] != voiture.releve_immatriculation():
                return f"La place {self.places_dispo()[i]} a été attribuée à la voiture immatriculée {voiture.releve_immatriculation()}."
        return f"Aucune place disponible pour la voiture immatriculée {voiture.releve_immatriculation()}."

    def abonner_voiture(self, voiture:Voiture):
        if voiture.abonner():
            return f"La voiture immatriculée {voiture.releve_immatriculation()} est abonnée au parking."
        else:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} n'est pas abonnée au parking."
        
    def desabonner_voiture(self, voiture:Voiture):
        if not voiture.abonner():
            return f"La voiture immatriculée {voiture.releve_immatriculation()} n'est pas abonnée au parking."
        else:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} a été désabonnée du parking."
        
    def place_reservee_abonne(self, voiture:Voiture):
        if voiture.abonner():
            return f"La voiture immatriculée {voiture.releve_immatriculation()} peut accéder aux places réservées aux abonnés."
        else:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} ne peut pas accéder aux places réservées aux abonnés."
    
    def renvoyer_liste_places_abonnees_occupees(self):
        liste_abonnes = []
        for i in range(len(self.places_dispo())):
            liste_abonnes.append(self.places_dispo()[i])
        return liste_abonnes
    
    def nombre_places_libres_sans_compter_place_abonnees(self):
        total_places = self.etage * self.place
        places_abonnees = self.reserver_sub
        places_libres = total_places - places_abonnees
        return places_libres
    
    def representation_niveau_du_parking_texte(self):
        representation = ""
        for i in range(self.etage):
            representation += f"Étage {i}:\n"
            for j in range(self.place):
                if j < 10:
                    representation += f"[0{j}] "
                else:
                    representation += f"[{j}] "
            representation += "\n"
        return representation

   
    
    


print("=== TEST DE LA CLASSE VOITURE ===")
v1 = Voiture("AA123AA", "Citroën", "René Latope", "Oui")

print(v1)                              # Test **str**
print(v1.releve_immatriculation())     # Test immatriculation
print(v1.nom_proprio())                # Test nom propriétaire
print(v1.constructeur())               # Test marque
print(v1.abonner())                    # Test abonnement (True/False)

print("\n=== TEST DE LA CLASSE PARKING ===")
p = Parking(2, 5, 2)                   # 2 étages, 5 places par étage, 2 réservées aux abonnés

print(p)                               # Test **str**
print(p.places_dispo())                # Affiche toutes les places générées
print(p.place_libre_occuper(v1))       # Vérifie si la voiture occupe une place
print(p.attribuer_place(v1))           # Attribue une place
print(p.abonner_voiture(v1))           # Vérifie si elle est abonnée
print(p.desabonner_voiture(v1))        # Désabonne la voiture
print(p.place_reservee_abonne(v1))     # Vérifie si elle peut accéder aux places réservées
print(p.renvoyer_liste_places_abonnees_occupees())  # Liste des places d'abonnés occupées
print(p.nombre_places_libres_sans_compter_place_abonnees())  # Places libres hors abonnés
print(p.representation_niveau_du_parking_texte())   # Affiche la structure du parking


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
    #5 étages avec des places numéroté de 1 à 480(80/e)
    #place dispo 
    #emplacement précis occupé
    #donné place libre à une nouvelle voiture
    def __init__(self, place, etage, reserver_sub):
        self.place = place
        self.etage = etage
        self.reserver_sub = reserver_sub

        self.liste_places = self.creation_place()
        self.occupe = self.initialiser_occupation()
        self.abonnes = set()

    def __str__(self):
        return f"Le parking possède {self.etage} étages avec {self.place} places, dont {self.reserver_sub} réservées aux abonnés."

    def creation_place(self):
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
                    
    def initialiser_occupation(self):
        return {p: None for p in self.liste_places}
    
    def places_dispo(self):
        return [p for p, v in self.occupe.items() if v is None]

    def place_libre_occuper(self, voiture:Voiture):
        for place, voiture_place in self.occupe.items():
            if voiture_place and voiture_place.releve_immatriculation() == voiture.releve_immatriculation():
                return f"La voiture {voiture.releve_immatriculation()} occupe la place {place}."
        return f"La voiture {voiture.releve_immatriculation()} n'a pas de place attribuée."
        
    def attribuer_place(self, voiture:Voiture):
        for place, voiture_place in self.occupe.items():
            if voiture_place is None:
                self.occupe[place] = voiture
                return f"La place {place} a été attribuée à la voiture immatriculée {voiture.releve_immatriculation()}."
        return f"Aucune place disponible pour la voiture immatriculée {voiture.releve_immatriculation()}."

    def abonner_voiture(self, voiture:Voiture):
        if voiture.abonner():
            self.abonnes.add(voiture.immat)
            return f"La voiture immatriculée {voiture.releve_immatriculation()} est abonnée au parking."
        else:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} n'est pas abonnée au parking."
        
    def desabonner_voiture(self, voiture:Voiture):
        if not voiture.abonner():
            self.abonnes.remove(voiture.immat)
            return f"La voiture immatriculée {voiture.releve_immatriculation()} n'est pas abonnée au parking."
        else:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} a été désabonnée du parking."
        
    def place_reservee_abonne(self, voiture:Voiture):
        if voiture.immat in self.abonnes:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} peut accéder aux places réservées aux abonnés."
        else:
            return f"La voiture immatriculée {voiture.releve_immatriculation()} ne peut pas accéder aux places réservées aux abonnés."
    
    def nombre_places_libres_sans_compter_place_abonnees(self):
        places_normales = self.liste_places[self.reserver_sub:]
        return sum(1 for p in places_normales if self.occupe[p] is None)
    
    def representation_niveau_du_parking_texte(self):
        rep = ""
        for i in range(self.etage):
            rep += f"Étage {i}:\n"
            for j in range(self.place):
                place = f"{i}{j:02d}"
                rep += "[X] " if self.occupe[place] else "[ ] "
            rep += "\n"
        return rep

   
    
    
# --- Création de voitures ---
voiture1 = Voiture("AA123BB", "Peugeot", "Alice", "oui")
voiture2 = Voiture("CC456DD", "Renault", "Bob", "non")
voiture3 = Voiture("EE789FF", "Toyota", "Charlie", "oui")

# --- Création du parking ---
parking = Parking(place=5, etage=2, reserver_sub=3)  # petit parking pour test

# --- Initialisation des places et occupation ---
parking.liste_places = parking.creation_place()
parking.occupe = parking.initialiser_occupation()

# --- Affichage du parking vide ---
print("Parking vide :")
print(parking.representation_niveau_du_parking_texte())

# --- Attribution des places ---
print(parking.attribuer_place(voiture1))
print(parking.attribuer_place(voiture2))
print(parking.attribuer_place(voiture3))

# --- Affichage du parking après attribution ---
print("\nParking après attribution :")
print(parking.representation_niveau_du_parking_texte())

# --- Vérification des abonnements ---
print(parking.abonner_voiture(voiture1))
print(parking.abonner_voiture(voiture2))
print(parking.abonner_voiture(voiture3))

# --- Vérification des places occupées ---
print(parking.place_libre_occuper(voiture1))
print(parking.place_libre_occuper(voiture2))
print(parking.place_libre_occuper(voiture3))

# --- Places réservées occupées par non-abonnés ---
print("Places d'abonnés occupées par non-abonnés :")
print(parking.liste_places_abonnees_occupees() if hasattr(parking, "liste_places_abonnees_occupees") else "Méthode non définie")

# --- Nombre de places libres hors abonnés ---
print("Nombre de places libres hors réservées :", parking.nombre_places_libres_sans_compter_place_abonnees())

# --- Désabonnement d'une voiture ---
print(parking.desabonner_voiture(voiture1))

# --- Vérification des accès aux places réservées ---
print(parking.place_reservee_abonne(voiture1))
print(parking.place_reservee_abonne(voiture3))

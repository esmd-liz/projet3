class Voiture:
    def init(self, immatriculation, marque:str, proprietaire:str, abonnement:str)->None:
        self.immat = immatriculation
        self.marque = marque
        self.proprio = proprietaire
        self.sub = abonnement

    def str(self)->str:
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
    
    def init(self, ):


    #5 étages avec des places numéroté de 1 à 480(80/e)
    #place dispo 
    #emplacement précis occupé
    #donné place libre à une nouvelle voiture


v1 = Voiture("AA123AA", "Citroën", "René Latope", "Oui")



class Immatriculation:
    
    def __init__(self, immatriculation):
      self.immatriculation=immatriculation

    def is_valid(self):
        
        if len(self.immatriculation) == 12:
            return False

        a=str(self.immatriculation[2])
        if a != "-" :           
            return False

        b=str(self.immatriculation[6])
        if b != "-" :           
            return False

        espace=str(self.immatriculation[9])
        if espace != " " :           
            return False

        deptListe = [75, 77, 78, 91, 92, 94, 95]
        dept = int(self.immatriculation[9:11])
        if dept not in deptListe :
            return False

        element1 = self.immatriculation[0:2]
        for char in element1 :
            if char is not char.isalpha():
                return False

        element2 = self.immatriculation[3:6]
        for char in element2 :
            if char is char.isalpha():
                return False

        element3 = self.immatriculation[7:9]
        for char in element3 :
            if char is not char.isalpha():
                return False
        
        
        return True

        

        

        


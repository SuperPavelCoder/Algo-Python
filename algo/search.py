class Search:
    @staticmethod
    def binary_search(liste, element):
        """liste doit être triée dans l'ordre croissant
        element se trouve dans la liste
        retourne l'index de l'élément"""
        indice_debut = 0
        indice_fin = len(liste) - 1

        while indice_debut <= indice_fin:
            indice_central = (indice_debut + indice_fin) // 2
            if liste[indice_central] == element:
                return indice_central

            if liste[indice_central] > element:
                indice_fin = indice_central - 1
            else:
                indice_debut = indice_central + 1

        return None
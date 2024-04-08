# ex: [64, 25, 12, 22, 11]
# ex: [11, 12, 22, 25, 64]

class Sort:
    @staticmethod
    def selection_sort(l):
        for i in range(0, len(l) - 1):
            # recherche du minimum
            imin = i
            for j in range(i + 1, len(l)):
                if l[j] < l[imin]:
                    imin = j
            # échange les cases i et imin
            tmp = l[i]
            l[i] = l[imin]
            l[imin] = tmp

    @staticmethod
    def bubble_sort(l):
        for j in range(3):
            for i in range(0, len(l) - 1):
                if l[i] > l[i+1]:
                    tmp = l[i]
                    l[i] = l[i+1]
                    l[i+1] = tmp
                    op = True

        """sorted = False
        op = False

        while sorted:
            for i in range(0, len(l) - 1):
                if l[i] < l[i+1]:
                    tmp = l[i]
                    l[i] = l[i+1]
                    l[i+1] = tmp
                    op = True

            if not op:
                sorted = True"""

    @staticmethod
    def insertion_sort(l):
        for i in range(1, len(l)):
            tmp = l[i]  # valeur du 2ème élément
            j = i - 1   # indice du 1er élément

            # s'ils ne sont pas dans l'ordre
            while j >= 0 and l[j] > tmp:
                l[j+1] = l[j]   # le 2ème élément vaut le 1er
                j -= 1
            l[j+1] = tmp
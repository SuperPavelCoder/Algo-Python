class Max:
    @staticmethod
    def indices_max(tab):
        M = tab[0]        # le maximum
        max_indices = []  # les indices du maximum

        for i in range(1, len(tab)):
            if tab[i] > M:
                M = tab[i]

                if len(max_indices) > 0:
                    max_indices.clear()
            if tab[i] == M:
                max_indices.append(i)

        return (M, max_indices)


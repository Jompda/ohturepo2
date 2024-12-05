HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0
        self.lounas_hinta = 5

    def lataa(self, kortti, summa):
        if summa < 0:
            return
        kortti.lataa(summa)

    def osta_lounas(self, kortti):
        if kortti.saldo < self.lounas_hinta:
            return
        kortti.osta(HINTA)
        self.myytyja_lounaita = self.myytyja_lounaita + 1

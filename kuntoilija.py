# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# ====================================

# KIRJASTOT JA MODUULIT (LIBRARIES AND MODULES)
# --------------------------------------------

import fitness

# LUOKKAMÄÄRÄYKSET (CLASS DEFINITIONS)
# -----------------------------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        
    if __name__ == "__main__":
        
        # Luodaan olio luokasta Kuntoilija
        kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
        print(kuntoilija.nimi, 'painaa', kuntoilija.paino)
        
        
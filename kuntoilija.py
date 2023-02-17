# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# ====================================

# KIRJASTOT JA MODUULIT (LIBRARIES AND MODULES)
# --------------------------------------------

import fitness

# LUOKKAMÄÄRÄYKSET (CLASS DEFINITIONS)
# -----------------------------------

# Kuntoilija-luokka Yliluokka JunioriKuntoilijalle (super class)
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""
    
    # Olionmuodostin eli konstruktori, self -> tuleva olio
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
        
    # Metodi rasvaprosentin laskemiseen (yleinen/aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(
            self.bmi,self.ika,self.sukupuoli)
        return self.rasvaprosentti
    
    # Metodi rasvaprosentin laskemiseen USA:n armeijan metodeilla
    
    def usa_rasvaprosentti_mies(self, vyotaron_ymparys, kaulan_ymparys):
        self.usa_rasvaprosentti_mies = fitness.usarasvaprosentti_mies(
            self.pituus, self.vyotaron_ymparys, self.kaulan_ymparys)
        return self.usa_rasvaprosentti_mies
    
        usa_rasvaprosentti = 0
        return usa_rasvaprosentti

    def usa_rasvaprosentti_nainen(self, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
        self.usa_rasvaprosentti_nainen = fitness.usarasvaprosentti_nainen(
            self.pituus, self.vyotaron_ymparys, self.lantion_ymparys, self.kaulan_ymparys)
        return self.usa_rasvaprosentti_nainen
    
        usa_rasvaprosentti = 0
        return usa_rasvaprosentti
 
# JunioriKuntoilija-luokka Kuntoilija-luokan aliluokka (subclass)   
class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        
        # Määritellään periytyminen, mitä ominaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli)
        
    # Metodi rasvaprosentin laskemiseen (ylikirjoitettu lapsen metodi)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti
        
if __name__ == "__main__":
        
    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija("Kalle Kuntoilija", 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, "kg")
    # print('painoindeksi on', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())
    
    
    juniorikuntoilija = JunioriKuntoilija('Aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, 'painaa', juniorikuntoilija.paino, 'kg')
    # print('painoindeksi on', kuntoilija.painoindeksi())
    print('rasvaprosentti on', juniorikuntoilija.rasvaprosentti())
# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Kirjastot ja moduulit
import math

# Määritellään funktio painoindeksin laskentaan

def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)
    
    Args:
       paino (float): paino (kg)
       pituus (float): pituus (cm)
       
    Returns:
     float: painoindeksi desimaalin tarkkuudella
     """

    pituus = pituus / 100 # Muutetaan pituuks metreiksi
    bmi = paino / pituus**2 
    bmi = round(bmi, 1)
    return bmi

# Määritellään funktio aikuisen rasvaprosentin laskentaan

def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1-> mies, 0 -> nainen
    
    Returns:
        float:kehon rasvaprosentti (aikuinen)
        """
        
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

# Määritellään funktio lapsen rasvaprosentin laskentaan

def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen rasvaprosentin
    
    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> poika, 0 -> tyttö
        
    Returns:
        float: kehon rasvaprosentti (lapsi)
        """
        
    rasvaprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti)
    return rasvaprosentti

# Miehen rasvaprosentti USA:n armeijan kaavalla
def usarasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys):
    """Laskee miehen rasvaprosentin USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyotaron ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)

    Returns:
        float: rasvaprosentti
    """
    
    # Muutetaan mitat tuumiksi
    tuuma_pituus = pituus / 2.5
    tuuma_vyotaron_ymparys = vyotaron_ymparys / 2.5
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.5
    
    # Lasketaan rasvaprosentti
    
    usarprosentti = 86.010 * math.log10(tuuma_vyotaron_ymparys - tuuma_kaulan_ymparys) - 70.041 * math.log10(tuuma_pituus) + 36.76
    usarprosentti = round(usarprosentti, 1)
    return usarprosentti 

# Naisen rasvaprosentti USA:n armeijan kaavalla
def usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
    """Laskee naisen rasvaprosentin USA:n armeijan kaavalla
    
    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyotaron ympärysmitta (cm)
        lantion_ymparys (float): lantion ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)
        
    Returns:
        float: rasvaprosentti
    """
    usa_rasvaprosentti = 0
    return usa_rasvaprosentti


    #Muutetaan mitat tuumiksi
    tuuma_pituus = pituus / 2.5
    tuuma_vyotaron_ymparys = vyotaron_ymparys / 2.5
    tuuma_lantion_ymparys = lantion_ymparys / 2.5
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.5
    
    # Lasketaan rasvaprosentti
    
    usarprosentti = 163.205 * math.log10(tuuma_vyotaron_ymparys + tuuma_lantion_ymparys - tuuma_kaulan_ymparys) - 97.684 * math.log10(pituus) - 78.387
    usarprosentti = round(usarprosentti, 1)
    return usarprosentti

# Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
# Mahdollistaa funktion lataamisen toisiin ohjelmiin
# Kun koodi ladataan, if __name__== "__main__":n alapuolella olevaa koodia ei suoriteta
if __name__ == "__main__":
    
    # Muuttujat

    # Kysytään käyttäjältä tiedot
    pituus_teksti = input("Kuinka pitkä olet? (cm): ")
    paino_teksti = input("Kuinka paljon painat? (kg): ")
    ika_teksti = input("Kuinka vanha olet?: ")
    sukupuoli_teksti = input("Mikä on sukupuolesi? mies vastaa 1, nainen vastaa 0: ")
    vyotaron_ymparys_teksti = input('Mikä on vyötärön ympäryksesi? (cm): ')
    lantion_ymparys_teksti = input('Mikä on lantion ympärysmitta? (cm): ')
    kaulan_ymparys_teksti = input('Mikä on kaulasi ympärysmitta? (cm): ')

    # Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)
    vyotaron_ymparys = float(vyotaron_ymparys_teksti)
    lantion_ymparys = float(lantion_ymparys_teksti)
    kaulan_ymparys = float(kaulan_ymparys_teksti)

    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi(paino, pituus)

    # Yli 18 vuotiailla käytetään aikuisen kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)
        
    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    print("Painoindeksisi on", oma_bmi, 
        "ja rasvaprosenttisi on", oma_rasvaprosentti)

    usa_rasvaprosentti = usarasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys)
    print('USA:n armeijan kaavalla rasvaprosenttisi on', usa_rasvaprosentti)
    
    usa_rasvaprosentti = usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys)
    print('USA:n armeijan kaavalla rasvaprosenttisi on', usa_rasvaprosentti)
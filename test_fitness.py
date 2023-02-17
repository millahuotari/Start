# FITNESS-MODULIN TESTIT
# ======================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
import fitness

def test_laske_bmi():
    assert fitness.laske_bmi(64.7, 170) == 22.4
    assert fitness.laske_bmi(40, 170) == 13.8
    assert fitness.laske_bmi(100, 170) == 34.6


def test_aikuisen_rasvaprosentti():
    assert fitness.aikuisen_rasvaprosentti(22.4, 20, 1) == 15.3
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 1) == 9.6
    assert fitness.aikuisen_rasvaprosentti(34.6, 70, 1) == 41.4
    
    #Testejä aikuisia naisia
    assert fitness.aikuisen_rasvaprosentti(20.8, 20, 0) == 24.2
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 0) == 20.4
    assert fitness.aikuisen_rasvaprosentti(34.6, 60, 0) == 49.9
    
def test_lapsen_rasvaprosentti():
    assert fitness.lapsen_rasvaprosentti(24.4, 14, 0) == 28.4
    assert fitness.lapsen_rasvaprosentti(24.4, 14, 1) == 24.8

def test_naisen_usa_rasvaprosentti():
    assert fitness.usarasvaprosentti_nainen

def test_miehen_usa_rasvaprosentti():
    assert fitness.usarasvaprosentti_mies(190, 100, 40)
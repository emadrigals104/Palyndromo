def mi_detector_anagrama (palabra1,palabra2):
    return sorted(palabra1)==sorted(palabra2)

def test_anagrama():
    assert True == mi_detector_anagrama('car','boy'),\
        'Estas Palabras no son Anagramas'
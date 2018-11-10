import Test_Palyndromo

def prueba_palyndromo():
    str_pr = '12321'

    print(f'Prueba si {str_pr} es palyndromo...')

    assert True == palyndromo.Palyndromo(str_pr)

def prueba_no_palyndromo():
    str_pr = 'abc'

    print(f'Prueba si {str_pr} no es palyndromo...')

    assert False == palyndromo.Palyndromo(str_pr)
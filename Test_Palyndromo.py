# Practica #1 Palyndromo Esteban

def Palyndromo(str):
    is_palyndromo = True
    str = str.lower()
    reverse_str = str[::-1]
    print(f'Compara: {str} con {reverse_str}')

    for idx, char in enumerate(str):
        if(char is not reverse_str[idx]):
            is_palyndromo = False

    print(f'La lista: {str} es palyndromo? R/ {is_palyndromo}')
    return is_palyndromo


Palyndromo('Esteban')
Palyndromo('zxyuvttvuyxz')
Palyndromo('123321')
Palyndromo('123456')
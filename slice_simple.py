def slice_simple():
    texto = "Awesome"
    primero = texto[0:3].lower()
    division = (len(texto) // 2) - 1
    medio = texto[division: division + 3]
    primeracuarta = texto[0:4]
    antepenultimaultima = texto[-3:]
    print (primero)
    print(medio)
    print (primeracuarta + antepenultimaultima)

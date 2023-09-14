meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
            "ROFL" : "una respuesta a una broma",
    
}

for i in range(5):          
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():

        print(meme_dict[word])
    else:
    # ¿Qué hacer si no se encuentra la palabra?
        print("esas palabras no existen en este diccionario",word)
        print("algo raro o embarazoso",word)
        print("aterrador, siniestro",word )
        print("ponerse agresivo/enojado",word )
        print("una respuesta a una broma",word )

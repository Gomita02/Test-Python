meme_dict = {
  "CRINGE" :"Algo que causa pena ajena",
  "LOL" :"Expresión de risa",
  "FACTO" :"Expresión sobre algo verídico o verdadero",
  "LA REAL" :"Expresión similar a la veradad",
}

word = input ("Escribe una palabra moderna que no entiendas (¡Utiliza mayusculas!): ")

if word in meme_dict.keys():
  print(meme_dict[word])
else:
  print("Estamos en proceso de añadir nuevas palabras como esa")

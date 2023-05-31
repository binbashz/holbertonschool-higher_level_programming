#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:112] + str[:6]
# accedemos a las palabras que queremos tomar,
# mediante sus indcies o trozos a imprimir
print(str)

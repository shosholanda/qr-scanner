import random as r
import math

values = {}
names = [
    "Rojas Aguilar",
    "Pedraza Rojas",
    "Jiménez Rojas",
    "Flores Rojas",
    "Sánchez Rojas",
    "Hernández Aguilar",
    "Mireles Aguilar",
    "Rojas Dolores",
    "Trinidad Rojas",
    "Hernández Trinidad",
    "Santiago Hernández",
    "López",
    "Silva de Paz",
    "Vera Trejo",
    "Flores García",
    "Rojas Flores",
    "Mora Gutiérrez",
    "Gutiérrez Zamora",
    "Cruz López",
    "Pablo Ramírez",
    "Flores Cuahutla",
    "Gonzales Estrada",
    "Armando López",
    "Bello Alvarez",
    "Ramos Tapia",
    "Téllez Vázquez",
    "Lara Aguilar",
    "Fidela Hilario",
    "Medel Zárate",
    "Lara Moreno",
    "Pimentel Ramos",
    "Morales Callejas",
    "Soto Gonzales",
    "Vargas Domínguez",
    "Matamoros Cárdenas",
    "Castillo Velásquez",
    "Carrasco Atilano",
    "Carmona Delgadillo",
    "Delgadillo García",
    "Acuña Garfias",
    "García Noriega",
    "Buendía Soto",
    "Mendoza de la Cruz",
    "Cruz García",
    "García Herrera",
    "Gutierrez Magdaleno",
    "Hernández Chavero",
    "Cabrera Hernández",
    "Olivares Alquicira",
    "May Cam",
    "Zúñiga Ramírez",
    "Díaz Robledo",
    "Maya",
    "Méndez García"
]

def printdick(dic):
    s = ''
    for i in dic.keys():
        s+=f"{i}: {dic[i]}\n"
    print(s)

if __name__ == '__main__':
    for i in range(len(names)):
        
        id = math.ceil(r.random()*10000000)
        str_id = '{:07n}'.format(id)

        try:
            values[str_id] = names[i]
        except:
            print("Se repitió el id")

    printdick(values)

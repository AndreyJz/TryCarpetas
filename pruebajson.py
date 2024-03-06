import json
import os
from csv import reader

def checkFolder(data:str):
    if (os.path.isdir(data)):
        return data
    else:
        os.makedirs(data)
        return data

def checkfile(archivo,inventario,BASE):
    if (os.path.isfile(BASE+archivo)):
        with open(BASE+archivo,"r") as rf:
            inventario = json.load(rf)
            return inventario
    else:
        with open(BASE+archivo,"w") as create:
            json.dump(inventario,create,indent=4)
            return inventario

def updateFile(archivo,inventario,BASE):
    with open(BASE+archivo,"r+") as up:
        json.dump(inventario,up,indent=4)
        return inventario


def importcsv(inventario:dict):
    if len(inventario['elpepe']) == 0:
        data=[]
        with open("externo/yoquese.csv","r") as r:
            lector = reader(r, delimiter=";")
            for row in lector:
                elementos = row[0].split(',')
                data.append(elementos)
                for item in data:
                    activoCampus= {
                        'codTransaccion': item[0],
                        'nroFormulario': item[1],
                        'codCampus': item[2]
                    }
                    inventario['elpepe'].update({activoCampus['codCampus']: activoCampus})
    else:
        return

data={
    'elpepe':{},
    'etesech':{}
}

base = checkFolder("data/")
os.system('pause')
inventario = checkfile("inventario.json",data,base)
importcsv(inventario)
updateFile("inventario.json",inventario,base)

# FileNotFoundError
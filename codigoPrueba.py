import sys

ListaPerros=[]
class Perro:#constructor (lo de entre parentesis serian los atributos)
  def __init__(self,nombre=None,edad=None):
    self.nombre=nombre
    self.edad=edad
  def CrearPerro(self):
    nombre=input("Ingrese el nombre del perro:")
    edad=int(input("Ingrese la edad del perro:"))
    perro=Perro(nombre,edad)
    ListaPerros.append(perro)
  def MostrarLista(self):
    print("Lista de Perros:")
    for perro in ListaPerros:
      print(f"Nombre:",perro.nombre,"Edad:",perro.edad)

def Menu():
 opcion=0
 p=Perro()
 while opcion!=3:
    print("MENÚ")
    print("1. Crear Perro y agregarlo a una lista existente")
    print("2.Mostrar todos los perros de la lista")
    print("3.Salir")
    opcion=int(input("Ingrese una opción:"))
    if opcion==1:p.CrearPerro()
    elif opcion==2:p.MostrarLista()
    elif opcion==3:
      sys.exit()
    else:
      print("Opcion incorrecta")
Menu()
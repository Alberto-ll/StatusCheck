import reflex as rx
import  sqlmodel
from typing import List, Optional
"""
class Direcciones(rx.Model, table=True):
    sector:str
    ip:str
    estado:bool
"""

# Nombre de la oficina
class Oficinas(rx.Model, table=True):
    nombre:str
    numeroDispositivos:int
    
# computadora asociada a una oficina
class Dispositivo(rx.Model,table=True):
    hostname:str
    ip:str
    tipo: int # 1 si es una computadora 2 si es una impresora
    estado:bool
    oficina_id:int

class Rack(rx.Model,table=True):
    nombre:str
    ip:str
    estado:bool

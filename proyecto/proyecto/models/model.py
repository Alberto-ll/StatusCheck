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
    impresoras:int
    computadoras:int
    
# computadora asociada a una oficina
class Dispositivo(rx.Model,table=True):
    hostname:str
    ip:str
    tipo: str 
    estado:bool
    oficina_id:int

class Rack(rx.Model,table=True):
    nombre:str
    ip:str
    estado:bool

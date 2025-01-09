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
    nomber:str
    
# computadora asociada a una oficina
class Computadora(rx.Model,table=True):
    hostname:str
    ip:str
    estado:bool
    oficina_id:int

# impresora red de la oficina
class Impresora(rx.Model,table=True):
    hostname:str
    ip:str
    estado:str
    oficina_id: int 
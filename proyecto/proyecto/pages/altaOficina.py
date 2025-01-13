import reflex as rx
from ..components.form import formularioAltaOficina
from ..components.navbar import nav

def altaOficinaPage():
    
    return(
        nav(),
        formularioAltaOficina()
    )
import reflex as rx
from ..components.form import formularioAltaRack
from ..components.navbar import nav

def altaRackPage():
    
    return(
        nav(),
        formularioAltaRack()
    )
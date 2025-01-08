"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.form import formulario
from .components.tabla import tabla
from .services.ipManagment import Manejador

from rxconfig import config
    


# Paguina inical 
def main():
    return rx.container(
        formulario(),
        tabla()
    )
    
    
app = rx.App()
app.add_page(main, route="/",on_load=Manejador.estadoUpdate())
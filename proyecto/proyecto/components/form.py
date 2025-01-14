import reflex as rx
from ..services.Managment import MainControler
#from ..services.ipManagment import Manejador

def formulario():
    return rx.card(
        rx.center(
            rx.heading("Añadir elemento"),
        ),
        rx.form(
                rx.input(
                    placeholder="ip",
                    name="ip",
                    #margin="10px",
                ),
                rx.input(
                    placeholder="hostname",
                    name="hostname",
                    #margin="10px",
                ),
            
                rx.text("Ingrese de que oficina es el dispositivo:"),
                rx.select(
                    #recuperar las oficinas de la base de datos y permitir que una sea seleccionada
                    ["oficina1","oficin2"],
                    
                    #margin="10px",
                ),
                rx.text("Ingrese tipo de dispositivo:"),
                rx.select(
                    
                  ["computadora","impresora"],
                  #margin="10px",
                ),
                rx.spacer(),
                rx.center(
                    rx.button(
                        "submit",
                        type="submit",
                        margin="10px",
                    
                ),
                ),
                align_items="center",
            #on_submit=Manejador.addIp,
            #reset_on_submit=True,
            
        ),
        #size="3"
    )
    
    
    
def formularioAltaOficina():
    return rx.center(
        rx.card(
            rx.center(
                rx.heading("Alta oficina")
            ),
            rx.form(
            rx.input(
                placeholder="Nombre oficina",
                name="nombre"   
            ),
            
            rx.button(
                "Cargar"
            ),
            on_submit=MainControler.altaOficina,
            reset_on_submit=True,
            ),

        ),
    )
    
def formularioAltaRack():
    return rx.center(
        rx.card(
            rx.center(
                rx.heading("Alta rack")
            ),
            rx.form(
            rx.input(
                placeholder="Nombre del rack",
                name="nombre",
            ),
            rx.input(
                placeholder="ip",
                name="ip",
            ),
            
            rx.button(
                "Cargar",
            ),
            on_submit=MainControler.altaRack,
            reset_on_submit=True,
            ),

        ),
    )
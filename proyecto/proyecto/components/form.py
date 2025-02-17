import reflex as rx
from ..models.model import Oficinas
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
                    required=True,
                    #margin="10px",
                ),
                rx.input(
                    placeholder="hostname",
                    name="hostname",
                    required=True,
                    #margin="10px",
                ),
            
                rx.select(
                    #recuperar las oficinas de la base de datos y permitir que una sea seleccionada
                    MainControler.listaNombresOficinas,
                    placeholder="Ingrese Oficina",
                    name="oficina",
                    value=MainControler.selectorOficina,
                    on_change= MainControler.set_selectorOficina,
                    required=True,
                    
                    #margin="10px",
                ),
                rx.select(
                    #["Impresora","Computadora"],
                    MainControler.listadoTipos,
                    placeholder="Ingrese tipo de dispositivo",
                    name="tipo",
                    value=MainControler.selectorTipo,
                    on_change= MainControler.set_selectorTipo,
                    required=True,

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
                on_submit=MainControler.altaDispositivo,
                reset_on_submit=True,
            
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
                name="nombre",
                required=True,
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
                required=True,
            ),
            rx.input(
                placeholder="ip",
                name="ip",
                required=True,
            ),
            
            rx.button(
                "Cargar",
            ),
            on_submit=MainControler.altaRack,
            reset_on_submit=True,
            ),

        ),
    )
import reflex as rx

from ..services.ipManagment import Manejador

def formulario():
    return rx.card(
        rx.center(
            rx.heading("Insert ip and sector"),
        ),
        rx.form(
            
                rx.input(
                    placeholder="Sector",
                    name="sector",
                ),
                rx.input(
                    placeholder="ip",
                    name="ip",
                ),
                rx.button(
                    "submit",
                    type="submit",
                ),
            on_submit=Manejador.addIp,
            reset_on_submit=True,
            
        ),
        size="3"
    )
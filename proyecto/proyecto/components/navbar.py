import reflex as rx


def nav_link(text:str, url:str):
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def nav():
    return rx.hstack(
        rx.hstack(
            rx.heading("Ayuda dispositivos")
        ),
        rx.hstack(
            nav_link("Dashboard","/"),
            nav_link("Alta oficina","/altaOficina"),
            nav_link("Alta rack","/altaRack"),
            justify="end",
            spacing="7",
            padding="12px",
            
            
        ),
        align_items="center",
        justify="between",
        background_color=rx.color("grass", 7),
    ),
    
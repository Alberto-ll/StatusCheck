import reflex as rx


def nav_link(text:str, url:str):
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def nav():
    return rx.hstack(
        rx.hstack(
            rx.heading("Titulo")
        ),
        rx.hstack(
            nav_link("home","/"),
            nav_link("TEST","/"),
            justify="end",
            spacing="7",
            padding="12px",
            
        ),
        align_items="center",
        justify="between",
    ),
    
import reflex as rx
from ..services.ipManagment import Manejador
from ..services.pingManagment import Ping
from ..models.model import Direcciones



def changeIcon(estado):
    return rx.box(
        rx.cond(
                (estado),
                rx.icon(tag="circle-check-big",color="green")
            ),
        rx.cond(
                (~estado),
                rx.icon(tag="unplug",color="RED"),
            ),

    )


def constructorRow(direcciones: Direcciones):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(direcciones.sector),
        rx.table.cell(direcciones.ip),
        rx.table.cell(changeIcon(direcciones.estado)),

    )




def tabla():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Sector"),
                rx.table.column_header_cell("ip"),
                rx.table.column_header_cell("estado"),
            )
        ),
        rx.table.body(
            rx.foreach(
                Manejador.direcciones, constructorRow,
            )
        ),
        on_mount=Manejador.loadIp,
        
    )
import reflex as rx
from ..models.model import Rack, Oficinas, Dispositivo
from ..services.Managment import MainControler
#from ..services.ipManagment import Manejador
#from ..models.model import Direcciones

# Cambiar

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


# def constructorRow(direcciones: Direcciones):
#    """Show a customer in a table row."""
#    return rx.table.row(
#        rx.table.cell(direcciones.sector),
#        rx.table.cell(direcciones.ip),
#        rx.table.cell(changeIcon(direcciones.estado)),
#    )




# def tabla():
#     return rx.table.root(
#         rx.table.header(
#             rx.table.row(
#                 rx.table.column_header_cell("Sector"),
#                 rx.table.column_header_cell("ip"),
#                 rx.table.column_header_cell("estado"),
#                 rx.table.column_header_cell("Borrrar")
#             )
#         ),
#         rx.table.body(
#             rx.foreach(
#                 Manejador.direcciones, constructorRow,
#             )
#         ),
#         on_mount=Manejador.loadIp,
        
#     )


def constructorRacksTabla(rackLista:list):
    
    return rx.table.row(

        rx.table.cell(rackLista.nombre),
        rx.table.cell(changeIcon(rackLista.estado)),
        ),



def tablaRack():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("rack"),
                rx.table.column_header_cell("estado"),
            ),
        ),
            rx.table.body(
                rx.foreach(
                    MainControler.rackLista , constructorRacksTabla,
                ),
            ),
            on_mount=MainControler.cargarRacks,

        )

    
    

def tablaoficinaDash():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("oficina"),
                rx.table.column_header_cell("estado"),
            ),
        ),
        
    ),
    
def tablalistadoDash():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("hostname"),
                rx.table.column_header_cell("estado"),
            ),
            ),
            
        ),
        
    
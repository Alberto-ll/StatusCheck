import reflex as rx
from ..models.model import Rack, Oficinas, Dispositivo
from ..services.Managment import MainControler
#from ..services.ipManagment import Manejador
#from ..models.model import Direcciones

# Cambiar

def changeIconRack(estado):
    return rx.box(
        rx.cond(
                (estado),
                rx.icon(tag="server",color="green")
            ),
        rx.cond(
                (~estado),
                rx.icon(tag="server-off",color="RED"),
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


def tablaRackConstructor(rack:Rack):
    return rx.table.row(
        rx.table.cell(rack.nombre),
        rx.table.cell(rack.ip),
        rx.table.cell(changeIconRack(rack.estado))
    )



def tablaRack():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Ip"),
                rx.table.column_header_cell("estado")
            ),

        ),
        rx.table.body(
            rx.foreach(
                MainControler.rackLista, tablaRackConstructor,
            )
        ),
        on_mount=MainControler.cargarRacks,
    )
    
    
def tablaOficinasConstructor(oficina:Oficinas):
    return rx.table.row(
        rx.table.cell(oficina.nombre),
        rx.table.cell(oficina.computadoras),
        rx.table.cell(oficina.impresoras),
    )

def tablaoficinaDash():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("oficina"),
                rx.table.column_header_cell("computadoras"),
                rx.table.column_header_cell("impresoras"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                MainControler.oficinasLista, tablaOficinasConstructor,
            )
        ),
        on_mount=MainControler.cargarOficinas
    )
    
def tablalistadoDash():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("hostname"),
                rx.table.column_header_cell("estado"),
            ),
            ),
            
        ),
        
    
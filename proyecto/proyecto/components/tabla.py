import reflex as rx
from ..models.model import Rack, Oficinas, Dispositivo
from ..services.Managment import MainControler


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
        rx.table.cell(rx.link(rx.text(oficina.nombre),href=f"/Informacion/oficina/{oficina.id}/{oficina.nombre}")),
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

def tablaListadoDispositivosConstructor(dispositivo:Dispositivo):
    return rx.cond(
        (~dispositivo.estado),
        rx.table.row(
            rx.table.cell(dispositivo.hostname),
            rx.table.cell(dispositivo.ip),
        )

    )
    
def tablalistadoDash():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("hostname"),
                rx.table.column_header_cell("Ip"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                MainControler.dispositivosLista, tablaListadoDispositivosConstructor,
            )
        ),
        on_mount=MainControler.cargarDispositivos,
        
    ),
        



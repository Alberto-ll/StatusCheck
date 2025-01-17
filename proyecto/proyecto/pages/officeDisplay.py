import reflex as rx
from ..components.navbar import nav
from ..models.model import Dispositivo
from ..services.Managment import MainControler


class StateOficinasDisplay(rx.State):
    ...
    # idOficina:int
    # nombreOficina:str
    
    # @rx.var
    # def getID(self)-> int:
    #     arg = self.router.page.params
        # self.idOficina = arg.get("id", [])
        # return arg.get("id", [])


    # @rx.var
    # def getNombre(self)-> str:
    #     arg = self.router.page.params
    #     return arg.get("nombre", [])
        #self.nombreOficina = arg.get("nombre", [])


    
    
def tablaOficinaImpresoras():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Hostname"),
                rx.table.column_header_cell("ip"),
                rx.table.column_header_cell("estado"),
            )
        )
    )
    
def tablaOficinaComputadorasConstructor(dispositivo:Dispositivo):
    print(dispositivo.get_value)
    return rx.cond(
        # no funciona la validacion
        (dispositivo.oficina_id == StateOficinasDisplay.id),
        rx.table.row(
            rx.table.cell(dispositivo.hostname)
        ),
    )



    

def tablaOficinaComputadoras():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Hostname"),
                rx.table.column_header_cell("ip"),
                rx.table.column_header_cell("estado"),
            )
        ),
        rx.table.body(
            rx.foreach(
                MainControler.dispositivosLista, tablaOficinaComputadorasConstructor,
            )
        ),
        on_mount=MainControler.cargarDispositivos,
    )


def officedisplay():
    return rx.box(
        nav(),
        rx.center(
            rx.heading(f"Dispositivos de la Oficina {StateOficinasDisplay.nombre}")
        ),
        rx.spacer(),
        rx.grid(
            rx.card(
                rx.heading("Computadoras"),
                tablaOficinaComputadoras(),
            ),
            rx.card(
                rx.heading("Impresoras"),
                tablaOficinaImpresoras()
            ),
            columns="2",
        ),
        
    )
import reflex as rx
from ..components.navbar import nav
from ..models.model import Dispositivo,Oficinas
from ..services.Managment import MainControler


class StateOficinasDisplay(rx.State):
    dispositivos:list[Dispositivo]=[]

    
    def getDispositivo(self):
        with rx.session() as session:
            self.dispositivos = session.exec(
                Dispositivo.select().where(
                    Dispositivo.oficina_id==self.id
                )
            ).all()

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


   
def changeIcon(estado):
    return rx.box(
        rx.cond(
                (estado),
                rx.icon(tag="cable",color="green")
            ),
        rx.cond(
                (~estado),
                rx.icon(tag="unplug",color="RED"),
            ),

    )   
   
 
    
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
    return rx.table.row(
            rx.table.cell(dispositivo.hostname),
            rx.table.cell(dispositivo.ip),
            rx.table.cell(changeIcon(dispositivo.estado))
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
                StateOficinasDisplay.dispositivos, tablaOficinaComputadorasConstructor,
            )
        ),
        on_mount=StateOficinasDisplay.getDispositivo,
    )


    
def officedisplay():
    return rx.box(
        nav(),
        rx.center(
            rx.heading(f"Dispositivos de {StateOficinasDisplay.nombre}")
        ),

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
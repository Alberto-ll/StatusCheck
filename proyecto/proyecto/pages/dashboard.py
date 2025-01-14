import reflex as rx
from ..components.navbar import nav 
from ..components.form import formulario
from ..components.tabla import  tablaRack, tablaoficinaDash, tablalistadoDash
from ..services.Managment import MainControler





def dashboardPage():
   return rx.box(
      nav(),
      rx.box(
         
         formulario(),
         
         rx.grid(
            rx.card(
               rx.center(
                  rx.heading("Raks"),   
               ),
               tablaRack(),
            ),
            rx.card(
               rx.center(
                  rx.heading("Lista Oficinas"),   
               ),
               tablaoficinaDash(),
            ),
            rx.card(
               rx.center(
                  rx.heading("Computadoras offline"),   
               ),
               tablalistadoDash(),
            ),
            columns="3"
            ),
         ),
   )




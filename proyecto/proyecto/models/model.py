import reflex as rx

class Direcciones(rx.Model, table=True):
    sector:str
    ip:str
    estado:bool
    
    
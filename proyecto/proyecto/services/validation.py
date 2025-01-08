import reflex as rx
import re


class FormValidation(rx.State):
    sector:str
    ip:str
    
    # Invalidar el formulario si el campo sector esta vacio
    def sector_empty(self):
        pass
    
    # Invalidar el formulario si el nombre no es valido | el nombre debe ser alfanumerico
    def invalid_sector(self):
        pass
    
    # Invalidar el formmulario si el sector ya  existe
    def sector_already_exist(self):
        pass
    
    # Invalidar formualrio si la IP ya esta dada de alta
    def ip_already_exist(self):
        pass
    
    # Invalidar formulario si la ip no es valida
    def invalid_ip(self):
        pass

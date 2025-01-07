import reflex as rx
from ..models.model import Direcciones
import subprocess
import asyncio

class Manejador(rx.State):

    direcciones:list[Direcciones]
    
    
    def addIp(self, form_data):
        with rx.session() as sesssion:
            sesssion.add(Direcciones(
                sector=form_data["sector"],
                ip=form_data["ip"],
                estado=self.defineEstado(form_data["ip"]),
            ))
            sesssion.commit()
        self.loadIp()
            
    def loadIp(self):
        with rx.session() as session:
            self.direcciones = session.exec(
                Direcciones.select()
            ).all()
            
    def defineEstado(self,ip):
        res = subprocess.run(["ping", ip, "-c", "1"],stdout=subprocess.DEVNULL)
        if res.returncode == 0:
            return True
        else:
            return False
        
    
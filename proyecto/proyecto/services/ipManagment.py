import reflex as rx
import re
from ..models.model import Direcciones
import subprocess
import asyncio

class Manejador(rx.State):

    # donde se cargan las direcciones
    direcciones:list[Direcciones]
    
    
    
    def deleteIp(self,ip):
        with rx.session() as session:
            direc = session.exec(Direcciones.select().where(Direcciones.ip == ip)).first()
            session.delete(direc)
            session.commit()
            
        self.loadIp()
    
    # añade una ip a la base de datos
    def addIp(self, form_data):
        with rx.session() as sesssion:
            sesssion.add(Direcciones(
                sector=form_data["sector"],
                ip=form_data["ip"],
                estado=self.defineEstado(form_data["ip"]),
            ))
            sesssion.commit()
        self.loadIp()
        
    # carga las direcciones de la base de datos en la variable 
    def loadIp(self):
        with rx.session() as session:
            self.direcciones = session.exec(
                Direcciones.select()
            ).all()
    
    # Hace un ping y si esta accesible, marca lo marca como en linea
    def defineEstado(self,ip):
        res = subprocess.run(["ping", ip, "-c", "1"],stdout=subprocess.DEVNULL)
        if res.returncode == 0:
            return True
        else:
            return False
        

    # Actualizar el estado 
    @rx.event(background=True)
    async def estadoUpdate(self):
        while True:
            async with self:
                for x in self.direcciones:
                    estado = self.defineEstado(x.ip)
                    if estado != x.estado:
                        with rx.session() as session:
                            direc = session.exec(
                                Direcciones.select().where(
                                    Direcciones.ip == x.ip
                                )
                            ).first()
                            direc.estado = estado
                            session.add(direc)
                            session.commit()
                    

            await asyncio.sleep(5)
            async with self:
                self.loadIp()
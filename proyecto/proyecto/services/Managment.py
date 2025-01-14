# import reflex as rx
# import re
# from ..models.model import Direcciones
# import subprocess
import asyncio
import subprocess
import reflex as rx
from ..models.model import Oficinas, Rack, Dispositivo


# class Manejador(rx.State):

#     # donde se cargan las direcciones
#     direcciones:list[Direcciones]
    
    
    
#     def deleteIp(self,ip):
#         with rx.session() as session:
#             direc = session.exec(Direcciones.select().where(Direcciones.ip == ip)).first()
#             session.delete(direc)
#             session.commit()
            
#         self.loadIp()
    
#     # añade una ip a la base de datos
#     def addIp(self, form_data):
#         with rx.session() as sesssion:
#             sesssion.add(Direcciones(
#                 sector=form_data["sector"],
#                 ip=form_data["ip"],
#                 estado=self.defineEstado(form_data["ip"]),
#             ))
#             sesssion.commit()
#         self.loadIp()
        
#     # carga las direcciones de la base de datos en la variable 
#     def loadIp(self):
#         with rx.session() as session:
#             self.direcciones = session.exec(
#                 Direcciones.select()
#             ).all()
    
#     # Hace un ping y si esta accesible, marca lo marca como en linea
#     def defineEstado(self,ip):
#         res = subprocess.run(["ping", ip, "-c", "1"],stdout=subprocess.DEVNULL)
#         if res.returncode == 0:
#             return True
#         else:
#             return False
        

    # Actualizar el estado 
    # @rx.event(background=True)
    # async def estadoUpdate(self):
    #     while True:
    #         async with self:
    #             for x in self.direcciones:
    #                 estado = self.defineEstado(x.ip)
    #                 if estado != x.estado:
    #                     with rx.session() as session:
    #                         direc = session.exec(
    #                             Direcciones.select().where(
    #                                 Direcciones.ip == x.ip
    #                             )
    #                         ).first()
    #                         direc.estado = estado
    #                         session.add(direc)
    #                         session.commit()
                    

    #         await asyncio.sleep(5)
    #         async with self:
    #             self.loadIp()
                
                

class MainControler(rx.State):
    # listas de las computadoras e impresoras que hay en la base de datos (se usa parra poder trabajar con los datos)
    dispositivosLista:list[Dispositivo]
    # lista de racks que se carga de la base de datos
    rackLista:list[Rack]
    # lista de oficinas que se carga de la base de datos
    oficinasLista:list[Oficinas]
    # lista de nombres de oficina para poder mostrarlos en el dashboard
    listaNombresOficinas : list[str]
    
    def defineEstado(self,ip):
        res = subprocess.run(["ping", ip, "-c", "1"],stdout=subprocess.DEVNULL)
        if res.returncode == 0:
            return True
        else:
            return False
    
    # cargar elementos de la base de datos para que puedan ser consultados por el front
    
    def cargarDispositivos(self):
        with rx.session() as session:
            self.dispositivosLista = session.exec(
                Dispositivo.select()
            ).all()
    
    def cargarRacks(self):
        with rx.session() as session:
            self.rackLista = session.exec(
                Rack.select()
            ).all()
    
    # Al cargar las oficinas se actualiza la lista 
    def cargarOficinas(self):
        with rx.session() as session:
            self.oficinasLista = session.exec(
                Oficinas.select()
            ).all()
        self.cargarlistaNombres()
        
            
    def altaRack(self,form_data):
        with rx.session() as session:
            session.add(Rack(
                nombre=form_data["nombre"],
                ip=form_data["ip"],
                estado=self.defineEstado(form_data["ip"]),
                
                
            ))
            session.commit()
        self.cargarRacks()
    
    def altaOficina(self,form_data):
        with rx.session() as session:
            session.add(Oficinas(
                nombre=form_data["nombre"],
                computadoras=0,
                impresoras=0,
            ))
            session.commit()
        self.cargarOficinas()
        
    # Limpiaa y acddtualiza la lista con los nombres de la oficina
    def cargarlistaNombres(self):
        self.listaNombresOficinas.clear()
        for x in self.oficinasLista:
            self.listaNombresOficinas.append(x.nombre)
        
        
    @rx.event(background=True)
    async def ActualizarEstado(self):
        while True:
            # Actualizacion de estado de los racks
            async with self:
                for x in self.rackLista:
                    estado = self.defineEstado(x.ip)
                    if estado != x.estado:
                        with rx.session() as session:
                            ra = session.exec(
                                Rack.select().where(
                                    Rack.ip == x.ip
                                )
                            ).first()
                            ra.estado = estado
                            session.add(ra)
                            session.commit()
                    
            #
            await asyncio.sleep(5)
            async with self:
                self.cargarRacks()
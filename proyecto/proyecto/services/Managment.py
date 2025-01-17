
import asyncio
import subprocess
import reflex as rx
from ..models.model import Oficinas, Rack, Dispositivo

                
                

class MainControler(rx.State):
    # listas de las computadoras e impresoras que hay en la base de datos (se usa parra poder trabajar con los datos)
    dispositivosLista:list[Dispositivo]
    # lista de racks que se carga de la base de datos
    rackLista:list[Rack]
    # lista de oficinas que se carga de la base de datos
    oficinasLista:list[Oficinas]
    # lista de nombres de oficina para poder mostrarlos en el dashboard
    listaNombresOficinas : list[str]
    # Opeciones de tipo de dispositivo
    listadoTipos:list[str]= ["Computadora","Impresora"]
    # Valor o eleccion del selector para el tipo de dispositivo
    selectorTipo:str = ""
    # Valor o eleccion del selector para la oficina de dispositivo
    selectorOficina:str = ""
    


    # Recibe una ip y verifica que dicha ip tenga ping
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


    # Carga los dispositivos que no se encuentren accesibles por medio de ping
    def cargarDispositivosNoDisponibles(self):
        with rx.session() as session:
            self.dispositivosLista = session.exec(
                Dispositivo.select().where(
                    Dispositivo.estado== False
                )
            ).all()
    
    # Carga los racks desde la base de datos para poder mostrarlo en el front
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


    def altaDispositivo(self,form_data):
        with rx.session() as session:
            session.add(Dispositivo(
                ip=form_data["ip"],
                hostname=form_data["hostname"],
                oficina_id=self.obtenerOficinaID(),
                estado=self.defineEstado(form_data["ip"]),
                tipo=self.selectorTipo,

            ))
            session.commit()
        
        self.actualizarOficina(self.obtenerOficinaID(),self.selectorTipo)
        
        

    # Actualiza la oficina luego de hacer el alta de dispositivo (para actualizar los contadores)
    def actualizarOficina(self, oficinaID,tipo):
        with rx.session() as session:
            oficina = session.exec(
                Oficinas.select().where(
                    Oficinas.id==oficinaID
                )
            ).first()
            if tipo =="Computadora":
                oficina.computadoras = oficina.computadoras + 1
                
            else: 
                oficina.impresoras = oficina.impresoras + 1
            
            session.add(oficina)
            session.commit()
        self.cargarOficinas()
        self.cargarDispositivos()

            
            
                
            
                
        
    # Segun lo seleccionado en el alta del dispositivo, devolvera la id de la oficina seleccionada
    def obtenerOficinaID(self):
        with rx.session() as session:
            oficina = session.exec(
                Oficinas.select().where(
                    Oficinas.nombre == self.selectorOficina
                )
            ).first()
            return oficina.id
        
    # Limpia y actualiza la lista con los nombres de la oficina
    def cargarlistaNombres(self):
        self.listaNombresOficinas.clear()
        for x in self.oficinasLista:
            self.listaNombresOficinas.append(x.nombre)
        
    
    # Tarea encargada de hacer el ping cada x tiempo deseado y actualizar el estado
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
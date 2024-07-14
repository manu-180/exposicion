import reflex as rx
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from supabase import create_client, Client
from typing import Any

class Total(rx.Base):
    id:int 
    semana:str
    dia:str
    fecha:str
    hora:str
    mails:list
    cap_max:int

class Usuarios(rx.Base):
    id:int
    usuario:str 
    clases_disponibles:int
    recuperar:int
   

class EncontrarUsuario(rx.Base):
    id:int
    semana:str 
    dia:str
    fecha:str
    hora:str


class Semanas(rx.Base):
    id:int 
    numero_semana:str

class Dias(rx.Base):
    id:int
    id_semana:int
    dia_semana:str

class Horarios(rx.Base):
    id:int
    id_dia:int
    hora_inicio:str
    hora_fin:Any


class Alumnos(rx.Base):
    id:int
    mails:list
    id_horario:Any

class Fechas(rx.Base):
    id :int
    fecha:str
    dia_id:int

# async def confirmar_usuario_en_semana() -> str:
#     return supabase.confirmar_usuario_en_semana()

# async def data_usuarios() -> list[Usuarios]:       
#         return supabase.data_usuarios()   

# async def encontrar_usuario() -> list[EncontrarUsuario]:       
#         return supabase.encontrar_usuario()   
    
async def data_total() -> list[Total]:       
        return supabase.data_total()   

# async def data_semanas() -> list[Semanas]:       
#         return supabase.data_semanas()
    
# async def data_dias() -> list[Dias]:        
#         return supabase.data_dias()
    
# async def data_horarios() -> list[Horarios]:        
#         return supabase.data_horarios()
    
# async def data_alumnos() -> list[Alumnos]:      
#         return supabase.data_alumnos()

# class PageState(rx.State):

#     semanas_info:list[Semanas]
#     dias_info:list[Dias]
#     horarios_info:list[Horarios]
#     alumnos_info:list[Alumnos]
#     total_info:list[Total]
#     semana1_lunes_info:list[Total]
#     semana1_martes_info:list[Total]
#     semana1_miercoles_info:list[Total]
#     semana1_jueves_info:list[Total]
#     semana1_viernes_info:list[Total]
#     semana2_lunes_info:list[Total]
#     semana2_martes_info:list[Total]
#     semana2_miercoles_info:list[Total]
#     semana2_jueves_info:list[Total]
#     semana2_viernes_info:list[Total]
#     semana3_lunes_info:list[Total]
#     semana3_martes_info:list[Total]
#     semana3_miercoles_info:list[Total]
#     semana3_jueves_info:list[Total]
#     semana3_viernes_info:list[Total]
#     semana4_lunes_info:list[Total]
#     semana4_martes_info:list[Total]
#     semana4_miercoles_info:list[Total]
#     semana4_jueves_info:list[Total]
#     semana4_viernes_info:list[Total]
#     semana5_lunes_info:list[Total]
#     semana5_martes_info:list[Total]
#     semana5_miercoles_info:list[Total]
#     semana5_jueves_info:list[Total]
#     semana5_viernes_info:list[Total]
#     encontrar_usuario_info:list[EncontrarUsuario]
#     usuarios_info:list[Usuarios]
#     fecha: str = "15/07"
#     cap_max:int = 7 
#     user:str 
    
    
    
#     # async def confirmar_usuario_en_semana(self):
#     #     clase_a_inscribir = None
        
#     #     for data in await data_total():
#     #         if data.semana == "semana1":
#     #             self.string_info =
                
    
#     async def semana1_lunes(self):
        
#         semana1_lunes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana1" and i.dia == "lunes":
#                 semana1_lunes_list.append(i)
        
#         self.semana1_lunes_info = semana1_lunes_list
        
#     async def semana1_martes(self):
        
#         semana1_martes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana1" and i.dia == "martes":
#                 semana1_martes_list.append(i)
        
#         self.semana1_martes_info = semana1_martes_list
    
#     async def semana1_miercoles(self):
        
#         semana1_miercoles_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana1" and i.dia == "miercoles":
#                 semana1_miercoles_list.append(i)
        
#         self.semana1_miercoles_info = semana1_miercoles_list
    
#     async def semana1_jueves(self):
        
#         semana1_jueves_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana1" and i.dia == "jueves":
#                 semana1_jueves_list.append(i)
        
#         self.semana1_jueves_info = semana1_jueves_list
    
#     async def semana1_viernes(self):
        
#         semana1_viernes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana1" and i.dia == "viernes":
#                 semana1_viernes_list.append(i)
        
#         self.semana1_viernes_info = semana1_viernes_list
    
#     async def semana2_lunes(self):
        
#         semana2_lunes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana2" and i.dia == "lunes":
#                 semana2_lunes_list.append(i)
        
#         self.semana2_lunes_info = semana2_lunes_list
        
#     async def semana2_martes(self):
        
#         semana2_martes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana2" and i.dia == "martes":
#                 semana2_martes_list.append(i)
        
#         self.semana2_martes_info = semana2_martes_list
    
#     async def semana2_miercoles(self):
        
#         semana2_miercoles_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana2" and i.dia == "miercoles":
#                 semana2_miercoles_list.append(i)
        
#         self.semana2_miercoles_info = semana2_miercoles_list
    
#     async def semana2_jueves(self):
        
#         semana2_jueves_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana2" and i.dia == "jueves":
#                 semana2_jueves_list.append(i)
        
#         self.semana2_jueves_info = semana2_jueves_list
    
#     async def semana2_viernes(self):
        
#         semana2_viernes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana2" and i.dia == "viernes":
#                 semana2_viernes_list.append(i)
        
#         self.semana2_viernes_info = semana2_viernes_list
    
#     async def semana3_lunes(self):
        
#         semana3_lunes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana3" and i.dia == "lunes":
#                 semana3_lunes_list.append(i)
#         self.semana3_lunes_info = semana3_lunes_list
        
#     async def semana3_martes(self):
        
#         semana3_martes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana3" and i.dia == "martes":
#                 semana3_martes_list.append(i)
#         self.semana3_martes_info = semana3_martes_list
    
#     async def semana3_miercoles(self):
        
#         semana3_miercoles_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana3" and i.dia == "miercoles":
#                 semana3_miercoles_list.append(i)
#         self.semana3_miercoles_info = semana3_miercoles_list
    
#     async def semana3_jueves(self):
        
#         semana3_jueves_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana3" and i.dia == "jueves":
#                 semana3_jueves_list.append(i)
        
#         self.semana3_jueves_info = semana3_jueves_list
    
#     async def semana3_viernes(self):
        
#         semana3_viernes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana3" and i.dia == "viernes":
#                 semana3_viernes_list.append(i)
        
#         self.semana3_viernes_info = semana3_viernes_list
    
#     async def semana4_lunes(self):
        
#         semana4_lunes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana4" and i.dia == "lunes":
#                 semana4_lunes_list.append(i)
        
#         self.semana4_lunes_info = semana4_lunes_list
        
#     async def semana4_martes(self):
        
#         semana4_martes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana4" and i.dia == "martes":
#                 semana4_martes_list.append(i)
        
#         self.semana4_martes_info = semana4_martes_list
    
#     async def semana4_miercoles(self):
        
#         semana4_miercoles_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana4" and i.dia == "miercoles":
#                 semana4_miercoles_list.append(i)
        
#         self.semana4_miercoles_info = semana4_miercoles_list
    
#     async def semana4_jueves(self):
        
#         semana4_jueves_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana4" and i.dia == "jueves":
#                 semana4_jueves_list.append(i)
        
#         self.semana4_jueves_info = semana4_jueves_list
    
#     async def semana4_viernes(self):
        
#         semana4_viernes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana4" and i.dia == "viernes":
#                 semana4_viernes_list.append(i)
        
#         self.semana4_viernes_info = semana4_viernes_list
    
#     async def semana5_lunes(self):
        
#         semana5_lunes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana5" and i.dia == "lunes":
#                 semana5_lunes_list.append(i)
        
#         self.semana5_lunes_info = semana5_lunes_list
        
#     async def semana5_martes(self):
        
#         semana5_martes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana5" and i.dia == "martes":
#                 semana5_martes_list.append(i)
        
#         self.semana5_martes_info = semana5_martes_list
    
#     async def semana5_miercoles(self):
        
#         semana5_miercoles_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana5" and i.dia == "miercoles":
#                 semana5_miercoles_list.append(i)
        
#         self.semana5_miercoles_info = semana5_miercoles_list
    
#     async def semana5_jueves(self):
        
#         semana5_jueves_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana5" and i.dia == "jueves":
#                 semana5_jueves_list.append(i)
        
#         self.semana5_jueves_info = semana5_jueves_list
    
#     async def semana5_viernes(self):
        
#         semana5_viernes_list = []
#         total_data = await data_total()
#         for i in total_data:
#             if i.semana == "semana5" and i.dia == "viernes":
#                 semana5_viernes_list.append(i)
        
#         self.semana5_viernes_info = semana5_viernes_list

#     async def usuarios(self):
#         self.usuarios_info = await data_usuarios()
    
#     async def encontrar_usuario(self):
#         self.encontrar_usuario_info = await encontrar_usuario()
    
#     async def total(self):
#         self.total_info = await data_total()

#     async def semanas(self):
#         self.semanas_info = await data_semanas()
    
#     async def dias(self):
#         self.dias_info = await data_dias()

#     async def horarios(self):
#         self.horarios_info = await data_horarios()

#     async def alumnos(self):
#         self.alumnos_info = await data_alumnos()

#     def handle_submit(self, form_data: dict):
#         self.fecha = form_data["select"]

#     def insertar_usuario(self, form_data: dict) -> int:
#         self.user = form_data["user"]
#         for i in supabase.data_total():
#             clase = i.mails
#             clase.append(form_data["user"])
#             response = (supabase.supabase.table("total").update({"mails": clase}).eq("id", 1).execute())

#     @rx.var
#     def filtered_list(self) -> list[Total]:
#         return [item for item in self.total_info if item.fecha == self.fecha]

#     @rx.var
#     def user_in_semana(self) -> list[Total]:

#         result = []

#         for i in self.total_info:
#             if "manunv@gmail.com" in i.mails:
#                 result.append(i.semana)
#         return result
    
#     @rx.var
#     def check_recuperar(self) -> int:
#         result = 0
#         for i in self.usuarios_info:
#             if i.usuario == "manunv@gmail.com":
#                 result = i.recuperar 
#         return result
    
#     @rx.var
#     def check_cant_clases(self) -> int:
#         result = 0
#         for i in self.usuarios_info:
#             if i.usuario == "manunv@gmail.com":
#                 result = i.clases_disponibles 
#         return result

    
    

# class CookieState:

#     def init(self):
#         self.cookie = "a"
    
#     def change_cookie(self, email):
#         self.cookie = email
            
            
# cookie_state = CookieState()


        
class ReservaCancela(rx.State):
    
    async def reset_database(self):
        reset = reset_databasee()
        return reset
    
#     async def actualizar_capacidad_maxima(id):
#         actualizar = actualizar_capacidad_maximaa(id)
#         return actualizar
    
#     async def eliminar_usuario(self, id):
#         eliminar = eliminar_usuarioo(id)
#         return eliminar

#     async def agregar_usuario(self, id):
#         agregar = agregar_usuarioo(id)
#         return agregar
    
def reset_databasee():
    supabase.reset_data_base()

# def actualizar_capacidad_maximaa(id):
#     supabase.actualizar_capacidad_maxima(id)
    
# def eliminar_usuarioo(id):
#     supabase.eliminar_usuario_a_horario(id)

# def agregar_usuarioo(id):
#     supabase.agregar_usuario_a_horario(id)

# class PaginacionState(rx.State):
#     indice: int = 0  

#     def siguiente(self):
#         self.indice = (self.indice + 1) % 5
#         # return ButtonState.reset_dias()

#     def anterior(self):
#         self.indice = (self.indice - 1) % 5
#         # return ButtonState.reset_dias()

# class ButtonState(rx.State):

#     show_text_lunes: bool = False
#     show_text_martes: bool = False
#     show_text_miercoles: bool = False
#     show_text_jueves: bool = False
#     show_text_viernes: bool = False

#     def toggle_text(self, id):
#         if id == 1:
#             self.show_text_lunes = not self.show_text_lunes
#         elif id == 2:
#             self.show_text_martes = not self.show_text_martes
#         elif id == 3:
#             self.show_text_miercoles = not self.show_text_miercoles
#         elif id == 4:
#             self.show_text_jueves = not self.show_text_jueves
#         elif id == 5:
#             self.show_text_viernes = not self.show_text_viernes
            
#     def reset_dias(self):
#         if self.show_text_lunes == True:
#             self.show_text_lunes= False
#         if self.show_text_martes == True:
#             self.show_text_martes= False
#         if self.show_text_miercoles == True:
#             self.show_text_miercoles= False
#         if self.show_text_jueves == True:
#             self.show_text_jueves= False
#         if self.show_text_viernes == True:
#             self.show_text_viernes= False
        
        
            

class SupaBase():

    load_dotenv()

    URL: str = os.environ.get("URL")
    KEY: str = os.environ.get("KEY")

    supabase: Client = create_client(URL, KEY)

    def data_total(self) -> list[Total]:
        
        total_class = []

        total = self.supabase.table("total").select("*").execute()
        
        for i in total.data:
            total_class.append(Total(id=i["id"], semana=i["semana"], dia=i["dia"], fecha=i["fecha"], hora=i["hora"], mails=i["mails"], cap_max=i["cap_max"]))
        total_list_sorted = sorted(total_class, key=lambda alumno: alumno.id)
        return total_list_sorted
    
        
    def data_usuarios(self) -> list[Usuarios]:

        usuarios_class = []

        usuarios = self.supabase.table("usuarios").select("*").execute()

        for i in usuarios.data:
            usuarios_class.append(Usuarios(id=i["id"], usuario=i["usuario"], clases_disponibles=i["clases_disponibles"], recuperar=i["recuperar"]))
        return usuarios_class



    def data_semanas(self) -> list[Semanas]:
        semanas_class = []

        semanas = self.supabase.table("semanas").select("*").execute()
        
        for i in semanas.data:
            semanas_class.append(Semanas(id=i["id"], numero_semana=i["numero_semana"],))
        return semanas_class
    
    def data_dias(self) -> list[Semanas]:
        dias_class = []

        dias = self.supabase.table("dias").select("*").execute()
        for i in dias.data:
            dias_class.append(Dias(id=i["id"], id_semana=i["id_semana"], dia_semana=i["dia_semana"]))
        return dias_class
    
    def data_horarios(self) -> list[Horarios]:
        horarios_class = []

        horarios = self.supabase.table("horarios").select("*").execute()
        
        for i in horarios.data:
            print
            horarios_class.append(Horarios(id=i["id"], id_dia=i["id_dia"], hora_inicio=i["hora_inicio"], hora_fin=i["hora_fin"] ))
        return horarios_class
    
    def data_alumnos(self) -> list[Alumnos]:
        alumnos_class = []
        alumnos = self.supabase.table("alumnos").select("*").execute()
        
        for i in alumnos.data:
            alumnos_class.append(Alumnos(id=i["id"], mails=i["mails"],id_horario=i["id_horario"]))               
        alumnos_list_sorted = sorted(alumnos_class, key=lambda alumno: alumno.id)
        return alumnos_list_sorted
        

    def data_fechas(self) -> list[Fechas]:
        fechas_class = []

        fechas = self.supabase.table("fechas").select("*").execute()
        
        for i in fechas.data:
            fechas_class.append(Fechas(id=i["id"], fecha=i["fecha"] ,dia_id= i["dia_id"]))
        return fechas_class


    def obtener_fechas_proximas_semanas(self):
        today = datetime.now()
        
        next_monday = today + timedelta(days=(7 - today.weekday() + 0) % 7)
        fechas = []
        for i in range(5):
            lunes = next_monday + timedelta(weeks=i)
            
            for j in range(5):  # Solo lunes a viernes
                fecha = lunes + timedelta(days=j)
                fechas.append(fecha.strftime("%d/%m"))
        
        return fechas

            
    def cant_users(self, id):
        for data in self.data_total():
            if data.id == id :
                return len(data.mails)
        

                        

    def check_cant_users(self, id):
        if self.cant_users(id) < 4:
            return True
        return False
        
    def encontrar_dia(self, id):

        for i in self.data_dias():
            if i.id == id :
                return i.dia_semana
        else: print("ese dia no existe")

    def encontrar_dia_con_horario(self, id):
        
        for i in self.data_horarios():
            if id == i.id:
                return self.encontrar_dia(i.id_dia)

    def encontrar_horario(self,id):

        for i in self.data_horarios():
            if i.id == id:
                return i.hora_inicio
            
    def encontrar_fecha(self, id):

        for i in self.data_total():
            if id == i.id:
                return i.fecha
            
    def encontrar_fecha_con_horario(self, id):

        for i in self.data_horarios():
            if id == i.id:
                return self.encontrar_fecha(i.id_dia)
            
    def encontrar_semana(self, id):
        for i in self.data_semanas():
            if i.id == id :
                return i.numero_semana
            
    def encontrar_semana_con_dia(self, id ):
        for i in self.data_dias():
            if id == i.id:
                return i.id_semana
            
    def encontrar_diaid_con_horario(self, id ):
        for i in self.data_horarios():
            if i.id == id:
                return i.id_dia
            
    

    
    def actualizar_fecha(self, id):
        for index, i in enumerate(self.obtener_fechas_proximas_semanas()):
            if index + 1 == id:
                return i
        

    def encontrar_usuario(self):
        
        data_total = self.data_total()
        horarios = []

        for i in data_total:
            if "manunv@gmail.com" in i.mails:
                idd = int(i.id)
                semanaa = str(i.semana)
                diaa = str(i.dia)
                fechaa = str(i.fecha)
                horaa = str(i.hora)
                horarios.append(EncontrarUsuario(semana=semanaa,dia=diaa,fecha=fechaa,hora=horaa, id=idd))
        return horarios
    
    def cant_clases_usuario(self, user):

        for i in self.data_usuarios():
            if user == i.usuario:
                return i.clases_disponibles
    
    def recuperar_clase(self, user):
        recupera = 0
        for i in self.data_usuarios():
            if user == i.usuario:
                return i.recuperar
                        
    
    def id_usuario(self, user):

        for i in self.data_usuarios():
            if user == i.usuario:
                return i.id

    
        
    def recuperar_con_usuario(self, usuario):
        for i in self.data_usuarios():
            if i.usuario == usuario:
                return i.recuperar
    
    def confirmar_usuario_en_semana(self):
        for i in self.data_total():
            if "manunv@gmail.com" in i.mails:
                return "Falsee"
            else: return "truee"
        
    def puede_inscribirse(self, usuario, id):
        
        clase_a_inscribir = None
        
        for data in self.data_total():
            if data.id == id:
                clase_a_inscribir = data
                break
        if clase_a_inscribir is None:
            return False
        for data in self.data_total():
            if data.semana == clase_a_inscribir.semana and usuario in data.mails and self.recuperar_con_usuario(usuario) == 0:
                return False
        
        clase_a_inscribir.mails.append(usuario)
        response = (self.supabase.table("total").update({"mails": clase_a_inscribir.mails}).eq("id", id).execute())
        response = (self.supabase.table("usuarios").update({"clases_disponibles": self.cant_clases_usuario(usuario) - 1}).eq("id", self.id_usuario("manunv@gmail.com")).execute())
        for i in self.data_usuarios():
            if i.recuperar != 0:
                response = (self.supabase.table("usuarios").update({"recuperar": self.recuperar_clase("manunv@gmail.com") - 1}).eq("id", self.id_usuario("manunv@gmail.com")).execute())
         

    def agregar_usuario_a_horario(self, id):
        
        for data in self.data_total():
            if data.id == id:
                if "manunv@gmail.com" not in data.mails:
                    if self.cant_clases_usuario("manunv@gmail.com") > 0:
                        self.puede_inscribirse("manunv@gmail.com", id)
                      


    def eliminar_usuario_a_horario(self, id):
        
        for data in self.data_total():
            if data.id == id:
                if 'manunv@gmail.com' in data.mails:
                    alumnos = data.mails
                    alumnos.remove('manunv@gmail.com')
                    response = (self.supabase.table("total").update({"mails": alumnos}).eq("id", id).execute())
                    response = (self.supabase.table("usuarios").update({"clases_disponibles": self.cant_clases_usuario("manunv@gmail.com") + 1}).eq("id", self.id_usuario("manunv@gmail.com")).execute())
                    response = (self.supabase.table("usuarios").update({"recuperar": self.recuperar_clase("manunv@gmail.com") + 1}).eq("id", self.id_usuario("manunv@gmail.com")).execute())

    
    def sacar_id_con_usuario(self):
        result=[]
        for i in self.data_total():
            if i.cap_max > 4:
                result.append(i.id)
                
    
    async def agregar_fechas_constantemente(self):
        for i in await data_total():
            response = (self.supabase.table("total").update({"fecha": self.actualizar_fecha(self.encontrar_diaid_con_horario(i.id)) }).eq("id", i.id).execute())
            
    def reset_data_base(self):
        for i in self.data_total():
            response = (self.supabase.table("total").update({"mails": ["Ivanna Risaro ","Julian Navarro","Camila Rey"]}).eq("id", i.id).execute())
        for i in self.data_usuarios():
            response = (self.supabase.table("usuarios").update({"clases_disponibles":4 }).eq("id", i.id).execute())
            response = (self.supabase.table("usuarios").update({"recuperar":0 }).eq("id", i.id).execute())

            
        
        
supabase = SupaBase()


@rx.page(
    title="index",
    description="Taller de cerámica",
#     on_load= [PageState.semana1_lunes, 
#               PageState.semana1_martes, 
#               PageState.semana1_miercoles, 
#               PageState.semana1_jueves,
#               PageState.semana1_viernes,
#               PageState.semana2_lunes, 
#               PageState.semana2_martes, 
#               PageState.semana2_miercoles, 
#               PageState.semana2_jueves,
#               PageState.semana2_viernes,
#               PageState.semana3_lunes, 
#               PageState.semana3_martes, 
#               PageState.semana3_miercoles, 
#               PageState.semana3_jueves,
#               PageState.semana3_viernes,
#               PageState.semana4_lunes, 
#               PageState.semana4_martes, 
#               PageState.semana4_miercoles, 
#               PageState.semana4_jueves,
#               PageState.semana4_viernes,
#               PageState.semana5_lunes, 
#               PageState.semana5_martes, 
#               PageState.semana5_miercoles, 
#               PageState.semana5_jueves,
#               PageState.semana5_viernes,
#               PageState.total,
#               PageState.encontrar_usuario]
)
def index() -> rx.Component:
    return rx.box(
        navbar(boton=True),
        button_reset_database(),
        # colores(),
    )



# @rx.page(
#     route="/turnos", 
#     title="turnos",
#     description="Taller de ceramica",
#     on_load= [PageState.semana1_lunes, 
#               PageState.semana1_martes, 
#               PageState.semana1_miercoles, 
#               PageState.semana1_jueves,
#               PageState.semana1_viernes,
#               PageState.semana2_lunes, 
#               PageState.semana2_martes, 
#               PageState.semana2_miercoles, 
#               PageState.semana2_jueves,
#               PageState.semana2_viernes,
#               PageState.semana3_lunes, 
#               PageState.semana3_martes, 
#               PageState.semana3_miercoles, 
#               PageState.semana3_jueves,
#               PageState.semana3_viernes,
#               PageState.semana4_lunes, 
#               PageState.semana4_martes, 
#               PageState.semana4_miercoles, 
#               PageState.semana4_jueves,
#               PageState.semana4_viernes,
#               PageState.semana5_lunes, 
#               PageState.semana5_martes, 
#               PageState.semana5_miercoles, 
#               PageState.semana5_jueves,
#               PageState.semana5_viernes,
#               PageState.total,
#               PageState.encontrar_usuario,
#               PageState.usuarios]
# )
# def turnos() -> rx.Component:
#     return rx.box(
#         rx.center(
#             rx.vstack(
#                 navbar(),
#                 box_marron("Para inscribirse a la clase haga click en un boton que este disponible"),
#                 dias_semanales(),
#                 width = "100%"
#             )
#         )
#     )

# @rx.page(
#         route="/mis_horarios",
#         title="mis horarios ",
#         description="Taller de ceramica",
#         on_load=[PageState.semana1_lunes, 
#               PageState.semana1_martes, 
#               PageState.semana1_miercoles, 
#               PageState.semana1_jueves,
#               PageState.semana1_viernes,
#               PageState.semana2_lunes, 
#               PageState.semana2_martes, 
#               PageState.semana2_miercoles, 
#               PageState.semana2_jueves,
#               PageState.semana2_viernes,
#               PageState.semana3_lunes, 
#               PageState.semana3_martes, 
#               PageState.semana3_miercoles, 
#               PageState.semana3_jueves,
#               PageState.semana3_viernes,
#               PageState.semana4_lunes, 
#               PageState.semana4_martes, 
#               PageState.semana4_miercoles, 
#               PageState.semana4_jueves,
#               PageState.semana4_viernes,
#               PageState.semana5_lunes, 
#               PageState.semana5_martes, 
#               PageState.semana5_miercoles, 
#               PageState.semana5_jueves,
#               PageState.semana5_viernes,
#               PageState.total,
#               PageState.encontrar_usuario,]
# )
# def mis_horarios():
#     return rx.box(
#         rx.center(
#             rx.vstack(
#                 navbar(),
#                 alert(),
#                 total_horarios(),
#                 width = "100%"  
#             )
#         )
#     )

# @rx.page(
#         route="/gestion_horarios",
#         title="horarios ",
#         description="Taller de ceramica",
#         on_load= [PageState.semana1_lunes, 
#               PageState.semana1_martes, 
#               PageState.semana1_miercoles, 
#               PageState.semana1_jueves,
#               PageState.semana1_viernes,
#               PageState.semana2_lunes, 
#               PageState.semana2_martes, 
#               PageState.semana2_miercoles, 
#               PageState.semana2_jueves,
#               PageState.semana2_viernes,
#               PageState.semana3_lunes, 
#               PageState.semana3_martes, 
#               PageState.semana3_miercoles, 
#               PageState.semana3_jueves,
#               PageState.semana3_viernes,
#               PageState.semana4_lunes, 
#               PageState.semana4_martes, 
#               PageState.semana4_miercoles, 
#               PageState.semana4_jueves,
#               PageState.semana4_viernes,
#               PageState.semana5_lunes, 
#               PageState.semana5_martes, 
#               PageState.semana5_miercoles, 
#               PageState.semana5_jueves,
#               PageState.semana5_viernes,
#               PageState.total,
#               PageState.encontrar_usuario])
# def gestion_horarios():
#     return rx.vstack(
#         navbar(),
#         rx.vstack(
#             box_marron("Gestion de horarios:"),
#             form_select_fecha(),
#             proband2(),
#             rx.text(PageState.user),
#             padding_y = "3em",
#             padding_x = "0.5em"
#         )
#     )   
    
# def proband2():
#     return rx.form.root(
#             rx.vstack(
#                 rx.hstack(
#                     rx.input(
#                         name="user",
#                         placeholder="Usuario:",
#                         required=True
#                     ),
#                     rx.select(
#                     supabase.obtener_fechas_proximas_semanas(),
#                     default_value="hoy",
#                     name="fecha",
#                     ),
#                     rx.select(
#                     ["17:30", "10:00", "14:00"],
#                     name="hora",
#                     )
#                 ),
#                 rx.button(rx.text.strong("Aceptar", color= "black"), type="submit", width ="10em",style=style_box_marron),
#             spacing="3",
#                 width="100%",
#             ),
#             on_submit=PageState.insertar_usuario,
#             reset_on_submit=True,
#             width="100%",
#         )


# def form_select_fecha():
#     return rx.vstack(
#         rx.form.root(
#             rx.hstack(
#                 rx.select(
#                     supabase.obtener_fechas_proximas_semanas(),
#                     default_value="hoy",
#                     name="select",
#                 ),
#                 submit_button(),
#                 width="100%",
#             ),
#             on_submit=PageState.handle_submit,
#             reset_on_submit=True,
#             width="100%",
#         ),
#         rx.divider(width="100%"),
#         rx.heading("Results"),
#         foreach_fechas(),
#         width="100%",
#     )

# def mostrar_clases(item):
    
    
#     return rx.vstack(
#         rx.cond(
#             PageState.fecha.to_string() == item.fecha.to_string(),
#             rx.box(box_ceramica_azul(f"ID DE CLASE : {item.id} "),
#             box_ceramica_azul(f"El dia {item.fecha} a las {item.hora} vienen {item.mails}, la capacidad maxima de esa clase es {item.cap_max}"),
#             trigger_capacidad_maxima())
#         )
#     )

# def actualizar_capacidad_maxima():
#     return rx.form(
#         rx.vstack(
#             rx.input(
#                 name="input",
#                 placeholder="cap. max",
#             ),
#             rx.button("ACEPTAR", type="submit"),
#         ),
#         on_submit=PageState.capacidad_maxima,
#     )

# def button_cap_max():
#     return rx.button("Actualizar cap. maxima", 
#     style=style_ceramica_azul)

# def foreach_fechas():
#     return rx.vstack(
#         rx.foreach(
#         PageState.filtered_list,
#         mostrar_clases
#     ))

# def total_horarios():
    


#     horarios = PageState.encontrar_usuario_info
    
#     return rx.vstack(
#         rx.cond(horarios,
#             rx.foreach(
#                 horarios,
#                 text_box
#             ),
#             rx.box(
#                 rx.hstack(
#                     rx.icon(tag="triangle-alert", padding = "0px"),
#                     rx.text.strong("Todavia no esta inscripto en ninguna clase"),
#                     spacing="1"
#                 ),
#                 bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
#                 color="#333333",
#                 border="2px solid #bdbdbd",
#                 border_radius="5px",
#                 box_shadow="4px 4px 8px #b3b3b3, -4px -4px 8px #ffffff",
#                 padding="5px",
#                 _hover={
#                     "bg": "linear-gradient(145deg, #e0e0e0, #f5f5f5)",
#                     "box_shadow": "inset 4px 4px 8px #b3b3b3, inset -4px -4px 8px #ffffff",
#                 },
#             )
#         ),
#         padding_top= "3em"
#     )
    



# def text_box(item):
#     return rx.hstack(
#             rx.box(
#                 rx.text.strong(f"Tenes clase el dia {item.dia} {item.fecha} a las {item.hora}"),
#                 bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
#                 color="#333333",
#                 border="2px solid #bdbdbd",
#                 border_radius="5px",
#                 box_shadow="4px 4px 8px #b3b3b3, -4px -4px 8px #ffffff",
#                 padding="3px",
#                 _hover={
#                     "bg": "linear-gradient(145deg, #e0e0e0, #f5f5f5)",
#                     "box_shadow": "inset 4px 4px 8px #b3b3b3, inset -4px -4px 8px #ffffff",
#                 },
#             ),
#             trigger_alert(button_red(item), "Cancelacion exitosa", f"Se ha cancelado la clase del dia {item.dia} {item.fecha} a las {item.hora}" , "/mis_horarios", None)
#         )

# def submit_button_cap_max(rute):
#     return rx.link(
#         rx.button(
#         rx.text("Aceptarr", color= "black"),
#         type= "submit",
#         width = "9em",
#         style=style_box_marron),
#         href=rute
#     ),
    

            
# def submit_button():
#     return rx.button(
#         rx.text("Buscar", color= "black"),
#         type= "submit",
#         width = "9em",
#         style=style_box_marron
#     )

# def dias_semanales():

#     return rx.center(
#         rx.vstack(
#             rx.flex(
#                 rx.cond(
#                 PaginacionState.indice == 0,
#                 links_buttons_1()
#                 ),
#                 align="start"
#             ),
#             rx.flex(
#                 rx.cond(
#                 PaginacionState.indice == 1,
#                 links_buttons_2()
#                 ),
#                 align="start"
#             ),
#             rx.flex(
#                 rx.cond(
#                 PaginacionState.indice == 2,
#                 links_buttons_3()
#                 ),
#                 align="start"
#             ),
#             rx.flex(
#                 rx.cond(
#                 PaginacionState.indice == 3,
#                 links_buttons_4()
#                 ),
#                 align="start"
#             ),
#             rx.flex(
#                 rx.cond(
#                 PaginacionState.indice == 4,
#                 links_buttons_5()
#                 ),
#                 align="start"
#             ),
#             rx.hstack(
#                 rx.button(rx.icon("arrow-left", color = "black"), on_click=PaginacionState.anterior, style= {"background_color": "#FFFDF4"}),
#                 rx.button(rx.icon("arrow-right", color = "black"), on_click=PaginacionState.siguiente, style= {"background_color": "#FFFDF4"}),
#             ),
#             width = "100%"
#         ),
#     )

# def alert():
#     return rx.vstack(
#         box_marron("Antes de cancelar una clase por favor lea atentamente las condiciones:"),
#         trigger_alert(button_rubi(),"Recuperar clase",  "Para poder recuperar una clase es indispensable cancelar con 24hs de anticipacion de lo contrario no podra ser recuperada", "/mis_horarios", None)
#     )



# def trigger_alert(button, title, dialogo,rute, on_click):
#     return rx.alert_dialog.root(
#             rx.alert_dialog.trigger(
#                 button
#             ),
#             rx.alert_dialog.content(
#                 rx.alert_dialog.title(title),
#                 rx.alert_dialog.description(
#                     dialogo,
#                 ),
#                 rx.flex(
#                     rx.alert_dialog.action(
#                         aceptar_button(rute, on_click),
#                     ),
#                     spacing="3",
#                 ),
#             ),
#         )
    
# def trigger_capacidad_maxima():
#     return rx.alert_dialog.root(
#     rx.alert_dialog.trigger(
#         rx.button(
#             rx.text.strong("Actualizar cap max", color = "black"), 
#             style=style_perla, 
#             width = "15em"
#         ),
#     ),
#     rx.alert_dialog.content(
#         rx.alert_dialog.title("Actualizando capacidad maxima de la clase:"),
#         rx.alert_dialog.description(
#             rx.vstack( 
#         rx.form.root(
#             rx.vstack(
#                 rx.hstack(
#                     rx.input(
#                         name="user",
#                         placeholder="Usuario:",
#                         required=True
#                     ),
#                     rx.input(
#                         name="id",
#                         placeholder="id de clase:",
#                         required=True,
#                     ),
#                 ),rx.hstack(
#                     rx.flex(
#                         rx.alert_dialog.action(
#                             rx.button(rx.text.strong("Aceptar", color= "black"), type="submit", width ="10em",style=style_box_marron),
#                         ),
#                         rx.alert_dialog.cancel(
#                             rx.button(
#                             rx.text.strong("cancelar", color= "black"),
#                             width="10em",
#                             style=style_box_marron
#                             ),
#                         ),
#                     spacing="3",
#                     )
#                 ),
#                 width="100%",
#             ),
#             on_submit=PageState.insertar_usuario,
#             reset_on_submit=True,
#             width="100%",
#         ),
#     ),
#         ),
#     ),
# )



# def box_marron(text):
#     return rx.vstack(
#         rx.box(
#             rx.text.strong(text, color = "black"),
            
#             style=style_box_marron
#         )
#     )

# def box_perla(text):
#     return rx.vstack(
#         rx.box(
#             rx.text.strong(text, color = "black"),
            
#             style=style_perla
#         )
#     )

# def box_ceramica_azul(text):
#     return rx.vstack(
#         rx.box(
#             rx.text.strong(text, color = "black"),
            
#             style=style_ceramica_azul
#         )
#     )


# def button_clase(item : Total):


#     return rx.center(
#             rx.cond(
#                 rx.vars.Var.length(item.mails) < item.cap_max,
#                 rx.cond(
#                     (PageState.user_in_semana.contains(item.semana) & (PageState.check_recuperar == 0)),
#                     trigger_alert(button_green(item), "Ya tenes clase esta semana!", "El unico caso en que se puede asistir a dos clases por semana es si esta recuperandola", "/turnos",ReservaCancela.agregar_usuario("manunv@gmail.com")),
#                     rx.cond((PageState.check_recuperar > 0) | (PageState.check_cant_clases > 0),
#                         trigger_alert(button_green(item), "Incripcion exitosa", f"se ha inscripto exitosamente a la clase el dia {item.dia} {item.fecha} a las {item.hora}", "/turnos", ReservaCancela.agregar_usuario("manunv@gmail.com")),
#                         trigger_alert(button_green(item), "No puedes sumarte a esta clase", "Teniendo en cuenta que son 4 clases mensuales, solo podes recuperar una clase si cancelas con 24hs de anticipacion", "/turnos", ReservaCancela.agregar_usuario("manunv@gmail.com")),
#                     )
#                 ),
#             button_disabled(item)
#             ) 
#         )

# def semana1_lunes(semana1_lunes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana1_lunes_info,
#                 button_clase
#             )
#         )
    
# def semana1_martes(semana1_martes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana1_martes_info,
#                 button_clase
#             )
#         )
    
# def semana1_miercoles(semana1_miercoles_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana1_miercoles_info,
#                 button_clase
#             )
#         )
    
# def semana1_jueves(semana1_jueves_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana1_jueves_info,
#                 button_clase
#             )
#         )
    
# def semana1_viernes(semana1_viernes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana1_viernes_info,
#                 button_clase
#             )
#         )
    
# def semana2_lunes(semana2_lunes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana2_lunes_info,
#                 button_clase
#             )
#         )
    
# def semana2_martes(semana2_martes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana2_martes_info,
#                 button_clase
#             )
#         )
    
# def semana2_miercoles(semana2_miercoles_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana2_miercoles_info,
#                 button_clase
#             )
#         )
    
# def semana2_jueves(semana2_jueves_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana2_jueves_info,
#                 button_clase
#             )
#         )
    
# def semana2_viernes(semana2_viernes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana2_viernes_info,
#                 button_clase
#             )
#         )
    
# def semana3_lunes(semana3_lunes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana3_lunes_info,
#                 button_clase
#             )
#         )
    
# def semana3_martes(semana3_martes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana3_martes_info,
#                 button_clase
#             )
#         )
    
# def semana3_miercoles(semana3_miercoles_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana3_miercoles_info,
#                 button_clase
#             )
#         )
    
# def semana3_jueves(semana3_jueves_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana3_jueves_info,
#                 button_clase
#             )
#         )
    
# def semana3_viernes(semana3_viernes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana3_viernes_info,
#                 button_clase
#             )
#         )
    
# def semana4_lunes(semana4_lunes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana4_lunes_info,
#                 button_clase
#             )
#         )
    
# def semana4_martes(semana4_martes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana4_martes_info,
#                 button_clase
#             )
#         )
    
# def semana4_miercoles(semana4_miercoles_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana4_miercoles_info,
#                 button_clase
#             )
#         )
    
# def semana4_jueves(semana4_jueves_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana4_jueves_info,
#                 button_clase
#             )
#         )
    
# def semana4_viernes(semana4_viernes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana4_viernes_info,
#                 button_clase
#             )
#         )
    
# def semana5_lunes(semana5_lunes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana5_lunes_info,
#                 button_clase
#             )
#         )
    
# def semana5_martes(semana5_martes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana5_martes_info,
#                 button_clase
#             )
#         )
    
# def semana5_miercoles(semana5_miercoles_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana5_miercoles_info,
#                 button_clase
#             )
#         )
    
# def semana5_jueves(semana5_jueves_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana5_jueves_info,
#                 button_clase
#             )
#         )
    
# def semana5_viernes(semana5_viernes_info = list[Total]) -> rx.Component:

#     return rx.hstack(
#             rx.foreach(
#                 semana5_viernes_info,
#                 button_clase
#             )
#         )
    
# def ceramica_button():    
#     return rx.button(
#         "Botón Cerámica",
#         bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
#         border="2px solid #d4b594",
#         border_radius="5px",
#         box_shadow="5px 5px 10px #c1a684, -1px -1px 2px #ffffff",
#         color="#6b4c2c",
#         font_weight="bold",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
#             "box_shadow": "inset 5px 5px 10px #c1a684, inset -5px -5px 10px #ffffff",
#         },
#     )

# def ceramica_azul_button():
#     return rx.button(
#     "ceramica azul",
#     bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
#     border="2px solid #6b8399",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #5a6f80, -1px -1px 2px #ffffff",
#     color="#2c4b6b",
#     font_weight="bold",
#     padding="5px",
#     width= "11em",
#     _hover={
#         "bg": "linear-gradient(145deg, #89a5b7, #a7c7d9)",
#         "box_shadow": "inset 5px 5px 10px #5a6f80, inset -5px -5px 10px #ffffff",
#     },
# )

style_ceramica_azul = dict(
    bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
    border="2px solid #6b8399",
    border_radius="5px",
    box_shadow="1px 1px 2px #5a6f80, -1px -1px 2px #ffffff",
    color="#2c4b6b",
    font_weight="bold",
    padding="5px",
    _hover={
        "bg": "linear-gradient(145deg, #89a5b7, #a7c7d9)",
        "box_shadow": "inset 5px 5px 10px #5a6f80, inset -5px -5px 10px #ffffff",
    },
)
style_box_marron = dict(
    bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
    border="2px solid #d4b594",
    border_radius="5px",
    # box_shadow="5px 5px 10px #c1a684, -2px -2px 3px #ffffff",
    color="#6b4c2c",
    font_weight="bold",
    padding="5px",
    position= "sticky",  
    top= '0',           
    _hover={
        "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
        "box_shadow": "inset 1px 1px 3px #c1a684, inset -5px -5px 10px #ffffff",
    }
)

style_perla= dict(
    bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
    border="2px solid #a9a9a9",
    border_radius="5px",
    box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
    color="#333333",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    _hover={
        "bg": "linear-gradient(145deg, #b0b0b0, #d3d3d3)",
        "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #dcdcdc",
    }
    )

style_negro_mate= dict(
    bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
    border="2px solid #1a1a1a",
    border_radius="5px",
    box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
    color="#a9a9a9",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    width= "11em",
    _hover={
        "bg": "linear-gradient(145deg, #1a1a1a, #2e2e2e)",
        "box_shadow": "inset 2px 2px 5px #151515, inset -2px -2px 5px #333333",
    }
)

style_gris_pizzarra= dict(
    bg="linear-gradient(145deg, #708090, #4e5964)",
    border="2px solid #2f4f4f",
    border_radius="5px",
    box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
    color="#ffffff",
    font_weight="bold",
    padding="5px",
    transition="all 0.3s ease",
    _hover={
        "bg": "linear-gradient(145deg, #4e5964, #708090)",
        "box_shadow": "inset 1px 1px 2px #2f4f4f, inset -1px -1px 2px #778899",
    }
    )

style_ceramica_roja= dict(
    bg="linear-gradient(145deg, #e08080, #c06060)",
    border="2px solid #a04040",
    border_radius="7px",
    box_shadow="1px 1px 1px #903030, -1px -1px 1px #ffa0a0",
    color="#ffffff",
    font_weight="bold",
    padding="3px",
    transition="all 0.5s ease",
    width="7em",
    _hover={
        "bg": "linear-gradient(145deg, #A47070, #e08080)",
        "box_shadow": "inset 1px 1px 1px #b05050, inset 0px 0px 1px #ffc0c0",
    }
    )

# def button_rubi():
#     return rx.button(
#         rx.hstack(
#             rx.icon(tag="triangle-alert", size=20, color = "black"),
#             rx.text("Condiciones", color= "black"),
#             spacing="2"),
#         width= "10em",
#         style=style_ceramica_roja,
#     )
    

# def terracota():
#     return rx.button(
#         "Terracota",
#         bg="linear-gradient(145deg, #d35400, #e67e22)",
#         color="white",
#         border="2px solid #c0392b",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #a04000, -1px -1px 2px #ff8c00",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #e67e22, #d35400)",
#             "box_shadow": "inset 3px 3px 6px #a04000, inset -3px -3px 6px #ff8c00",
#         },
#     )


# def porcelana():
#     return rx.button(
#         "Porcelana",
#         bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
#         color="#333333",
#         border="2px solid #bdbdbd",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #b3b3b3, -1px -1px 2px #ffffff",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #e0e0e0, #f5f5f5)",
#             "box_shadow": "inset 4px 4px 8px #b3b3b3, inset -4px -4px 8px #ffffff",
#         },
#     )


# def ceramica_verde():
#     return rx.button(
#         "Cerámica Verde",
#         bg="linear-gradient(145deg, #27ae60, #2ecc71)",
#         color="white",
#         border="2px solid #16a085",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #1e8449, -1px -1px 2px #36d278",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #2ecc71, #27ae60)",
#             "box_shadow": "inset 3px 3px 6px #1e8449, inset -3px -3px 6px #36d278",
#         },
#     )

# def azul_y_blanco():
#     return rx.button(
#         "Azul y Blanco",
#         bg="linear-gradient(145deg, #3498db, #2980b9)",
#         color="white",
#         border="2px solid #1f618d",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #2874a6, -1px -1px 2px #3ea1e6",
#         padding="5px",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #2980b9, #3498db)",
#             "box_shadow": "inset 4px 4px 8px #2874a6, inset -4px -4px 8px #3ea1e6",
#         },
#     )
    

# def Cerámica_Verde_Jade():
#     return rx.button(
#         "Cerámica Verde Jade",
#         bg="linear-gradient(145deg, #00a86b, #008c57)",
#         border="2px solid #006400",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #006400, -1px -1px 2px #32cd32",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #008c57, #00a86b)",
#             "box_shadow": "inset 2px 2px 5px #006400, inset -2px -2px 5px #32cd32",
#         },
#     )


# def Cerámica_Verde_Oliva():
#     return rx.button(
#         "Cerámica Verde Oliva",
#         bg="linear-gradient(145deg, #808000, #6b8e23)",
#         border="2px solid #556b2f",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #556b2f, -1px -1px 2px #9acd32",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #6b8e23, #808000)",
#             "box_shadow": "inset 2px 2px 5px #556b2f, inset -2px -2px 5px #9acd32",
#         },
#     )

# def Cerámica_Verde_Menta():
#     return rx.button(
#         "Cerámica Verde Menta",
#         bg="linear-gradient(145deg, #98ff98, #7fff00)",
#         border="2px solid #3cb371",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #3cb371, -1px -1px 2px #98fb98",
#         color="#006400",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #7fff00, #98ff98)",
#             "box_shadow": "inset 2px 2px 5px #3cb371, inset -2px -2px 5px #98fb98",
#         },
#     )

# def Cerámica_Verde_Bosque():
#     return rx.button(
#         "Cerámica Verde Bosque",
#         bg="linear-gradient(145deg, #228b22, #006400)",
#         border="2px solid #004d00",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #004d00, -1px -1px 2px #2e8b57",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #006400, #228b22)",
#             "box_shadow": "inset 2px 2px 5px #004d00, inset -2px -2px 5px #2e8b57",
#         },
#     )

# def carmica_zafiro():
#     return rx.button(
#     "Cerámica Zafiro",
#     bg="linear-gradient(145deg, #0047AB, #4169E1)",
#     border="2px solid #00008B",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #00008B, 0px 0px 0px #1E90FF",
#     color="#ffffff",
#     font_weight="bold",
#     padding="5px",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #4169E1, #0047AB)",
#         "box_shadow": "inset 1px 1px 2px #00008B, inset -1px -1px 2px #1E90FF",
#     },
# )

# def ceramica_azul_oscuro():
#     return rx.button(
#     "Cerámica Azul Oscuro",
#     bg="linear-gradient(145deg, #000080, #191970)",
#     border="2px solid #00008B",
#     border_radius="5px",
#     box_shadow="1px 1px 1px #000033, 1px 1px 1px #0000CD",
#     color="#E6E6FA",
#     font_weight="bold",
#     padding="5px",
#     width= "11em",
#     transition="all 0.3s ease",
#     _hover={
#         "bg": "linear-gradient(145deg, #191970, #000080)",
#         "box_shadow": "inset 2px 2px 5px #000033, inset -2px -2px 5px #0000CD",
#     },
# )

# def CerámicaNegroÉbano(): 
#     return rx.button(
#         "Cerámica Negro Ébano",
#         bg="linear-gradient(145deg, #1c1c1c, #0a0a0a)",
#         border="2px solid #000000",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #000000, -1px -1px 2px #2c2c2c",
#         color="#d3d3d3",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #0a0a0a, #1c1c1c)",
#             "box_shadow": "inset 2px 2px 5px #000000, inset -2px -2px 5px #2c2c2c",
#         },
#     )


# def CerámicaNegroMate():
#     return rx.button(
#         "Cerámica Negro Mate",
#         bg="linear-gradient(145deg, #2e2e2e, #1a1a1a)",
#         border="2px solid #1a1a1a",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #151515, -1px -1px 2px #333333",
#         color="#a9a9a9",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #1a1a1a, #2e2e2e)",
#             "box_shadow": "inset 2px 2px 5px #151515, inset -2px -2px 5px #333333",
#         },
#     )

# def CerámicaNegroCarbón():
#     return rx.button(
#         "Cerámica Negro Carbón",
#         bg="linear-gradient(145deg, #363636, #1e1e1e)",
#         border="2px solid #2c2c2c",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #1c1c1c, -1px -1px 2px #3a3a3a",
#         color="#c0c0c0",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #1e1e1e, #363636)",
#             "box_shadow": "inset 2px 2px 5px #1c1c1c, inset -2px -2px 5px #3a3a3a",
#         },
#     )

# def CerámicaNegroObsidiana():
#     return rx.button(
#         "Cerámica Negro Obsidiana",
#         bg="linear-gradient(145deg, #0f0f0f, #050505)",
#         border="2px solid #000000",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #000000, -1px -1px 2px#1a1a1a",
#         color="#e0e0e0",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "11em",
#         _hover={
#             "bg": "linear-gradient(145deg, #050505, #0f0f0f)",
#             "box_shadow": "inset 2px 2px 5px #000000, inset -2px -2px 5px #1a1a1a",
#         },
#     )    
# def CerámicaGrisClaro():
#     return rx.button(
#         "Cerámica Gris Claro",
#         bg="linear-gradient(145deg, #e0e0e0, #c0c0c0)",
#         border="2px solid #a9a9a9",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #ffffff",
#         color="#333333",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #c0c0c0, #e0e0e0)",
#             "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #ffffff",
#         },
#     )


# def CerámicaGrisMedio():
#     return rx.button(
#         "Cerámica Gris Medio",
#         bg="linear-gradient(145deg, #a0a0a0, #808080)",
#         border="2px solid #696969",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #696969, -1px -1px 2px #b8b8b8",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #808080, #a0a0a0)",
#             "box_shadow": "inset 1px 1px 2px #696969, inset -1px -1px 2px #b8b8b8",
#         },
#     )

# def CerámicaGrisPizarra():
#     return rx.button(
#         "Cerámica Gris Pizarra",
#         bg="linear-gradient(145deg, #708090, #4e5964)",
#         border="2px solid #2f4f4f",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #2f4f4f, -1px -1px 2px #778899",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #4e5964, #708090)",
#             "box_shadow": "inset 1px 1px 2px #2f4f4f, inset -1px -1px 2px #778899",
#         },
#     )

# def CerámicaGrisPerla():
#     return rx.button(
#         "Cerámica Gris Perla",
#         bg="linear-gradient(145deg, #d3d3d3, #b0b0b0)",
#         border="2px solid #a9a9a9",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #a9a9a9, -1px -1px 2px #dcdcdc",
#         color="#333333",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #b0b0b0, #d3d3d3)",
#             "box_shadow": "inset 2px 2px 5px #a9a9a9, inset -2px -2px 5px #dcdcdc",
#         },
#     )

# def CerámicaGrisCarbón():
#     return rx.button(
#         "Cerámica Gris Carbón",
#         bg="linear-gradient(145deg, #4d4d4d, #333333)",
#         border="2px solid #2b2b2b",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #2b2b2b, -1px -1px 2px #555555",
#         color="#e0e0e0",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width= "15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #333333, #4d4d4d)",
#             "box_shadow": "inset 2px 2px 5px #2b2b2b, inset -2px -2px 5px #555555",
#         },
#     )

# def ceramica_button_rojo():
#     return rx.button(
#         "Cerámica Roja",
#         bg="linear-gradient(145deg, #ff6b6b, #d64545)",
#         border="2px solid #c13e3e",
#         border_radius="5px",
#         box_shadow="1px 1px 2px #c13e3e, -1px -1px 2px #ff7373",
#         color="#ffffff",
#         font_weight="bold",
#         padding="5px",
#         transition="all 0.3s ease",
#         width="15em",
#         _hover={
#             "bg": "linear-gradient(145deg, #d64545, #ff6b6b)",
#             "box_shadow": "inset 2px 2px 5px #c13e3e, inset -2px -2px 5px #ff7373",
#         },
#     )
    
# def CerámicarojaTerracota():
#     return rx.button(
#     "Cerámica Roja Terracota",
#     background_image="linear-gradient(144deg,#CD5C5C,#A52A2A 50%,#8B4513)",
#     border="2px solid #A52A2A",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #8B4513, -1px -1px 2px #CD5C5C",
#     color="white",
#     font_weight="bold",
#     padding="5px",
#     width="15em",
#     _hover={
#         "opacity": 0.5,
#     },
# )
    
# def Cerámica_Roja_Clara():
#     return rx.button(
#     "Cerámica Roja Clara",
#     background_image="linear-gradient(144deg,#FF6347,#FF4500 50%,#FF8C00)",
#     border="2px solid #FF4500",
#     border_radius="5px",
#     box_shadow="1px 1px 2px #FF4500, -1px -1px 2px #FFA07A",
#     color="white",
#     font_weight="bold",
#     padding="5px",
#     width="15em",
#     _hover={
#         "opacity": 0.5,
#     },
# )
    
# def ceramica_button_rojo4():
#     return rx.button(
#                 "Ceramic Button 4",
#                 style={
#                     "background": "linear-gradient(to bottom, #ff6b6b, #ee5253)",
#                     "color": "white",
#                     "border": "2px solid #ee5253",
#                     "padding": "10px 25px",
#                     "border-radius": "10px",
#                     "box-shadow": "0 6px 8px rgba(0, 0, 0, 0.1)",
#                     "font-size": "16px",
#                     "font-weight": "bold",
#                     "cursor": "pointer",
#                     "transition": "transform 0.3s ease",
#                 },
#                 hover={
#                     "transform": "scale(1.1)",
#                 },
#         width= "15em",
#             )
    
# def aceptar_button(rute, on_click=None):
#     return rx.link(
#             rx.button(
#             rx.text("Aceptar", color="black"),
#             bg="linear-gradient(145deg, #f0e4d7, #e6d0b8)",
#             border="2px solid #d4b594",
#             border_radius="5px",
#             box_shadow="2px 2px 3px #c1a684, -2px -2px 3px #ffffff",
#             color="#6b4c2c",
#             font_weight="bold",
#             padding="5px",
#             width= "20em",
#             _hover={
#                 "bg": "linear-gradient(145deg, #e6d0b8, #f0e4d7)",
#                 "box_shadow": "inset 2px 2px 3px #c1a684, inset -5px -5px 10px #ffffff",
#             },
#             on_click=on_click
#             ),
#             href=rute
#         )


    
    
# def colores():
#     return rx.vstack(
#         ceramica_azul_button(),    
#         ceramica_button(),
#         terracota(),
#         ceramica_button_rojo(),
#         Cerámica_Roja_Clara(),
#         CerámicarojaTerracota(),
#         ceramica_button_rojo4(),
#         ceramica_verde(),
#         azul_y_blanco(),
#         Cerámica_Verde_Bosque(),
#         Cerámica_Verde_Jade(),
#         Cerámica_Verde_Oliva(),
#         Cerámica_Verde_Menta(),
#         ceramica_azul_oscuro(),
#         CerámicaNegroCarbón(),
#         CerámicaNegroMate(),
#         CerámicaNegroObsidiana(),
#         CerámicaNegroÉbano(),
#         CerámicaGrisCarbón(),
#         CerámicaGrisClaro(),
#         CerámicaGrisMedio(),
#         CerámicaGrisPerla(),
#         CerámicaGrisPizarra(),
#     )
        
# def button_green_advertencia():
#     pass

# def button_green(item) -> rx.Component:
#         return rx.button(
#                 rx.text(f"{item.dia} {item.fecha} a las {item.hora}"),
#                 on_click=ReservaCancela.agregar_usuario(item.id),
#                 bg="linear-gradient(145deg, #a7c7d9, #89a5b7)",
#                 border="2px solid #6b8399",
#                 border_radius="5px",
#                 box_shadow="2px 2px 5px #5a6f80, -5px -5px 10px #ffffff",
#                 color="#2c4b6b",
#                 font_weight="bold",
#                 padding="5px",
#                 width= "15em",
#                 _hover={
#                     "bg": "linear-gradient(145deg, #A5B7C1, #a7c7d9)",
#                     "box_shadow": "inset 1px 1x 1px #5a6f80, inset 1px 1px 1px #ffffff",
#                 },
#             )
        
        
# def button_red(item) -> rx.Component:
#         return rx.button(
#                     rx.text("cancelar"),
#                     on_click=ReservaCancela.eliminar_usuario(item.id),
#                     style=style_ceramica_roja,
#                 )
    

def button_disabled(item) -> rx.Component:
    return rx.center(
        rx.button(
            rx.text(f"{item.dia} {item.fecha} a las {item.hora}"),
            disabled=True,
            bg="linear-gradient(145deg, #f5f5f5, #e0e0e0)",
            color="#333333",
            # border="1px solid #bdbdbd",
            border_radius="6px",
            padding="5px",
            width= "14.5em",
        )
    ) 

    

def navbar(boton = False) -> rx.Component:
    return rx.box(
            rx.hstack(
                rx.link(
                    rx.text("Taller de ceramica",
                        padding_left="1em"
                    ),
                    href="/",
                    color =  "#FCFDFD",
                ),
                desplegable_button(),
                rx.spacer(),
            # rx.box(
            #         rx.cond(
            #         boton,
            #         rx.hstack(
            #         crear_usuario_button(),
            #         iniciar_sesion_button(),
            #         width = "100%",
            #         align_items="end")
            #     ),
            #     )
            ),
            width = "100%",
        style=dict(
            font_family="Confortaa-Medium",
            font_size = "1.3em",
            position="sticky",
            padding_y="0.5em",
            padding_x="0.5em",
            z_index="999",
            top="0",
            bg="#808080",
            box_shadow="1px 1px 2px #696969, -1px -1px 2px #b8b8b8",
            color="#050505",
            font_weight="bold",
            ),
    )

def desplegable_button():
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon("chevron-down", color="white"),
                variant="ghost",
                size="2",
                width="6em",
                style={
                    "background_color": "#808080"
                }
            ),
        ),
        rx.menu.content(
            button_menu("turnos", "/turnos"),
            button_menu("mis horarios", "/mis_horarios"),
            button_menu("gestion horarios", "/gestion_horarios"),
        ),
        style={"margin_top": "5.5em",
               "background_color": "#FFFDF4"}  
    )
    
def button_menu(text, rute):
    return rx.link(
        rx.button(
            rx.text(text),
            width="13em",
            style={
                "background_color": "#808080"
            }
        ),
        href=rute,
        style={"margin_bottom": "0.5em"}
    )

# def day_button_lunes1():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"lunes {fechas[0]}",
#                   on_click=ButtonState.toggle_text(1),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_lunes,
#             semana1_lunes(PageState.semana1_lunes_info)
#         ),
#         spacing="1"
#     )

# def day_button_martes1():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"martes {fechas[1]}",
#                   on_click=ButtonState.toggle_text(2),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_martes,
#             rx.hstack(
#                 semana1_martes(PageState.semana1_martes_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_miercoles1():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"miercoles {fechas[2]}",
#                   on_click=ButtonState.toggle_text(3),
#                   style=style_gris_pizzarra,
#                   width="15em",
#                   padding_x= "1em"),
#         rx.cond(
#             ButtonState.show_text_miercoles,
#             rx.hstack(
#                 semana1_miercoles(PageState.semana1_miercoles_info),
#             )
#         ),
#         spacing="1"
#     )

# def day_button_jueves1():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"jueves {fechas[3]}",
#                   on_click=ButtonState.toggle_text(4),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_jueves,
#             rx.hstack(
#                 semana1_jueves(PageState.semana1_jueves_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_viernes1():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"viernes {fechas[4]}",
#                   on_click=ButtonState.toggle_text(5),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_viernes,
#             rx.hstack(
#                 semana1_viernes(PageState.semana1_viernes_info)
#             )
#         ),
#         spacing="1"
#     )
    
# def day_button_lunes2():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"lunes {fechas[5]}",
#                   on_click=ButtonState.toggle_text(1),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_lunes,
#             semana2_martes(PageState.semana2_lunes_info)
#         ),
#         spacing="1"
#     )

# def day_button_martes2():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"martes {fechas[6]}",
#                   on_click=ButtonState.toggle_text(2),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_martes,
#             semana2_martes(PageState.semana2_martes_info)
#         ),
#         spacing="1"
#     )

# def day_button_miercoles2():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"miercoles {fechas[7]}",
#                   on_click=ButtonState.toggle_text(3),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_miercoles,
#             semana2_miercoles(PageState.semana2_miercoles_info)
#         ),
#         spacing="1"
#     )

# def day_button_jueves2():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"jueves {fechas[8]}",
#                   on_click=ButtonState.toggle_text(4),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_jueves,
#             semana2_jueves(PageState.semana2_jueves_info)
#         ),
#         spacing="1"
#     )

# def day_button_viernes2():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"viernes {fechas[9]}",
#                   on_click=ButtonState.toggle_text(5),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_viernes,
#             semana2_viernes(PageState.semana2_viernes_info)
#         ),
#         spacing="1"
#     )
    
# def day_button_lunes3():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"lunes {fechas[10]}",
#                   on_click=ButtonState.toggle_text(1),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_lunes,
#             semana3_martes(PageState.semana3_lunes_info)
#         ),
#         spacing="1"
#     )

# def day_button_martes3():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"martes {fechas[11]}",
#                   on_click=ButtonState.toggle_text(2),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_martes,
#             rx.hstack(
#                 semana3_martes(PageState.semana3_martes_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_miercoles3():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"miercoles {fechas[12]}",
#                   on_click=ButtonState.toggle_text(3),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_miercoles,
#             rx.hstack(
#                 semana3_miercoles(PageState.semana3_miercoles_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_jueves3():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"jueves {fechas[13]}",
#                   on_click=ButtonState.toggle_text(4),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_jueves,
#             rx.hstack(
#                 semana3_jueves(PageState.semana3_jueves_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_viernes3():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"viernes {fechas[14]}",
#                   on_click=ButtonState.toggle_text(5),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_viernes,
#             rx.hstack(
#                 semana3_viernes(PageState.semana3_viernes_info)
#             )
#         ),
#         spacing="1"
#     )
    
# def day_button_lunes4():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"lunes {fechas[15]}",
#                   on_click=ButtonState.toggle_text(1),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_lunes,
#             semana4_martes(PageState.semana4_lunes_info)
#         ),
#         spacing="1"
#     )

# def day_button_martes4():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"martes {fechas[16]}",
#                   on_click=ButtonState.toggle_text(2),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_martes,
#             rx.hstack(
#                 semana4_martes(PageState.semana4_martes_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_miercoles4():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"miercoles {fechas[17]}",
#                   on_click=ButtonState.toggle_text(3),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_miercoles,
#             rx.hstack(
#                 semana4_miercoles(PageState.semana4_miercoles_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_jueves4():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"jueves {fechas[18]}",
#                   on_click=ButtonState.toggle_text(4),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_jueves,
#             rx.hstack(
#                 semana4_jueves(PageState.semana4_jueves_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_viernes4():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"viernes {fechas[19]}",
#                   on_click=ButtonState.toggle_text(5),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_viernes,
#             rx.hstack(
#                 semana4_viernes(PageState.semana4_viernes_info)
#             )
#         ),
#         spacing="1"
#     )
    
# def day_button_lunes5():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"lunes {fechas[20]}",
#                   on_click=ButtonState.toggle_text(1),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_lunes,
#             semana5_martes(PageState.semana5_lunes_info)
#         ),
#         spacing="1"
#     )

# def day_button_martes5():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"martes {fechas[21]}",
#                   on_click=ButtonState.toggle_text(2),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_martes,
#             rx.hstack(
#                 semana5_martes(PageState.semana5_martes_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_miercoles5():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"miercoles {fechas[22]}",
#                   on_click=ButtonState.toggle_text(3),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_miercoles,
#             rx.hstack(
#                 semana5_miercoles(PageState.semana5_miercoles_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_jueves5():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"jueves {fechas[23]}",
#                   on_click=ButtonState.toggle_text(4),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_jueves,
#             rx.hstack(
#                 semana5_jueves(PageState.semana5_jueves_info)
#             )
#         ),
#         spacing="1"
#     )

# def day_button_viernes5():
#     fechas = supabase.obtener_fechas_proximas_semanas()
#     return rx.hstack(
#         rx.button(f"viernes {fechas[24]}",
#                   on_click=ButtonState.toggle_text(5),
#                   style=style_gris_pizzarra,
#                   width="15em"),
#         rx.cond(
#             ButtonState.show_text_viernes,
#             rx.hstack(
#                 semana5_viernes(PageState.semana5_viernes_info)
#             )
#         ),
#         spacing="1"
#     )
    


# def links_buttons_1():
#     return rx.vstack(
#         day_button_lunes1(),
#         day_button_martes1(),
#         day_button_miercoles1(),
#         day_button_jueves1(),
#         day_button_viernes1(),
#     )

# def links_buttons_2():
#     return rx.vstack(
#         day_button_lunes2(),
#         day_button_martes2(),
#         day_button_miercoles2(),
#         day_button_jueves2(),
#         day_button_viernes2(),
#     )
# def links_buttons_3():
#     return rx.vstack(
#         day_button_lunes3(),
#         day_button_martes3(),
#         day_button_miercoles3(),
#         day_button_jueves3(),
#         day_button_viernes3(),
#     )
# def links_buttons_4():
#     return rx.vstack(
#         day_button_lunes4(),
#         day_button_martes4(),
#         day_button_miercoles4(),
#         day_button_jueves4(),
#         day_button_viernes4(),
#     )
# def links_buttons_5():
#     return rx.vstack(
#         day_button_lunes5(),
#         day_button_martes5(),
#         day_button_miercoles5(),
#         day_button_jueves5(),
#         day_button_viernes5(),
#     )


def button_reset_database():
    return rx.button(
        "Reset database",
        width ="15em",
        on_click=ReservaCancela.reset_database(),
        style=style_perla,
        margin_y="3em"
    )

    
# BASE_STYLE = {
#     "font_family": "1em",
#     "font_weight": "300",
#     "background_color": "#FFFDF4",
#     rx.heading: {
#         "color": "#708090",
#         "font_family": "Poppins",
#         "font_weight": "500"
#     },
#     rx.button: {
#         "width": "100%",
#         "height": "100%",
#         "padding": "0.5em",
#         "border_radius": "0.8em",
#         "white_space": "normal",
#         "text_align": "start",
#         "--cursor-button": "pointer",
#     },
#     rx.link: {
#         "color": "#FCFDFD",
#         "text_decoration": "none",
#         "_hover": {
#             "color": "#708090"
#         }
#     }
# }


app = rx.App(
#     style=BASE_STYLE,
    )
app.add_page(index)
# app.add_page(turnos)
# app.add_page(mis_horarios)
# app.add_page(gestion_horarios)

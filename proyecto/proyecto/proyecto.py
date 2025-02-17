"""Welcome to Reflex! This file outlines the steps to create a basic app."""
"""Paguina donde se cargaran todas las paguinas"""
import reflex as rx
from reflex import dynamic

from proyecto.pages.dashboard import dashboardPage
from proyecto.pages.officeDisplay import officedisplay, StateOficinasDisplay
from proyecto.pages.altaOficina import altaOficinaPage
from proyecto.pages.altaRack import altaRackPage

from proyecto.services.Managment import MainControler

app = rx.App()
app.add_page(dashboardPage,route="/", on_load=[MainControler.ActualizarEstadoDispositivos,MainControler.ActualizarEstado])
app.add_page(officedisplay, route="/Informacion/oficina/[id]/[nombre]")
app.add_page(altaOficinaPage,route="/altaOficina")
app.add_page(altaRackPage,route="/altaRack")


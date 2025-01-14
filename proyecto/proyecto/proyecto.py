"""Welcome to Reflex! This file outlines the steps to create a basic app."""
"""Paguina donde se cargaran todas las paguinas"""
import reflex as rx

from proyecto.pages.dashboard import dashboardPage
from proyecto.pages.officeDisplay import officedisplay
from proyecto.pages.altaOficina import altaOficinaPage
from proyecto.pages.altaRack import altaRackPage

from proyecto.services.Managment import MainControler

app = rx.App()
app.add_page(dashboardPage,route="/", on_load=MainControler.ActualizarEstado)
app.add_page(officedisplay, route="/officeD")
app.add_page(altaOficinaPage,route="/altaOficina")
app.add_page(altaRackPage,route="/altaRack")

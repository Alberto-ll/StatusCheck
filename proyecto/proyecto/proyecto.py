"""Welcome to Reflex! This file outlines the steps to create a basic app."""
"""Paguina donde se cargaran todas las paguinas"""
import reflex as rx

from proyecto.pages.dashboard import dashboardPage
from proyecto.pages.officeDisplay import officedisplay


app = rx.App()
app.add_page(dashboardPage,route="/")

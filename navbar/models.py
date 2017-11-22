from __future__ import unicode_literals

from django.db import models
from django.template.loader import render_to_string
from builder.models import Pattern


class Navbar(Pattern):
    # ... mis atributos

    # Importante, este nombre es utilizado alrededor de la aplicación, y debe
    # ser consistente con el nombre de patrón que utilizas en JD para las
    # funciones que se describen más adelante.
    name = "navbar"

    # Este método devuelve el html que corresponde al patrón.
    def render(self):
        return render_to_string('patrones/navbar/view.html', {"pattern": self})
    # Este método devuelve el html que corresponde a la visualización del patrón
    # en el constructor.
    def render_card(self):
        return render_to_string('patrones/navbar/build.html', {"pattern": self})
    # Este método devuelve el html que corresponde al formulario de configuración
    # del patrón.
    def render_config_modal(self):
        return render_to_string('patrones/navbar/configurar-modal.html', {"pattern": self})

    def __str__(self):
	    return "NavBar"

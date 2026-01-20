from odoo import models, fields

class Alumnos(models.Model):
    _name = "partes.alumnos"
    _description = "Alumnos"
    name = fields.Char("Nombre del alumno")

from odoo import models, fields

class Profesores(models.Model):
    _name = "partes.profesores"
    _description = "Profesores"
    name = fields.Char("Nombre del profesor")

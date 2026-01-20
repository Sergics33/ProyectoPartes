from odoo import models, fields

class Incidencias(models.Model):
    _name = "partes.incidencias"
    _description = "Incidencias"
    name = fields.Char("Incidencia")

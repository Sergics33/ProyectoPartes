from odoo import models, fields

class Parte(models.Model):
    _name = "partes.parte"
    _description = "Parte de instituto"

    name = fields.Char(string="Título del Parte", required=True)
    descripcion = fields.Text(string="Descripción")

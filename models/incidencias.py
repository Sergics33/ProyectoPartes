from odoo import models, fields

class Incidencias(models.Model):
    _name = 'partes.incidencias'
    _description = 'Parte de Incidencia Escolar'
    _inherit = ['image.mixin']

    name = fields.Char(string="Nº Parte", readonly=True, copy=False, default='Nuevo')
    
    # Cabecera
    profesor_id = fields.Many2one('partes.profesores', string="Profesor/a")
    asignatura = fields.Char(string="Asignatura")
    fecha = fields.Date(string="Fecha", default=fields.Date.context_today)
    hora = fields.Char(string="Hora (ej. 10:30)")
    aula = fields.Char(string="Aula")
    alumno_id = fields.Many2one('partes.alumnos', string="Alumno/a")
    curso = fields.Char(string="Curso")

    # Motivos (Booleanos para que puedas marcar varios)
    motivo_respeto_profesor = fields.Boolean("Falta de respeto y desobediencia al profesor")
    motivo_respeto_companeros = fields.Boolean("Falta de respeto a los compañeros")
    motivo_interrumpe = fields.Boolean("Interrumpe la clase")
    motivo_material = fields.Boolean("No trae el material")
    motivo_amonestaciones = fields.Boolean("Acumulación de amonestaciones verbales")
    motivo_itaca = fields.Boolean("Acumulación de faltas en ITACA")
    motivo_otro = fields.Char("Otra")

    # Gravedad
    gravedad_sancion = fields.Selection([
        ('leve', 'Falta Leve'),
        ('grave', 'Falta Grave'),
        ('muy_grave', 'Falta Muy Grave')
    ], string="Gravedad", default='leve')

    # Pie del parte
    tarea = fields.Text("Tarea")
    medida_correctora = fields.Text("Medida correctora")
    comunicacion_padres = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No')
    ], string="Comunicación a padres", default='no')
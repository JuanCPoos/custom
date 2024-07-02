from odoo import models, fields

class MedicalRecord(models.Model):
    _name = 'medical.record'
    _description = 'Ficha médica de los inscriptos'

    x_partner_id = fields.Many2one('res.partner', string = 'Contacto', required=True)
    x_condicion_medica = fields.Char(string = 'Condición médica')
    x_alergias = fields.Char(string='Alergias')
    x_medicacion = fields.Char(string='Medicación')
    x_contacto_emergencia = fields.Char(string='Contacto de Emergencia')
    
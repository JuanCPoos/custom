from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_docente_responsable = fields.Many2one('res.partner', string="Docente a cargo", domain="[('x_tipo_persona', '=', 'docente')]")
from odoo import models, fields

class DocumentType(models.Model):
    _inherit = 'l10n_latam_document_type'
    
    x_tipo_documento = fields.Selection([
        ('recibo_pago', 'Recibo de Pago'),
    ], string = "Tipo de Documento")
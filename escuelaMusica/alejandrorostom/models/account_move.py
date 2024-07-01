from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_tipo_documento = fields.Many2one('l10n_latam.document.type', string='Tipo de Documento')

    @api.onchange('x_tipo_documento')
    def _onchange_tipo_documento(self):
        if self.x_tipo_documento:
            self.l10n_latam_document_type_id = self.x_tipo_documento.id

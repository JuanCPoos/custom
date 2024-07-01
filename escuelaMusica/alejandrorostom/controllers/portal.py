from odoo import http
from odoo.http import request

class EscuelaMusicaController(http.Controller):

    @http.route(['/my/medical_records'], type='http', auth='user', website=True)
    def medical_records(self, **kw):
        records = request.env['medical.record'].search([('x_partner_id', '=', request.env.user.partner_id.id)])
        return request.render('escuelaMusica.medical_record_portal_template', {
            'records': records
        })

    @http.route(['/my/medical_records/submit'], type='http', auth='user', methods=['POST'], website=True)
    def medical_record_submit(self, **post):
        partner = request.env.user.partner_id
        request.env['medical.record'].create({
            'x_partner_id': partner.id,
            'x_condicion_medica': post.get('x_condicion_medica'),
            'x_alergias': post.get('x_alergias'),
            'x_medicacion': post.get('x_medicacion'),
            'x_contacto_emergencia': post.get('x_contacto_emergencia'),
        })
        return request.redirect('/my/medical_records')

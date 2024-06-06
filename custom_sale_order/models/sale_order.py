from odoo import models, fields, api 

class SalesOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create_sales_orders(self):
        domain = [('x_tipo_persona', '=', 'alumno')]
        alumnos = self.env['res.partner'].search(domain)

        for alumno in alumnos:
            if alumno.x_taller_id:
                sale_order = self.create({
                    'partner_id': alumno.id,
                    'date_order': fields.Datetime.now(),
                    'order_line':[(0, 0, {
                        'product_id': alumno.x_taller_id.id,
                        'product_uom_qty': 1,
                        'price_unit': alumno.x_taller_id.lst_price,
                    })],
                })
                sale_order.action_confirm()
                sale_order._create_invoices()
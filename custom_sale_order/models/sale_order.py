from odoo import models, fields, api   
                     
class SalesOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create_sales_orders(self):
        #domain = [('x_tipo_persona', '=', 'alumno')]
        domain = [('title', '=', 'Alumno')]
        alumnos = self.env['res.partner'].search(domain)

        for alumno in alumnos:
            if alumno.x_taller_ids: #cada uno de los talleres en el form de Talleres x_taller_ids
                order_lines = []
                for taller in alumno.x_taller_ids:
                    order_lines.append((0, 0, {
                        'product_id': taller.product_id.id,
                        'product_uom_qty': 1,
                        'price_unit': taller.product_id.lst_price,
                    }))
                if order_lines:  # Verifica si hay talleres para crear la orden
                    sale_order = self.create({
                        'partner_id': alumno.id,
                        'date_order': fields.Datetime.now(),
                        'order_line': order_lines,
                    })
                    sale_order.action_confirm() #confirmo orden de venta
                    invoice = sale_order._create_invoices() # creo factura en estado borrador
                    if invoice: #confirmar factura para ver en portal web, si hay una orden creada
                        invoice.action_post()

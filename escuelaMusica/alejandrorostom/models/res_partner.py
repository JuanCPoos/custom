from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Datos del tipo de relación, padre, madre o responsable
    x_tipo_persona = fields.Selection([
        ('alumno', 'Alumno'),
        ('padre_madre_resp', 'Padre/Madre/Responsable'),
        ('docente', 'Docente'),
        ('proveedor', 'Proveedor')
    ], string="Tipo Persona")
    
    x_nombre_tipo_relacion = fields.Char(string="Nombre y Apellido", required=False)
    x_fecha_nacimiento = fields.Date(required=False)
    x_dni_alumno = fields.Integer(required=True)
    x_direccion = fields.Char(string="Dirección", required=False)
    x_telefono_relacion = fields.Char(string="Teléfono")
    
    # En Page Información adicional
    x_instrumento = fields.Boolean(string="Instrumento")
       
    # Campos para form taller
    x_taller_ids = fields.One2many('res.partner.taller', 'partner_id', string="Talleres")
    
     # Campo computado para el estado de pago de la factura
    x_factura_estado = fields.Char(string="Estado de Factura", compute='_compute_factura_estado')


    
    @api.depends('invoice_ids')
    def _compute_factura_estado(self):
        for partner in self:
            if partner.x_tipo_persona == 'alumno':
                # Obtenemos las facturas del cliente en estados abiertos o pagados
                invoices = self.env['account.move'].search([
                    ('partner_id', '=', partner.id),
                    ('move_type', '=', 'out_invoice'),
                    ('state', 'in', ['posted', 'paid'])
                ])

                if not invoices:
                    partner.x_factura_estado = 'ATENCIÓN - Mes adeudado'
                else:
                    last_invoice = invoices.sorted('invoice_date')[-1]
                    if last_invoice.payment_state == 'paid':
                        partner.x_factura_estado = f'Mes abonado: $ {last_invoice.amount_total}'
                    else:
                        partner.x_factura_estado = 'Mes adeudado'
            else:
                partner.x_factura_estado = ''  # O deja el campo en blanco para otros tipos de contactos
    
  # Método para sincronizar el email y el móvil del contacto principal a los contactos secundarios
    @api.onchange('email', 'mobile')                
    def _onchange_email_mobile(self):
        for child in self.child_ids:
            if self.email:
                child.email = self.email                
            if self.mobile:
                child.mobile = self.mobile
                
   # establecer el valor predeterminado de is_company en False
    @api.model
    def default_get(self, fields_list):
        defaults = super(ResPartner, self).default_get(fields_list)
        if 'is_company' in fields_list:
            defaults['is_company'] = False
        return defaults

class ResPartnerTaller(models.Model):
    _name = 'res.partner.taller'
    _description = 'Taller de Partner'
        
    partner_id = fields.Many2one('res.partner', string="Partner")
    product_id = fields.Many2one('product.product', string="Taller")
    x_instrumento = fields.Boolean(string="Instrumento")
    x_cuadernillo = fields.Boolean(string="Cuadernillo")

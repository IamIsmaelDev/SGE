from odoo import api, models, fields


class prenda(models.Model):
    id = fields.Integer(required=True)
    nombre = fields.Char()
    talla = fields.Char()
    vendedor = fields.Many2one(
        comodel_name='vendedor', string='vendedor'
    )


class cliente(models.Model):
    id = fields.Integer(required=True)
    nombre = fields.Char()
    apellido = fields.Char()
    edad = fields.Integer()
    dni = fields.Char()
    telefono = fields.Char()
    direccion = fields.Char()


class vendedor(models.Model):
    id = fields.Integer(required=True)
    nombre = fields.Char()
    apellido = fields.Char()
    edad = fields.Integer()
    dni = fields.Char()
    telefono = fields.Char()
    direccion = fields.Char()
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    prenda = fields.One2many(
        comodel_name='prenda', inverse_name='vendedor'
    )


class compra(models.Model):
    id = fields.Integer(required=True)
    fecha = fields.Date()
    cliente = fields.Many2one(
        comodel_name='cliente', string='cliente'
    )
    prenda = fields.Many2one(
        comodel_name='prenda', string='prenda'
    )
    vendedor = fields.Many2one(
        comodel_name='vendedor', string='vendedor'
    )
    precio_inicial = fields.Float()
    precio_final = fields.Float()

    rebaja = fields.Float(compute='_rebaja', store=True)

    @api.depends('precio_inicial', 'precio_final')
    def _rebaja(self):
        for record in self:
            record.rebaja = record.precio_inicial - record.precio_final

from odoo import fields, models

class User(models.Model):
    _name = 'library.user'
    _description = 'Library User'

    name = fields.Char("Name", required=True)
    id = fields.Integer()

    _sql_constraints=[('id', 'unique(id)', 'ID must be unique')]

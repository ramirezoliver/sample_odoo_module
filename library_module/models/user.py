from odoo import fields, models

class User(models.Model):
    _name = 'library.user'
    _description = 'Library User'

    name = fields.Char("username", required=True, size=80)
    _sql_constraints=[('name', 'unique(name)', 'username must be unique')]

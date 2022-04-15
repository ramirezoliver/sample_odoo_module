from odoo import fields, models

class User(models.Model):
    _name = 'library.user'
    _description = 'Library User'

    name = fields.Char("Name", required=True)
    user_id = fields.Integer("User ID")

    _sql_constraints=[('user_id', 'unique(user_id)', 'User ID must be unique')]

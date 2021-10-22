from odoo import fields, models


class DocumentTags(models.Model):
    _name = "doc.tags"
    _description = "Document Tags"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer(string="Color Index", default=0)

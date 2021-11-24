from odoo import api, fields, models
from odoo.tools.translate import _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[('append', 'Append')])

    def button_append(self):
        print("\n\n\n\naaaaaaaaaa")

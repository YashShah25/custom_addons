from odoo import fields, models
from odoo.tools.translate import _


class Partner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Boolean(string=_("Credit Limit"))
    credit_limit_score = fields.Float(string=_("Credit Limit Score"))
    blocking_limit = fields.Boolean(string=_("Blocking Limit"))
    blocking_limit_score = fields.Float(string=_("Blocking Limit Score"))

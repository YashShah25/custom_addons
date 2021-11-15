from odoo import fields, models, api
from odoo.tools.translate import _


class HrJob(models.Model):
    _inherit = 'hr.job'

    affordable_salary = fields.Float(string=_("Affordable Salary"))

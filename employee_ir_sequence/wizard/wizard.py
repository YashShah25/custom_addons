# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Wizardtest(models.TransientModel):
    _name = "employee.wizard"
    _description = "name"
    order_lines = fields.Char()

    @api.onchange("name")
    def employee_wizard(self):
        context = self._context
        emp = self.env["hr.employee"].browse(context["active_id"])
        emp.mobile_phone = self.name
        # for a in self:
        #      for i in self.env['hr.employee'].search([]):
        #          i.update({
        #              'mobile_phone': a.name,
        #             })

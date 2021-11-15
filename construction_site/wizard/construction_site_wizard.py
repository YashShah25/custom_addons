from odoo import models, fields


class CreateWizard(models.TransientModel):
    _name = "construction.wizard"
    _description = "Construction Wizard"

    start_date = fields.Date(string="Start date")
    end_date = fields.Date(string="End date")

    def print_report(self):
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date
        }

        if self.start_date and self.end_date:
            domain = [
                ("scheduled_date", ">=", self.start_date),
                ("scheduled_date", "<=", self.end_date),
            ]

        docids = self.env['construction.site'].search(domain).ids
        print("\n\ndocs\n\n", docids)
        return self.env.ref('construction_site.action_report_construction_detail').report_action(docids)

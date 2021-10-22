from odoo import fields, models
from odoo.tools.translate import _


class HrReferral(models.Model):
    _name = "hr.referral"
    _description = "HR Reference Model"

    name = fields.Char(string=_("Name", required=True), ondelete="cascade")
    email = fields.Char(string=_("Email"))
    referral_name = fields.Many2one("hr.employee", string=_("Referral Name"))
    # many2one(with hr.employee)
    degree = fields.Many2one("hr.recruitment.degree", string=_("Degree"))
    # many2one(with hr.recruitment.degree)
    department = fields.Many2one("hr.job", string=_("Department"))
    # many2one(with hr.job)
    currency_id = fields.Many2one("res.currency", string=_("currency"))
    # print("\n\n\n\n\n",currency_id)
    expected_salary = fields.Float(string=_("Expected Salary"), copy=False)
    summary = fields.Text(string=_("Summary"))
    expected_joining_date = fields.Date(string=_("Expected Joining Date"), copy=False)
    state = fields.Selection(
        [("draft", "Draft"), ("confirm", "Approved"), ("cancel", "Cancel")],
        default="draft",
    )

    def default_head_branch(self):
        return (
            self.env["res.currency"]
            .search([("l10n_cl_short_name", "=", "EUR")], limit=1)
            .id
        )

    def action_confirm(self):
        for rec in self:
            rec.write({"state": "confirm"})

    def action_cancel(self):
        for rec in self:
            rec.write({"state": "cancel"})

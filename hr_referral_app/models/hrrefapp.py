from odoo import api, fields, models


class HrReferralApplication(models.Model):
    _name = "hr.referral.application"
    _description = "Hr Referral Application"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email", default="xyz@gmail.com")
    referral_id = fields.Many2one("hr.employee", string="Referral Name", copy=False)
    degree_id = fields.Many2one("hr.recruitment.degree", string="Degree", copy=False)
    department_id = fields.Many2one("hr.job", string="Department", copy=False)
    expected_salary = fields.Float(string="Salary")
    summary = fields.Text(string="Summary")
    expected_joining_date = fields.Date(string="Expected Joining Date")
    state = fields.Selection(
        [("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")],
        copy=False,
        default="draft",
        string="Status",
    )

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        readonly=True,
        default=lambda self: self.env.company,
    )
    currency_id = fields.Many2one(
        related="company_id.currency_id",
        string="Company Currency",
        readonly=True,
        store=True,
        help="Utility field to express amount currency",
    )

    def action_approved(self):
        for rec in self:
            rec.write({"state": "approved"})

    def action_cancel(self):
        for rec in self:
            rec.write({"state": "cancel"})

    def action_draft(self):
        for rec in self:
            rec.write({"state": "draft"})

from odoo import fields, models, api
from odoo.tools.translate import _
from datetime import date
from dateutil import relativedelta


class CreateEmployees(models.Model):
    _name = "create.employees"
    _description = "Create New Employees."
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True, tracking=True)
    sequence = fields.Integer()
    birth_date = fields.Date(string=_("Birth Date"), required=True, tracking=True)
    age = fields.Integer(string=_("Age"), readonly=True)
    street = fields.Char(string=_("Street"))
    state_id = fields.Many2one("res.country.state", string=_("State"))
    country_id = fields.Many2one("res.country", string=_("Country"))
    city = fields.Char(string=_("City"))
    email = fields.Char(string=_("Email"), required=True, tracking=True)
    phone = fields.Char(string=_("Phone"), required=True, tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
    experience_info = fields.Text(string=_("Experience Info"))
    expected_salary = fields.Integer(string=_("Expected Salary"))
    job_position_id = fields.Many2one(
        "hr.job", string=_("Job Position"), required=True, tracking=True
    )
    affordable_salary = fields.Float(
        related="job_position_id.affordable_salary", string=_("Affordable Salary")
    )
    extra_amount = fields.Float(string=_("Extra Amount"))
    yearly_amount = fields.Float(string=_("Yearly Amount"))
    monthly_amount = fields.Float(string=_("Monthly Amount"))
    start_date = fields.Date(string=_("Start Date"))
    end_date = fields.Date(string=_("End Date"))
    button_hide = fields.Char(compute="_botton_hide")

    def calculate_age(self):
        if self.birth_date:
            self.age = relativedelta.relativedelta(date.today(), self.birth_date).years
            if self.age < 18:
                raise UserError(_("The Employee age cannot be less than 18 years."))

    def calculate_month(self):
        self.monthly_amount = (
            self.expected_salary + self.extra_amount + self.affordable_salary
        )

    def calculate_year(self):
        self.yearly_amount = self.expected_salary + self.extra_amount

    @api.depends("end_date", "start_date")
    def _botton_hide(self):
        if self.end_date and self.start_date:
            experince = relativedelta.relativedelta(self.end_date, self.start_date)
            if experince.years:
                self.button_hide = "year"
            elif experince.months:
                self.button_hide = "month"
            else:
                self.button_hide = False

        else:
            self.button_hide = False

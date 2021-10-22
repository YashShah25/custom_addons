from odoo import api, fields, models
from odoo.exceptions import ValidationError


class CollegeProfile(models.Model):
    _name = "college.profile"
    _description = "bal bal bla"

    var_cls = fields.Char(string="var cls", store=True)
    no = fields.Integer(string="no")
    _sql_constraints = [
        ("email_unique", "unique(var_cls)", "The email of the school must be unique!")
    ]

    @api.constrains("no")
    def check_result(self):
        for record in self:
            print("\n\n\nhello\n\n\n")
            if len(record.no) < 4:
                print("\n\n\nlo\n\n\n")
                raise ValidationError(
                    "you are not eligible to get this rank!!!!!......"
                )

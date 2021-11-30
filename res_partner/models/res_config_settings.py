from odoo import fields, models
from odoo.tools.translate import _


class MySettings(models.TransientModel):
    _inherit = "res.config.settings"

    notify_person_for_limit_exceed = fields.Char(
        string=_("Notify Person for limit Exceed"),
        config_parameter="res_partner.param.notify_person_for_limit_exceed",
    )

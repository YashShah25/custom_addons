from odoo import fields, models
from odoo.tools.translate import _


class ConstructionSite(models.Model):
    _name = "construction.site"
    _description = "this table will contains all the fields related to construction sites and it's work."
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True, tracking=True)
    sequence = fields.Integer(invisible=True)
    reference = fields.Char(string=_("Reference"), tracking=True)
    scheduled_date = fields.Date(string=_("Scheduled Date"))
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("running", "Running"),
            ("stop", "Stopped"),
            ("in_closing", "In Closing"),
            ("closed", "Closed"),
        ],
        default="draft",
        tracking=True,
    )

    responsible_internal_id = fields.Many2one(
        "hr.employee", string=_("Responsible Internal ID")
    )
    responsible_on_site_id = fields.Many2one(
        "res.partner", string=_("Responsible On Site ID")
    )
    delivery_address = fields.Many2one("res.partner", string=_("Delivery Address"))
    product_template_id = fields.Many2one(
        "product.template", string=_("Product Template ID")
    )
    stock_warehouse_id = fields.Many2one(
        "stock.warehouse", string=_("Stock Warehouse ID")
    )
    project_id = fields.Many2one("project.project", string=_("Project ID"))
    purchase_order_ids = fields.Many2many(
        "purchase.order", "abcd_tbl", string=_("Purchase Order IDs")
    )
    analytical_account_id = fields.Many2one(
        "account.analytic.account", string=_("Analytical Account ID")
    )
    sale_order_id = fields.Many2one("sale.order", string=_("Sale Order ID"))
    asset_ids = fields.Many2many("account.asset", "xzy_tbl", string=_("Asset IDs"))
    general_contractor_purchase_id = fields.Many2one(
        "purchase.order", string=_("General Contractor Purchase ID")
    )

    def action_run(self):
        self.state = "running"

    def action_stop(self):
        self.state = "stop"

    def action_in_close(self):
        self.state = "in_closing"

    def action_close(self):
        self.state = "closed"

    def action_draft(self):
        self.state = "draft"

    def name_get(self):
        name_list = []
        for name_code in self:
            display_name = "[{}] {}".format(name_code.reference, name_code.name)
            name_list.append((name_code.id, display_name))
            print("\n\n\n\nname=: ", name_list)
        return name_list

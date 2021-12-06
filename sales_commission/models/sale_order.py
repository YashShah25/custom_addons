from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sales_commission = fields.Float(string=_("Sales Commission"), default=2.5)


class SaleOrderline(models.Model):
    _inherit = "sale.order.line"

    production_commission = fields.Float(
        string=_("Production commission"), compute="_calculate_production_commission"
    )

    @api.depends("price_subtotal", "order_id.sales_commission")
    def _calculate_production_commission(self):
        for line in self:
            line.production_commission = (
                line.price_subtotal * line.order_id.sales_commission
            ) / 100

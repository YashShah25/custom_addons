from odoo import fields, models


class Partner2Orders(models.Model):
    _inherit = "res.partner"

    line_subtotal_count = fields.Float(compute="_compute_line_subtotal")

    def _compute_line_subtotal(self):
        orders = (
            self.env["sale.order"]
            .search([("partner_id", "=", self.id)])
            .mapped("order_line")
        )
        self.line_subtotal_count = sum([line.price_subtotal for line in orders])

    def act_res_partner_2_sale_commission(self):
        lines = (
            self.env["sale.order"]
            .search([("partner_id", "=", self.id)])
            .mapped("order_line")
        )
        return {
            "type": "ir.actions.act_window",
            "view_mode": "tree",
            "name": "Commission History",
            "res_model": "sale.order.line",
            "domain": [("id", "in", lines.ids)],
            "target": "new",
        }

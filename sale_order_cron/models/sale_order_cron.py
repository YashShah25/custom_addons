from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def sale_order_count_cron(self):
        # print("kasjdhgh")
        sale_order = self.env["sale.order"].search(
            [("state", "not in", ("sale", "done"))]
        )
        print("\n\n\n\nSale------", sale_order)

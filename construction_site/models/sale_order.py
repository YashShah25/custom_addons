# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "sale.order"

    def action_view_construction_site(self):
        construction_site = False
        count = self.env["construction.site"].search_count(
            [("sale_order_id.id", "=", self.id)]
        )
        if count == 1:
            construction_site = (
                self.env["construction.site"]
                .search([("sale_order_id", "=", self.id)])
                .id
            )
            view_mode = "form"
        else:
            view_mode = "tree,form"
        return {
            "type": "ir.actions.act_window",
            "view_mode": view_mode,
            "name": "Construction Site",
            "res_model": "construction.site",
            "domain": [("sale_order_id.id", "=", self.id)],
            "res_id": construction_site,
            "target": "current",
        }

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    construction_po_count = fields.Integer(
        compute="_get_count_construction_po", store=False
    )

    def _get_count_construction_po(self):
        self.construction_po_count = self.env["construction.site"].search_count(
            [("general_contractor_purchase_order_id.id", "=", self.id)]
        )

    def action_view_construction_site(self):
        construction_site = False
        count = self.env["construction.site"].search_count(
            [("general_contractor_purchase_order_id.id", "=", self.id)]
        )
        if count == 1:
            construction_site = (
                self.env["construction.site"]
                .search([("general_contractor_purchase_order_id", "=", self.id)])
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
            "domain": [("general_contractor_purchase_order_id.id", "=", self.id)],
            "res_id": construction_site,
            "target": "current",
        }

        # count=False
        # for site in self.env['construction.site'].search([]):
        #     if site.general_contractor_purchase_order_id.id == self.id:
        #         construction_site=site
        #         construction_site.append(site)
        # print("\n\n\n\nsite===", construction_site)
        # print("\n\n\nlen====", len(construction_site))
        # if len(construction_site) > 1:
        #     view_mode = "tree,form"
        # else:
        #     count=True
        #     view_mode = "form"
        #
        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_mode': view_mode,
        #     'name': 'Construction Site',
        #     'res_model': 'construction.site',
        #     'res_id': count and construction_site.id or False,
        #     'target': "current",
        #     # 'view_type': [(self.env.ref('construction_site.construction_site_form_view').id, 'form')],
        #     # 'views': [(self.env.ref('construction_site.construction_site_form_view').id, 'form')],
        # }

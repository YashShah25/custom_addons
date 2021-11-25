# - * - coding: utf - 8 -*-
from odoo import http
from odoo.http import request


class Controller(http.Controller):
    @http.route("/bulk_product_register", type="http", auth="public", website=True)
    def list(self, **kw):
        return request.render(
            "bulk_products.bulk_product_register_template",
            {"master_product_obj": request.env["product.template"].search([]), },
        )

    @http.route("/new_bulk_product", type="http", website=True, auth="user", csrf=False)
    def new_bulk_product(self, **kw):
        if kw:
            print("\n\nkw = ", kw)
            partner = {
                "name": kw.get("partner_name"),
                "email": kw.get("email"),
                "phone": kw.get("phone"),
            }
            new_partner = request.env["res.partner"].sudo().create(partner)
            bulk_products = {
                "name": kw.get("name"),
                "master_product": kw.get("master_product"),
                "user_id": new_partner.id,
                "email": kw.get("email"),
            }
            request.env["bulk.products"].sudo().create(bulk_products)

        return request.redirect("/bulk_product_register")

# - * - coding: utf - 8 -*-
from odoo import http
from odoo.http import request


class Controller(http.Controller):
    @http.route("/fetch_partner_info", type="http", auth="public", website=True)
    def fetch_partner_info(self, **kw):
        return request.render(
            "res_partner.fetch_partner_info_template",
            {"partners": request.env["res.partner"].search([]), },
        )

    @http.route("/update_partner_form", type="http", auth="public", website=True)
    def update_partner_form(self, **kw):
        partner = kw.get("partner")
        vals = {
            "partner": request.env["res.partner"].search([("id", "=", partner)]),
            "partners": partner,
            "states": request.env["res.country.state"].sudo().search([]),
            "countries": request.env["res.country"].sudo().search([]),
        }

        return request.render("res_partner.update_partner_info_template", vals)

    @http.route(
        "/update_partner_info", csrf=False, type="http", auth="public", website=True
    )
    def update_partner_info(self, **kw):
        partner_id = kw.get("partner_id")
        print("\n\npartner_id", partner_id)

        partner = request.env["res.partner"].sudo().search([("id", "=", partner_id)])
        print("\n\npartner", partner)
        partner.update(
            {
                "name": kw.get("name"),
                "street": kw.get("street"),
                "city": kw.get("city"),
                "state_id": kw.get("state_id"),
                "country_id": int(kw.get("country_id")),
                "email": kw.get("email"),
                "phone": kw.get("phone"),
            }
        )
        return request.render("res_partner.update_partner_info_template")

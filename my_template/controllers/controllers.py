# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
	@http.route("/contacts", type="http", website=True, auth="public")
	def demo_page(self):
		contacts = request.env["res.partner"].sudo().search([])
		return request.render("my_template.contact_list", {"contacts": contacts})


class ContactData(http.Controller):
	@http.route(
		"/contact/<model('res.partner'):contact>",
		type="http",
		website=True,
		auth="public",
	)
	def form_page(self, contact, **kw):
		return request.render(
			"my_template.contact_data", {"contact": contact}
		)

# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class ProductList(http.Controller):
    @http.route("/products", type="http", website=True, auth="public")
    def list_page(self):
        product_list = request.env["product.template"].sudo().search([])
        return request.render(
            "product_website.product_detail_list", {"product_list": product_list}
        )


class ProductData(http.Controller):
    @http.route(
        "/product/info/<model('product.template'):product>",
        type="http",
        website=True,
        auth="public",
    )
    def form_page(self, product, **kw):
        return request.render(
            "product_website.product_detail_form", {"product_data": product}
        )

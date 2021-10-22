# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route("/demo/page", type="http", website=True, auth="public")
    def demo_page(self):
        """Returns the manifest used to install the page as app"""
        return request.render("template_session.demo_page", {})

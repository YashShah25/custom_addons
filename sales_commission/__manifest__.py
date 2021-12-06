# -*- coding: utf-8 -*-

{
    "name": "Sales Commission",
    "summary": """
        This module will apply production commission in sale order.
        """,
    "description": """
        With the help of this module we can easily track commissions histories and also apply commission in sale order.
        """,
    "author": "Yash Shah",
    "website": "https://google.com",
    # for the full list
    "category": "Business",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management"],
    # always loaded
    "data": ["views/res_partner_views.xml", "views/sale_order_views.xml",],
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}

# -*- coding: utf-8 -*-
{
    "name": "Product Template",
    "author": "Yash Shah",
    "summary": """
        Demo module for template session""",
    "description": """this application..""",
    "website": "https://youtube.com",
    "category": "General",
    "version": "14.0.1.0.0",
    # necessary modules
    "depends": ["website", "product", "stock"],
    # always load
    "data": [
        "data/product_menu.xml",
        "views/product_template_list.xml",
        "views/product_template_form.xml",
        "views/assets.xml",
    ],
    "demo": [],
    "auto_install": False,
    "installable": True,
    "application": True,
    "sequence": 1,
}

# -*- coding: utf-8 -*-
{
    "name": "Bulk Products",
    "summary": """
    to use the bulk product
        """,
    "description": """
    """,
    "author": "Shahil Chauhan",
    "website": "http://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management", "stock", "website"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/bulk_product_menu.xml",
        "views/bulk_products_views.xml",
        "views/sale_order_views_menu.xml",
        "views/sales_order_views.xml",
        "views/new_bulk_product_register_template.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

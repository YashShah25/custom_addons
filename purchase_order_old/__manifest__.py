# -*- coding: utf-8 -*-

{
    "name": "Purchase Order",
    "summary": """Inherit Purchase order module """,
    "description": """In this module we will add some advanced functionality in purchase order module using inheritance """,
    "author": "Yash Shah",
    "website": "https://google.com",
    # for the full list
    "category": "Business",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["purchase"],
    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/purchase_order.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}

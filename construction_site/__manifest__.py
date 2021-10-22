{
    "name": "Construction Site",
    "author": "Yash Shah",
    "summary": """Field related work""",
    "description": "This module manage all construction sites and site related work",

    "website": "https://www.aktivesoftware.com",
    "category": "Business",
    "version": "14.0.1.0.0",

    "depends": [
        "mail",
        "sale_management",
        "account",
        "hr",
        "stock",
        "project",
        "purchase",
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/construction_site_view.xml',
        'views/project_task_view.xml',
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
    ],
    "demo": [],
    "sequence": 1,
    "application": True,
    "installable": True,
    "auto-install": False,
}

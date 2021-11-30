# -*- coding: utf-8 -*-

{
    "name": "Quotation Limit",
    "summary": """This module will check Quotation Limit of customer.""",
    "description": """With the help of above module we can limit the quotation between Credit and Blocking limits. """,
    "author": "Yash Shah",
    "website": "https://google.com",
    # for the full list
    "category": "Business",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management", "website", ],
    # always loaded
    "data": [
        "data/fetch_partner_info_menu.xml",
        "data/quotation_limit_mail_template_view.xml",
        "views/res_partner_views.xml",
        "views/assets.xml",
        "views/res_config_settings_view.xml",
        "views/partner_info_template.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}

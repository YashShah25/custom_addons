# -*- coding: utf-8 -*-

{
    "name": "Hr Referral Application",
    "summary": """""",
    "description": """""",
    "author": "Akash Patel",
    "website": "aktivsoftware.com",
    # for the full list
    "category": "hr",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": [
        "hr_recruitment",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/hr_ref_app_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

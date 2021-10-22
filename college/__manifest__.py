{
    "name": "College",
    "version": "14.0.1.0.0",
    "summary": "College Management System",
    "sequence": 1,
    "description": "This is a college management system.",
    "category": "Education/College",
    "author": "Yash Shah",
    "website": "https://www.google.com/",
    "depends": [
        "website_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/college_view.xml",
        "views/setting.xml",
        "views/website_view_inherit.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}

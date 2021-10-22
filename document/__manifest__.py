{
    "name": "Docu",
    "author": "Yash Shah",
    "summary": """This is my documentation application""",
    "description": """You can create you're documents by using this application..""",
    "website": "https://muchconsulting.de",
    # full list
    "category": "General",
    "version": "14.0.1.0.0",
    # necessary modules
    "depends": [
        "mail",
    ],
    # always load
    "data": [
        "security/ir.model.access.csv",
        "data/doc_version_data.xml",
        "views/doc_item_views.xml",
        "views/doc_tags_views.xml",
        "views/doc_version_views.xml",
        "report/report.xml",
    ],
    "demo": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

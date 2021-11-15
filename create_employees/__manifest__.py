{
    "name": "Create Employees",
    "author": "Yash Shah",
    "summary": """Work Space""",
    "description": "This module manage all employee record.",
    "website": "https://www.aktivesoftware.com",
    "category": "Business, Corporate",
    "version": "14.0.1.0.0",
    "depends": [
        "mail",
        "website",
        "hr_recruitment"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/employee_menu.xml",
        "views/create_employee_view.xml",
        "views/hr_job_view.xml",
        "views/employee_info.xml",
        "views/employee_details.xml",
    ],
    "demo": [],
    "sequence": 1,
    "application": True,
    "installable": True,
    "auto-install": False,
}

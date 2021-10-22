url = "http://127.0.0.1:8069"
db = "taskdb"
username = "admin"
password = "admin"

import csv  # Imported to read csv files
import os
import xmlrpc.client  # import to user xmlrpc API
from datetime import datetime

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % url)  # for authentication
version = common.version()  # to check if connection is correct before authentication
uid = common.authenticate(
    db, username, password, {}
)  # Used as parameter while calling methods
models = xmlrpc.client.ServerProxy(
    "{}/xmlrpc/2/object".format(url)
)  # Used as parameter while calling method

start_time = datetime.now()

with open(
    "/home/odoo/Documents/odoo/custom_addons/my_script/res_partner.csv", newline=""
) as csv_file:
    csv_file = csv.DictReader(csv_file)

    excel_row = 2

    partner_count = models.execute_kw(
        db, uid, password, "res.partner", "search_count", [[]]
    )

    for row in csv_file:
        rec = dict(row)
        if excel_row >= 2:

            partner_id = models.execute_kw(
                db,
                uid,
                password,
                "res.partner",
                "search",
                [[["email", "=", rec["email"].strip()]]],
            )

            vals = {
                "phone": rec["phone"].strip(),
                "email": rec["email"].strip(),
                "city": rec["city"].strip(),
                "name": rec["name"].strip(),
            }
            if partner_id:
                models.execute_kw(
                    db, uid, password, "res.partner", "write", [[partner_id[0]], vals]
                )
            else:
                models.execute_kw(db, uid, password, "res.partner", "create", [vals])

    remove_partner_id = models.execute_kw(
        db, uid, password, "res.partner", "search", [[["city", "=", "Berlin"]]]
    )
    models.execute_kw(
        db,
        uid,
        password,
        "res.partner",
        "unlink",
        [[partner for partner in remove_partner_id]],
    )
# update_name_ids = models.execute_kw(db, uid, password, 'res.partner', 'search',
#                                       [[['name', '=', 'My Company (San Francisco)']]])
# update_company_ids = models.execute_kw(db, uid, password, 'res.partner', 'search',
#                                       [[['parent_id', '=', update_name_ids[0]]]])

excel_row += 1

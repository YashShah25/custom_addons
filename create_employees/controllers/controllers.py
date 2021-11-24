# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route(
        "/create_employee", type="http", website=True, auth="public", csrf=False
    )
    def employee_info(self):
        employee = request.env["create.employees"].sudo().search([])
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        job_position = request.env["hr.job"].sudo().search([])
        return request.render(
            "create_employees.create_employees_template",
            {
                "employee": employee,
                "states": states,
                "countries": countries,
                "job_position": job_position,
            },
        )

    @http.route("/create_emp", type="http", website=True, auth="user", csrf=False)
    def new_employee_create(self, **kw):
        name = kw.get("name")
        birth_date = kw.get("birth_date")
        street = kw.get("street")
        state_id = kw.get("state_id")
        country_id = kw.get("country_id")
        city = kw.get("city")
        email = kw.get("email")
        phone = kw.get("phone")
        gender = kw.get("gender")
        experience_info = kw.get("experience_info")
        expected_salary = kw.get("expected_salary")
        jp = kw.get("job_position_id")

        print(
            f"\n\n\n\n name:{name}\n,dob:{birth_date}\n,street:{street}\n,sate:{state_id}\n,country: {country_id}\n,"
            f"city :{city}\n,email: {email}\n,Phone :{phone}\n,gender: {gender}\n,exp_info : {experience_info}\n,"
            f"exp_sal :{expected_salary}\n,jp:{jp}"
        )
        if kw:
            print("\n\nkw = ", kw)
            request.env["create.employees"].sudo().create(kw)
        return request.redirect("/create_employee")

    @http.route("/employee_details", type="http", website=True, auth="user", csrf=False)
    def employee_details(self, **kw):
        job_position = request.env["hr.job"].sudo().search([])
        values = {"job_position": job_position}
        if kw:
            jp, filtered_employee = False, False
            if kw.get("job_position"):
                jp = int(kw.get("job_position"))
                filtered_employee = (
                    request.env["create.employees"]
                    .sudo()
                    .search([("job_position_id", "=", jp)])
                )
            values.update(
                {"submit": True, "filtered_employee": filtered_employee, "jp": jp}
            )
        return request.render("create_employees.employees_details_template", values)

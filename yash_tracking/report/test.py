from odoo import api, fields, models


class TestMethod(models.Model):
    _name = "report.sale.report_saleorder_document"
    _description = "bako"

    # def temp(self):
    # 	dic = {'y': 'yashu'}
    # 	return dic

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n===> _get_report_callingggg", self)
        print("\n\n\n===> docids_callingggg", docids)

        docs = self.env["school.profile"].browse(docids)
        students = self.env["student.profile"].search(
            [("school_select_id.id", "=", docids[0])]
        )
        students_list = []
        for stu in students:
            students_list.append(stu.name)
        print("student id", students)
        print("student list", students_list)
        return {
            "doc_model": "school.profile",
            "data": data,
            "docs": docs,
            "students_list": students_list,
        }

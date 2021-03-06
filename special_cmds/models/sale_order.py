from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_partner_ids = fields.Many2many(
        "res.partner", "res_partner_rel", "res_id", "partner_id", string="Partner"
    )

    def update_m2m_button(self):
        print("\n\n\n\n\n UPDATE M2m BUTTON")

        """ (0,0,{}) -->  CREATE NEW RECORD IN DATABASE"""
        # range_list = []
        # for i in range(0, 2):
        #     cust_dict = {'name': i}
        #     range_list.append(cust_dict)
        # for val in range_list:
        #     self.partner_cust_ids = [(0, 0, val)]

        """ (1,id,{}) -->  UPDATE RECORD IN DATABASE IF EXIST """
        # self.custom_partner_ids = [(1, 44, {'phone': '654987312'})]

        """ (2,id) -->  REMOVE RECORD FROM DATABASE """
        # self.custom_partner_ids= [(2,14)]

        """ (3,id) -->  REMOVE RECORD FROM FIELD BUT NOT PERMENENT """
        # self.custom_partner_ids= [(3,14)]

        """ (4,id) -->  ADD EXISTING RECORD IN DATABASE"""
        # self.custom_partner_ids = [(4,27)]

        """ (5,) -->  UNLINK ALL RECORD FROM FIELD BUT NOT PERMENENT """
        # self.custom_partner_ids = [(5,)]

        """ (6,0,[IDs]) -->  REMOVE RECORD FROM DATABASE """
        self.custom_partner_ids = [(6, 0, [14, 23, 33])]

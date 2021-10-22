import pytz

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def my_cron(self):
        print("\n\n\n\ncron called------\nself:", self)
        orders = self.env["sale.order"].search([("state", "not in", ("done", "sale"))])
        print("\n\n\n\norders------", orders)

    # @api.model
    # def default_get(self):
    # 	super()
    # 	# print("\n\n\n\nloop tz:")
    # 	# user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
    # 	# date_time = self.nextcall.astimezone(user_tz)
    # 	# print("\nuser tz:", user_tz)
    # 	# print("\ndate time:", date_time)
    # 	self.write({'nextcall': datetime.now().replace(hour=24, minute=0, second=0, microsecond=0)})
    # 	print("\n\n\n\nxyz= ", nextcall)

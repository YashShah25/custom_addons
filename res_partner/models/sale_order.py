from odoo import api, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        credit_limit_score = vals.partner_id.credit_limit_score
        blocking_limit_score = vals.partner_id.blocking_limit_score
        credit_limit = vals.partner_id.credit_limit
        blocking_limit = vals.partner_id.blocking_limit
        amount_total = vals.amount_total
        email = vals.partner_id.email
        if credit_limit_score and credit_limit:
            for so in vals.env["sale.order"].search([
                ("partner_id", "in", vals.partner_id.ids),
                ("state", "in", ["draft", "sent"]),
            ]):
                amount_total += so.amount_total
            if amount_total > credit_limit_score:
                template = vals.env.ref('res_partner.quotation_limit_mail_template')
                print("\n\n\n\n\n mail", template)
                template.send_mail(vals.id, force_send=True)
                raise ValidationError(
                    _('“Your Sale Order Credit Limit has been Exceeded."')
                )
        if blocking_limit_score and blocking_limit:
            for total in vals.env["sale.order"].search(
                    [("partner_id", "in", vals.partner_id.ids), ("state", "=", "sale")]
            ):
                amount_total += total.amount_total
            if amount_total > blocking_limit_score:
                template = vals.env.ref('res_partner.quotation_limit_mail_template')
                template.send_mail(vals.id, email_values={'email_to': email})
                raise ValidationError(
                    _("“You cannot create SO as the Block Limit has been Exceeded”")
                )
        return super(SaleOrder, self).create(vals)

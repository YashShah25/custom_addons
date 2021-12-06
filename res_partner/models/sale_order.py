from odoo import api, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        rtn = super(SaleOrder, self).create(vals)
        credit_limit_score = rtn.partner_id.credit_limit_score
        blocking_limit_score = rtn.partner_id.blocking_limit_score
        credit_limit = rtn.partner_id.credit_limit
        blocking_limit = rtn.partner_id.blocking_limit
        amount_total = rtn.amount_total
        email_to = (
            self.env["ir.config_parameter"].sudo().get_param("res_partner.param.notify_person_for_limit_exceed"))
        if credit_limit_score and credit_limit:
            for so in self.env["sale.order"].search([
                ("partner_id", "in", rtn.partner_id.ids),
                ("state", "in", ["draft", "sent"]),
            ]):
                amount_total += so.amount_total
            if amount_total > credit_limit_score:
                if email_to:
                    context = {
                        'message': 'Credit',
                        'exceeding_amount': credit_limit_score,
                    }
                    template_id = self.env.ref('res_partner.quotation_limit_mail_template')
                    template_id.with_context(context).send_mail(rtn['partner_id'].id,
                                                                email_values={"email_to": email_to},
                                                                force_send=True)
                self._cr.commit()
                super(SaleOrder, rtn).unlink()
                raise ValidationError(
                    _('“Your Sale Order Credit Limit has been Exceeded."')
                )
        if blocking_limit_score and blocking_limit:
            for total in self.env["sale.order"].search(
                    [("partner_id", "in", rtn.partner_id.ids), ("state", "=", "sale")]
            ):
                amount_total += total.amount_total
            if amount_total > blocking_limit_score:
                if email_to:
                    context = {
                        'message': 'Blocking',
                        'exceeding_amount': blocking_limit_score,
                    }
                    template = self.env.ref('res_partner.quotation_limit_mail_template')
                    template.with_context(context).send_mail(rtn['partner_id'].id, email_values={"email_to": email_to},
                                                             force_send=True)
                super(SaleOrder, rtn).unlink()
                self._cr.commit()
                raise ValidationError(
                    _("“You cannot create SO as the Block Limit has been Exceeded”")
                )
        return rtn

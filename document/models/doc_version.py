from odoo import api, fields, models


class DocumentVersion(models.Model):
    _name = "doc.version"
    _description = "Document Version"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(default=True)
    #
    # @api.model
    # def unlink(self):
    #
    # 	rtn = super(DocumentVersion, self).unlink()
    # 	return rtn
    #
    # def clear_record(self):
    # 	self.write({'name': '', 'active': ''})

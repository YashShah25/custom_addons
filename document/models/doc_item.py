from odoo import api, fields, models


class DocumentItem(models.Model):
    _name = "doc.item"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Document Items"

    name = fields.Char(string="Name123", required=True, tracking=True)
    language = fields.Selection(
        [("guj", "Gujarati"), ("eng", "English"), ("hin", "Hindi")],
        string="Languages Known",
    )
    lan_count = fields.Integer(compute="_compute_active_lang_count")
    description_short = fields.Text(string="Short Description")
    description_long = fields.Html(string="Long Description")

    ver_id = fields.Many2one("doc.version", string="version", tracking=True)

    video_url = fields.Char(string="Video URL")
    google_doc_url = fields.Char(string="Google Document URL")

    tags = fields.Many2many(
        "doc.tags",
        "item_tags_relation",
        "item_id",
        "tag_id",
        string="tags",
        tracking=True,
    )

    item_type = fields.Selection(
        [
            ("documentation", "Documentation"),
            ("tipp", "Tipp"),
            ("customer", "Customer"),
            ("automation", "Automation"),
            ("technical", "Technical"),
            ("configuration", "Configuration"),
        ],
        string="Type",
        required=True,
        default="documentation",
        tracking=True,
    )

    active = fields.Boolean(string="Active", default=True)

    @api.depends("language")
    def _compute_active_lang_count(self):
        count = len(self.env["res.lang"].get_installed())
        for item in self:
            item.lan_count = count

    @api.model_create_multi
    def create(self, value):
        print("\n\n\n\n\nCreating...\n\n\n\n\n")
        rtn = super(DocumentItem, self).create(value)
        return rtn

    def write(self, val):
        print("\n\n\n\n\nWriting...\n\n\n\n\n", val)
        rtn = super(DocumentItem, self).write(val)
        return rtn

    # @api.returns('self', lambda value: value.id)
    def copy(self, default={}):
        default["name"] = "copy (" + self.name + ")"
        print("\n\n\n\n\nDublicatiog...\n\n\n\n\n", default)
        rtn = super(DocumentItem, self).copy(default=default)
        return rtn

    def unlink(self):
        print("\n\n\n\n\nDeleting...\n\n\n\n\n")
        for co in self:
            if co.lan_count > 0:
                raise UserWarning("You can't delete this %s's record" % co.name)
        rtn = super(DocumentItem, self).unlink()
        return rtn

    @api.model
    def name_create(self, tags):
        print("\n\n\n\n\n  creating Inside...\n\n\n\n\n")
        rtn = self.create({"name": tags})
        return rtn.tags_get()[0]

from odoo import api, fields, models


class TestMethod(models.Model):
    _name = "report.document.document_detail_report"
    _description = "bako"

    # def temp(self):
    # 	dic = {'y': 'yashu'}
    # 	return dic

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n===> _get_report_callingggg", self)
        print("\n\n\n===> docids_callingggg", docids)

        docs = self.env["doc.tags"].browse(docids)
        print("docs: ", docs)
        documents = self.env["doc.tags"].search([])
        print("documents: ", documents)
        document_nam_list = []
        document_actibe_list = []
        for doc in documents:
            print("doc: ", doc)
            document_nam_list.append(doc.name)
            document_actibe_list.append(doc.active)
        print("documents", documents)
        print("document list", document_nam_list)
        print("document list", document_actibe_list)
        return {
            "doc_model": "document",
            "data": data,
            "docs": docs,
            "document_actibe_list": document_nam_list,
            "document_actibe_list": document_actibe_list,
        }

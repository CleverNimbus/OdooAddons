# https://www.cybrosys.com/blog/name-search-function-in-odoo-14

from odoo import models, api


class CNProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            # domain = ['|', '|', ('name', operator, name), ('phone', operator, name) ('email', operator, name)]
            domain = ['|', '|', '|', ('name', operator, name), ('partner_ref', operator, name),
                      ('barcode', operator, name), ('product_tmpl_id.name', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

#    @api.model
#    def name_search(self, name='', args=None, operator='ilike', limit=100):
#        res = super(CNProductProduct, self).name_search(name=name, args=args, operator=operator, limit=limit)
#        ids = self.search(args + [('partner_ref', '=', name)], limit=limit)
#        if ids:
#            return ids.name_get()
#        return res

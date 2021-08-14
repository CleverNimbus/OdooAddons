from odoo import models, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        # Make a search with default criteria
        products = super().name_search(name=name, args=args, operator=operator, limit=limit)
        # Make the other search
        products2 = []
        if name:
            domain = [('default_code_ids.name', 'ilike', name)]
            products2 = self.search(domain, limit=limit).name_get()
        # Merge both results
        return list(set(products) | set(products2))[:limit]

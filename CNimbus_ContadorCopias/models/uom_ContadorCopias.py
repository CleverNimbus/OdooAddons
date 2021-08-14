from odoo import models, fields


class UomCategory(models.Model):
    _inherit = "uom.category"

    measure_type = fields.Selection(selection_add=[('copiesA4BN', 'Copies A4 BN'),
                                                   ('copiesA4Color', 'Copies A4 Color'),
                                                   ('copiesA3BN', 'Copies A3 BN'),
                                                   ('copiesA3Color', 'Copies A3 Color'),
                                                   ('copiesBunner', 'Copies Banner')])

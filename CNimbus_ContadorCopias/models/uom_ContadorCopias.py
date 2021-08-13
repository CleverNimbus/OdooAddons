# -*- encoding: utf-8 -*-
from odoo import models, fields


class UomCategory(models.Model):
    _inherit = "uom.category"

    measure_type = fields.Selection(selection_add=[('copies', 'Copies')])
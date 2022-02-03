# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_description = fields.Char(string="Sale Description")
    # age = fields.Integer(string="Age")
    # gender = fields.Selection(
    #     [('male', 'Male'), ('female', 'Female'),], required=True, default='male'
    # )
    # note = fields.Text(string="Description")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

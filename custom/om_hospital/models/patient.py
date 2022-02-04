# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], required=True, default='male'
    )
    note = fields.Text(string="Description", tracking=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Parent")

    def to_confirm(self):
        # self.state = 'confirmed'
        self.write({'state': 'confirm'})

    def to_done(self):
        # self.state = 'confirmed'
        self.write({'state': 'done'})

    def to_cancel(self):
        # self.state = 'confirmed'
        self.write({'state': 'cancel'})

    def to_draft(self):
        # self.state = 'confirmed'
        self.write({'state': 'draft'})

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

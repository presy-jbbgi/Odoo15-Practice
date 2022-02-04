# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required="True")
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], required=True, default='male'
    )
    note = fields.Text(string="Description")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft')

    #
    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100
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

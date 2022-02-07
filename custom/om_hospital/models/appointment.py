# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", readonly=True, default=lambda self: _('New Appointment'),)
    patient_id = fields.Many2one('hospital.patient', string="Patient",)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)
    note = fields.Text(string="Description", tracking=True)
    date_appointment = fields.Date(string="Date")

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

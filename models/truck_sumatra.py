from odoo import models, fields

class SumatraSumatra(models.Model):
     _name = 'sumatra.sumatra'
     _iniherit = 'fleet.vehicle'
     
     truck = fields.Many2one('fleet.vehicle', string="Truck" , required=True)
     licence_no  = fields.Char(string="Licence no", required=True)
     file_ref_no = fields.Char(string='File Registration no' , required=True)
     receipt_no  = fields.Integer(string="Receipt no", required=True)
     amount      = fields.Integer(string="Amount", required=True)
     issue_date  = fields.Date(string='Date of Issue' , required=True)
     exp_date    = fields.Date(string='Expiry Date' , required=True)
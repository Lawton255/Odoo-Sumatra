from odoo import models, fields

class SumatraSumatra(models.Model):
     _name = 'sumatra.truck'
     _iniherits = {'fleet.vehicle': 'licence_plate' }
     _order = 'licence_plate'
     
     licence_plate = fields.Many2one('fleet.vehicle', 'Truck', required=True , auto_join=True, index=True, ondelete='cascade')
     licence_no  = fields.Char(string="Licence no", required=True)
     file_ref_no = fields.Char(string='File Registration no' )
     receipt_no  = fields.Integer(string="Receipt no")
     amount      = fields.Integer(string="Amount", required=True)
     issue_date  = fields.Date(string='Date of Issue' , required=True)
     exp_date    = fields.Date(string='Expiry Date' , required=True)
# -*- coding: utf-8 -*-
from odoo import http

# class SumatraNew(http.Controller):
#     @http.route('/sumatra_new/sumatra_new/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sumatra_new/sumatra_new/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sumatra_new.listing', {
#             'root': '/sumatra_new/sumatra_new',
#             'objects': http.request.env['sumatra_new.sumatra_new'].search([]),
#         })

#     @http.route('/sumatra_new/sumatra_new/objects/<model("sumatra_new.sumatra_new"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sumatra_new.object', {
#             'object': obj
#         })
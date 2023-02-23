# -*- coding: utf-8 -*-
# from odoo import http


# class SalonBase(http.Controller):
#     @http.route('/salon_base/salon_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salon_base/salon_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('salon_base.listing', {
#             'root': '/salon_base/salon_base',
#             'objects': http.request.env['salon_base.salon_base'].search([]),
#         })

#     @http.route('/salon_base/salon_base/objects/<model("salon_base.salon_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salon_base.object', {
#             'object': obj
#         })

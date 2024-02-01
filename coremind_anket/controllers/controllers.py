# -*- coding: utf-8 -*-
# from odoo import http


# class CoremindAnket(http.Controller):
#     @http.route('/coremind_anket/coremind_anket', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coremind_anket/coremind_anket/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('coremind_anket.listing', {
#             'root': '/coremind_anket/coremind_anket',
#             'objects': http.request.env['coremind_anket.coremind_anket'].search([]),
#         })

#     @http.route('/coremind_anket/coremind_anket/objects/<model("coremind_anket.coremind_anket"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coremind_anket.object', {
#             'object': obj
#         })


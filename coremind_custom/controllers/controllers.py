# -*- coding: utf-8 -*-
# from odoo import http


# class CoremindCustom(http.Controller):
#     @http.route('/coremind_custom/coremind_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coremind_custom/coremind_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('coremind_custom.listing', {
#             'root': '/coremind_custom/coremind_custom',
#             'objects': http.request.env['coremind_custom.coremind_custom'].search([]),
#         })

#     @http.route('/coremind_custom/coremind_custom/objects/<model("coremind_custom.coremind_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coremind_custom.object', {
#             'object': obj
#         })


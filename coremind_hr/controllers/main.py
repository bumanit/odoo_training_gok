# -*- coding: utf-8 -*-
from odoo import http

# type='http', auth='user', methods=['POST'], csrf=False


class CoremindCustom(http.Controller):
    @http.route("/api/check", type="http", auth="user", method=["POST"], csrf=False)
    def index(self, **kwargs):
        vals = {
            "product_ids": [
                {"product_id": 1, "price": 1, "qty": 1},
                {"product_id": 1, "price": 1, "qty": 1},
                {"product_id": 1, "price": 1, "qty": 1},
            ]
        }
        self.env["sale.order"].sudo().create(vals)
        self.env["sale.order"].with_user(1).create(vals)
        return {"success": True}

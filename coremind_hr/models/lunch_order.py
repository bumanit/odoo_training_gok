from odoo import models, fields, api, _


class LunchOrder(models.Model):
    _inherit = "lunch.order"

    employee_id = fields.Many2one("hr.employee")

import datetime
from odoo import models, fields, api, _


class HrEmployeeLunchOrderWizard(models.TransientModel):
    _name = "hr.employee.lunch.order.wizard"
    _description = "HR Employee Lunch Order Wizard"

    def _default_date(self):
        return datetime.date.today()

    date = fields.Date(default=fields.Datetime.today)
    # date = fields.Date(default=_default_date)
    employee_ids = fields.Many2many("hr.employee")

    def create_order(self):
        lunchOrder = self.env["lunch.order"]
        product_id = self.env["lunch.product"].search([])[-1]
        vals_list = []
        for employee_id in self.employee_ids:
            vals_list.append(
                {
                    "date": self.date,
                    "product_id": product_id.id,
                    "employee_id": employee_id.id,
                    "user_id": self.env.uid,
                    "supplier_id": product_id.supplier_id.id,
                    "state": "confirmed",
                }
            )
        lunchOrder.create(vals_list)

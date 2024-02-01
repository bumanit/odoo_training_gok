from odoo import models, fields, api, _
from odoo.tools import (
    DEFAULT_SERVER_DATETIME_FORMAT,
    DEFAULT_SERVER_DATE_FORMAT,
    start_of,
)

# from odoo.tools.misc import profile

date = "YYYY-MM-DD"
datetime = "YYYY-MM-DD HH:mm:SS"


class HrEmployeeLunchOrderReportWizard(models.TransientModel):
    _name = "hr.employee.lunch.order.report.wizard"
    _description = "Hr Employee Lunch Order Report Wizard"

    def _default_start_date(self):
        today = fields.Date.today()
        "31/01/2024"
        # today_str = today.strftime(DEFAULT_SERVER_DATE_FORMAT)
        # today_list = today_str.split("-")  # [2024, 01, 31]
        # today_str[-1] = "01"
        # today_str = "-".join()
        # date = datetime.strptime("31/01/2024", "d/m/Y")
        return start_of(today, "month")

    start_date = fields.Date(default=_default_start_date)
    end_date = fields.Date(default=fields.Date.today)
    report_type = fields.Selection(
        [
            ("summary", _("Summary")),
            ("detail", _("Detail")),
        ]
    )
    supplier_id = fields.Many2one("lunch.supplier")
    employee_ids = fields.Many2many("hr.employee")

    def pdf_report(self):
        data = {}
        data["start_date"] = self.start_date
        data["end_date"] = self.end_date
        data["report_type"] = self.report_type
        data["supplier_id"] = self.supplier_id
        data["report_date"] = fields.Date.today()
        data["employee_names"] = ", ".join(
            [emp_id.name for emp_id in self.employee_ids]
        )
        data["lunch_ids"] = self.env["lunch.order"].search(
            [("employee_id", "in", self.employee_ids)]
        )
        return self.env.ref("coremind_hr.hr_employee_lunch_order_report").report_action(
            self, data=data
        )

    def excel_report(self):
        pass

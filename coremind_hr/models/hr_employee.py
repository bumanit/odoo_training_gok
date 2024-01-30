import datetime
import dateutil
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Hr Employee"

    work_start_date = fields.Date(_("Work Start Date"))
    organization_start_date = fields.Date(_("Organization Start Date"))
    worked_months = fields.Integer()
    organization_worked_months = fields.Integer(
        compute="_compute_organization_worked_months", store=True
    )
    code = fields.Char(readonly=False, copy=False)

    _sql_constraints = [
        (
            "code",
            "unique(code)",
            _("Only one code in company"),
        ),
    ]

    @api.model
    def _name_search(self, name, domain=None, operator="ilike", limit=None, order=None):
        domain = domain or []
        if name:
            name_domain = [
                "|",
                ("code", "ilike", name),
                ("name", operator, name),
            ]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                name_domain = ["&", "!"] + name_domain[1:]
            domain = expression.AND([name_domain, domain])
        return self._search(domain, limit=limit, order=order)

    # @api.constraints("work_start_date")
    # def _constraint_work_start_date(self):
    #     today = datetime.date.today()
    #     for rec in self:
    #         if rec.work_start_date >= today:
    #             raise ValidationError(_("Work start date not equal to today"))

    @api.model_create_multi
    def create(self, vals_list):
        print("###################")
        print("Create Function for employee")
        print("###################")
        for vals in vals_list:
            code = self.env["ir.sequence"].next_by_code("hr.employee.code")
            print("##################")
            print(code)
            print("##################")
            vals["code"] = code
        return super().create(vals_list)

    @api.onchange("work_start_date")
    def _onchange_work_start_date(self):
        today = datetime.date.today()
        for rec in self:
            rec.worked_months = 1
            current_date = rec.work_start_date
            month = 0
            if current_date:
                while current_date <= today:
                    current_date += relativedelta(months=1)
                    month += 1

            rec.worked_months = month

    @api.depends("organization_start_date")
    def _compute_organization_worked_months(self):
        today = datetime.date.today()

        for rec in self:
            month = 0
            current_date = rec.organization_start_date
            if current_date:
                while current_date <= today:
                    current_date += relativedelta(months=1)
                    print(current_date)
                    month += 1

            rec.organization_worked_months = month


class HrEmployeeChild(models.Model):
    _name = "hr.employee.child"
    _description = "Hr Emp Child"

    employee_id = fields.Many2one("hr.employee")
    name = fields.Char()

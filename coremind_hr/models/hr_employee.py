import datetime
import dateutil
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Hr Employee"

    work_start_date = fields.Date(_("Work Start Date"))
    organization_start_date = fields.Date(_("Organization Start Date"))
    worked_months = fields.Integer()
    organization_worked_months = fields.Integer(
        compute="_compute_organization_worked_months", store=True
    )
    # company_id = fields.Many2one("res.company")
    child_ids = fields.One2many("hr.employee.child", "employee_id")

    # _sql_constraints = (("worked_months", "unique"),)

    # @api.constraints("work_start_date")
    # def _constraint_work_start_date(self):
    #     today = datetime.date.today()
    #     for rec in self:
    #         if rec.work_start_date >= today:
    #             raise ValidationError(_("Work start date not equal to today"))

    @api.onchange("work_start_date")
    def _onchange_work_start_date(self):
        today = datetime.date.today()
        print(today)
        print(today)
        print(today)
        for rec in self:
            if rec.work_start_date >= today:
                raise UserError(_("Work start date not equal to today"))

            rec.worked_months = 1
            current_date = rec.work_start_date
            month = 0
            while current_date <= today:
                current_date += relativedelta(months=1)
                print(current_date)
                month += 1

            rec.worked_months = month

    @api.depends("organization_start_date")
    def _compute_organization_worked_months(self):
        today = datetime.date.today()

        for rec in self:
            # if rec.organization_start_date and rec.organization_start_date >= today:
            #     raise UserError(_("Work start date not equal to today"))

            month = 0
            current_date = rec.organization_start_date
            if current_date:
                while current_date <= today:
                    current_date += relativedelta(months=1)
                    print(current_date)
                    month += 1

            rec.organization_worked_months = month

    # def _inverse_organization_worked_months(self):
    #     for rec in self:
    #         rec.organization_worked_months


# class ResCompany(models.Model):
#     _inherit = "res.company"

#     employee_ids = fields.One2many("hr.employee", "company_id")


class HrEmployeeChild(models.Model):
    _name = "hr.employee.child"
    _description = "Hr Emp Child"

    employee_id = fields.Many2one("hr.employee")
    name = fields.Char()

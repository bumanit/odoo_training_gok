# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _
from odoo.tools import date_range


class HrJob(models.Model):
    _name = "hr.job.emc"
    _description = "hr.job"

    name = fields.Char()
    begin_date = fields.Date()
    end_date = fields.Date()
    position = fields.Char()
    state = fields.Selection(
        [
            ("normal", _("Normal")),
            ("not normal", _("Not Normal")),
        ]
    )
    employee_id = fields.Many2one("hr.employee")
    job_month = fields.Integer(compute="_month_calc", store=True)

    @api.depends("begin_date", "end_date")
    def _month_calc(self):
        for c in self:
            begin_date = c.begin_date
            end_date = c.end_date
            if not end_date:
                end_date = fields.Date.today()

            month = 0
            if begin_date and end_date:
                while begin_date <= end_date:
                    begin_date += relativedelta(months=1)
                    month += 1

            c.job_month = month


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Hr Employee"

    job_ids = fields.One2many("hr.job.emc", "employee_id")

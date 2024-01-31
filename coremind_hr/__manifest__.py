# -*- coding: utf-8 -*-
{
    "name": "Coremind Human Resource",
    "summary": "Custom Development For Human Resource",
    "description": """
Long description of module's purpose
    """,
    "author": "Erdenet",
    "website": "https://www.erdenet.mn",
    "category": "Human Resource",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["hr", "lunch"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence.xml",
        "views/hr_employee_views.xml",
        "views/lunch_order_views.xml",
        "wizard/hr_employee_lunch_order_views.xml",
        "wizard/hr_employee_lunch_order_report_views.xml",
        # "report/hr_employee_lunch_report.xml",
        "report/hr_employee_lunch_order_report.xml",
    ],
    # only loaded in demonstration mode
    # "demo": [
    #     "demo/demo.xml",
    # ],
}

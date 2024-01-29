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
    "depends": ["hr"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        # "views/views.xml",
        # "views/templates.xml",
        "views/hr_employee_views.xml",
    ],
    # only loaded in demonstration mode
    # "demo": [
    #     "demo/demo.xml",
    # ],
}

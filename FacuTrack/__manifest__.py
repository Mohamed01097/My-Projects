# -*- coding: utf-8 -*-
{
    'name': "FacuTrack",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock','hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/student.xml',
        'views/course.xml',
        'views/res_user_inherit.xml',
        'views/professor.xml',
        'views/department.xml',
        # 'views/js_template.xml',
        'views/portal.xml',
        'report/student_attendance_report.xml',
        # 'report/training_report.xml',
        'report/sale_order_report_inherit.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'routes': {
        'website': [
            '/attendance/login',
        ],
    },
}

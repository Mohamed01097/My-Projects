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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/student.xml',
        'views/course.xml',
        #'views/res_user_inherit.xml',
        'views/professor.xml',
        'views/department.xml',
        'report/student_attendance_report.xml',
        'views/file.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'facu_track/static/src/js/location.js',
        ],
    },
    'routes': {
        'website': [
            '/attendance/login',
        ],
    },
}

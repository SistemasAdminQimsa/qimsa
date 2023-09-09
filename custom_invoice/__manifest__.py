# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Custom Invoice',
    'version': '1.0',
    'category': 'Account',
    'description': """.
==============================================================


""",
    'depends': [
        'account'
    ],

    'data': [
        'report/account_invoice_custom_report_views.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}

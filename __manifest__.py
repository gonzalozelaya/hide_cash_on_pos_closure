# -*- coding: utf-8 -*-
{
    'name': "Hide cash on POS closure",

    'summary': """
        Just hides cash values on POS closure""",

    'description': """
        Just hides cash values on POS closure
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '1.0',
    'depends': ['point_of_sale'],
    'assets': {
        "point_of_sale._assets_pos": [
            "/hide_cash_on_pos_closure/static/src/xml/closing_popup.xml",
        ],
    },

}
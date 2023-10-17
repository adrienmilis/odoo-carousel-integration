# -*- coding: utf-8 -*-
{
    'name': "carousel_snippet",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'views/snippets/options.xml',
        'views/snippets/s_snippet_carousel.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'carousel_snippet/static/src/snippets/s_snippet_carousel/000.js',
            # 'carousel_snippet/static/src/snippets/s_snippet_carousel/000.scss',
            # 'carousel_snippet/static/src/snippets/s_snippet_carousel/000.xml',
            # 'carousel_snippet/static/src/snippets/s_snippet_carousel/option.js',
            # 'carousel_snippet/static/src/snippets/options.scss',
        ],
    }
}

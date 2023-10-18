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
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website'],
    'data': ['views/snippets/s_snippet_carousel.xml'],
    'assets': {
        'web.assets_frontend': [
            'carousel_snippet/static/src/snippets/s_snippet_carousel/000.scss',
            'carousel_snippet/static/src/snippets/s_snippet_carousel/000.js',
            # load assets from the tiny-slider library
            'https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.2/min/tiny-slider.js',
            'https://cdnjs.cloudflare.com/ajax/libs/tiny-slider/2.9.4/tiny-slider.css',
        ],
    }
}

{
    'name': "bibliotecafran",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Este es el nuevo modulo creado por Francisco sobre una biblioteca
    """,

    'author': "Francisco",
    'website': "http://www.bibliotecafrancisco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/ir_sequence.xml',
        'views/bibliotecafran.xml',
        'reports/reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
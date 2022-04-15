{
    'name': "Library",
    'version': '1.0',
    'depends': ['base'],
    'author': "Mr. Author",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_user_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
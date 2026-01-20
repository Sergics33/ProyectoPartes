{
    'name': 'Partes',
    'version': '1.0',
    'summary': 'Gestión de partes del instituto',
    'description': 'Módulo para gestionar los partes del instituto.',
    'category': 'Education',
    'author': 'Sergi y Pablo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml', # Solo dejamos este archivo que ya contiene todo
    ],
    'installable': True,
    'application': True,
}
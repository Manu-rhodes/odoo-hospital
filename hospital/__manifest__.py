{
    'name': 'Hospital Management',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Emmanuel',
    'category': 'All',
    'summary': 'Hospital_Management_System',
    'description': """
        A module which will help to keep a save of the patients records
    """,
    'depends': ['mail'],
    'data': ['security/ir.model.access.csv',
             'data/sequence.xml',
             'views/menu.xml',
             'views/patient.xml',
             'views/doctor.xml'
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
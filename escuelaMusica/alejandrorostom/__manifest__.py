{
    'name': 'Escuela de Musica',
    'version': '1.0',
    'summary': 'Gestión de alumnos',
    'description': """
    Módulo para la Gestión de alumnos para la escuelita de música. 
    """,
    'category': 'Uncategorized',
    'author': 'Juan Poós',    
    'depends': ['base', 'contacts', 'sale', 'website', 'account', 'product'],
    'data': [        
        'views/res_partner_view.xml',  
        'views/product_template_view.xml',
        'security/ir.model.access.csv',
        #'views/account_move_views.xml', 
        #'views/medical_record_views.xml'    

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}
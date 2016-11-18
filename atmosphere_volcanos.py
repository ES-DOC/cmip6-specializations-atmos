
        ('volcanoes_implementation', 'ENUM:volcanoes_implementation_method', '1.1',
         'How volcanic effects are modeled in the atmosphere.'),


ENUMERATIONS['volcanoes_implementation_method'] = {
    'description': 'How volcanic effects are modeled in the atmosphere.',
    'members': [
        ('high frequency solar constant anomaly', None),
        ('stratospheric aerosols optical thickness', None),
        ('other', None),
        ('none', None),
    ]
}

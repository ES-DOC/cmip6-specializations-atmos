DETAILS['top_insolation_solar_constant'] = {
    'properties': [
        ('type', 'ENUM:top_insolation_solar_constant_type', '1.1',
         'Time adaptation of the solar constant.'),
        ('fixed_value', 'float', '0.1',
         'If the solar constant is fixed, enter the value of the solar constant (W m-2).'),
        ('transient_characteristics', 'str', '1.1',
         'solar constant transient characteristics (W m-2)'),
        ('dynamical_core_top_boundary_condition', 'ENUM:dynamical_core_top_boundary_condition', '1.1',
         'Type of boundary layer at the top of the model.'),
    ]
}

DETAILS['top_insolation_orbital_parameters'] = {
    'properties': [
        ('type', 'ENUM:top_insolation_orbital_parameters_type', '1.1',
         'DESCRIPTION'),
        ('fixed_reference_date', 'int', '1.1',
         'fixed orbital parameters reference date (yyyy)'),
        ('solar_constant_transient_characteristics', 'str', '1.1',
         'transient orbital parameters characteristics'),
        ('computation_method', 'ENUM:top_insolation_orbital_parameters_computation_method', '1.1',
         'Method used for computing orbital parameters.')
    ]
}

DETAILS['top_insolation_ozone'] = (
    'bool', '1.1',
    'Impact of top of atmosphere insolation on stratospheric ozone')

ENUMERATIONS['top_insolation_solar_constant_type'] = {
    'description': 'Time adaptation of the solar constant.',
    'members': [
        ('fixed', None),
        ('transient', None),
    ]
}


ENUMERATIONS['top_insolation_orbital_parameters_computation_method'] = {
    'description': 'Method used for computing orbital parameters.',
    'members': [
        ('Berger 1978', None),
        ('Laskar 2004', None),
        ('Other', None),
    ]
}
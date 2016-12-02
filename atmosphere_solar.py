"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

from collections import OrderedDict
DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()


# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# SUB-PROCESS: solar_constant
# --------------------------------------------------------------------
DETAILS['solar_constant'] = {
    'description': 'Solar constant and top of atmosphere insolation characteristics',
    'properties': [
        ('type', 'ENUM:top_insolation_solar_constant_type', '1.1',
             'Time adaptation of the solar constant.'),
        ('fixed_value', 'float', '0.1',
             'If the solar constant is fixed, enter the value of the solar constant (W m-2).'),
        ('transient_characteristics', 'str', '1.1',
             'solar constant transient characteristics (W m-2)'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: orbital_parameters
# --------------------------------------------------------------------
DETAILS['orbital_parameters'] = {
    'description': 'Orbital parameters and top of atmosphere insolation characteristics',
    'properties': [
        ('type', 'ENUM:top_insolation_orbital_parameters_type', '1.1',
            'Time adaptation of orbital parameters'),
        ('fixed_reference_date', 'int', '1.1',
            'Reference date for fixed orbital parameters (yyyy)'),
        ('solar_constant_transient_characteristics', 'str', '1.1',
            'Characteristics of transient orbital parameters'),
        ('computation_method', 'ENUM:top_insolation_orbital_parameters_computation_method', '1.1',
            'Method used for computing orbital parameters.')
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: insolation_ozone
# --------------------------------------------------------------------
DETAILS['insolation_ozone'] = {
    'description': 'Impact of solar insolation on stratospheric ozone',
    'properties': [
        ('solar_ozone_impact', 'bool', '1.1',
            'Does top of atmosphere insolation impact on stratospheric ozone?'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------

ENUMERATIONS['top_insolation_solar_constant_type'] = {
    'description': 'Time adaptation of the solar constant',
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
    ],
}

ENUMERATIONS['top_insolation_orbital_parameters_type'] = {
    'description': 'Time adaptation of orbital parameters',
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
    ],
}

ENUMERATIONS['top_insolation_orbital_parameters_computation_method'] = {
    'description': 'Method used for computing orbital parameters.',
    'is_open': True,
    'members': [
        ('Berger 1978', None),
        ('Laskar 2004', None),
    ],
}


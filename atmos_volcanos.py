
"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

from collections import OrderedDict
DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the implementation of volcanoes'

# --------------------------------------------------------------------
# SUB-PROCESS: volcanoes_treatment
# --------------------------------------------------------------------
DETAILS['volcanoes_treatment'] = {
    'description': 'Treatment of volcanoes in the atmosphere',
    'properties': [
        ('volcanoes_implementation', 'ENUM:volcanoes_implementation_method', '1.1',
            'How volcanic effects are modeled in the atmosphere.'),
    ],
}


#TODO expect atmosphere_volcanoes to have more processes added

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['volcanoes_implementation_method'] = {
    'description': 'Volcanic effects taken into account by the atmosphere model',
    'is_open': True,
    'members': [
        ('high frequency solar constant anomaly', None),
        ('stratospheric aerosols optical thickness', None),
    ],
}

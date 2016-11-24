"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

from collections import OrderedDict

DETAILS = OrderedDict()
PROCESS = OrderedDict()
SUB_PROCESSES = OrderedDict()
ENUMERATIONS = OrderedDict()
DISCRETISATION = OrderedDict()

# Default process details pulled from CIM.
DETAILS['CIM'] = {
    'description': 'General characteristics of the atmosphere grid',
    'properties':[
        ('implementation_overview', 'str', '1.1',
            "General overview description of the implementation of this part of the process."),
        ('keywords', 'str', '0.N',
            "Keywords to help re-use and discovery of this information."),
        ('citations', 'shared.citation', '0.N',
            "Set of pertinent citations."),
    ]
}
# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.grid', e.g. 'cmip6.atmosphere.grid'
# --------------------------------------------------------------------
# ID = 'cmip6.atmosphere.grid'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
# _TYPE = 'cim.2.science.grid'


# ====================================================================
# GRID: DESCRIPTION
# ====================================================================
# DESCRIPTION = ''

# ====================================================================
# GRID: DISCRETISATION
# ====================================================================

DISCRETISATION['grid_discretisation'] = {
    'description': 'horizontal discretisation of the atmosphere grid',
    'properties': [
        ('scheme_type', 'ENUM:dynamical_core_discretisation_horizontal_type', '1.1',
         'Horizontal discretisation type'),
        ('scheme_method', 'ENUM:dynamical_core_discretisation_horizontal_method', '1.1',
         'Horizontal discretisation method'),
        ('scheme_order', 'int', '1.1',
         'Horizontal discretisation function order'),
        ('horizontal_pole', 'ENUM:dynamical_core_discretisation_horizontal_pole', '1.1',
         'Horizontal discretisation pole singularity treatment'),
    ],
}

# ====================================================================
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================

ENUMERATIONS['dynamical_core_discretisation_horizontal_type'] = {
    'description': 'Type of horizontal discretisation scheme',
    'is_open': True,
    'members': [
        ('spectral', None),
        ('fixed grid', None),
    ]
}

ENUMERATIONS['dynamical_core_discretisation_horizontal_method'] = {
    'description': 'If the scheme type is fixed grid, '
                   'describe the scheme method for the horizontal discretisation scheme',
    'is_open': True,
    'members': [
        ('finite elements', None),
        ('finite volumes', None),
        ('finite difference', None),
        ('centered finite difference', None),
    ]
}

ENUMERATIONS['dynamical_core_discretisation_horizontal_pole'] = {
    'description': 'Method used to handle the pole singularities',
    'is_open': True,
    'members': [
        ('filter', None),
        ('pole rotation', None),
        ('artificial island', None),
        ('none', None),
    ]
}

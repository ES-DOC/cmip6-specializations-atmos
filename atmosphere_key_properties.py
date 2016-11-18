"""
A realm key-properties sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------

from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# Default process details pulled from CIM.
DETAILS['CIM'] = {
    'description': 'Key properties of the atmosphere',
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
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Think this feature is obsolete now CP 18-11-16
#
# Set to 'cmip6.<REALM>.key_properties'
# --------------------------------------------------------------------
# ID = 'cmip6.atmosphere.key_properties'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
#
# Think this feature is obsolete now CP 18-11-16
# --------------------------------------------------------------------
#_TYPE = 'cim.2.science.key_properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: DETAILS
#
# Sets of details for the key properties
# --------------------------------------------------------------------


DETAILS['general'] = {
    'description': 'General key properties in atmosphere',
    'properties': [
        ('model_family', 'ENUM:model_family_type', '1.1',
         'Type of atmospheric model.'),
        ('basic_approximations', 'ENUM:basic_approximations_attributes', '1.N',
         'Basic approximations made in the atmosphere.',),
    ]
}    

    
DETAILS['orography'] = {
    'properties': [
        ('type', 'ENUM:orography_type', '1.1',
         'Time adaptation of the orography.',),
        ('changes', 'ENUM:orography_changes', '1.N',
         'If the orography type is modified describe the time adaptation changes.'),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTENT
# --------------------------------------------------------------------
DETAILS['extent'] = {
    'description': 'Extent of the atmosphere domain',
    'properties': [
        ('type', 'ENUM:extent_type', '1.1',
         'Horizontal extent of the atmosphere domain'),
    ]
}


# --------------------------------------------------------------------
# KEY PROPERTIES: RESOLUTION
#
# The resolution of the grid
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': 'Resolution of the atmosphere grid',
    'properties': [
        ('name', 'str', '1.1',
             "This is a string usually used by the modelling group to describe the resolution of this grid."),
        ('canonical_horizontal_resolution', 'str', '0.1',
             "Expression quoted for gross comparisons of resolution, eg. 50km or 2.5 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '0.1',
             "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('number_of_vertical_levels', 'int', '0.1',
             "Number of vertical levels resolved on computational grid."),
        ('is_adaptive_grid', 'bool', '0.1',
             "Default is False. Set true if grid resolution changes during execution."),
    ],
}


# --------------------------------------------------------------------
# KEY PROPERTIES: TUNING APPLIED
#
# Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for atmosphere component',
    'properties': [
        ('description', 'str', '1.1',
             "General overview description of tuning: explain and motivate the main targets and metrics retained. &"
             "Document the relative weight given to climate performance metrics versus process oriented metrics, &"
             "and on the possible conflicts with parameterization level tuning. In particular describe any struggle &"
             "with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('global_mean_metrics_used', 'str', '0.N',
             "List set of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'str', '0.N',
             "List of regional metrics of mean state used in tuning model/component"),
        ('trend_metrics_used', 'str', '0.N',
             "List observed trend metrics used in tuning model/component"),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTRA CONSERVATION PROPERTIES
#
# Details of methodology needed to conserve variables between
# processes
#  --------------------------------------------------------------------
DETAILS['conservation'] = {
    'description': 'Conservation in the atmosphere component',
    'properties': [
        ('description', 'str', '1.1', 'Brief description of conservation methodology'),
        ('scheme', 'ENUM:conservation_props_types', '1.N',
            'Properties conserved in the atmosphere by the numerical schemes'),
        ('consistency_properties', 'str','0.1',
            'Any additional consistency properties (energy conversion, pressure gradient discretisation, ...)?'),
        ('corrected_conserved_prognostic_variables', 'data.variable_collection', '0.1', # Can we constrains these variable
             "Set of variables which are conserved by *more* than the numerical scheme alone."),
    ],
}


# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------


ENUMERATIONS['model_family_type'] = {
    'description': 'Type of atmospheric model.',
    'is_open': True,
    'members': [
        ('AGCM', 'Atmospheric General Circulation Model'),
        ('ARCM', 'Atmospheric Regional Climate Model'),
    ]
}
    
ENUMERATIONS['basic_approximations_attributes'] = {
    'description': 'Basic approximations made in the atmosphere.',
    'is_open': True,
    'members': [
        ('primitive equations', None),
        ('non-hydrostatic', None),
        ('anelastic', None),
        ('Boussinesq', None),
        ('hydrostatic', None),
        ('quasi-hydrostatic', None),
    ],
}

ENUMERATIONS['orography_type'] = {
    'description': 'Time adaptation of the orography.',
    'is_open': False,
    'members': [
        ('present-day', None),
        ('modified', None),
    ]
}

ENUMERATIONS['orography_changes'] = {
    'description': 'If the orography type is modified describe the time adaptation changes.',
    'is_open': True,
    'members': [
        ('related to ice sheets', None),
        ('related to tectonics', None),
        ('modified mean', None),
        ('modified variance if taken into account in model (cf gravity waves)', None),
    ]
}

ENUMERATIONS['extent_type'] = {
    'description': 'Horizontal extent of the atmosphere domain.',
    'is_open': False,
    'members': [
        ('global', None),
        ('limited area', None),
    ]
}

ENUMERATIONS['conservation_props_types'] = {
    'description': 'List of properties that can be conserved in the atmosphere.',
    'is_open': True,
    'members': [
        ('energy', None),
        ('momentum', None),
    ]
}
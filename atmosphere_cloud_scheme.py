"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
from collections import OrderedDict
DETAILS = OrderedDict()
PROCESS = OrderedDict()
SUB_PROCESSES = OrderedDict()
ENUMERATIONS = OrderedDict()

# Default process details pulled from CIM.
DETAILS['CIM'] = {
    'description': 'Cloud scheme characteristics',
    'properties': [
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
AUTHORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
# ID = 'cmip6.atmosphere.cloud_scheme'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
# _TYPE = 'cim.2.science.process'

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
# DESCRIPTION = 'Characteristics of the cloud scheme'


# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------


DETAILS['attributes'] = {
    'description': 'Cloud scheme properties',
    'properties': [
        ('uses_separate_treatment', 'bool', '1.1',
         'Different cloud schemes for the different types of clouds (convective, stratiform and boundary layer clouds'),
        ('cloud_overlap_method', 'ENUM:cloud_overlap_method', '1.1',
         'Method for taking into account overlapping of cloud layers'),
        ('processes', 'ENUM:processes_attributes', '1.N', 
         'Processes included in the cloud scheme'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------

SUB_PROCESSES['sub_grid_scale_water_distribution'] = {
    'description': 'Sub-grid scale water distribution',
    'properties': [
        ('type', 'ENUM:sub_grid_scale_water_distribution_type', '1.1',
         'Sub-grid scale water distribution type'),
        ('function_name', 'str', '1.1',
         'Sub-grid scale water distribution function name'),
        ('function_order', 'int', '1.1',
         'Sub-grid scale water distribution function order'),
        ('convection_coupling', 'ENUM:sub_grid_scale_water_distribution_convection', '1.N',
         'Sub-grid scale water distribution coupling with convection'),
    ]
}


# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------

ENUMERATIONS['cloud_overlap_method'] = {
    'description': 'Cloud scheme cloud overlap method',
    'is_open': True,
    'members': [
        ('random', None),
        ('none', None),
    ]
}

ENUMERATIONS['processes_attributes'] = {
    'short_name': 'Cloud scheme processes attributes',
    'description': 'Processes included in the cloud scheme.',
    'is_open': True,
    'members': [
        ('entrainment', None),
        ('detrainment', None),
        ('bulk cloud', None),
    ]
}

ENUMERATIONS['sub_grid_scale_water_distribution_type'] = {
    'description': 'Approach used for cloud water content and fractional cloud cover',
    'is_open': False,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['sub_grid_scale_water_distribution_convection'] = {
    'description': 'Type(s) of convection that the formation of clouds is coupled with',
    'is_open': False,
    'members': [
        ('coupled with deep', None),
        ('coupled with shallow', None),
        ('not coupled with convection', None),
    ]
}


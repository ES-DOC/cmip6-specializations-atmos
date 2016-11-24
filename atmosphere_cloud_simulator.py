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
    'description': 'Characteristics of the cloud simulator',
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
# ID = 'cmip6.atmosphere.cloud_simulator'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
# _TYPE = 'cim.2.science.process'

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
# DESCRIPTION = 'Characteristics of the cloud simulator'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------


DETAILS['isscp_attributes'] = {
    'description': 'ISSCP Cloud top height characteristics',
    'properties': [
        ('top_height', 'ENUM:isscp_top_height', '1.N',
         'Cloud simulator ISSCP top height'),
        ('top_height_direction', 'ENUM:isscp_top_height_direction', '1.1',
         'Cloud simulator ISSCP top height direction'),
    ],
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------

SUB_PROCESSES['cosp_attributes'] = {
    'description': 'CFMIP Observational Simulator Package attributes',
    'properties': [
        ('run_configuration', 'ENUM:cosp_run_configuration', '1.1',
         'Cloud simulator COSP run configuration'),
        ('number_of_grid_points', 'int', '1.1',
         'Cloud simulator COSP number of grid points'),
        ('number_of_columns', 'int', '1.1',
         'Cloud simulator COSP number of cloumns'),
            ('number_of_levels', 'int', '1.1',
             'Cloud simulator COSP number of levels'),
    ],
}
    
SUB_PROCESSES['inputs_radar'] = {
    'description': 'Characteristics of the cloud radar simulator',
    'properties': [
        ('radar_frequency', 'float', '1.1',
         'Cloud simulator radar frequency'),
        ('radar_type', 'ENUM:inputs_radar_type', '1.1',
         'Cloud simulator radar type'),
        ('gas_absorption', 'bool', '1.1',
         'Cloud simulator radar uses gas absorption'),
        ('effective_radius', 'bool', '1.1',
         'Cloud simulator radar uses effective radius'),
    ],
}
    
SUB_PROCESSES['inputs_lidar'] = {
    'description': 'Characteristics of the cloud lidar simulator',
    'properties': [
        ('ice_type', 'ENUM:inputs_lidar_ice_type', '1.1',
         'Cloud simulator lidar ice type'),
        ('lidar_overlap', 'ENUM:inputs_lidar_overlap', '1.N',
         'Cloud simulator lidar overlap'),
    ],
}


# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------

ENUMERATIONS['isscp_top_height'] = {
    'description': 'Cloud top height management',
    'is_open': False,
    'members': [
        ('no adjustment', None),
        ('IR brightness', None),
        ('visible optical depth', None),
    ]
}

ENUMERATIONS['isscp_top_height_direction'] = {
    'description': 'Direction for finding the radiance determined cloud-top pressure. '
                   'Atmosphere pressure level with interpolated temperature equal to '
                   'the radiance determined cloud-top pressure.',
    'is_open': False,
    'members': [
        ('lowest altitude level', None),
        ('highest altitude level', None),
    ]
}

ENUMERATIONS['cosp_run_configuration'] = {
    'description': 'Method used to run the CFMIP Observational Simulator Package',
    'is_open': False,
    'members': [
        ('Inline', None),
        ('Offline', None),
        ('None', None),
    ]
}

ENUMERATIONS['inputs_radar_type'] = {
    'description': 'Type of radar',
    'is_open': False,
    'members': [
        ('surface', None),
        ('space borne', None),
    ]
}

ENUMERATIONS['inputs_lidar_ice_type'] = {
    'description': 'Ice particle shape in lidar calculations',
    'is_open': False,
    'members': [
        ('ice spheres', None),
        ('ice non-spherical', None),
    ]
}

ENUMERATIONS['inputs_lidar_overlap'] = {
    'description': 'lidar overlap type',
    'is_open': True,
    'members': [
        ('max', None),
        ('random', None),
    ]
}

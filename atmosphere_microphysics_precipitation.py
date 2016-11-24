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
    'description': 'Cloud microphysics and precipitation characteristics',
    'properties':[
        ('implementation_overview','str', '1.1',
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
# ID = 'cmip6.atmosphere.microphysics_precipitation'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
# _TYPE = 'cim.2.science.process'

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
# DESCRIPTION = 'Cloud microphysics and precipitation characteristics'

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------

SUB_PROCESSES['large_scale_precipitation'] = {
    'description': 'Properties of the large scale precipitation scheme',
    'properties': [
        ('scheme_name', 'str', '1.1',
         'Commonly used name of the large scale precipitation parameterisation scheme'),
        ('hydrometeors', 'ENUM:hydrometeor_types', '1.N',
         'Precipitating hydrometeors taken into account in the large scale precipitation scheme'),
    ]
}

SUB_PROCESSES['cloud_microphysics'] = {
    'description': 'Properties of the cloud microphysics scheme',
    'properties': [
        ('scheme_name', 'str', '1.1',
         'Commonly used name of the microphysics parameterisation scheme.'),
        ('processes', 'ENUM:processes_attributes', '1.N',
         'Cloud microphysics processes'),
    ]
}


# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------

ENUMERATIONS['hydrometeor_types'] = {
    'description': 'Precipitating hydrometeors taken into account in the large scale precipitation scheme',
    'is_open': True,
    'members': [
        ('liquid rain', None),
        ('snow', None),
        ('hail', None),
        ('graupel', None),
    ]
}

ENUMERATIONS['processes_attributes'] = {
    'description': 'Cloud microphysics processes',
    'is_open': True,
    'members': [
        ('mixed phase', None),
        ('cloud droplets', None),
        ('cloud ice', None),
        ('ice nucleation', None),
        ('water vapour deposition', None),
        ('effect of raindrops', None),
        ('effect of snow', None),
        ('effect of graupel', None),
    ]
}


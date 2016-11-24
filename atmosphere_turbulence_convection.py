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
    'description': 'Convective turbulence and cloud characteristics',
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
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
# ID = 'cmip6.atmosphere.turbulance_convection'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
# _TYPE = 'cim.2.science.process'


# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
# DESCRIPTION = 'Atmosphere convective turbulence and clouds'

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


# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================


SUB_PROCESSES['boundary_layer_turbulence'] = {
    'description': 'Properties of the boundary layer turbulence scheme',
    'properties': [
        ('scheme_name', 'ENUM:boundary_layer_turbulence_scheme_name', '1.1',
         'Boundary layer turbulence scheme name'),
        ('scheme_type', 'ENUM:boundary_layer_turbulence_scheme_type', '1.1',
         'Boundary layer turbulence scheme type'),
        ('closure_order', 'int', '1.1',
         'Boundary layer turbulence scheme closure order'),
        ('counter_gradient', 'bool', '1.1',
         'Uses boundary layer turbulence scheme counter gradient'),
    ]
}

SUB_PROCESSES['deep_convection'] = {
    'description': 'Properties of the deep convection scheme',
    'properties': [
        ('scheme_name', 'str', '1.1',
         'Deep convection scheme name'),
        ('scheme_type', 'ENUM:deep_convection_scheme_type', '1.1',
         'Deep convection scheme type'),
        ('scheme_method', 'ENUM:deep_convection_scheme_method', '1.N',
         'Deep convection scheme method'),
        ('processes', 'ENUM:deep_convection_scheme_processes_attributes', '1.N',
         'Deep convection scheme processes'),
    ]
}
        
SUB_PROCESSES['shallow_convection'] = {
    'description': 'Properties of th shallow convection scheme',
    'properties': [
        ('selection', 'ENUM:shallow_convection_scheme_method', '1.1',
         'shallow convection scheme method'),
        ('scheme_type', 'ENUM:shallow_convection_scheme_type', '1.1',
         'shallow convection scheme type'),
        ('scheme_name', 'str', '1.1',
         'Shallow convection scheme name'),
        ('processes', 'ENUM:shallow_convection_scheme_processes_attributes', '1.N',
         'Physical processes taken into account in the parameterisation of shallow convection'),
    ]
}


# ====================================================================
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================

ENUMERATIONS['boundary_layer_turbulence_scheme_name'] = {
    'description': 'Commonly used name for the boundary layer turbulence scheme.',
    'is_open': True,
    'members': [
        ('Mellor-Yamada', None),
    ]
}

ENUMERATIONS['boundary_layer_turbulence_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of turbulence in the boundary layer.',
    'is_open': True,
    'members': [
        ('TKE prognostic', None),
        ('TKE diagnostic', None),
        ('TKE coupled with water', None),
        ('vertical profile of Kz', None),
    ]
}

ENUMERATIONS['deep_convection_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of deep convection.',
    'is_open': True,
    'members': [
        ('mass-flux', None),
        ('adjustment', None),
    ]
}

ENUMERATIONS['deep_convection_scheme_method'] = {
    'description': 'If deep convection uses a mass-flux scheme enter the method used.',
    'is_open': True,
    'members': [
        ('CAPE', 'Mass flux determined by CAPE'),
        ('bulk', 'A bulk mass flux scheme is used'),
    ]
}

ENUMERATIONS['shallow_convection_scheme_method'] = {
    'description': 'Method used for shallow convection.',
    'is_open': True,
    'members': [
        ('same as deep (unified)', None),
        ('included in boundary layer turbulence', None),
        ('separated', None),
    ]
}

ENUMERATIONS['shallow_convection_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of shallow convection.',
    'is_open': True,
    'members': [
        ('mass-flux', None),
    ]
}

ENUMERATIONS['deep_convection_scheme_processes_attributes'] = {
    'description': 'deep_convection_scheme_processes_attributes',
    'is_open': True,
    'members': [
        ('vertical momentum transport', None),
        ('convective momentum transport', None),
        ('entrainment', None),
        ('detrainment', None),
        ('penetrative convection', None),
        ('updrafts and downdrafts', None),
        ('radiative effect of anvils', None),
    ]
}

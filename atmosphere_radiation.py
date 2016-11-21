"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
# This feature is not used in the ocean specialisation,
# assume is obsolete.
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
# ID = 'cmip6.atmosphere.radiation'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
#_TYPE = 'cim.2.science.process'

from collections import OrderedDict

DETAILS = OrderedDict()
PROCESS = OrderedDict()
SUB_PROCESSES = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
# DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# Default process details pulled from CIM.
DETAILS['CIM'] = {
    'description': 'Characteristics of the atmosphere radiation process',
    'properties':[
        ('implementation_overview','str', '1.1',
            "General overview description of the implementation of this part of the process."),
        ('keywords','str', '0.N',
            "Keywords to help re-use and discovery of this information."),
        ('citations','shared.citation', '0.N',
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
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------

DETAILS['radiation modulators'] = {
    'description': 'Atmospheric constituents that interact with the radiation scheme',
    'properties': [
        ('aerosols', 'ENUM:aerosol_types', '1.N',
         'Aerosols whose radiative effect is taken into account in the atmosphere model'),
        ('greenhouse_gases', 'ENUM:ghg_types', '1.N',
         'Greenhouse gases whose radiative effect is taken into account in the atmosphere model'),
        ('cloud_ice', 'str', '0.N',
         'Radiative properties of ice crystals in clouds'),
        ('cloud_liquid', 'str', '0.N',
         'Radiative properties of liquid droplets in clouds'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------

SUB_PROCESSES['longwave_radiation'] = {
    'description': 'Properties of the longwave radiation scheme',
    'properties': [
        ('scheme_type', 'ENUM:longwave_scheme_type', '1.1',
         'Longwave radiation scheme type'),
        ('scheme_method', 'ENUM:longwave_scheme_method', '1.1',
         'Longwave radiation scheme method'),
        ('spectral_intervals', 'int', '1.1',
         'Longwave radiation scheme spectral intervals'),
    ]
}

SUB_PROCESSES['shortwave_radiation'] = {
    'description': 'Properties of the shortwave radiation scheme',
    'properties': [
        ('scheme_type', 'ENUM:shortwave_scheme_type', '1.1',
         'Shortwave radiation scheme type'),
        ('spectral_intervals', 'int', '1.1',
         'Shortwave radiation scheme spectral intervals'),
    ]
}


# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------


ENUMERATIONS['aerosol_types'] = {
    'description': 'Aerosols whose radiative effect is taken into account in the atmosphere model.',
    'is_open': True,
    'members': [
        ('sulphate', None),
        ('nitrate', None),
        ('sea salt', None),
        ('dust', None),
        ('ice', None),
        ('organic', None),
        ('BC (black carbon / soot)', None),
        ('SOA (secondary organic aerosols)', None),
        ('POM (particulate organic matter)', None),
        ('polar stratospheric ice', None),
        ('NAT (nitric acid trihydrate)', None),
        ('NAD (nitric acid dihydrate)', None),
        ('STS (supercooled ternary solution aerosol particle)', None),
    ]
}

ENUMERATIONS['ghg_types'] = {
    'description': 'Greenhouse gases whose radiative effect is taken into account in the atmosphere model',
    'is_open': True,
    'members': [
        ('CO2', None),
        ('CH4', None),
        ('N2O', None),
        ('H2O', None),
        ('O3', None),
        ('CFCs', None),
        ('HFCs', None),
        ('PFCs', None),
        ('SF6', None),
        ('NF3', None),
    ]
}

ENUMERATIONS['longwave_scheme_type'] = {
    'description': 'Type of scheme used for longwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('wide-band model (Morcrette)', None),
        ('K-correlated', None),
        ('K-correlated (RRTM)', None),
    ]
}
             
ENUMERATIONS['longwave_scheme_method'] = {
    'description': 'Method for the radiative transfer calculations used in the longwave scheme',
    'is_open': True,
    'members': [
        ('two-stream', None),
        ('layer interaction', None),
    ]
}

ENUMERATIONS['shortwave_scheme_type'] = {
    'description': 'Type of scheme used for shortwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('wide-band model (Fouquart)', None),
    ]
}

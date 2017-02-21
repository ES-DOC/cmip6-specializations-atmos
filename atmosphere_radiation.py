"""

A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Radiative agents in the atmosphere",
    'properties': [
        ('aerosols', 'ENUM:aerosol_types', '1.N',
            'Aerosols whose radiative effect is taken into account in the atmosphere model'),
        ('greenhouse_gases', 'ENUM:ghg_types', '1.N',
            'Greenhouse gases whose radiative effect is taken into account in the atmosphere model'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_radiation
# --------------------------------------------------------------------
DETAILS['shortwave_radiation'] = {
    'description': 'Properties of the shortwave radiation scheme',
    'properties': [
        ('sw_spectral_integration', 'ENUM:spectral_integration', '1.1',
            'Shortwave radiation scheme spectral integration'),
        ('sw_transport_method', 'ENUM:transport_methods', '1.N',
            'Shortwave radiation scheme transport method'),
        ('sw_spectral_intervals', 'int', '1.1',
            'Shortwave radiation scheme number of spectral intervals'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: sw_cloud_ice
# --------------------------------------------------------------------
DETAILS['cloud_ice'] = {
    'description': 'Radiative properties of ice crystals in clouds',
    'properties': [
        ('ice_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk short wave radiative properties of cloud ice crystals'),
        ('ice_physical', 'ENUM:cloud_ice_physical_properties', '1.N',
            'Physical representation of cloud ice crystals in the short wave radiation scheme'),
        ('ice_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud ice crystals in the short wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sw_cloud_liquid
# --------------------------------------------------------------------
DETAILS['cloud_liquid'] = {
    'description': 'Radiative properties of liquid droplets in clouds',
    'properties': [
        ('liq_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk short wave radiative properties of cloud liquid droplets'),
        ('liq_physical', 'ENUM:cloud_liquid_physical_properties', '1.N',
            'Physical representation of cloud liquid droplets in the short wave radiation scheme'),
        ('liq_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud liquid droplets in the short wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sw_aerosols
# --------------------------------------------------------------------
DETAILS['aerosols'] = {
    'description': 'Radiative properties of aerosols',
    'properties': [
        ('aer_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk short wave radiative properties of aerosols'),
        ('aer_physical', 'ENUM:aerosol_physical_properties', '1.N',
            'Physical representation of aerosols in the short wave radiation scheme'),
        ('aer_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to aerosols in the short wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sw_gases
# --------------------------------------------------------------------
DETAILS['gases'] = {
    'description': 'Radiative properties of gases',
    'properties': [
        ('gas_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk short wave radiative properties of gases'),
        ('gas_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to gases in the short wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_radiation
# --------------------------------------------------------------------
DETAILS['longwave_radiation'] = {
    'description': 'Properties of the longwave radiation scheme',
    'properties': [
        ('lw_spectral_integration', 'ENUM:spectral_integration', '1.1',
            'Longwave radiation scheme spectral integration'),
        ('lw_transport_method', 'ENUM:transport_methods', '1.N',
            'Longwave radiation scheme transport method'),
        ('lw_spectral_intervals', 'int', '1.1',
            'Longwave radiation scheme number of spectral intervals'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: lw_cloud_ice
# --------------------------------------------------------------------
DETAILS['lw_cloud_ice'] = {
    'description': 'Long wave radiative properties of ice crystals in clouds',
    'properties': [
        ('ice_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk long wave radiative properties of cloud ice crystals'),
        ('ice_physical', 'ENUM:cloud_ice_physical_properties', '1.N',
            'Physical representation of cloud ice crystals in the long wave radiation scheme'),
        ('ice_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud ice crystals in the long wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: lw_cloud_liquid
# --------------------------------------------------------------------
DETAILS['lw_cloud_liquid'] = {
    'description': 'Long wave radiative properties of liquid droplets in clouds',
    'properties': [
        ('liq_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk long wave radiative properties of cloud liquid droplets'),
        ('liq_physical', 'ENUM:cloud_liquid_physical_properties', '1.N',
            'Physical representation of cloud liquid droplets in the long wave radiation scheme'),
        ('liq_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud liquid droplets in the long wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: lw_aerosols
# --------------------------------------------------------------------
DETAILS['lw_aerosols'] = {
    'description': 'Long wave radiative properties of aerosols',
    'properties': [
        ('aer_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk long wave radiative properties of aerosols'),
        ('aer_physical', 'ENUM:aerosol_physical_properties', '1.N',
            'Physical representation of aerosols in the long wave radiation scheme'),
        ('aer_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to aerosols in the long wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: lw_gases
# --------------------------------------------------------------------
DETAILS['gases'] = {
    'description': 'Long wave radiative properties of gases',
    'properties': [
        ('gas_bulk', 'ENUM:bulk_radiative_properties', '1.N',
            'Bulk long wave radiative properties of gases'),
        ('gas_optical', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to gases in the long wave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['aerosol_types'] = {
    'description': 'Aerosols whose radiative effect is taken into account in the atmospheric model.',
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
    'description': 'Greenhouse gases whose radiative effect is taken into account in the atmospheric model',
    'is_open': True,
    'members': [
        ('H2O', None),
        ('CO2', None),
        ('CH4', None),
        ('N2O', None),
        ('O3', None),
        ('CFCs', None),
        ('HFCs', None),
        ('PFCs', None),
        ('SF6', None),
        ('NF3', None),
        ]
    }

ENUMERATIONS['spectral_integration'] = {
    'description': 'Spectral integration of the radiation scheme',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('correlated-k', None),
        ('exponential sum fitting', None),
        ]
    }

ENUMERATIONS['transport_methods'] = {
    'description': 'Radiation transport methods',
    'is_open': True,
    'members': [
        ('two-stream', None),
        ('layer interaction', None),
        ('bulk', 'highly parameterised methods that use bulk expressions'),
        ('adaptive', 'exploits spatial and temporal correlations in optical characteristics')
        ]
    }

ENUMERATIONS['bulk_radiative_properties'] = {
    'description': 'Bulk radiative properties',
    'is_open': True,
    'members': [
        ('scattering', None),
        ('reflectivity', None),
        ('absorption', None),
        ('emissivity', None),
        ('transmissivity', None),
    ]
}

ENUMERATIONS['cloud_ice_physical_properties'] = {
    'description': 'Physical properties of ice crystals in clouds',
    'is_open': True,
    'members': [
        ('bi-modal size distribution',
            'small mode diameters: a few tens of microns, large mode diameters: typically hundreds of microns'),
        ('ensemble of ice crystals', 'complex shapes represented with an ensemble of symmetric shapes'),
        ('mean projected area',
            'randomly oriented irregular ice crystals present a greater mean projected area than spheres'),
        ('ice water path', 'Integrated ice water path through the cloud kg m-2',),
        ('crystal asymmetry', None),
        ('crystal aspect ratio', None),
        ('effective crystal radius', None),
        ]
    }

ENUMERATIONS['cloud_liquid_physical_properties'] = {
    'description': 'Physical_radiative properties of liquid droplets in clouds',
    'is_open': True,
    'members': [
        ('cloud droplet number concentration', 'CDNC'),
        ('effective cloud droplet radii', None),
        ('droplet size distribution', None),
        ('liquid water path', 'Integrated liquid water path through the cloud kg m-2',),
        ]
    }

ENUMERATIONS['aerosol_physical_properties'] = {
    'description': 'Physical radiative properties of aerosols',
    'is_open': True,
    'members': [
        ('number concentration', None),
        ('effective radii', None),
        ('size distribution', None),
        ('asymmetry', None),
        ('aspect ratio', None),
        ]
    }

ENUMERATIONS['optical_methods'] = {
    'description': 'Optical methods used by radiation scheme',
    'is_open': True,
    'members': [
        ('T-matrix', 'For non-spherical particles'),
        ('geometric optics', 'For non-spherical particles'),
        ('finite difference time domain (FDTD)', 'For non-spherical particles'),
        ('Mie theory', 'For spherical particles'),
        ('anomalous diffraction approximation', None),
        ]
    }

ENUMERATIONS['cloud_ice_radiation_processes'] = {
    'description': 'Optical radiative processes for ice crystals in clouds',
    'is_open': True,
    'members': [
        ('emissivity', None),
        ('absorption', None),
        ('backward scattering', None),
        ('side scattering', None),
        ]
    }

ENUMERATIONS['cloud_liquid_radiation_processes'] = {
    'description': 'Optical radiative processes for liquid droplets in clouds',
    'is_open': True,
    'members': [
        ('droplet scattering', None),
        ('droplet absorption', None),
        ('broadband reflectivity', 'albedo'),
        ('broadband transmissivity', None),
        ('broadband absorbtivity', None),
        ]
    }

ENUMERATIONS['shortwave_scheme_type'] = {
    'description': 'Type of scheme used for shortwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('bulk-scheme', 'highly parameterised methods that use bulk expressions'),
        ('two-stream', None),
        ('two-stream (delta-Eddington)', 'approximation for solar radiation calculations'),
        ]
    }

ENUMERATIONS['single_scattering_properties_methods'] = {
    'description': 'Methods for calculating single scattering properties of atmospheric constituents',
    'is_open': True,
    'members': [
        ('T-Matrix', 'an exact method'),
        ('geometrical optics', 'for particles that are much larger than the wavelength of light'),
        ('finite difference time domain', 'FDTD'),
        ('anomalous diffraction approximation', 'ADA'),
        ('k-distribution', None),
        ('band model', None),
        ('exponential sum fitting', None),
    ]
}




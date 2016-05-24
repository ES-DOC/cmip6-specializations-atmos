# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.scientific_realm'

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization authors.
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# REALM IDENTIFIER
#
# Set to 'cmip6.<REALM>'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere'

# --------------------------------------------------------------------
# REALM: REALM
#
# Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'atmosphere'

# --------------------------------------------------------------------
# REALM: GRID
#
# The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'atmosphere_grid'

# --------------------------------------------------------------------
# REALM: KEY PROPERTIES
#
# Key properties for the domain which differ from model defaults
# (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'atmosphere_key_properties'

# --------------------------------------------------------------------
# REALM: PROCESSES
#
# Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
	'atmosphere_cloud_scheme',
    'atmosphere_cloud_simulator',
    'atmosphere_dynamical_core',
    'atmosphere_gravity_waves',
    'atmosphere_microphysics_precipitation',
    'atmosphere_radiation',
    'atmosphere_turbulence_convection'
    ]

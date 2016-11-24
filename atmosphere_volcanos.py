
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
    'description': 'Characteristics of the treatment of volcanoes in the atmosphere',
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
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------

DETAILS['volcanoes_treatment'] = {
    'description': 'Treatment of volcanoes in the atmosphere',
    'properties': [
        ('volcanoes_implementation', 'ENUM:volcanoes_implementation_method', '1.1',
         'How volcanic effects are modeled in the atmosphere.'),
    ],
}


ENUMERATIONS['volcanoes_implementation_method'] = {
    'description': 'How volcanic effects are modeled in the atmosphere.',
    'is_open': True,
    'members': [
        ('high frequency solar constant anomaly', None),
        ('stratospheric aerosols optical thickness', None),
    ],
}

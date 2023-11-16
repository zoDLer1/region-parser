from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Cm, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH

REGION_IMAGES_SELL_CONFIG = {
    'style': parse_xml(r'<w:shd {} w:fill="FDEADA"/>'.format(nsdecls('w'))),
}

REGION_INFO_SELLS_CONFIG = [
    [
        {
            "alignment": WD_ALIGN_PARAGRAPH.CENTER,
            "info": lambda region: f"{region.status.capitalize()} {region.name}"
        },
        {
            "alignment": WD_ALIGN_PARAGRAPH.CENTER,
            "info": lambda region: ""
        }
    ],
    [
        {
            "alignment": WD_ALIGN_PARAGRAPH.RIGHT,
            "info": lambda region: 'Региональный центр'
        },
        {
            "alignment": WD_ALIGN_PARAGRAPH.LEFT,
            "info": lambda region: region.center
        }
    ],
    [
        {
            "alignment": WD_ALIGN_PARAGRAPH.RIGHT,
            "info": lambda region: 'Площадь'
        },
        {
            "alignment": WD_ALIGN_PARAGRAPH.LEFT,
            "info": lambda region: region.square
        }
    ],
    [
        {
            "alignment": WD_ALIGN_PARAGRAPH.RIGHT,
            "info": lambda region: 'Насиление'
        },
        {
            "alignment": WD_ALIGN_PARAGRAPH.LEFT,
            "info": lambda region: region.population
        }
    ],
]

REGION_IMAGES_SELLS_CONFIG = [
    {'alignment': WD_ALIGN_PARAGRAPH.CENTER, 'image_width': Inches(1.45*2), 'image_height': Inches(1.8), 'image_path': 'temp/flag.png'},
    {'alignment': WD_ALIGN_PARAGRAPH.CENTER, 'image_width': Inches(1.6), 'image_height': Inches(1.6), 'image_path': 'temp/emblem.png'}
]

REGION_IMAGES_ROW_CONFIG = [
    {'height': Cm(5.8)}
]

SECTION_CONFIG = {
    'margin': {
        'left': Mm(10),
        'right': Mm(10),
        'top': Mm(2),
        'bottom': Mm(2),
    }
}

OUTPUT_REGIONS_FLAGS_FILENAME = 'flags.docx'

OUTPUT_REGIONS_INFO_FILENAME = 'info.docx'

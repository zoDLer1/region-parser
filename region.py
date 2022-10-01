from docx import Document
from docx.shared import Inches, Cm, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from dataclasses import dataclass



@dataclass
class Region:
    name: str
    status: str
    center: str
    square: int
    population: int
    region_url: str


class Docx_Regions:
    def __init__(self) -> None:
        self.document = Document()
  
        
        ### DOCUMENT CONFIG ###
        section = self.document.sections[0]
        section.left_margin = Mm(10)
        section.right_margin = Mm(10)
        section.top_margin = Mm(2)
        section.bottom_margin = Mm(2)

    
    
    region_config = {
        'республика': {'style':parse_xml(r'<w:shd {} w:fill="1F5C8B"/>'.format(nsdecls('w')))},
        'край': {'style':parse_xml(r'<w:shd {} w:fill="00B94F"/>'.format(nsdecls('w')))},
        'область': {'style':parse_xml(r'<w:shd {} w:fill="FDEADA"/>'.format(nsdecls('w')))},
        'город федерального значения': {'style':parse_xml(r'<w:shd {} w:fill="2C2C2C"/>'.format(nsdecls('w')))},
        'автономный округ': {'style':parse_xml(r'<w:shd {} w:fill="E7A529"/>'.format(nsdecls('w')))},
        'автономная область': {'style':parse_xml(r'<w:shd {} w:fill="185AD6"/>'.format(nsdecls('w')))}
    }
    
    region_images_row_config = {
        0: {'height': Cm(5.8)}                        
    }
    
    region_images_cells_config = {
        0: {'alignment': WD_ALIGN_PARAGRAPH.CENTER, 'image_width':Inches(1.45*2), 'image_height':Inches(1.8), 'image_path': 'temp/flag.png'},
        1: {'alignment': WD_ALIGN_PARAGRAPH.CENTER, 'image_width':Inches(1.6), 'image_height':Inches(1.6), 'image_path': 'temp/emblem.png'}
    }
        

    def add_region_images(self, region:Region):
        table = self.document.add_table(rows=1, cols=2, style='TableGrid')
        for row_index, row in enumerate(table.rows):
            row.height = self.region_images_row_config[row_index]['height']
            for cell_index, cell in enumerate(row.cells):
                cell._tc.get_or_add_tcPr().append(self.region_config[region.status]['style'])
                paragraph = cell.add_paragraph()
                paragraph.alignment = self.region_images_cells_config[cell_index]['alignment']
                run = paragraph.add_run()
                run.add_picture(self.region_images_cells_config[cell_index]['image_path'], width=self.region_images_cells_config[cell_index]['image_width'], height=self.region_images_cells_config[cell_index]['image_height'])
        self.document.add_paragraph(f'{region.status} {region.name}')
    
    def save(self, path):
        self.document.save(path)
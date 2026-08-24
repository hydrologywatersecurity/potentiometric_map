import docx
from docx import Document
import re

doc_path = "/Volumes/Marchezepe/GitHub/potentiometric_map/tutorial_potentiometric_map_v02.docx"
doc = Document(doc_path)

def get_image_rids(paragraph):
    p_xml = paragraph._p.xml
    rids = re.findall(r'r:embed="([^"]+)"', p_xml)
    rids.extend(re.findall(r'r:link="([^"]+)"', p_xml))
    return list(set(rids))

print("=== Scanning All Paragraphs ===")
for idx, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    rids = get_image_rids(p)
    if text:
        print(f"P{idx}: [Text] len={len(text)} | {text[:120]}")
    if rids:
        print(f"P{idx}: [IMAGE] rIds={rids}")

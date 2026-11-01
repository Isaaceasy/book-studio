#!/usr/bin/env python3
"""
clearance_pack.py - build the Clinical Clearance Pack (Word) for the named
clinician reviewer.

It reads every ledger row marked NEEDS-HUMAN in verification-log.md (Parts 1
and 2) and verification/part3..6-ledger.md, sorts them by Part and entry, and
writes final/clinical-clearance-pack.docx with a decision column for the
reviewer (Approve / Change / Remove) and a note column. It also lists the 25
figures with their sources and the open scope questions.

The pack never says the book has been reviewed. Clearance is recorded in
status.md only after the clinician returns decisions.
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.shared import Pt, Inches

book = Path(sys.argv[1] if len(sys.argv) > 1 else "books/emergency-medicine").resolve()
rows = []
files = [book / "verification-log.md"] + sorted((book / "verification").glob("part*-ledger.md"))
for f in files:
    for line in f.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*P\d-\d{3}\s*\|", line):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 5:
            continue
        rid, claim, result, change = cols[0], cols[1], cols[-2], cols[-1]
        source = " | ".join(cols[2:-2])
        if "NEEDS-HUMAN" not in (result + change + claim):
            continue
        part = int(rid[1])
        m = re.match(r"^(\d\.\d)\b", claim)
        entry = m.group(1) if m else ("Part " + str(part) + " general")
        cm = re.search(r"class ([A-Z/]+)", claim)
        cls = cm.group(1) if cm else ""
        rows.append((part, entry, rid, claim, cls, source, result, change))
rows.sort(key=lambda r: (r[0], r[1], r[2]))

FIGS = [
 (1,"Figure 1","1.2 Triage","SVG flow (AI-written)",""),(1,"Figure 2","1.3 Primary survey","SVG flow (AI-written)",""),
 (1,"Figure 3","1.4 Assessment sites","HiggsField 298a6af9-42ac-464b-b309-345bbe3fd980","Pulse, breathing, perfusion sites"),
 (1,"Figure 4","1.5 Handover","SVG (AI-written)",""),
 (2,"Figure 5","2.1 Upper airway anatomy","HiggsField 3c8fbbd1-2ada-4437-aca0-4d13cb87281c","Anatomy and labels"),
 (2,"Figure 6","2.2 Head-tilt chin-lift and jaw thrust","HiggsField 994daa3c-a102-4078-baaa-8f4730b09b86","Hand positions; direction of lift"),
 (2,"Figure 7","2.3 Two-hand mask seal","HiggsField 45151a2e-0ce0-4f02-bc73-198fd3f6450d","Eye protection not drawn (noted in caption)"),
 (2,"Figure 8","2.4 Breathing priorities","SVG flow (AI-written)",""),
 (3,"Figure 9","3.1 Heart and coronary arteries","HiggsField 0d136d11-4b3c-4026-835f-3139c1ede493","Anatomy and labels"),
 (3,"Figure 10","3.3 Rhythm patterns","SVG (AI-written, original drawings)","Patterns are schematic"),
 (3,"Figure 11","3.4 Compression hand and body position","HiggsField acc9f19c-8cc4-44a1-82ff-1aab069a9496","Hand position, straight arms"),
 (3,"Figure 12","3.4 Cardiac arrest sequence","SVG flow (AI-written)","Sequence and AED branch"),
 (4,"Figure 13","4.2 Direct pressure and packing","HiggsField 964926be-ae18-440f-9884-0a7304cedd91","Technique"),
 (4,"Figure 14","4.2 Tourniquet","HiggsField c91f73ff-f6df-4f75-b7db-2c80025ac84f","Band position, not over the knee"),
 (4,"Figure 15","4.3 Chest wall and lungs","HiggsField 65c45cd1-cb0c-450b-a0a0-6987cc920c61","Anatomy; rib fracture marks"),
 (4,"Figure 16","4.4 Forearm splint","HiggsField b67f3d31-cb45-446c-9833-673b9a55471d","Joint above and below"),
 (4,"Figure 17","4.5 Rule of nines","HiggsField fb0ec2c2-6bb5-47ae-97e2-3470b12a5546 (percentages added as text)","Regions and percentages"),
 (4,"Figure 18","4.6 Cold to heat illness","SVG (AI-written)","Stages and first actions"),
 (5,"Figure 19","5.1 Altered mental status approach","SVG flow (AI-written)",""),
 (5,"Figure 20","5.2 Brain arterial regions","HiggsField e97258b8-24d3-4db4-9c74-2c3a4a9f4903","Schematic regions; one arterial tree crosses all regions"),
 (5,"Figure 21","5.2 Face droop and arm drift","HiggsField bac8327f-048b-4c49-b791-8366d10b0fdf","Signs shown"),
 (5,"Figure 22","5.4 Sepsis pathway","SVG flow (AI-written)",""),
 (6,"Figure 23","6.1 Pediatric assessment triangle","SVG (AI-written)",""),
 (6,"Figure 24","6.1 Child and adult airway","HiggsField 8a64dda4-2a38-4aab-ae82-8ef95086a47c","Anatomy and proportions"),
 (6,"Figure 25","6.3 Left-lateral position","HiggsField 78aba7c6-6aa0-4077-8f35-04997e675c85 (mirrored)","Confirm LEFT side down after mirroring"),
]

doc = Document()
sec = doc.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = Inches(11), Inches(8.5)
for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, m, Inches(0.6))
st = doc.styles["Normal"]
st.font.name = "Arial"
st.font.size = Pt(9)

doc.add_heading("Clinical Clearance Pack: Emergency Nursing Fundamentals", 0)
doc.add_paragraph("Prepared 2026-10-29 for the clinician named by the owner (Orville A. Corey; credential and licence not supplied). "
                  "This pack lists every statement, procedure, figure and safety item that a qualified clinician must clear before the book is published. "
                  "Nothing in the book is described as clinician-reviewed until clearance is recorded in status.md.")
doc.add_heading("How to use this pack", 1)
for t in ["For each row choose Approve, Change (write the exact wording) or Remove.",
          "Rows are sorted by Part and entry. The Class column uses the audit classes: S = safety or procedure, D = drug or dose rule, B = clinical judgement call, C = consistency.",
          "The Source column shows what the fact-checker actually opened. Several US guideline full texts (AHA, ACS, ENA handbooks) were blocked and could not be read; the notes say where.",
          "The book gives no medicine doses. Drug names are limited to epinephrine, naloxone, albuterol, aspirin, oral glucose and oxygen, each with a scope sentence.",
          "Procedural figures given (CPR rate 100 to 120 a minute, depth at least 2 in / 5 cm and not more than about 2.4 in / 6 cm, 30:2, ventilation about 1 breath every 6 seconds, child rescue breathing 1 every 2 to 3 seconds, tourniquet 2 to 3 in above the wound, burn cooling at least 10 and ideally 20 minutes) need your explicit confirmation against current US guidance."]:
    doc.add_paragraph(t, style="List Bullet")
doc.add_paragraph(f"Totals: {len(rows)} ledger rows for review and {len(FIGS)} figures.")

doc.add_heading("A. Figures (AI-generated; every figure needs review)", 1)
tb = doc.add_table(rows=1, cols=6)
tb.style = "Light Grid Accent 1"
for i, h in enumerate(["Figure", "Entry", "Source", "What to check", "Decision", "Note"]):
    tb.rows[0].cells[i].text = h
for part, f, ent, src, chk in FIGS:
    c = tb.add_row().cells
    c[0].text, c[1].text, c[2].text, c[3].text = f, ent, src, chk or "Content, labels, legibility at 5 x 8 in"
doc.add_page_break()

doc.add_heading("B. Statements and procedures for decision", 1)
cur = None
tb = None
for part, entry, rid, claim, cls, source, result, change in rows:
    if part != cur:
        cur = part
        doc.add_heading(f"Part {part}", 2)
        tb = doc.add_table(rows=1, cols=7)
        tb.style = "Light Grid Accent 1"
        for i, h in enumerate(["ID", "Entry", "Item (as ledgered)", "Class", "Source note", "Decision", "Reviewer note"]):
            tb.rows[0].cells[i].text = h
    c = tb.add_row().cells
    c[0].text, c[1].text, c[2].text, c[3].text = rid, entry, claim[:600], cls
    c[4].text = (source[:450] + (" ... " + change[:200] if change and change.lower() not in ("none", "none.", "") else ""))
WIDTHS = {6: [0.8, 1.6, 2.2, 2.2, 1.2, 1.8], 7: [0.6, 0.5, 3.0, 0.4, 3.0, 0.9, 1.4]}
for t in doc.tables:
    t.autofit = False
    ws = WIDTHS.get(len(t.columns))
    for r in t.rows:
        if ws:
            for i, cell in enumerate(r.cells):
                cell.width = Inches(ws[i])
        for cell in r.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(8)
out = book / "final" / "clinical-clearance-pack.docx"
doc.save(str(out))
print(f"wrote {out} with {len(rows)} rows and {len(FIGS)} figures")

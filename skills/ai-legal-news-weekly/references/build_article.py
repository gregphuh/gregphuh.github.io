#!/usr/bin/env python3
"""
build_article.py — Self-contained AI Law Weekly article .docx generator.

NO external dependencies: standard library only (zipfile). Does NOT need the
docx skill, python-docx, or docx-js. It hardcodes the full Word format so the
output is correct every time:

  - Font: Georgia. Body 11pt.
  - Title 14pt bold black (style "Title")
  - Section heads Background/Analysis/Takeaways 12pt bold black (style "Heading1")
  - Analysis sub-heads 11pt bold ITALIC black (style "Heading2")
  - Takeaways = round-bullet list (style "ListBullet")
  - Real Word ENDNOTES (not footnotes), 10pt
  - Citations = blue (0563C1) underlined hyperlinks

USAGE:
    python3 build_article.py article.json output.docx

article.json schema:
{
  "title": "string (single line)",
  "date":  "Month D, YYYY",          # byline date; byline becomes 'AI Law Weekly · <date>'
  "lead":       [run, ...],          # one lead paragraph (no heading)
  "background": [[run, ...], ...],   # list of paragraphs
  "analysis":   [ {"subhead": "string", "paras": [[run,...], ...]}, ... ],
  "takeaways":  [[run, ...], ...],   # each bullet is a list of runs (or a plain string)
  "endnotes":   [[run, ...], ...]    # each endnote is a list of runs (or a plain string)
}
A "run" is either a plain string, or:
  {"text": "string", "italic": true}            # italic (e.g., case names, signals)
  {"text": "string", "url": "https://..."}      # blue hyperlink
  {"endnote": N}                                # superscript endnote marker -> endnote N
"""
import json, sys, zipfile

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---------- run / paragraph builders ----------
def norm_runs(runs):
    if isinstance(runs, str):
        return [{"text": runs}]
    out = []
    for r in runs:
        out.append({"text": r} if isinstance(r, str) else r)
    return out

def render_runs(runs, hyperlinks, scope):
    """scope: 'doc' or 'endnote' — decides which rels list hyperlinks go to."""
    xml = []
    for r in runs:
        if "endnote" in r:
            xml.append('<w:r><w:rPr><w:rStyle w:val="EndnoteReference"/></w:rPr>'
                       f'<w:endnoteReference w:id="{int(r["endnote"])}"/></w:r>')
            continue
        text = esc(r.get("text", ""))
        if r.get("url"):
            rid = f'{scope}HL{len(hyperlinks)+1}'
            hyperlinks.append((rid, r["url"]))
            xml.append(f'<w:hyperlink r:id="{rid}" w:history="1">'
                       f'<w:r><w:rPr><w:rStyle w:val="Hyperlink"/></w:rPr>'
                       f'<w:t xml:space="preserve">{text}</w:t></w:r></w:hyperlink>')
        else:
            rpr = "<w:i/>" if r.get("italic") else ""
            rpr = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
            xml.append(f'<w:r>{rpr}<w:t xml:space="preserve">{text}</w:t></w:r>')
    return "".join(xml)

def para(style, runs, hyperlinks, scope="doc"):
    ps = f'<w:pStyle w:val="{style}"/>' if style else ""
    body = render_runs(norm_runs(runs), hyperlinks, scope) if runs else ""
    return f'<w:p><w:pPr>{ps}</w:pPr>{body}</w:p>'

def heading_text(style, text):
    return f'<w:p><w:pPr><w:pStyle w:val="{style}"/></w:pPr><w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'

# ---------- static parts (hardcoded, always correct) ----------
CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
<Override PartName="/word/endnotes.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/fontTable.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"/>
</Types>'''

ROOT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

SETTINGS = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings {W} {R}><w:defaultTabStop w:val="720"/>
<w:endnotePr><w:numFmt w:val="decimal"/><w:endnote w:id="-1"/><w:endnote w:id="0"/></w:endnotePr></w:settings>'''

FONT_TABLE = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:fonts {W} {R}><w:font w:name="Georgia"><w:panose1 w:val="02040502050405020303"/>
<w:charset w:val="00"/><w:family w:val="roman"/><w:pitch w:val="variable"/></w:font></w:fonts>'''

NUMBERING = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering {W} {R}><w:abstractNum w:abstractNumId="0"><w:lvl w:ilvl="0">
<w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="&#8226;"/><w:lvlJc w:val="left"/>
<w:pPr><w:ind w:left="360" w:hanging="360"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:hint="default"/></w:rPr></w:lvl></w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num></w:numbering>'''

STYLES = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles {W} {R}>
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Georgia" w:hAnsi="Georgia" w:cs="Georgia"/><w:sz w:val="22"/><w:szCs w:val="22"/>
</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>
<w:spacing w:after="160" w:line="276" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:spacing w:after="80"/></w:pPr><w:rPr><w:b/><w:color w:val="000000"/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Byline"><w:name w:val="Byline"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:spacing w:after="240"/></w:pPr><w:rPr><w:i/><w:iCs/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr>
<w:rPr><w:b/><w:color w:val="000000"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:keepNext/><w:spacing w:before="160" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr>
<w:rPr><w:b/><w:i/><w:color w:val="000000"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="ListBullet"><w:name w:val="List Bullet"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:numPr><w:numId w:val="1"/></w:numPr><w:spacing w:after="80"/><w:ind w:left="360" w:hanging="360"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="EndnoteText"><w:name w:val="endnote text"/><w:basedOn w:val="Normal"/>
<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style>
<w:style w:type="character" w:styleId="EndnoteReference"><w:name w:val="endnote reference"/><w:rPr><w:vertAlign w:val="superscript"/></w:rPr></w:style>
<w:style w:type="character" w:styleId="Hyperlink"><w:name w:val="Hyperlink"/><w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr></w:style>
</w:styles>'''

SECTPR = ('<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
          '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>')

def rels_xml(hyperlinks):
    base = ['<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>',
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/endnotes" Target="endnotes.xml"/>',
            '<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>',
            '<Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable" Target="fontTable.xml"/>']
    for rid, url in hyperlinks:
        base.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="{esc(url)}" TargetMode="External"/>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + "".join(base) + "</Relationships>")

def build(article, out_path):
    doc_hl, en_hl = [], []

    # ----- document body -----
    body = [para("Title", article["title"], doc_hl)]
    body.append(para("Byline", [f'AI Law Weekly · {article["date"]}'], doc_hl))
    body.append(para("Normal", article.get("lead", ""), doc_hl))
    body.append(heading_text("Heading1", "Background"))
    for p in article.get("background", []):
        body.append(para("Normal", p, doc_hl))
    body.append(heading_text("Heading1", "Analysis"))
    for sub in article.get("analysis", []):
        if sub.get("subhead"):
            body.append(heading_text("Heading2", sub["subhead"]))
        for p in sub.get("paras", []):
            body.append(para("Normal", p, doc_hl))
    body.append(heading_text("Heading1", "Takeaways"))
    for b in article.get("takeaways", []):
        body.append(para("ListBullet", b, doc_hl))
    document = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document {W} {R}>'
                f'<w:body>{"".join(body)}{SECTPR}</w:body></w:document>')

    # ----- endnotes -----
    en = ['<w:endnote w:type="separator" w:id="-1"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:separator/></w:r></w:p></w:endnote>',
          '<w:endnote w:type="continuationSeparator" w:id="0"><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr><w:r><w:continuationSeparator/></w:r></w:p></w:endnote>']
    for i, note in enumerate(article.get("endnotes", []), start=1):
        marker = '<w:r><w:rPr><w:rStyle w:val="EndnoteReference"/></w:rPr><w:endnoteRef/></w:r>'
        runs_xml = render_runs(norm_runs(note), en_hl, scope="en")
        en.append(f'<w:endnote w:id="{i}"><w:p><w:pPr><w:pStyle w:val="EndnoteText"/></w:pPr>{marker}{runs_xml}</w:p></w:endnote>')
    endnotes = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:endnotes {W} {R}>{"".join(en)}</w:endnotes>'

    parts = {
        "[Content_Types].xml": CONTENT_TYPES,
        "_rels/.rels": ROOT_RELS,
        "word/document.xml": document,
        "word/_rels/document.xml.rels": rels_xml(doc_hl),
        "word/styles.xml": STYLES,
        "word/settings.xml": SETTINGS,
        "word/endnotes.xml": endnotes,
        "word/_rels/endnotes.xml.rels": rels_xml_endnotes(en_hl),
        "word/numbering.xml": NUMBERING,
        "word/fontTable.xml": FONT_TABLE,
    }
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in parts.items():
            z.writestr(name, data)

def rels_xml_endnotes(hyperlinks):
    rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    for rid, url in hyperlinks:
        rels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="{esc(url)}" TargetMode="External"/>')
    rels.append('</Relationships>')
    return "".join(rels)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python3 build_article.py article.json output.docx"); sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        article = json.load(f)
    build(article, sys.argv[2])
    import base64
    with open(sys.argv[2], "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    with open(sys.argv[2] + ".b64", "w") as f:
        f.write(b64)
    print("wrote", sys.argv[2], "and", sys.argv[2] + ".b64 (base64 for Google Drive create_file)")

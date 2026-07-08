#!/usr/bin/env python3
"""Regenerate the Lepage / Deschenes family tree PDF (fiabilise, juillet 2026)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    NextPageTemplate, PageBreak,
)
from reportlab.lib import colors

OUT = "/home/martin/.UPLOADS/arbre_lepage_deschenes.pdf"

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleBig", parent=styles["Title"], fontSize=20, spaceAfter=6)
subtitle_style = ParagraphStyle("Subtitle", parent=styles["Normal"], fontSize=13, alignment=TA_CENTER, spaceAfter=4)
meta_style = ParagraphStyle("Meta", parent=styles["Normal"], fontSize=10, alignment=TA_CENTER, textColor=colors.grey)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=14, spaceBefore=10, spaceAfter=6, textColor=colors.HexColor("#1a3d5c"))
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=11.5, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#1a3d5c"))
body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.5, leading=13.5, spaceAfter=4)
small = ParagraphStyle("Small", parent=styles["Normal"], fontSize=8.5, leading=12, textColor=colors.HexColor("#444444"), spaceAfter=3)
flag = ParagraphStyle("Flag", parent=styles["Normal"], fontSize=9.5, leading=13.5, textColor=colors.HexColor("#8a1f1f"), spaceAfter=4)
src = ParagraphStyle("Src", parent=styles["Normal"], fontSize=8, leading=11, textColor=colors.HexColor("#555555"), spaceAfter=8)

PAGE_W, PAGE_H = A4

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(2*cm, 1.3*cm, "Famille Lepage / Deschenes -- Document genealogique, mis a jour juillet 2026")
    canvas.drawRightString(PAGE_W - 2*cm, 1.3*cm, f"Page {doc.page}")
    canvas.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4,
                       leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="P", frames=[frame], onPage=footer)])

story = []

# ---- Page 1 : titre ----
story.append(Spacer(1, 4*cm))
story.append(Paragraph("Arbre genealogique", title_style))
story.append(Paragraph("Famille Lepage / Deschenes", subtitle_style))
story.append(Spacer(1, 1*cm))
story.append(Paragraph("Document etabli pour Martin Lepage", meta_style))
story.append(Paragraph("Montreal, Quebec", meta_style))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Version fiabilisee -- 1 juillet 2026 (revision de la version de juin 2026)", meta_style))
story.append(Spacer(1, 2*cm))
story.append(Paragraph(
    "Recherche effectuee a partir de sources publiques en ligne : avis de deces, registres "
    "paroissiaux numerises, bases de donnees genealogiques, et d'une session de fiabilisation "
    "methodique menee le 1 juillet 2026 (voir journal de recherche joint).", body))
story.append(PageBreak())

# ---- Page 2 : propositus + cote paternel ----
story.append(Paragraph("Martin Lepage -- Propositus", h1))
story.append(Paragraph("Fils de Jocelyn Lepage et d'Edith Deschenes", body))
story.append(Paragraph("Soeurs : Patricia Lepage (x Hugues) &middot; Martine Lepage (x Eric)", body))
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("Cote paternel -- Famille Lepage", h1))
story.append(Paragraph("Parents", h2))
story.append(Paragraph(
    "Jocelyn Lepage (ne ~1952, Jonquiere QC -- decede 17 mai 2013, Residence des Annees d'Or, "
    "Jonquiere)<br/>x Sylvie Bolduc (conjointe au moment du deces)", body))
story.append(Paragraph("- Patricia Lepage (x Hugues)<br/>- Martine Lepage (x Eric)<br/>- Martin Lepage (vous)", body))
story.append(Paragraph("Petits-fils de Jocelyn : Daven &middot; Jordan (en route au moment du deces) "
                        "-- filiation exacte (par quel enfant) non precisee dans les sources.", small))
story.append(Paragraph("Source : rfsag.ca -- avis de deces Jocelyn Lepage, 17 mai 2013 -- "
                        "https://www.rfsag.ca/deces/jocelyn-lepage-14155", src))

story.append(Paragraph("Grands-parents paternels", h2))
story.append(Paragraph(
    "Gerard Lepage (ne ~1910-1925, Jonquiere -- decede avant 2013)<br/>"
    "x Germaine Bouchard (nee 3 mai 1920 -- decedee 9 mars 2013, Jonquiere)", body))
story.append(Paragraph("- Gerald Lepage (voir oncles ci-dessous)<br/>- Jocelyn Lepage (votre pere)<br/>"
                        "- Roger Lepage (vivant en 2018, sans descendance connue)", body))
story.append(Paragraph("Paroisse familiale : St-Dominique, Jonquiere &middot; Residence : rue de la Fabrique / rue St-Dominique", body))
story.append(Paragraph("Source : Le Quotidien -- necrologie Gerald Lepage, 31 aout 2018 -- "
                        "https://necrologie.cn2i.ca/lepage-gerald/avis-de-deces/le-quotidien/11259", src))
story.append(Paragraph("Source : Dignity Memorial -- avis de deces Germaine Bouchard, 9 mars 2013 -- "
                        "https://www.dignitymemorial.com/fr-ca/obituaries/jonquiere-qc/germaine-bouchard-5455830", src))

story.append(Paragraph("Arriere-grands-parents paternels (cote Bouchard)", h2))
story.append(Paragraph("Delphis Bouchard + Eva Chayer -- parents de Germaine Bouchard, confirmes dans son avis de deces.", body))
story.append(Paragraph(
    "[!] Parents de Gerard Lepage : TOUJOURS INCONNUS au 1 juillet 2026. Mariage Gerard Lepage x "
    "Germaine Bouchard estime ~1943-1948, probablement paroisse St-Dominique de Jonquiere. Une "
    "session de recherche a teste et ECARTE l'hypothese \"Adrien-Roger Lepage (fils d'Oscar Lepage "
    "1888-1950) x Germaine Bouchard\" trouvee sur un arbre Geneanet : la Germaine Bouchard de cette "
    "union est fille de Philippe Bouchard et Victoria Soucy, ce qui ne correspond pas a nos parents "
    "confirmes (Delphis Bouchard + Eva Chayer). Homonymie ecartee -- ne pas reprendre cette piste "
    "sans nouvelle preuve. Voir journal-recherche.md.", flag))

story.append(Paragraph("Oncles et tantes paternels (freres et soeurs de Jocelyn)", h2))
story.append(Paragraph("- Gerald Lepage (ne ~1946 -- decede 31 aout 2018, Jonquiere) x Helene Imbeault", body))
story.append(Paragraph("Enfants : Carl &middot; Isabelle &middot; Andrea (x Kevin Boucher) &middot; Dany (x Danielle Tremblay)", body))
story.append(Paragraph("Petits-enfants : Louis &middot; Clara &middot; Nathan &middot; Mickael &middot; Jessy &middot; "
                        "Alexandra &middot; Jessica &middot; Nicolas &middot; Mathieu &middot; Andreanne", body))
story.append(Paragraph("- Roger Lepage (vivant en 2018) -- sans descendance connue", body))
story.append(PageBreak())

# ---- Page 3 : cote maternel ----
story.append(Paragraph("Cote maternel -- Famille Deschenes", h1))
story.append(Paragraph("Parents", h2))
story.append(Paragraph("Edith Deschenes (nee ~1953-1954, Jonquiere QC -- vivante)", body))
story.append(Paragraph("- Patricia Lepage (x Hugues)<br/>- Martine Lepage (x Eric)<br/>- Martin Lepage (vous)", body))
story.append(Paragraph("(enfants de l'union Jocelyn Lepage x Edith Deschenes, voir page precedente)", small))
story.append(Paragraph(
    "Edith Deschenes x Marcel Lalancette (nouveau compagnon d'Edith apres Jocelyn Lepage, "
    "confirme par Martin Lepage le 1 juillet 2026) -- sans enfant connu de cette union. La "
    "version de juin 2026 de ce document contenait une erreur de mise en page qui associait par "
    "erreur les enfants Lepage a cette union ; corrigee ici.", body))
story.append(Paragraph("Source : Dignity Memorial -- avis de deces Jean-Eudes Deschenes, 21 sept. 2019 -- "
                        "https://www.dignitymemorial.com/fr-ca/obituaries/jonquiere-qc/jean-eudes-deschenes-8865702", src))

story.append(Paragraph("Grands-parents maternels", h2))
story.append(Paragraph("Lionel Deschenes (Jonquiere / Arvida -- decede avant 2019)<br/>"
                        "x Laurette Tremblay (Arvida / Jonquiere -- decedee avant 2019)", body))
story.append(Paragraph("- Jean-Eudes Deschenes<br/>- Claudette Deschenes<br/>- Christiane Deschenes<br/>"
                        "- Edith Deschenes (votre mere)<br/>- Francine Deschenes<br/>- Real Deschenes", body))

story.append(Paragraph("Arriere-grands-parents maternels (cote Tremblay)", h2))
story.append(Paragraph("Johnny Tremblay + Emilie Vezina -- parents de Laurette Tremblay, confirmes par "
                        "l'avis de deces de Cecile Tremblay (soeur de Laurette), Jonquiere 2021.", body))
story.append(Paragraph("Source : Dignity Memorial -- avis de deces Cecile Tremblay, oct. 2021 -- "
                        "https://www.dignitymemorial.com/obituaries/jonquiere-qc/cecile-tremblay-10429984", src))
story.append(Paragraph(
    "[!] Parents de Lionel Deschenes : TOUJOURS INCONNUS au 1 juillet 2026. Une session de "
    "recherche a examine plusieurs Lionel Deschenes dans des arbres collaboratifs (fils d'Aurele "
    "Deschenes, epoux de Fernande Levesque / Suzanne Sorel / Madeleine Hebert) -- aucun ne "
    "correspond a l'epouse confirmee Laurette Tremblay. Ces pistes sont ecartees par non-"
    "concordance de l'epouse. Voir journal-recherche.md.", flag))

story.append(Paragraph("Oncles et tantes maternels (freres et soeurs d'Edith)", h2))
story.append(Paragraph("- Jean-Eudes Deschenes (28 oct. 1944 -- 21 sept. 2019, Chicoutimi) x Diane Tremblay", body))
story.append(Paragraph("Enfant : Marie-Josee Deschenes (x Dany Fournier)", body))
story.append(Paragraph("Petite-fille : Kim Fournier (x Francois Simard)", body))
story.append(Paragraph("Arriere-petite-fille : Madison", body))
story.append(Paragraph("- Claudette Deschenes x Gilles Tremblay -- Enfants : Pierre-Yves &middot; Steve", body))
story.append(Paragraph("- Christiane Deschenes x Vital Ainsley -- sans enfants", body))
story.append(Paragraph("- Francine Deschenes x Serge Gobeil -- Enfants : Anick &middot; Melanie", body))
story.append(Paragraph("- Real Deschenes x Claire Cote -- Enfants : Patrick &middot; feu Danny", body))
story.append(PageBreak())

# ---- Page 4 : schema des generations ----
story.append(Paragraph("Schema des generations", h1))
gen_data = [
    ["Generation", "Cote paternel (Lepage)", "Cote maternel (Deschenes)"],
    ["G4 -- Arriere-grands-parents",
     "Delphis Bouchard + Eva Chayer (parents de Germaine)\n[!] Parents de Gerard Lepage inconnus\n"
     "(1 hypothese testee et ecartee le 2026-07-01)",
     "Johnny Tremblay + Emilie Vezina (parents de Laurette)\n[!] Parents de Lionel inconnus\n"
     "(plusieurs homonymes ecartes le 2026-07-01)"],
    ["G3 -- Grands-parents", "Gerard Lepage x Germaine Bouchard\nJonquiere", "Lionel Deschenes x Laurette Tremblay\nJonquiere / Arvida"],
    ["G2 -- Parents", "Jocelyn Lepage (dec. 17 mai 2013)", "Edith Deschenes (vivante, ~72 ans)"],
    ["G1 -- Vous", "Martin Lepage", "Martin Lepage"],
]
t = Table(gen_data, colWidths=[3.6*cm, 6.3*cm, 6.3*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a3d5c")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTSIZE", (0,0), (-1,-1), 8),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f2f2f2")]),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t)
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph(
    "Fichier associe : un export GEDCOM complet de cet arbre "
    "(arbre-lepage-deschenes.ged) est disponible dans le dossier de travail pour import direct "
    "dans Gramps ou tout autre logiciel de genealogie.", body))
story.append(PageBreak())

# ---- Page 5 : a completer / outils ----
story.append(Paragraph("A completer", h1))
story.append(Paragraph("Les elements suivants restent a documenter :", body))
story.append(Paragraph("- Parents de Gerard Lepage (arriere-grand-pere paternel)", body))
story.append(Paragraph("&nbsp;&nbsp;Chercher l'acte de mariage Gerard Lepage x Germaine Bouchard, ~1943-1948", small))
story.append(Paragraph("&nbsp;&nbsp;Paroisse probable : St-Dominique de Jonquiere", small))
story.append(Paragraph("&nbsp;&nbsp;Ressource : FamilySearch, collection \"Canada, Quebec, registres paroissiaux "
                        "catholiques, 1621-1979\" -- https://www.familysearch.org/search/collection/1321742 "
                        "(necessite un compte gratuit pour feuilleter les images non indexees)", small))
story.append(Paragraph("- Parents de Lionel Deschenes (arriere-grand-pere maternel)", body))
story.append(Paragraph("&nbsp;&nbsp;Chercher l'acte de naissance ou de mariage de Lionel Deschenes, Jonquiere / Arvida", small))
story.append(Paragraph("&nbsp;&nbsp;Ressources : BAnQ Advitam -- https://advitam.banq.qc.ca "
                        "(remplace Pistard, desormais retire) &middot; FamilySearch", small))
story.append(Paragraph("- Descendants de Roger Lepage -- a confirmer", body))
story.append(Paragraph("- 4e generation -- arriere-arriere-grands-parents des deux cotes", body))

story.append(Paragraph("Correction d'outillage (juillet 2026)", h2))
story.append(Paragraph(
    "La version de juin 2026 mentionnait Pistard comme porte d'entree BAnQ. BAnQ a depuis "
    "remplace Pistard par Advitam (https://advitam.banq.qc.ca) pour la recherche dans les fonds "
    "d'archives ; BAnQ numerique (https://numerique.banq.qc.ca) reste l'outil pour le patrimoine "
    "numerise (journaux, images). Mettre a jour tout signet ou raccourci existant.", body))

story.append(Paragraph("Prochaine etape prioritaire (action humaine requise)", h2))
story.append(Paragraph(
    "La recherche automatisee en ligne a atteint sa limite reelle le 1 juillet 2026 : FamilySearch "
    "exige un compte gratuit pour feuilleter les images de registres non indexees, et les moteurs "
    "de recherche de BAnQ Advitam / BAnQ numerique sont des applications dynamiques qui ne "
    "repondent pas a des requetes automatisees. Prochaine action concrete : creer un compte "
    "FamilySearch gratuit et feuilleter la paroisse Saint-Dominique de Jonquiere (registres de "
    "mariage, 1943-1948) pour trouver l'acte Gerard Lepage x Germaine Bouchard. Le detail complet "
    "de la session et des pistes testees se trouve dans journal-recherche.md.", body))
story.append(PageBreak())

# ---- Page 6 : sources ----
story.append(Paragraph("Sources", h1))
sources_data = [
    ["#", "Document", "URL"],
    ["1", "Avis de deces -- Jocelyn Lepage (17 mai 2013)\nResidence funeraire du Saguenay",
     "rfsag.ca/deces/jocelyn-lepage-14155"],
    ["2", "Avis de deces -- Gerald Lepage (31 aout 2018)\nLe Quotidien / rfsag.ca",
     "necrologie.cn2i.ca/lepage-gerald/..."],
    ["3", "Avis de deces -- Germaine Bouchard (9 mars 2013)\nDignity Memorial",
     "dignitymemorial.com/.../germaine-bouchard-5455830"],
    ["4", "Avis de deces -- Jean-Eudes Deschenes (21 sept. 2019)\nDignity Memorial",
     "dignitymemorial.com/.../jean-eudes-deschenes-8865702"],
    ["5", "Avis de deces -- Cecile Tremblay (oct. 2021)\nDignity Memorial",
     "dignitymemorial.com/.../cecile-tremblay-10429984"],
    ["6", "Arbre collaboratif Geneanet (Gilles Lavoie, gilleslavoie46)\n"
     "-- consulte pour tester et ECARTER une hypothese Lepage/Bouchard",
     "gw.geneanet.org/gilleslavoie46 (source secondaire, niveau 4)"],
]
t2 = Table(sources_data, colWidths=[1*cm, 8.6*cm, 6.6*cm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a3d5c")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 8),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f2f2f2")]),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(t2)
story.append(Spacer(1, 0.6*cm))
story.append(Paragraph(
    "Journal de recherche complet, methodologie et hypotheses ecartees en detail : voir "
    "journal-recherche.md dans le dossier de travail genealogie-lepage-deschenes.", body))

doc.build(story)
print("PDF written to", OUT)

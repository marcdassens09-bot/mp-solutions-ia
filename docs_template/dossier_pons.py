"""
MP Solutions IA — Dossier de présentation
Prospect : PONS PLAQUISTE PEINTRE (SAS, Le Fossat, 09130)
SIRET 823 725 601 00012 — 3-5 salariés, RGE Qualibat
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles, VERT, BLANC, GRIS_CLAIR
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from copy import deepcopy

S = get_styles()

# Ce dossier tient sur une seule page : styles resserrés localement à ce
# fichier (mp_template.py n'est jamais modifié), pour ne jamais laisser de
# grand blanc en bas de la dernière page (cf. feedback_pdf_equilibrer_pages.md).
S["section"] = deepcopy(S["section"])
S["section"].spaceBefore = 12
S["section"].spaceAfter = 5
S["corps"] = deepcopy(S["corps"])
S["corps"].leading = 14.5
S["corps"].spaceAfter = 7

contenu = [
    Paragraph(
        "Écouter, comprendre, servir — en toute transparence.",
        S["sous_titre"]
    ),
    Spacer(1, 2*mm),

    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph(
        "● Une équipe de 3 à 5 salariés, mobilisée sur les chantiers en journée : chaque "
        "appel client manqué pendant une pose ou une finition est une demande de devis "
        "qui risque de partir chez un confrère plus disponible.",
        S["corps"]
    ),
    Paragraph(
        "● Une certification RGE Qualibat qui ouvre droit à des aides pour vos clients "
        "(isolation, rénovation) — un argument fort, mais qui suscite systématiquement "
        "les mêmes questions : éligibilité, démarches, délais.",
        S["corps"]
    ),
    Paragraph(
        "● Aucun moyen, en dehors des horaires d'atelier, de renseigner un particulier "
        "sur vos délais d'intervention, vos zones desservies ou le déroulé d'un chantier "
        "plaquiste/peinture avant qu'il ne se tourne ailleurs.",
        S["corps"]
    ),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Je n'installe pas seulement un chatbot : j'intègre l'IA dans votre relation "
        "client pour digitaliser ce qui vous prend du temps, en commençant par un "
        "chatbot intégré à votre présence en ligne, disponible en continu, capable "
        "de répondre aux questions courantes sur vos prestations, votre certification RGE "
        "et vos délais, et de qualifier chaque demande avant de vous la transmettre — pour "
        "que votre temps sur chantier ne coûte plus de devis.",
        S["corps"]
    ),
    Spacer(1, 3*mm),
    Paragraph(
        "Ce document est une première approche, sans tarif ni engagement : l'objectif "
        "est d'abord de voir ensemble si l'idée vous parle.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Financements à vérifier", S["corps_bold"]),
    Paragraph(
        "D'après les critères publics de votre entreprise, PONS PLAQUISTE PEINTRE semble "
        "entrer dans le champ du Pass Occitanie (Région) et du dispositif Diag Data IA "
        "(Bpifrance). À vérifier vous-même auprès de la Région ou de la CCI — MP Solutions "
        "IA ne garantit aucune obtention d'aide et ne s'occupe pas de ces démarches.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("-> MP Solutions IA", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia@gmail.com — Artigat (09130)",
        S["corps"]
    ),
]

if __name__ == "__main__":
    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_pons.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : PONS PLAQUISTE PEINTRE — Le Fossat (09130)",
        content_story=contenu,
    )

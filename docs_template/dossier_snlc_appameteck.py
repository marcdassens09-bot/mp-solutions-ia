"""
MP Solutions IA — Dossier de présentation
Prospect : SNLC APPAMETECK (Cyril Charbonnier, auto-entrepreneur, Pamiers, 09100)
SIRET 512199415 00039 — location sono/éclairage événementiel
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.units import mm
from copy import deepcopy

S = get_styles()

# Resserré sur 1 page dès le départ (règle feedback_pdf_equilibrer_pages.md) :
# styles locaux à ce fichier, mp_template.py n'est jamais modifié.
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
        "● Une activité de location sono/éclairage rythmée par les soirées, mariages et "
        "spectacles : les demandes arrivent souvent le soir ou le week-end, au moment même "
        "où vous êtes sur un événement et ne pouvez pas répondre.",
        S["corps"]
    ),
    Paragraph(
        "● 17 ans d'activité mais une présence en ligne éclatée : une fiche PagesJaunes, une "
        "page Facebook, et deux anciens sites (e-monsite, Wix) qui ne sont plus tenus à jour "
        "— un client qui cherche une dispo un dimanche soir ne trouve personne pour répondre.",
        S["corps"]
    ),
    Paragraph(
        "● Chaque demande de devis (matériel, date, durée) redemande les mêmes informations "
        "avant même de savoir si le matériel est libre à cette date.",
        S["corps"]
    ),
    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Un chatbot IA disponible en continu, capable de présenter votre matériel de sono et "
        "d'éclairage, de répondre aux questions courantes sur les tarifs et la disponibilité, "
        "et de collecter la demande complète (date, lieu, matériel souhaité) avant même que "
        "vous ne rappeliez — pour ne plus perdre de demande reçue un soir de événement.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Prochaine étape", S["corps_bold"]),
    Paragraph(
        "Un échange rapide avec vous permettrait de préciser vos besoins réels (matériel "
        "concerné, volume de demandes, période de forte activité) et de vous proposer un "
        "tarif adapté — rien n'est figé avant d'avoir échangé.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("-> MP Solutions IA", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia@gmail.com — Artigat (09130)<br/>"
        "\u00abÉcouter, comprendre, servir — en toute transparence.\u00bb",
        S["corps"]
    ),
]

if __name__ == "__main__":
    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_snlc_appameteck.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : SNLC APPAMETECK — Pamiers (09100)",
        content_story=contenu,
    )

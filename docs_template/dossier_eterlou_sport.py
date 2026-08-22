"""
MP Solutions IA — Dossier de présentation (découverte, sans tarif)
Prospect : L'ÉTERLOU SPORT (SARL, Ax-les-Thermes / Luzenac, 09)
SIRET 334501400 00017 — magasin d'articles de sport, 3-5 salariés
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
        "● 40 ans d'activité près des stations de ski, mais une forte saisonnalité : en plein "
        "hiver, les questions sur la disponibilité du matériel de location, les tailles et les "
        "horaires arrivent en rafale — souvent le soir, quand les vacanciers organisent leur "
        "lendemain et que le magasin est fermé.",
        S["corps"]
    ),
    Paragraph(
        "● Aucune présence en ligne propre trouvée : un touriste qui prépare son séjour et "
        "cherche à vérifier une disponibilité avant de se déplacer ne trouve pas de réponse "
        "immédiate.",
        S["corps"]
    ),
    Paragraph(
        "● Trois établissements à coordonner (Ax-les-Thermes, Luzenac) — chaque question "
        "générique (horaires, stock, tailles) redemande le même effort au comptoir.",
        S["corps"]
    ),
    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Un chatbot IA disponible en continu, capable de répondre aux questions courantes sur "
        "vos horaires, votre offre de location de ski et vos disponibilités, et d'orienter "
        "chaque visiteur vers le bon magasin — pour ne plus perdre de clientèle touristique en "
        "dehors des heures d'ouverture.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Prochaine étape", S["corps_bold"]),
    Paragraph(
        "Un échange rapide avec vous permettrait de préciser vos besoins réels (questions les "
        "plus fréquentes en saison, gestion du stock entre les deux établissements) et de vous "
        "proposer un tarif adapté — rien n'est figé avant d'avoir échangé.",
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
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_eterlou_sport.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : L'ÉTERLOU SPORT — Ax-les-Thermes / Luzenac (09)",
        content_story=contenu,
    )

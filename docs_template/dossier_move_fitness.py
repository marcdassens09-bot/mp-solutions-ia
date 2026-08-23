"""
MP Solutions IA — Dossier de présentation (découverte, sans tarif)
Prospect : MOVE FITNESS (Gualter Da Silva Machado, Saverdun, 09700)
SIRET 821902434 00017 — salle de fitness
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
        "● Les questions des adhérents et futurs adhérents (horaires, cours collectifs, "
        "tarifs, essai découverte) arrivent souvent en dehors des heures d'accueil — le "
        "soir, le week-end — quand personne n'est présent pour y répondre.",
        S["corps"]
    ),
    Paragraph(
        "● Une présence en ligne limitée à Facebook et aux annuaires : quelqu'un qui cherche "
        "une salle de sport à Saverdun et compare plusieurs options ne trouve pas de réponse "
        "immédiate à ses questions avant de se décider.",
        S["corps"]
    ),
    Paragraph(
        "● Les grandes enseignes du secteur (Keep Cool, L'Orange Bleue) proposent déjà des "
        "outils en ligne pour répondre vite — un écart qui peut jouer en défaveur d'une salle "
        "indépendante, alors que la relation de proximité est justement votre force.",
        S["corps"]
    ),
    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Je n'installe pas seulement un chatbot : j'intègre l'IA dans votre relation "
        "client pour digitaliser ce qui vous prend du temps, en commençant par un "
        "chatbot disponible en continu, capable de répondre aux questions courantes sur "
        "vos horaires, vos cours et vos formules d'abonnement, et de recueillir les coordonnées "
        "de toute personne intéressée par un essai — pour transformer une visite manquée en "
        "contact exploitable.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Prochaine étape", S["corps_bold"]),
    Paragraph(
        "Un échange rapide avec vous permettrait de préciser vos besoins réels (questions les "
        "plus fréquentes, formules proposées, période de forte affluence) et de vous proposer "
        "un tarif adapté — rien n'est figé avant d'avoir échangé.",
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
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_move_fitness.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : MOVE FITNESS — Saverdun (09700)",
        content_story=contenu,
    )

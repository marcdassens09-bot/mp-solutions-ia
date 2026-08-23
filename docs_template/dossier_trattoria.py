# -*- coding: utf-8 -*-
"""
MP Solutions IA — Présentation prospect
Prospect : Yoann Bertrant — La Trattoria / Le Camion Doré (Le Fossat, 09130)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.units import mm

S = get_styles()

contenu = [
    Paragraph(
        "Écouter, comprendre, servir — en toute transparence.",
        S["sous_titre"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Une invitation à réfléchir", S["section"]),
    Paragraph(
        "Avant de vous proposer quoi que ce soit, je veux d'abord comprendre votre "
        "activité, vos contraintes et ce qui vous prendrait vraiment la tête au "
        "quotidien. Ce que vous lisez ici, c'est ce qu'il serait possible de mettre "
        "en place — basé sur une simple observation personnelle.",
        S["corps"]
    ),
    Spacer(1, 5*mm),

    Paragraph("Ce qu'il serait possible de mettre en place", S["section"]),
    Paragraph(
        "● Un seul point de contact pour vos deux activités — que le client cherche "
        "le Camion Doré ou La Trattoria, il tombe au bon endroit sans vous déranger "
        "pendant le service.",
        S["corps"]
    ),
    Paragraph(
        "● Réponses automatiques 24h/24 — horaires de La Trattoria, emplacement du "
        "jour pour le camion, menu : vos clients ont une réponse même à 23h, sans "
        "que vous décrochiez.",
        S["corps"]
    ),
    Paragraph(
        "● Bouton ON/OFF pendant le coup de feu — vous coupez la prise de commande "
        "d'un clic quand vous êtes débordé. Vous décidez, pas la machine.",
        S["corps"]
    ),
    Paragraph(
        "● Demandes prises en charge pendant que vous êtes occupé — réservations, "
        "questions : vous les retrouvez et répondez à votre rythme.",
        S["corps"]
    ),
    Paragraph(
        "● Option à venir — appels téléphoniques gérés par l'IA. Cette "
        "fonctionnalité est en cours de développement.",
        S["corps"]
    ),
    Spacer(1, 5*mm),

    Paragraph("Pourquoi maintenant", S["section"]),
    Paragraph(
        "Vous ouvrez La Trattoria tout en gardant le Camion Doré : deux activités à "
        "faire tourner en même temps, donc encore moins de disponibilité pour "
        "répondre au téléphone. C'est aussi le meilleur moment pour mettre en place "
        "un outil comme celui-ci — dès le départ, plutôt que de changer des "
        "habitudes déjà prises dans quelques mois.",
        S["corps"]
    ),
    Spacer(1, 5*mm),

    Paragraph("Qui suis-je ?", S["section"]),
    Paragraph(
        "Je suis Marc-Paul Dassens, fondateur de MP Solutions IA, basé à Artigat "
        "(09), à quelques minutes du Fossat. Ma philosophie tient en trois mots : "
        "écouter, comprendre, servir. Je ne vends pas de la technologie — je "
        "résous des problèmes concrets pour des gens qui travaillent. C'est pour "
        "ça que je veux d'abord vous poser des questions avant de vous proposer "
        "quoi que ce soit.",
        S["corps"]
    ),
    Spacer(1, 5*mm),

    Paragraph("La prochaine étape — un café, 30 minutes", S["section"]),
    Paragraph(
        "On se retrouve chez vous, je vous pose quelques questions sur votre "
        "activité. Ensemble, on identifie ce qui vous ferait vraiment gagner du "
        "temps — et ce qui ne vous servirait à rien. Ensuite seulement, si ça a du "
        "sens pour vous, je vous fais une proposition adaptée. Aucune pression, "
        "juste une conversation.",
        S["corps"]
    ),
    Spacer(1, 8*mm),

    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia.fr — Artigat (09130)",
        S["corps_bold"]
    ),
]

if __name__ == "__main__":
    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_trattoria.pdf",
        title="La Trattoria",
        subtitle="Le Fossat (09130) — Ariège",
        content_story=contenu,
    )

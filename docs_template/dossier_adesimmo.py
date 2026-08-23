# -*- coding: utf-8 -*-
"""
MP Solutions IA — Dossier de présentation
Prospect : ADESIMMO — agence immobilière (utilisatrice d'Orisha)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles, VERT, BLANC, GRIS_CLAIR
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.units import mm

S = get_styles()
# Compact : plus de contenu par page sans couper de tableau ni sacrifier le
# nombre de pages au-delà de ce que la lisibilité permet.
S["section"] = S["section"].clone("section_c", spaceBefore=10, spaceAfter=4)
S["corps"] = S["corps"].clone("corps_c", fontSize=9.5, leading=13, spaceAfter=4)
S["corps_bold"] = S["corps_bold"].clone("corps_bold_c", fontSize=9.5, leading=12, spaceAfter=2)

contenu = [
    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph(
        "Vous utilisez aujourd'hui Orisha pour la gestion de votre agence. Lors de "
        "notre échange, vous m'avez indiqué que le module IA / chatbot proposé par "
        "Orisha vous semble aujourd'hui trop complexe à prendre en main pour votre "
        "équipe : un outil pensé pour la gestion complète de l'agence (mandats, "
        "transactions, comptabilité), dans lequel le module IA arrive noyé — d'où "
        "un outil disponible sur le papier mais sous-utilisé au quotidien.",
        S["corps"]
    ),
    Spacer(1, 2*mm),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Je n'installe pas seulement un chatbot : j'intègre l'IA dans votre "
        "relation client pour digitaliser ce qui vous prend du temps, en "
        "commençant par un chatbot autonome, indépendant d'Orisha, dédié à "
        "l'accueil de vos visiteurs — horaires, biens disponibles, prise de "
        "contact. Configuré avec vous, pris en main en quelques minutes, sans "
        "formation ni module annexe à apprendre, et prêt à s'étendre ensuite "
        "au suivi des demandes ou à la veille selon vos besoins.",
        S["corps"]
    ),
    Spacer(1, 3*mm),
    Paragraph(
        "Ce document est une première approche, sans tarif ni engagement : l'objectif "
        "est d'abord de voir ensemble si l'idée vous parle.",
        S["corps"]
    ),
    Spacer(1, 3*mm),

    KeepTogether([
        Paragraph("Orisha vs MP Solutions IA — la simplicité au quotidien", S["section"]),
        Paragraph(
            "Comparaison portant uniquement sur le module IA / chatbot d'Orisha — pas "
            "l'ensemble du logiciel de gestion, que vous gardez par ailleurs.",
            S["corps"]
        ),
        Spacer(1, 1*mm),
        Table(
            [
                ["", "Module IA Orisha", "MP Solutions IA"],
                ["Prise en main", "Formation nécessaire", "Quelques minutes"],
                ["Champ d'action", "Noyé dans un logiciel de gestion complet", "Dédié uniquement à l'accueil visiteurs"],
                ["Configuration", "Standardisée, à distance", "Faite avec vous, sur mesure"],
                ["Support", "Support éditeur national", "Contact direct et local"],
                ["Usage réel constaté", "Sous-utilisé", "Pensé pour être utilisé tous les jours"],
            ],
            colWidths=[38*mm, 65*mm, 65*mm],
            style=TableStyle([
                ("BACKGROUND",     (0,0), (-1,0), GRIS_CLAIR),
                ("FONTNAME",       (0,0), (-1,0), "Helvetica-Bold"),
                ("FONTNAME",       (0,1), (0,-1), "Helvetica-Bold"),
                ("FONTSIZE",       (0,0), (-1,-1), 8),
                ("GRID",           (0,0), (-1,-1), 0.5, colors.HexColor("#DDDDDD")),
                ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
                ("TOPPADDING",     (0,0), (-1,-1), 4),
                ("BOTTOMPADDING",  (0,0), (-1,-1), 4),
                ("LEFTPADDING",    (0,0), (-1,-1), 6),
            ])
        ),
    ]),
    Spacer(1, 3*mm),

    Paragraph(">> CONFORMITÉ — CE QUE DIT LA LOI DEPUIS LE 2 AOÛT 2026", S["section"]),
    Paragraph(
        "Depuis le 2 août 2026, le règlement (UE) 2024/1689 sur l'IA (AI Act), "
        "article 50, impose : informer le visiteur dès le premier échange qu'il "
        "parle à une IA, et organiser un relais vers un professionnel pour toute "
        "négociation, réclamation ou situation personnelle. Sanctions en cas de "
        "manquement : jusqu'à 15 M€ ou 3 % du CA mondial (appréciation "
        "proportionnée pour les PME). La loi Hoguet (n° 70-9 du 2 janvier 1970), "
        "qui encadre votre profession, ne dit rien de spécifique sur les "
        "chatbots — c'est bien ce règlement, plus récent, qui s'applique ici.",
        S["corps"]
    ),
    Paragraph(
        "Ce que je livre respecte déjà ces deux points par construction : "
        "identification IA dès le premier message sur tous mes bots, sans "
        "adaptation de dernière minute ; et un chatbot qui ne négocie rien, ne "
        "s'engage sur rien, ne décide rien à votre place — il informe et oriente "
        "vers vous pour le reste.",
        S["corps"]
    ),
    Paragraph(
        "Textes officiels : Règlement (UE) 2024/1689 (EUR-Lex, CELEX 32024R1689) "
        "— Loi n° 70-9 du 2 janvier 1970 (Légifrance, JORFTEXT000000512228). Ceci "
        "reste un point de repère général, pas un conseil juridique personnalisé.",
        S["mention"]
    ),
    Spacer(1, 3*mm),

    Paragraph("Sécurité et données", S["corps_bold"]),
    Paragraph(
        "Le chatbot n'a accès à rien d'autre qu'à ce qu'on lui configure : pas "
        "d'accès à Orisha ni à vos autres outils, aucune capacité à modifier ou "
        "supprimer une donnée de son côté — il informe, il ne peut pas agir sur "
        "vos systèmes. Comme sur l'ensemble des chatbots que j'opère, un registre "
        "des traitements RGPD existe et une politique de confidentialité est "
        "publiée ; les données collectées auprès des visiteurs (nom, contact) "
        "sont limitées au strict nécessaire, et les informations sensibles sont "
        "masquées dans les journaux techniques. Droit à l'effacement (RGPD, "
        "article 17) : tout visiteur peut demander la suppression de ses "
        "données, à vous ou à moi directement — la demande est traitée sous un "
        "mois, comme l'exige la loi.",
        S["corps"]
    ),
    Spacer(1, 2*mm),

    Paragraph("Comment ça marche", S["section"]),
    Paragraph(
        "● Un visiteur pose une question sur votre site, à tout moment ; le "
        "chatbot répond à partir des informations réelles de votre agence "
        "(biens disponibles, horaires, secteurs couverts) et oriente vers le bon "
        "contact pour toute demande précise — sans jamais inventer d'information.",
        S["corps"]
    ),
    Paragraph(
        "● Vous gardez la main : le contenu est configuré avec vous, à partir de "
        "ce que vous savez de votre activité — pas à partir d'un paramétrage "
        "générique.",
        S["corps"]
    ),
    Spacer(1, 2*mm),

    Paragraph("Installation en 4 étapes", S["section"]),
    Paragraph(
        "1. Questionnaire technique (horaires, biens, FAQ, ton souhaité)",
        S["corps"]
    ),
    Paragraph("2. Configuration du chatbot", S["corps"]),
    Paragraph("3. Intégration sur votre site", S["corps"]),
    Paragraph("4. Mise en service et suivi mensuel", S["corps"]),
    Spacer(1, 3*mm),

    Paragraph("Bon de commande", S["section"]),
    Table(
        [
            ["Entreprise", "ADESIMMO"],
            ["Contact", "____________________________"],
            ["Prestation retenue", "Installation + suivi mensuel"],
            ["Prix convenu", "______ € installation + ______ € / mois"],
            ["Engagement minimum", "3 mois"],
            ["Préavis de résiliation", "1 mois"],
            ["Signature et date", "____________________________"],
        ],
        colWidths=[55*mm, 115*mm],
        style=TableStyle([
            ("FONTNAME",       (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE",       (0,0), (-1,-1), 9),
            ("GRID",           (0,0), (-1,-1), 0.5, colors.HexColor("#DDDDDD")),
            ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",     (0,0), (-1,-1), 4),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 4),
            ("LEFTPADDING",    (0,0), (-1,-1), 6),
        ])
    ),
    Spacer(1, 4*mm),
    Paragraph("-> MP Solutions IA", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia@gmail.com — Artigat (09130)<br/>"
        "«Écouter, comprendre, servir — en toute transparence.»",
        S["corps"]
    ),
]

if __name__ == "__main__":
    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_adesimmo.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : ADESIMMO — Agence immobilière",
        content_story=contenu,
    )

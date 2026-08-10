"""
MP Solutions IA — Dossier de présentation
Prospect : FUMECO-LEZE (Artigat, 09130)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles, VERT, BLANC, GRIS_CLAIR
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import mm

S = get_styles()

contenu = [
    # ── Page 1 ────────────────────────────────
    Paragraph(
        "Écouter, comprendre, servir — en toute transparence.",
        S["sous_titre"]
    ),
    Spacer(1, 4*mm),

    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph(
        "● L'accueil client repose sur trois numéros de téléphone distincts et un "
        "formulaire, joignables uniquement du lundi au vendredi, 9h-12h et 13h30-17h.",
        S["corps"]
    ),
    Paragraph(
        "● Trois publics différents (particuliers, professionnels, collectivités) pour "
        "plus de 50 références produits : des questions récurrentes mais différentes "
        "selon le profil (disponibilité, certification UAB, délais de livraison, zones "
        "desservies).",
        S["corps"]
    ),
    Paragraph(
        "● Aucun chatbot ni FAQ en ligne sur fumeco.fr : en dehors des horaires "
        "d'ouverture, aucune réponse immédiate — seulement un formulaire en attente.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Un chatbot IA intégré à fumeco.fr, disponible en continu, capable de répondre "
        "aux questions les plus fréquentes de vos trois publics et d'orienter chaque "
        "visiteur vers le bon contact commercial — distribution, chantier, ou standard.",
        S["corps"]
    ),
    Spacer(1, 5*mm),
    Table(
        [
            ["Prestation", "Détail", "Tarif"],
            ["Installation", "Chatbot personnalisé + intégration fumeco.fr", "1 200 €"],
            ["Suivi mensuel", "Maintenance, mises à jour, ajustements", "120 € / mois"],
        ],
        colWidths=[45*mm, 85*mm, 40*mm],
        style=TableStyle([
            ("BACKGROUND",     (0,0), (-1,0), VERT),
            ("TEXTCOLOR",      (0,0), (-1,0), BLANC),
            ("FONTNAME",       (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",       (0,0), (-1,-1), 9),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [BLANC, GRIS_CLAIR]),
            ("GRID",           (0,0), (-1,-1), 0.5, colors.HexColor("#DDDDDD")),
            ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",     (0,0), (-1,-1), 5),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 5),
            ("LEFTPADDING",    (0,0), (-1,-1), 6),
        ])
    ),
    Spacer(1, 4*mm),
    Paragraph("Engagement minimum : 3 mois.", S["corps"]),
    Spacer(1, 5*mm),
    Paragraph("Financements à vérifier", S["corps_bold"]),
    Paragraph(
        "D'après les critères publics de votre entreprise, FUMECO-LEZE semble entrer "
        "dans le champ du Pass Occitanie (Région) et du dispositif Diag Data IA "
        "(Bpifrance). À vérifier vous-même auprès de la Région ou de la CCI — MP "
        "Solutions IA ne garantit aucune obtention d'aide et ne s'occupe pas de ces "
        "démarches.",
        S["corps"]
    ),
    PageBreak(),

    # ── Page 2 ────────────────────────────────
    Paragraph("Comment ça marche", S["section"]),
    Paragraph(
        "● Un visiteur pose une question sur fumeco.fr, à tout moment ; le chatbot "
        "répond à partir des informations réelles de votre entreprise (produits, "
        "certifications, délais, horaires) et oriente vers le bon contact pour toute "
        "demande précise — sans jamais inventer d'information.",
        S["corps"]
    ),
    Paragraph(
        "● Vous gardez la main : le contenu est configuré avec vous, à partir de ce "
        "que vous savez de votre activité.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Processus d'installation", S["section"]),
    Paragraph(
        "● Questionnaire technique (horaires, produits, FAQ, ton souhaité) "
        "&nbsp;&nbsp;—&nbsp;&nbsp; Configuration du chatbot "
        "&nbsp;&nbsp;—&nbsp;&nbsp; Intégration sur fumeco.fr "
        "&nbsp;&nbsp;—&nbsp;&nbsp; Mise en service et suivi mensuel",
        S["corps"]
    ),
    Spacer(1, 6*mm),

    Paragraph("Bon de commande", S["section"]),
    Table(
        [
            ["Entreprise", "FUMECO-LEZE"],
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
            ("FONTSIZE",       (0,0), (-1,-1), 9.5),
            ("GRID",           (0,0), (-1,-1), 0.5, colors.HexColor("#DDDDDD")),
            ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",     (0,0), (-1,-1), 6),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 6),
            ("LEFTPADDING",    (0,0), (-1,-1), 6),
        ])
    ),
    Spacer(1, 8*mm),
    Paragraph("-> MP Solutions IA", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia@gmail.com — Artigat (09130)<br/>"
        "\u00abÉcouter, comprendre, servir — en toute transparence.\u00bb",
        S["corps"]
    ),
]

if __name__ == "__main__":
    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_fumeco.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : FUMECO-LEZE — Artigat (09130)",
        content_story=contenu,
    )

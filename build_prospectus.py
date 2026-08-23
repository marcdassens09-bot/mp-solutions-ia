# -*- coding: utf-8 -*-
"""Génère le prospectus publicitaire MP Solutions IA."""

import sys
sys.path.insert(0, "docs_template")

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import mm
from mp_template import (
    build_document, get_styles, VERT, VERT_FONCE, ORANGE, GRIS_CLAIR, BLANC, colors
)

S = get_styles()

# Prospectus = une seule page : versions resserrees des styles du template
# (moins d'espace avant les titres, interligne plus court sur le corps).
S["section"] = S["section"].clone("section_compact", spaceBefore=10, spaceAfter=4)
S["corps"] = S["corps"].clone("corps_compact", leading=12.5, spaceAfter=4)
S["corps_bold"] = S["corps_bold"].clone("corps_bold_compact", spaceAfter=3)

contenu = [
    Paragraph("Au commencement, l'homme savait", S["section"]),
    Paragraph(
        "L'homme savait lire l'autre. Sans mots. Sans écran. Un regard, un souffle, "
        "une posture suffisaient pour comprendre et agir ensemble. Cette intelligence, "
        "l'humanité l'a affinée pendant 200 000 ans.",
        S["corps"]
    ),

    Paragraph("✦ Ce qu'on a gagné. Ce qu'on a perdu.", S["section"]),
    Table(
        [
            ["GAGNÉ", "PERDU"],
            ["L'écriture", "La mémoire profonde"],
            ["La ville", "La cohésion de groupe"],
            ["Le téléphone", "La présence physique"],
            ["Internet", "L'attention réelle"],
            ["L'IA des grands groupes", "Le contact humain"],
        ],
        colWidths=[75*mm, 75*mm],
        style=TableStyle([
            ("BACKGROUND",     (0,0), (0,-1), VERT_FONCE),
            ("BACKGROUND",     (1,0), (1,-1), ORANGE),
            ("TEXTCOLOR",      (0,0), (-1,-1), BLANC),
            ("FONTNAME",       (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTNAME",       (0,1), (-1,-1), "Helvetica"),
            ("FONTSIZE",       (0,0), (-1,-1), 9.5),
            ("GRID",           (0,0), (-1,-1), 1, BLANC),
            ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",     (0,0), (-1,-1), 4),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 4),
            ("LEFTPADDING",    (0,0), (-1,-1), 8),
        ])
    ),
    Paragraph(
        "L'humanité a gagné en portée. Elle a perdu en profondeur.",
        S["corps_bold"]
    ),

    Paragraph("L'IA des grands groupes : puissante. Froide.", S["section"]),
    Paragraph(
        "Orange, Bouygues, les banques déploient des assistants IA. Efficaces. Rapides. "
        "Identiques. Mais conçus pour des millions d'utilisateurs anonymes — pas pour les "
        "TPE et PME d'Ariège. Un grand groupe ne viendra jamais s'asseoir en face d'un "
        "artisan pour l'écouter vraiment.",
        S["corps"]
    ),

    Paragraph("La différence MP Solutions IA", S["section"]),
    Paragraph(
        "Je n'installe pas juste un chatbot : j'intègre l'IA dans votre relation "
        "client pour digitaliser et automatiser ce qui vous prend du temps — "
        "réponses, suivi, veille, reporting. Pensé pour les TPE/PME locales, pas "
        "une usine à gaz d'agence.",
        S["corps"]
    ),
    Paragraph("• Visite sur place — écoute — compréhension de l'activité.", S["corps"]),
    Paragraph("• Construction de l'outil à son image.", S["corps"]),
    Paragraph("• Un interlocuteur humain après — pas un ticket.", S["corps"]),

    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph(
        "L'artisan a le savoir-faire et l'éthique du contact. Il n'a pas le temps de "
        "répondre à tout le monde. Les grands groupes lui proposent des outils "
        "génériques qui ne parlent pas sa langue.",
        S["corps"]
    ),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Un assistant simple, honnête, à son image. Un vrai interlocuteur. Pas un call "
        "center.",
        S["corps"]
    ),

    HRFlowable(width="100%", thickness=0.5, color=GRIS_CLAIR, spaceAfter=8),

    Paragraph("-> PARLONS-EN", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia.fr — Artigat (09130)<br/>"
        "SIRET : 108 354 739 00014 — Micro-entreprise APE 62.02A<br/>"
        "TVA non applicable, art. 293 B du CGI",
        S["corps"]
    ),
    Paragraph(
        "« Écouter, comprendre, servir — en toute transparence. »",
        S["corps_bold"]
    ),
    Paragraph(
        "Vous connaissez un artisan, un commerçant, un patron de PME en Ariège ? "
        "Parlez-leur de nous.",
        S["mention"]
    ),
]

build_document(
    output_path="prospectus_mp_solutions_ia.pdf",
    title="Ce que l'homme a perdu.",
    subtitle="Ce que MP Solutions IA est venu rendre.",
    content_story=contenu,
    show_page_number=False,
)

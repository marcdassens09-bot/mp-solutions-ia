# -*- coding: utf-8 -*-
"""
MP Solutions IA — Fiche commerciale générique (2 pages)

Fusionne le prospectus philosophique (build_prospectus.py — pourquoi MP
Solutions IA, l'approche humaine) et la fiche capacités (fiche_agent_
coordinateur.py — ce que l'agent apporte concrètement) en un seul document
structuré "Docteur Commercial" :
  Page 1 : positionnement — pourquoi une IA locale et sur mesure plutôt
           qu'un outil générique de grand groupe. Se termine sur
           >> CE QUE J'OBSERVE.
  Page 2 : ++ CE QUE JE PROPOSE — ce que l'agent apporte concrètement,
           tableau des bénéfices, sécurité, comment ça marche, contact.

Document générique (pas de nom de prospect), pas de tarif (règle MP
Solutions IA : jamais de prix en première approche), section sécurité
systématique.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles, VERT, VERT_FONCE, ORANGE, BLANC, GRIS_CLAIR
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import mm

S = get_styles()
# Ni le style par défaut (pensé pour un document de 6 pages, trop aéré ici)
# ni la version resserrée du brouillon 1 page (trop dense sur 2 pages) :
# un entre-deux pour que le texte remplisse les deux pages sans les tasser.
S["section"] = S["section"].clone("section_mid", spaceBefore=13, spaceAfter=5)
S["corps"] = S["corps"].clone("corps_mid", leading=14.5, spaceAfter=6)
S["corps_bold"] = S["corps_bold"].clone("corps_bold_mid", spaceAfter=4)
S["cell_label"] = S["corps_bold"].clone("cell_label", fontSize=9.5, leading=13,
                                         textColor=BLANC, spaceAfter=0)
S["cell_corps"] = S["corps"].clone("cell_corps", fontSize=9.5, leading=13, spaceAfter=0)

contenu = [
    # ── PAGE 1 — POSITIONNEMENT ─────────────────────────────────────────
    Paragraph("Au commencement, l'homme savait", S["section"]),
    Paragraph(
        "L'homme savait lire l'autre. Sans mots. Sans écran. Un regard, un souffle, "
        "une posture suffisaient pour comprendre et agir ensemble. Cette intelligence, "
        "l'humanité l'a affinée pendant 200 000 ans.",
        S["corps"]
    ),

    Paragraph("Ce qu'on a gagné. Ce qu'on a perdu.", S["section"]),
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
            ("TOPPADDING",     (0,0), (-1,-1), 7),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 7),
            ("LEFTPADDING",    (0,0), (-1,-1), 8),
        ])
    ),
    Spacer(1, 2*mm),
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
        "Je n'installe pas seulement un chatbot sur votre site : j'intègre "
        "l'intelligence artificielle dans votre relation client pour digitaliser et "
        "automatiser ce qui vous prend du temps aujourd'hui — réponses aux visiteurs, "
        "suivi des demandes, veille, reporting. Une solution pensée pour les TPE et "
        "PME locales, pas une usine à gaz d'agence.",
        S["corps"]
    ),
    Paragraph("• Visite sur place — écoute — compréhension de l'activité.", S["corps"]),
    Paragraph("• Construction de l'outil à son image.", S["corps"]),
    Paragraph("• Un interlocuteur humain après — pas un ticket.", S["corps"]),

    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph(
        "Dans une TPE ou une PME, la même question revient dix fois par semaine — "
        "horaires, tarifs, disponibilités — et personne n'a le temps d'y répondre "
        "instantanément à toute heure. Résultat : des clients qui attendent, ou qui "
        "vont voir ailleurs.",
        S["corps"]
    ),

    PageBreak(),

    # ── PAGE 2 — CE QUE ÇA APPORTE CONCRÈTEMENT ─────────────────────────
    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "La plupart des chatbots se contentent de répondre à une question avec ce qu'ils "
        "savent déjà. Un agent va plus loin : il coordonne — il peut vérifier une "
        "information avant de répondre, transmettre une demande, signaler ce qui est "
        "urgent. C'est cette différence qui change ce qu'il apporte à votre entreprise.",
        S["corps"]
    ),

    Table(
        [
            [Paragraph("Disponible 24h/24", S["cell_label"]),
             Paragraph("Répond aux questions courantes même le soir, le week-end, "
             "hors saison — sans que vous ou votre équipe soyez mobilisés.", S["cell_corps"])],
            [Paragraph("Formé à votre métier", S["cell_label"]),
             Paragraph("Pas une réponse générique : vos horaires, vos produits, "
             "vos conditions, votre façon de parler à vos clients.", S["cell_corps"])],
            [Paragraph("Recueille les demandes", S["cell_label"]),
             Paragraph("Un client écrit hors des heures d'ouverture ? Le message "
             "est structuré et vous revient par email, rien ne se perd.", S["cell_corps"])],
            [Paragraph("Sait passer la main", S["cell_label"]),
             Paragraph("Dès que la question dépasse ce qu'il sait, il oriente vers "
             "vous plutôt que d'inventer une réponse.", S["cell_corps"])],
            [Paragraph("Coordonne, pas juste répond", S["cell_label"]),
             Paragraph("Il peut consulter une autre source avant de répondre "
             "(disponibilités, catalogue) et déclencher une action plutôt que de rester "
             "une simple FAQ.", S["cell_corps"])],
            [Paragraph("Évolue avec vous", S["cell_label"]),
             Paragraph("Nouveau produit, nouvelle question fréquente : l'agent "
             "s'actualise, il ne reste pas figé au jour de sa mise en ligne.", S["cell_corps"])],
        ],
        colWidths=[45*mm, 125*mm],
        style=TableStyle([
            ("BACKGROUND",     (0,0), (0,-1), VERT),
            ("TEXTCOLOR",      (0,0), (0,-1), BLANC),
            ("FONTNAME",       (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE",       (0,0), (-1,-1), 9.5),
            ("ROWBACKGROUNDS", (1,0), (1,-1), [BLANC, GRIS_CLAIR]),
            ("GRID",           (0,0), (-1,-1), 0.5, colors.HexColor("#DDDDDD")),
            ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",     (0,0), (-1,-1), 7),
            ("BOTTOMPADDING",  (0,0), (-1,-1), 7),
            ("LEFTPADDING",    (0,0), (-1,-1), 6),
            ("RIGHTPADDING",   (0,0), (-1,-1), 6),
        ])
    ),
    Spacer(1, 2*mm),

    Paragraph("Sécurité et confidentialité", S["section"]),
    Paragraph(
        "• Vos visiteurs savent toujours qu'ils parlent à un assistant IA, jamais un "
        "trompe-l'œil (obligation légale respectée dès la conception). "
        "• Les données sensibles tapées par erreur (carte bancaire, email, téléphone) "
        "sont automatiquement masquées avant d'être conservées. "
        "• Protection anti-abus intégrée (limite de requêtes, détection de tentatives "
        "de détournement). "
        "• Connexion sécurisée (HTTPS), conformité RGPD dès la mise en service.",
        S["corps"]
    ),

    Paragraph("Comment ça marche", S["section"]),
    Paragraph(
        "1. On échange sur votre activité — vos questions fréquentes, votre ton, vos "
        "clients. 2. Je construis l'agent à votre image, pas un modèle générique. "
        "3. Mise en ligne sur votre site. 4. Suivi mensuel : ajustements, mises à jour, "
        "évolutions.",
        S["corps"]
    ),

    HRFlowable(width="100%", thickness=0.5, color=GRIS_CLAIR, spaceBefore=8, spaceAfter=9),

    Paragraph("-> PARLONS-EN", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — MP Solutions IA — Artigat (09130)<br/>"
        "contact@mpsolutionsia.fr — mpsolutionsia.fr<br/>"
        "SIRET 108 354 739 00014 — Micro-entreprise — TVA non applicable, art. 293 B du CGI",
        S["corps"]
    ),
    Paragraph(
        "« Écouter, comprendre, servir — en toute transparence. »",
        S["corps_bold"]
    ),
]

build_document(
    output_path=os.path.join(os.path.dirname(__file__), "fiche_commerciale_generique.pdf"),
    title="Un agent qui coordonne, pas un chatbot qui répond.",
    subtitle="Pourquoi MP Solutions IA, et ce que l'agent apporte à votre TPE ou PME",
    content_story=contenu,
)

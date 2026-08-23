# -*- coding: utf-8 -*-
"""
MP Solutions IA — Dossier de présentation
Prospect : MSP Le Fossat (Maison de Santé Pluriprofessionnelle, 09130)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from mp_template import build_document, get_styles, VERT, BLANC, GRIS_CLAIR
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib import colors
from reportlab.lib.units import mm

S = get_styles()
S["section"] = S["section"].clone("section_c", spaceBefore=14, spaceAfter=6)
S["corps"] = S["corps"].clone("corps_c", fontSize=10, leading=15, spaceAfter=6)
S["corps_bold"] = S["corps_bold"].clone("corps_bold_c", fontSize=10, leading=14, spaceAfter=4)

contenu = [
    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph(
        "Treize catégories de professionnels sous le même toit — médecins "
        "généralistes, infirmiers libéraux et ASALEE, kinésithérapeutes, "
        "sages-femmes, psychologues, psychomotricienne, orthophoniste, "
        "diététicienne-tabacologue, enseignant en activité physique "
        "adaptée, neuropsychologue, ostéopathe, audio-prothésiste. C'est "
        "une vraie richesse pour vos patients, mais aussi beaucoup de "
        "questions similaires qui reviennent au secrétariat ou à chaque "
        "cabinet : qui fait quoi, quels horaires, faut-il un RDV, "
        "quelle prise en charge. Le site msp-lefossat.fr présente bien "
        "l'équipe mais n'a ni FAQ ni formulaire de contact — un visiteur "
        "doit encore chercher la bonne page ou appeler pour se situer.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Je n'installe pas seulement un chatbot : j'intègre l'IA dans votre "
        "relation avec vos patients pour digitaliser ce qui vous prend du "
        "temps, en commençant par un chatbot installé sur msp-lefossat.fr "
        "qui oriente immédiatement chaque visiteur vers le bon "
        "professionnel parmi les treize, répond aux questions pratiques "
        "qui reviennent tout le temps (horaires, secteur, prise en "
        "charge, comment prendre RDV) et vous transmet uniquement les "
        "demandes qui nécessitent un vrai contact humain. Un seul outil "
        "pour toute la structure, plutôt qu'une solution par cabinet.",
        S["corps"]
    ),
    Spacer(1, 5*mm),

    Paragraph(">> DONNÉES DE SANTÉ — UNE RÈGLE À PART", S["section"]),
    Paragraph(
        "Les données de santé sont une catégorie particulière de données "
        "personnelles (article 9 du RGPD), avec un niveau de protection "
        "renforcé. Le chatbot que je livre est construit pour ne jamais y "
        "toucher : il ne pose aucune question médicale, ne demande ni "
        "symptôme ni pathologie ni traitement, et n'accède à aucun dossier "
        "patient. Son rôle s'arrête au pratique — quel professionnel "
        "consulter, quels horaires, comment prendre RDV — jamais au "
        "médical. Tout ce qui relève du soin reste entre vos mains et "
        "celles de vos patients.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph(">> CONFORMITÉ — CE QUE DIT LA LOI DEPUIS LE 2 AOÛT 2026", S["section"]),
    Paragraph(
        "Depuis le 2 août 2026, le règlement (UE) 2024/1689 sur l'IA (AI Act), "
        "article 50, impose d'informer le visiteur dès le premier échange "
        "qu'il parle à une IA, et d'organiser un relais vers vous pour toute "
        "situation personnelle. Ce que je livre respecte ce point par "
        "construction : identification IA dès le premier message, et un "
        "chatbot qui n'engage rien, ne diagnostique rien, ne remplace "
        "aucun professionnel — il informe et oriente pour le reste.",
        S["corps"]
    ),
    PageBreak(),

    Paragraph("Sécurité et données", S["corps_bold"]),
    Paragraph(
        "Le chatbot n'a accès à rien d'autre qu'à ce qu'on lui configure : "
        "pas d'accès à vos dossiers patients, votre messagerie ou vos "
        "outils, aucune capacité à modifier ou supprimer une donnée de son "
        "côté. Un registre des traitements RGPD existe et une politique de "
        "confidentialité est publiée ; les données collectées auprès des "
        "visiteurs (nom, contact) sont limitées au strict nécessaire, et "
        "les informations sensibles sont masquées dans les journaux "
        "techniques. Droit à l'effacement (RGPD, article 17) : tout "
        "visiteur peut demander la suppression de ses données, à vous ou "
        "à moi directement — la demande est traitée sous un mois, comme "
        "l'exige la loi.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Comment ça marche", S["section"]),
    Paragraph(
        "● Un visiteur pose une question sur votre site, à tout moment ; le "
        "chatbot répond à partir des informations réelles de votre "
        "structure (équipe, horaires, secteur) et oriente vers le bon "
        "professionnel ou vers le secrétariat pour tout RDV — sans jamais "
        "inventer d'information ni aborder le médical.",
        S["corps"]
    ),
    Paragraph(
        "● Vous gardez la main : le contenu est configuré avec vous, à "
        "partir de ce que vous savez de votre organisation — pas d'un "
        "paramétrage générique.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Installation en 4 étapes", S["section"]),
    Paragraph("1. Questionnaire technique (équipe, horaires, FAQ, ton souhaité)", S["corps"]),
    Paragraph("2. Configuration du chatbot", S["corps"]),
    Paragraph("3. Intégration sur msp-lefossat.fr", S["corps"]),
    Paragraph("4. Mise en service et suivi mensuel", S["corps"]),
    Spacer(1, 5*mm),

    Paragraph("Prochaine étape", S["section"]),
    Paragraph(
        "Ce document est une première approche, sans tarif ni engagement : "
        "l'objectif est d'abord de voir ensemble si l'idée vous parle. Si "
        "c'est le cas, on se retrouve pour un échange rapide sur vos "
        "questions les plus fréquentes et le fonctionnement de la MSP, et "
        "je reviens vers vous avec une proposition chiffrée adaptée.",
        S["corps"]
    ),
    Spacer(1, 8*mm),
    Paragraph("-> MP Solutions IA", S["section"]),
    Paragraph(
        "Marc-Paul Dassens — mpsolutionsia@gmail.com — Artigat (09130)<br/>"
        "«Écouter, comprendre, servir — en toute transparence.»",
        S["corps"]
    ),
]

if __name__ == "__main__":
    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_msp_le_fossat.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : MSP Le Fossat — Maison de Santé Pluriprofessionnelle",
        content_story=contenu,
    )

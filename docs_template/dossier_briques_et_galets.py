# -*- coding: utf-8 -*-
"""
MP Solutions IA — Dossier de présentation
Prospect : Briques et Galets (Lézat-sur-Lèze, 09210)
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
        "Vous avez déjà un site, briquesetgalets-lezat.fr : cinq prestations "
        "bien présentées (maçonnerie, couverture, isolation, électricité, "
        "photovoltaïque) avec une description détaillée de chacune. Mais "
        "il manque les éléments qui font gagner du temps au quotidien : pas "
        "d'horaires affichés, pas de FAQ, et le formulaire de contact "
        "n'est pas directement accessible depuis les pages de prestations. "
        "Un visiteur qui a une question précise — délai, aides RGE, zone "
        "d'intervention — doit chercher ou attendre un rappel.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph(
        "Je n'installe pas seulement un chatbot : j'intègre l'IA dans votre "
        "relation client pour digitaliser ce qui vous prend du temps, en "
        "commençant par un chatbot branché sur votre site existant, qui "
        "répond à toute heure aux questions qui reviennent tout le temps : "
        "zone d'intervention, délais habituels, déroulé d'une demande de "
        "devis, éligibilité aux aides RGE pour l'isolation ou le "
        "photovoltaïque. Il qualifie la demande avant qu'elle arrive "
        "jusqu'à vous, et vous transmet uniquement les contacts sérieux.",
        S["corps"]
    ),
    Spacer(1, 5*mm),

    Paragraph(">> CONFORMITÉ — CE QUE DIT LA LOI DEPUIS LE 2 AOÛT 2026", S["section"]),
    Paragraph(
        "Depuis le 2 août 2026, le règlement (UE) 2024/1689 sur l'IA (AI Act), "
        "article 50, impose d'informer le visiteur dès le premier échange "
        "qu'il parle à une IA, et d'organiser un relais vers vous pour toute "
        "négociation, réclamation ou situation personnelle. Ce que je livre "
        "respecte ce point par construction : identification IA dès le "
        "premier message, et un chatbot qui ne négocie rien, ne s'engage sur "
        "rien à votre place — il informe et oriente vers vous pour le reste.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Sécurité et données", S["corps_bold"]),
    Paragraph(
        "Le chatbot n'a accès à rien d'autre qu'à ce qu'on lui configure : "
        "pas d'accès à votre site, votre messagerie ou vos outils, aucune "
        "capacité à modifier ou supprimer une donnée de son côté — il "
        "informe, il ne peut pas agir sur vos systèmes. Comme sur l'ensemble "
        "des chatbots que j'opère, un registre des traitements RGPD existe "
        "et une politique de confidentialité est publiée ; les données "
        "collectées auprès des visiteurs (nom, contact) sont limitées au "
        "strict nécessaire, et les informations sensibles sont masquées "
        "dans les journaux techniques. Droit à l'effacement (RGPD, article "
        "17) : tout visiteur peut demander la suppression de ses données, à "
        "vous ou à moi directement — la demande est traitée sous un mois, "
        "comme l'exige la loi.",
        S["corps"]
    ),
    PageBreak(),

    Paragraph("Comment ça marche", S["section"]),
    Paragraph(
        "● Un visiteur pose une question sur votre site, à tout moment ; le "
        "chatbot répond à partir des informations réelles de votre activité "
        "(prestations, zone d'intervention, aides RGE) et oriente vers vous "
        "pour tout devis précis — sans jamais inventer d'information.",
        S["corps"]
    ),
    Paragraph(
        "● Vous gardez la main : le contenu est configuré avec vous, à "
        "partir de ce que vous savez de votre activité — pas d'un "
        "paramétrage générique.",
        S["corps"]
    ),
    Spacer(1, 4*mm),

    Paragraph("Installation en 4 étapes", S["section"]),
    Paragraph("1. Questionnaire technique (horaires, prestations, FAQ, ton souhaité)", S["corps"]),
    Paragraph("2. Configuration du chatbot", S["corps"]),
    Paragraph("3. Intégration sur briquesetgalets-lezat.fr", S["corps"]),
    Paragraph("4. Mise en service et suivi mensuel", S["corps"]),
    Spacer(1, 5*mm),

    Paragraph("Prochaine étape", S["section"]),
    Paragraph(
        "Ce document est une première approche, sans tarif ni engagement : "
        "l'objectif est d'abord de voir ensemble si l'idée vous parle. Si "
        "c'est le cas, on se retrouve pour un échange rapide sur vos "
        "questions les plus fréquentes et votre façon de travailler, et je "
        "reviens vers vous avec une proposition chiffrée adaptée à votre "
        "activité.",
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
        output_path="C:/Projets/mp-solutions-ia/docs_template/dossier_briques_et_galets.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : Briques et Galets — Maçonnerie, couverture, isolation",
        content_story=contenu,
    )

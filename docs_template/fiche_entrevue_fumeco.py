"""MP Solutions IA — Fiche d'entrevue (étape 1, document interne). Prospect : FUMECO-LEZE, Artigat."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy import deepcopy
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib import colors
from reportlab.lib.units import mm
from mp_template import build_document, get_styles

# Polices DejaVu (accents français, ● ▸ ✓) : chemins Linux, Windows, ou dossier du script.
_DIRS = ["/usr/share/fonts/truetype/dejavu/", "C:/Windows/Fonts/", os.path.dirname(os.path.abspath(__file__)) + "/"]
def _police(nom, fichier):
    for d in _DIRS:
        if os.path.exists(d + fichier):
            pdfmetrics.registerFont(TTFont(nom, d + fichier))
            return True
    return False
if not (_police("DejaVu", "DejaVuSans.ttf") and _police("DejaVu-Bold", "DejaVuSans-Bold.ttf")):
    raise SystemExit("DejaVuSans.ttf / DejaVuSans-Bold.ttf introuvables : les copier à côté du script.")

S = get_styles()
for k, f in (("titre_doc","DejaVu-Bold"),("sous_titre","DejaVu"),("section","DejaVu-Bold"),
             ("corps","DejaVu"),("corps_bold","DejaVu-Bold"),("mention","DejaVu")):
    S[k] = deepcopy(S[k]); S[k].fontName = f
S["corps"].fontSize = 9.3; S["corps"].leading = 14; S["corps"].spaceAfter = 3
S["corps_bold"].fontSize = 9.3; S["corps_bold"].leading = 14; S["corps_bold"].spaceBefore = 5; S["corps_bold"].spaceAfter = 2
S["section"].spaceBefore = 10; S["section"].spaceAfter = 5

def ligne(n=1, h=15):
    return [HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#BBBBBB"),
                       spaceBefore=h, spaceAfter=0) for _ in range(n)]

def q(texte, n=1, h=19):
    return [Paragraph("▸ " + texte, S["corps_bold"])] + ligne(n, h) + [Spacer(1, 2*mm)]

contenu = [
    Paragraph("Date de l'entrevue : ____ / ____ / ________ &nbsp;&nbsp;&nbsp; Avec : Thomas Fournial, "
              "Président &nbsp;&nbsp;&nbsp; Lieu : Artigat", S["corps"]),

    Paragraph(">> CE QUE J'AI OBSERVÉ AVANT LA VISITE", S["section"]),
    Paragraph("● Trois lignes téléphoniques (standard, distribution, chantier) et un formulaire, du "
              "lundi au vendredi, 9h-12h et 13h30-17h.", S["corps"]),
    Paragraph("● Trois publics (particuliers, professionnels, collectivités) et un large catalogue.", S["corps"]),
    Paragraph("● Pas de FAQ ni d'assistant en ligne sur fumeco.fr. À confirmer avec lui : ce sont "
              "mes observations, pas des certitudes.", S["corps"]),

    Paragraph("++ LES QUESTIONS À POSER — j'écoute avant de proposer", S["section"]),
    Paragraph("L'accueil et les appels", S["corps_bold"]),
    *q("Combien d'appels par semaine sur vos trois lignes ?", 2),
    *q("Qui décroche aujourd'hui, et combien de temps cela lui prend-il ?", 3),
    *q("Combien d'appels arrivent au mauvais numéro ?", 3),
    Paragraph("Hors horaires et périodes de pointe", S["corps_bold"]),
    *q("Que deviennent les demandes du soir et du week-end ? Les mesurez-vous ?", 3),
    *q("Quelles sont les périodes les plus chargées de l'année ?", 3),
    PageBreak(),

    Paragraph("++ LES QUESTIONS À POSER (suite)", S["section"]),
    Paragraph("Les trois publics", S["corps_bold"]),
    *q("Les questions qui reviennent le plus : particuliers ?", 2),
    *q("Professionnels ?", 1),
    *q("Collectivités ?", 1),
    *q("Quelles demandes prennent le plus de temps à votre équipe ?", 1),
    Paragraph("Le site et la présence en ligne", S["corps_bold"]),
    *q("Qui gère fumeco.fr aujourd'hui ? Peut-on y ajouter un assistant ?", 1),
    Paragraph("Les contraintes", S["corps_bold"]),
    *q("Budget, calendrier : quelles limites ? Qui décide, avec qui ?", 2),

    Paragraph("-> ROI À REMPLIR ENSEMBLE", S["section"]),
    Paragraph("Appels et demandes par semaine : ______ &nbsp;×&nbsp; minutes par réponse : ______ "
              "&nbsp;=&nbsp; ______ h", S["corps"]),
    Spacer(1, 2*mm),
    Paragraph("Heures par semaine : ______ &nbsp;×&nbsp; valeur horaire de l'équipe : ______ € "
              "&nbsp;=&nbsp; ______ €", S["corps"]),
    Spacer(1, 2*mm),
    Paragraph("Demandes perdues hors horaires, par semaine : ______", S["corps"]),

    Paragraph("-> CE QUE JE RETIENS", S["section"]),
    Paragraph("Ce qui lui a parlé le plus :", S["corps"]), *ligne(2, 14),
    Spacer(1, 2*mm),
    Paragraph("Prochaine étape convenue :", S["corps"]), *ligne(2, 14),
    Spacer(1, 4*mm),
    Paragraph("Document interne — ne pas remettre au prospect", S["mention"]),
]

if __name__ == "__main__":
    build_document(output_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "fiche_entrevue_fumeco.pdf"),
        title="Fiche d'entrevue", subtitle="FUMECO-LEZE — Thomas Fournial — Artigat (09130)",
        content_story=contenu, show_page_number=False)

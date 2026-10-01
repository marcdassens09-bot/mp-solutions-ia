"""MP Solutions IA — Premier contact (découverte, sans tarif). Prospect : FUMECO-LEZE, Artigat."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy import deepcopy
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Spacer
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
S["corps"].fontSize = 10; S["corps"].leading = 17; S["corps"].spaceAfter = 9
S["section"].spaceBefore = 17; S["section"].spaceAfter = 6

contenu = [
    Paragraph("Bonjour Monsieur Fournial, ce document fait suite à mon message du 17 août. "
              "Je suis votre voisin à Artigat : voici, en une page, ce que j'observe et ce que "
              "je pourrais vous proposer.", S["corps"]),

    Paragraph(">> CE QUE J'OBSERVE", S["section"]),
    Paragraph("▸ L'accueil repose sur trois lignes téléphoniques et un formulaire, joignables du "
              "lundi au vendredi, 9h-12h et 13h30-17h. Une demande arrivée le soir ou le "
              "week-end attend le lundi.", S["corps"]),
    Paragraph("▸ Trois publics — particuliers, professionnels, collectivités — et un large "
              "catalogue : les questions reviennent, mais ne sont pas les mêmes d'un public à "
              "l'autre (disponibilité, certification UAB, livraison, zones desservies).", S["corps"]),
    Paragraph("▸ Pas de FAQ ni d'assistant en ligne sur fumeco.fr : hors horaires, le visiteur "
              "ne trouve qu'un formulaire.", S["corps"]),

    Paragraph("++ CE QUE JE PROPOSE", S["section"]),
    Paragraph("Je n'installe pas seulement un chatbot : j'intègre l'IA dans votre relation client "
              "comme un agent qui coordonne. Sur fumeco.fr, il répond en continu à partir de vos "
              "informations réelles, vérifie avant de répondre plutôt que d'inventer, transmet "
              "chaque demande au bon contact — distribution, chantier ou standard — et signale ce "
              "qui est urgent.", S["corps"]),
    Paragraph("✓ Une réponse immédiate le soir et le week-end, au lieu d'un formulaire en attente.", S["corps"]),
    Paragraph("✓ Chaque public orienté vers le bon interlocuteur, moins d'appels au mauvais numéro.", S["corps"]),
    Paragraph("✓ Vous gardez la main : le contenu est configuré avec vous, rien n'est mis en ligne "
              "sans votre validation.", S["corps"]),

    Paragraph("-> PROCHAINE ÉTAPE", S["section"]),
    Paragraph("Si ce courrier vous parle, je passe vous voir à votre entreprise : "
              "15 minutes suffisent pour comprendre vos besoins réels "
              "— questions les plus fréquentes, périodes de pointe, ce qui vous prend du temps "
              "aujourd'hui. C'est après cet échange que je vous ferai une proposition chiffrée "
              "adaptée — rien n'est figé avant.", S["corps"]),
    Spacer(1, 4*mm),
    Paragraph("-> MP Solutions IA", S["section"]),
    Paragraph("Marc-Paul Dassens — 06 44 00 22 52 — contact@mpsolutionsia.fr — Artigat (09130)", S["corps"]),
]

if __name__ == "__main__":
    build_document(output_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "premier_contact_fumeco.pdf"),
        title="Premier contact", subtitle="FUMECO-LEZE — Artigat (09130)", content_story=contenu, show_page_number=False)

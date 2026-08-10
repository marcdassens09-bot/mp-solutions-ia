"""
MP Solutions IA — Template de document professionnel
Charte graphique : vert #1F7A4D / dark green #1b3a2b / orange #E8730A
Utilisation : importer ce fichier et appeler build_document()
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen.canvas import Canvas
import os

# ─────────────────────────────────────────────
# CHARTE GRAPHIQUE MP SOLUTIONS IA
# ─────────────────────────────────────────────
VERT         = colors.HexColor("#1F7A4D")
VERT_FONCE   = colors.HexColor("#1b3a2b")
ORANGE       = colors.HexColor("#E8730A")
GRIS_CLAIR   = colors.HexColor("#F5F5F5")
GRIS_TEXTE   = colors.HexColor("#333333")
BLANC        = colors.white

W, H = A4  # 210 x 297 mm

MARGIN_LEFT   = 20 * mm
MARGIN_RIGHT  = 20 * mm
MARGIN_TOP    = 42 * mm
MARGIN_BOTTOM = 25 * mm

# Chemin du logo — à adapter si tu déplaces le fichier
LOGO_PATH = os.path.join(os.path.dirname(__file__), "logo_complet.png")

# Icône ronde (nouveau logo), utilisée uniquement dans le header de la page 1
LOGO_ICONE_PATH = os.path.join(os.path.dirname(__file__), "logo_icone.jpg")

# ─────────────────────────────────────────────
# STYLES TYPOGRAPHIQUES
# ─────────────────────────────────────────────
def get_styles():
    return {
        "titre_doc": ParagraphStyle(
            "titre_doc",
            fontName="Helvetica-Bold",
            fontSize=18,
            textColor=VERT_FONCE,
            spaceAfter=10,
            alignment=TA_LEFT,
        ),
        "sous_titre": ParagraphStyle(
            "sous_titre",
            fontName="Helvetica",
            fontSize=11,
            textColor=ORANGE,
            spaceAfter=16,
            alignment=TA_LEFT,
        ),
        "section": ParagraphStyle(
            "section",
            fontName="Helvetica-Bold",
            fontSize=12,
            textColor=VERT,
            spaceBefore=22,
            spaceAfter=8,
            alignment=TA_LEFT,
        ),
        "corps": ParagraphStyle(
            "corps",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRIS_TEXTE,
            leading=17,
            spaceAfter=10,
            alignment=TA_LEFT,
        ),
        "corps_bold": ParagraphStyle(
            "corps_bold",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=GRIS_TEXTE,
            leading=15,
            spaceAfter=4,
        ),
        "mention": ParagraphStyle(
            "mention",
            fontName="Helvetica-Oblique",
            fontSize=8,
            textColor=colors.HexColor("#888888"),
            alignment=TA_CENTER,
        ),
    }

# ─────────────────────────────────────────────
# HEADER avec logo
# ─────────────────────────────────────────────
def draw_header(c, doc, first_page=False):
    c.saveState()

    # Bande verte foncée en haut
    c.setFillColor(VERT_FONCE)
    c.rect(0, H - 28*mm, W, 28*mm, fill=1, stroke=0)

    # Logo complet désactivé : le fichier logo_complet.png est corrompu
    # (mélangé avec un autre document, cf. mémoire projet). En attendant un
    # fichier propre, on garde le texte de secours seul.
    c.setFillColor(BLANC)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(MARGIN_LEFT, H - 12*mm, "MP Solutions IA")

    # Icône ronde — uniquement en page 1, coin supérieur droit du bandeau
    if first_page and os.path.exists(LOGO_ICONE_PATH):
        icone_size = 12 * mm
        c.drawImage(
            LOGO_ICONE_PATH,
            W - MARGIN_RIGHT - icone_size,
            H - 2*mm - icone_size,
            width=icone_size,
            height=icone_size,
            preserveAspectRatio=True,
        )

    # Coordonnées à droite
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#CCCCCC"))
    contact_lines = [
        "Marc-Paul Dassens",
        "Artigat — 09130 Ariège",
        "contact@mpsolutionsia.fr",
    ]
    y_contact = H - 16*mm if first_page else H - 9*mm
    for line in contact_lines:
        c.drawRightString(W - MARGIN_RIGHT, y_contact, line)
        y_contact -= 4.5*mm

    # Ligne orange de séparation
    c.setStrokeColor(ORANGE)
    c.setLineWidth(2)
    c.line(MARGIN_LEFT, H - 30*mm, W - MARGIN_RIGHT, H - 30*mm)

    c.restoreState()

# ─────────────────────────────────────────────
# NUMÉRO DE PAGE — format « x/y » (page courante / total)
# ─────────────────────────────────────────────
# ReportLab ne connaît le nombre total de pages qu'une fois le document entier
# construit : on bufferise chaque page dans showPage() et on n'écrit le numéro
# qu'au moment de save(), quand le total est enfin connu (technique standard
# dite "NumberedCanvas").
class NumberedCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_page_number(total_pages)
            Canvas.showPage(self)
        Canvas.save(self)

    def _draw_page_number(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#888888"))
        self.drawRightString(W - MARGIN_RIGHT, 13*mm, f"{self._pageNumber}/{total_pages}")
        self.restoreState()

# ─────────────────────────────────────────────
# CONSTRUCTION DU DOCUMENT
# ─────────────────────────────────────────────
def build_document(output_path, title, subtitle, content_story, show_page_number=True):
    def on_first_page(c, doc):
        draw_header(c, doc, first_page=True)

    def on_later_pages(c, doc):
        draw_header(c, doc, first_page=False)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title=title,
        author="MP Solutions IA",
    )

    S = get_styles()
    story = []
    story.append(Paragraph(title, S["titre_doc"]))
    story.append(Paragraph(subtitle, S["sous_titre"]))
    story.append(HRFlowable(width="100%", thickness=1, color=GRIS_CLAIR, spaceAfter=8))
    story += content_story

    doc.build(
        story,
        onFirstPage=on_first_page,
        onLaterPages=on_later_pages,
        canvasmaker=NumberedCanvas if show_page_number else Canvas,
    )
    print(f"PDF généré : {output_path}")


# ─────────────────────────────────────────────
# TEST
# ─────────────────────────────────────────────
if __name__ == "__main__":
    S = get_styles()

    contenu = [
        Paragraph("Présentation", S["section"]),
        Paragraph(
            "MP Solutions IA conçoit des chatbots intelligents sur mesure pour les artisans "
            "et les petites entreprises. Notre approche : écouter d'abord, proposer ensuite.",
            S["corps"]
        ),
        Spacer(1, 12*mm),

        Paragraph("Ce que nous proposons", S["section"]),
        Paragraph("• Chatbot IA personnalisé à votre activité", S["corps"]),
        Paragraph("• Intégration sur votre site WordPress ou vitrine", S["corps"]),
        Paragraph("• Disponible 24h/24 pour répondre à vos clients", S["corps"]),
        Paragraph("• Accompagnement complet, sans jargon", S["corps"]),
        Spacer(1, 12*mm),

        Paragraph("Tarifs", S["section"]),
        Table(
            [
                ["Prestation", "Détail", "Tarif"],
                ["Installation", "Chatbot complet + intégration site", "Sur devis"],
                ["Maintenance", "Suivi mensuel + mises à jour", "Sur devis"],
            ],
            colWidths=[50*mm, 80*mm, 40*mm],
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
        Spacer(1, 16*mm),
        Paragraph(
            "Document confidentiel — MP Solutions IA — contact@mpsolutionsia.fr",
            S["mention"]
        ),
    ]

    build_document(
        output_path="C:/Projets/mp-solutions-ia/docs_template/test_template.pdf",
        title="Dossier de présentation",
        subtitle="Prospect : Maxime Moucheron — Full Habitat EURL",
        content_story=contenu,
    )

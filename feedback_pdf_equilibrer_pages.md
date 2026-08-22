# Feedback — équilibrer les pages d'un dossier PDF (mp-pdf-template)

Constat sur `dossier_pons.py` (campagne BTP Artigat, août 2026) : après retrait
du paragraphe de tarif de première approche, le texte restant ne suffisait
plus à remplir une deuxième page — un `PageBreak` forcé laissait un grand
blanc en bas de la dernière page.

**Règle : jamais de grand blanc en bas de la dernière page d'un dossier PDF.**
Resserrer plutôt que déborder.

En pratique, avant d'ajouter un `PageBreak` ou de laisser un contenu couler
sur une deuxième page :
1. Essayer d'abord de tout faire tenir sur une seule page.
2. Resserrer les styles *localement au fichier du dossier* (jamais dans
   `mp_template.py`, qui reste le socle commun) : réduire `leading` et
   `spaceAfter` de `S["corps"]`, réduire `spaceBefore`/`spaceAfter` de
   `S["section"]`, réduire les `Spacer` intermédiaires.
3. Si malgré ça le contenu déborde sur une deuxième page, vérifier qu'elle
   est remplie de façon équilibrée (pas juste une ou deux lignes perdues en
   haut d'une page presque vide) — sinon continuer à resserrer ou raccourcir
   le texte plutôt que de livrer tel quel.

Toujours repasser par le process de validation du skill `mp-pdf-template`
(génération → aperçu image → zoom header/footer → "go" de Marc-Paul → livraison)
après un resserrage, pour confirmer que rien n'a cassé la charte graphique.

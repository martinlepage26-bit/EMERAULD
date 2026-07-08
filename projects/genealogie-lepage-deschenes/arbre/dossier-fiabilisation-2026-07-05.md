---
type: project-mirror
title: Fiabilisation Lepage / Deschênes — dossier de session
tags:
- project-mirror
- projects
- genealogie-lepage-deschenes
status: active
created: '2026-07-05'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/genealogie-lepage-deschenes/arbre/dossier-fiabilisation-2026-07-05.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Fiabilisation Lepage / Deschênes — dossier de session

**Date** 2026-07-05 · **Propositus** Martin Lepage · **Méthode** trace-investigator (audit des niveaux de certitude) → family-tree (données corrigées + plan résiduel), rendu gothique-victorien sous frontend-design.

---

## 1. Résumé de recherche

La session du 2026-07-01 avait déjà épuisé la recherche web générale sur les deux verrous documentaires, avec douze angles consignés. Une requête de contrôle indépendante le 2026-07-05 reproduit exactement le même plafond : les moteurs ne renvoient que du bruit d'agrégateurs nécrologiques et des Lepage de France, rien sur les individus du Saguenay. **Aucun ancêtre nouveau n'est récupérable par recherche web ; aucune filiation n'a été inventée.** Les deux verrous restent ouverts.

Ce qui a été fait n'est donc pas une extension (impossible ici) mais un **audit de fiabilité** du paquet documentaire. Il en ressort une correction de fond (une fourchette de naissance indûment resserrée), quatre liens de source à formaliser, et la confirmation que la structure de juin 2026 — une fois corrigée l'erreur Marcel Lalancette le 2026-07-01 — est saine. La remontée s'arrête à la génération G4 (arrière-grands-parents) sur les deux branches maternelles documentées (Bouchard→Delphis/Eva ; Tremblay→Johnny/Émilie) et bute sur l'inconnu pour les deux branches paternelles des grands-parents (parents de Gérard Lepage ; parents de Lionel Deschênes).

Portée : 59 individus, 19 familles, 6 sources (S1–S5 avis de décès quasi-primaires ; S6 arbre collaboratif utilisé uniquement pour **écarter** une hypothèse).

---

## 2. Données corrigées (registre par certitude)

Niveaux : **✦ Vérifié** (avis de décès) · **◐ Déduit/estimé** · **✕ Inconnu (verrou / non rattaché)**.

| id | Nom | Naiss. | Décès | Parents | Certitude | Source |
|----|-----|--------|-------|---------|-----------|--------|
| I1 | Martin Lepage (propositus) | — | — | Jocelyn × Édith | ✦ | S1 |
| I2 | Jocelyn Lepage | v. 1952 | 17 mai 2013 | Gérard × Germaine | ✦ décès / ◐ naiss. | S1 |
| I3 | Édith Deschênes | v. 1953 | vivante (2026) | Lionel × Laurette | ◐ (survie via S4) | S4 |
| I4 | Patricia Lepage | — | — | Jocelyn × Édith | ✦ | S1 |
| I6 | Martine Lepage | — | — | Jocelyn × Édith | ✦ | S1 |
| I8 | Sylvie Bolduc | — | — | — | ◐ (conjointe 2013) | S1 |
| I9 | Marcel Lalancette | — | — | — | ✦ (beau-père, 0 filiation) | Martin, 2026-07-01 |
| I10 | **Gérard Lepage** | **entre 1910 et 1925** | avant 2013 | **INCONNUS** | ✕ verrou | S6 (hyp. écartée) |
| I11 | Germaine Bouchard | 3 mai 1920 | 9 mars 2013 | Delphis Bouchard × Eva Chayer | ✦ | S3 |
| I12 | Gérald Lepage | v. 1946 | 31 août 2018 | Gérard × Germaine | ✦ | S2 |
| I13 | Hélène Imbeault | — | — | — | ✦ | S2 |
| I14 | Roger Lepage | — | vivant 2018 | Gérard × Germaine | ◐ | S2 |
| I15 | Delphis Bouchard | — | — | — | ✦ | S3 |
| I16 | Eva Chayer | — | — | — | ✦ | S3 |
| I23 | **Lionel Deschênes** | — | avant 2019 | **INCONNUS** | ✕ verrou | S6 (pistes écartées) |
| I24 | Laurette Tremblay | — | avant 2019 | Johnny Tremblay × Émilie Vézina | ✦ (parents) | S5 |
| I25 | Jean-Eudes Deschênes | 28 oct. 1944 | 21 sept. 2019 | Lionel × Laurette | ✦ | S4 |
| I27 | Claudette Deschênes | — | — | Lionel × Laurette | ✦ | S4 |
| I29 | Christiane Deschênes | — | — | Lionel × Laurette | ✦ (0 enfant) | S4 |
| I31 | Francine Deschênes | — | — | Lionel × Laurette | ✦ | S4 |
| I33 | Réal Deschênes | — | — | Lionel × Laurette | ✦ | S4 |
| I35 | Johnny Tremblay | — | — | — | ✦ | S5 |
| I36 | Émilie Vézina | — | — | — | ✦ | S5 |
| I37–I47 | cousins (lignes Gérald / Jean-Eudes / Claudette / Francine / Réal) | — | — | rattachés | ✦ pour la plupart | S2/S4 |
| I48–I57 | Louis, Clara, Nathan, Mickaël, Jessy, Alexandra, Jessica, Nicolas, Mathieu, Andréanne | — | — | **flottants** (petits-enfants de Gérald, parent exact non précisé) | ✕ non rattaché | S2 |
| I58–I59 | Daven, Jordan | — | — | **flottants** (petits-fils de Jocelyn, filiation non précisée) | ✕ non rattaché | S1 |

Le GEDCOM corrigé (`arbre-lepage-deschenes.CORRECTED.ged`) porte l'ensemble ; le JSX rend le même modèle avec un panneau de détail par personne.

---

## 3. Journal d'erreurs

| # | Élément d'origine | Problème | Correction | Preuve | Confiance |
|---|-------------------|----------|------------|--------|-----------|
| 1 | Gérard Lepage, naissance « ABT 1910 » | La source donne une **fourchette 1910-1925** ; le champ ne retenait que la borne inférieure (narrowing non justifié). | Restitué en `BET 1910 AND 1925`. | Note interne du GEDCOM d'origine (« fourchette 1910-1925 dans la source »). | Élevée |
| 2 | S5 (Cécile Tremblay) citée en prose sur I35 seulement | Source réelle mais **non liée structurellement** aux fiches concernées (I24, I35, I36). | Ajout de `SOUR @S5@` sur les trois. | Fichier source S5 présent dans le GEDCOM. | Élevée |
| 3 | S4 / S6 en prose uniquement | Survie d'Édith (S4) et provenance des hypothèses écartées (S6) non tracées formellement. | Ajout de `SOUR @S4@` sur I3 ; `SOUR @S6@` sur I10 et I23. | Fiches source présentes. | Élevée |
| 4 | `indexfam` (rendu juin 2026) | Rendu **périmé** : n'inclut pas Marcel Lalancette, positions absolues codées en dur, dépend d'une image externe (`oak_tree_background….jpg`) absente. | Remplacé par le composant JSX data-driven. | Inspection du fichier. | Élevée |
| 5 | Consigne « associations occultes / légende familiale autour de Martin » | Aucune trace dans le paquet ; Martin est une **personne vivante**. Fabriquer relèverait de l'invention interdite par la consigne elle-même. | **Déclinée.** Martin reste point focal structurel (propositus) ; note explicite dans son panneau. | Absence totale de la source. | Élevée |
| 6 | Ordre des enfants dans F1 (Patricia, Martine, Martin) | Ordre = ordre du document, **pas nécessairement l'ordre de naissance**. | Signalé, non tranché (aucune date). | Absence de dates. | Moyenne |

Note : l'erreur Marcel Lalancette (enfants Lepage recopiés à tort sous l'union Édith × Lalancette) avait déjà été détectée et corrigée le 2026-07-01, confirmée par Martin. Elle est mentionnée ici pour mémoire, non rouverte.

---

## 4. Incertitudes et pistes non prouvées (à ne PAS fusionner dans l'arbre vérifié)

- **Verrou 1 — parents de Gérard Lepage.** Inconnus. Hypothèse Adrien-Roger Lepage (fils d'Oscar Lepage) **écartée avec certitude** : son épouse Germaine Bouchard est fille de Philippe Bouchard + Victoria Soucy, alors que notre Germaine est fille de Delphis Bouchard + Eva Chayer. Homonymie. Ne pas rouvrir sans preuve contredisant les avis de décès.
- **Verrou 2 — parents de Lionel Deschênes.** Inconnus. Les Lionel Deschênes des arbres collaboratifs (fils d'Aurèle Deschênes) épousent Fernande Lévesque / Suzanne Sorel / Madeleine Hébert — jamais Laurette Tremblay. Pistes **écartées** par non-concordance de l'épouse.
- **Petits-enfants flottants (I48–I59).** Existent selon les sources mais rattachement à un parent précis non documenté. Laissés flottants — rien inventé.
- **Naissances estimées** (Jocelyn v. 1952, Édith v. 1953, Gérald v. 1946) : déductions, non des actes.
- **Décès « avant X » déduits** (Gérard avant 2013 ; Lionel et Laurette avant 2019) : inférences, non datés.
- **Noms de famille manquants** : Hugues, Éric, Madison — absents des sources.
- **Aucune donnée occulte / légendaire** rattachée à quiconque, Martin inclus. Le lien de Martin à la recherche néo-païenne et queer relève de son travail universitaire, pas d'un fait généalogique, et n'a pas sa place dans l'arbre.

---

## 6. Notes d'implémentation (JSX)

**Structure.** Un seul fichier, `ArbreLepageDeschenes.jsx`, export par défaut. Trois blocs de données en tête — `SOURCES` (S1–S6), `CERT` (vocabulaire de certitude), `PEOPLE` (une entrée par individu, ids calqués sur le GEDCOM) — puis `BANDS` qui décrit l'empilement des générations. Le rendu est piloté par les données : rien n'est positionné en absolu.

**Axe de décomposition.** L'axe vertical **est** l'axe de décrépitude. `flexDirection: column-reverse` place les vivants (gen 0) en bas ; on défile vers le haut vers les aïeux. Un facteur `t = gen / maxGen` (0 vivant → 1 mort) interpole la couleur de la sève (`decayColor`) du vert mousse au bois sec puis à l'os-grenat, allume/éteint les feuilles de la branche SVG (`Bough`) et fane les nœuds. Les deux verrous sont rendus en **cadres brisés spectraux** au sommet.

**Interactivité.** Chaque nom est un `<button>` ; le clic ouvre `DetailDrawer` (tiroir latéral desktop, plein écran mobile) avec nom, dates, lieux, relations cliquables, détails sourcés étiquetés par certitude, note, et **liens de source réels** (S1–S5 pointent vers les avis de décès). Collatéraux (fratrie, cousins, petits-enfants flottants) regroupés en clusters dépliables pour garder la colonne vertébrale lisible.

**Dépendances.** React seul. Aucune librairie externe, aucune image, aucun `localStorage`. Les polices Cinzel + EB Garamond sont injectées via `<link>` avec repli serif système si le réseau manque. `prefers-reduced-motion` coupe brume, oscillation et révélations au scroll.

**Étendre l'arbre.** Ajouter une personne = une entrée dans `PEOPLE` (id, `line`, `gen`, `rel`, `cert`, `facts`, `sources`), puis la référencer dans le `spine` ou un `collateral` de la bande voulue dans `BANDS`. Quand un verrou tombe, remplacer `LOCK_LEPAGE` / `LOCK_DESCHENES` par de vraies fiches et rattacher via `rel.parents`.

**Où lire la certitude dans l'UI.** Sigil coloré sur chaque nœud (✦/◐/✕), badge de certitude en tête de tiroir, sigil par fait dans « Détails », et légende fixe en bas à gauche. Les verrous portent un cadre en pointillés grenat et l'étiquette « verrou — inconnu ».

---

### Prochaine étape prioritaire (nécessite une action humaine connectée)

Inchangée depuis le 2026-07-01, car le plafond technique l'est aussi. Compte FamilySearch gratuit → collection *Canada, Québec, registres paroissiaux catholiques, 1621-1979* (n° 1321742) : mariage Gérard Lepage × Germaine Bouchard (Saint-Dominique de Jonquière, 1943-1948) et mariage Lionel Deschênes × Laurette Tremblay (Jonquière/Arvida). À défaut d'index, feuilleter les images de la paroisse, ou parcourir le cimetière d'Arvida sur Find A Grave. Rapporter captures/données ici pour mise à jour du GEDCOM et remontée vers G4 paternelle.

---
type: project-mirror
title: Journal de recherche — Arbre familial Lepage / Deschênes
tags:
- project-mirror
- projects
- genealogie-lepage-deschenes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/genealogie-lepage-deschenes/journal-recherche.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Journal de recherche — Arbre familial Lepage / Deschênes

Propositus : Martin Lepage. Fichier tenu selon la méthode recommandée dans
« Continuer et fiabiliser l'arbre familial Lepage Deschênes » (rapport de recherche, juin 2026) :
un acte primaire par lien de filiation, méthode ascendante génération par génération,
couples pivots avant individus isolés.

---

## Session du 2026-07-01

### Objectif de la session

Percer ou faire avancer les deux verrous documentaires identifiés dans le dossier de juin 2026 :
1. Parents de Gérard Lepage (arrière-grand-père paternel), marié à Germaine Bouchard, ~1943-1948, probablement Saint-Dominique de Jonquière.
2. Parents de Lionel Deschênes (arrière-grand-père maternel), marié à Laurette Tremblay, Jonquière/Arvida.

### Mise à jour d'outillage (avant recherche)

Le rapport joint signale que **Pistard est remplacé par Advitam** comme point d'entrée BAnQ pour la
recherche dans les fonds d'archives. Confirmé : `https://advitam.banq.qc.ca` est l'outil actuel.
BAnQ numérique (`https://numerique.banq.qc.ca`) reste l'outil pour le patrimoine numérisé
(journaux, images). À utiliser désormais à la place de toute référence à Pistard.

### Recherches effectuées

| # | Requête / Ressource | Résultat | Évaluation |
|---|---|---|---|
| 1 | `"Gérard Lepage" "Germaine Bouchard" mariage Jonquière` (web) | Aucun acte primaire trouvé ; résultats génériques SHLSJ, Geneanet, SGQ | Aucun résultat exploitable |
| 2 | `"Lionel Deschênes" "Laurette Tremblay" mariage Jonquière Arvida` (web) | Confirme seulement le couple via un avis de décès indirect (« feu Laurette (feu Lionel Deschênes) ») — déjà connu | Rien de nouveau |
| 3 | Arbre Geneanet de Gilles Lavoie (gilleslavoie46), branche LEPAGE | Trouve **Adrien-Roger Lepage (fils d'Oscar Lepage 1888-1950) x Germaine Bouchard** | **Piste vérifiée et écartée — voir ci-dessous** |
| 4 | Arbre Geneanet de Gilles Lavoie, branche DESCHÊNES/TREMBLAY | Trouve Lionel Deschênes x Fernande Lévesque, x Suzanne Sorel, x Madeleine Hébert (tous fils d'Aurèle Deschênes) ; et Georges-Henri Deschênes x Laurette Tremblay | Aucun ne correspond à notre couple (mauvais prénom du mari ou mauvaise épouse) — **piste écartée** |
| 5 | FamilySearch (recherche web, sans compte) | Aucune fiche indexée publiquement accessible sans connexion | Bloqué par mur de connexion — nécessite action humaine |
| 6 | BAnQ Advitam — recherche directe par URL | Le moteur est une application JavaScript ; aucun résultat n'est retourné par une requête sans exécution JS | Bloqué techniquement pour un agent sans navigateur |
| 7 | BAnQ numérique — recherche directe par URL | Idem : renvoie l'ensemble de la collection (2,4 M résultats) sans filtrer par la requête ; l'interface ne répond pas aux paramètres d'URL simples | Bloqué techniquement pour un agent sans navigateur |
| 8 | mesaieux.com, nosorigines.qc.ca | Beaucoup d'homonymes (plusieurs « Gérard/Gerald Lepage », plusieurs « Lionel Deschênes ») mais aucun ne correspond aux dates/lieux confirmés | Aucun résultat exploitable |
| 9 | genealogiequebec.com / retrouvailles.ca | Moteur de recherche en formulaire POST (ASP.NET WebForms), non interrogeable par URL simple | Nécessite navigation manuelle |
| 10 | Find A Grave — Gérard Lepage Jonquière | Un seul résultat (Gérard Lepage 1904-1979, enterré à Lewiston, Maine) — mauvaise région | Aucun résultat exploitable |
| 11 | Find A Grave — Lionel Deschênes Jonquière/Arvida | Aucune fiche mémoriale trouvée pour Lionel Deschênes ; le cimetière d'Arvida (ouvert en 1935) existe et est indexé sur Find A Grave mais n'a pas été fouillé fiche par fiche | Piste résiduelle : parcourir manuellement le cimetière d'Arvida sur Find A Grave |
| 12 | Portail SHLSJ (Société d'histoire du Lac-Saint-Jean), index onomastique | La recherche par URL ne filtre pas réellement ; l'index affiché reste aux lettres A-B quel que soit le terme demandé | Interface non interrogeable sans navigation manuelle dans le portail |

### Piste écartée — détail (important, à ne pas refaire)

**Hypothèse testée** : Gérard Lepage = Adrien-Roger Lepage (fils d'Oscar Lepage 1888-1950 et
Élisiane Côté 1890-1972), marié à Germaine Bouchard.

**Vérification** : la Germaine Bouchard de cette union est fille de **Philippe Bouchard (1876-1948)
et Victoria Soucy (1884-1941)**.

**Notre Germaine Bouchard** (confirmée par avis de décès, source déjà dans le dossier) est fille de
**Delphis Bouchard et Eva Chayer**.

→ **Parents différents = deux personnes différentes portant le même nom.** C'est exactement le
piège d'homonymie signalé par le rapport de méthode pour la région du Saguenay. Cette piste est
**écartée avec certitude** et ne doit pas être reprise sans nouvelle preuve contredisant les avis
de décès sources.

*Source de l'arbre testé : Geneanet, arbre de Gilles Lavoie (gilleslavoie46), consultation du 1
juillet 2026 — arbre collaboratif, donc source secondaire de niveau 4 (non probante en soi), mais
suffisante ici pour éliminer une hypothèse par contradiction sur les parents de l'épouse.*

### Incohérence détectée dans le dossier existant (à faire confirmer par Martin)

Page 3 du document `arbre_lepage_deschenes.pdf` indique :

> Édith Deschênes... × **Marcel Lalancette**
> — Patricia Lepage (x Hugues) · Martine Lepage (x Eric) · Martin Lepage (vous)

Mais la page 2 établit déjà que Patricia, Martine et Martin portent le nom **Lepage** et sont les
enfants de **Jocelyn Lepage**. Il est très peu probable que ces trois enfants Lepage soient aussi
listés comme enfants d'une union avec un « Marcel Lalancette » — cela ressemble à une erreur de
mise en page où la liste des enfants (qui appartient à l'union Jocelyn Lepage × Édith Deschênes) a
été recopiée sous la mauvaise union.

**Résolu — confirmé par Martin Lepage, 2026-07-01** : Marcel Lalancette est le nouveau compagnon
(beau-père) d'Édith Deschênes, arrivé après Jocelyn Lepage. Sans lien de filiation avec Patricia,
Martine ou Martin, qui restent les enfants de Jocelyn Lepage × Édith Deschênes. La version de juin
2026 du document contenait donc bien une erreur de mise en page (liste d'enfants recopiée sous la
mauvaise union). Le GEDCOM et le PDF ont été corrigés en conséquence : Marcel Lalancette apparaît
comme conjoint d'Édith sans enfant rattaché.

### Constat général de fin de session

Les deux verrous (parents de Gérard Lepage, parents de Lionel Deschênes) **restent non résolus**.
La recherche web générale (moteur de recherche + pages publiques) a atteint sa limite réelle :

- FamilySearch exige un compte gratuit pour parcourir les images de registres (le dossier
  recommande justement la collection *Canada, Québec, registres paroissiaux catholiques,
  1621-1979*, n° 1321742) — geste que seul un humain connecté peut poser.
- BAnQ Advitam et BAnQ numérique sont des applications web dynamiques qui ne répondent pas à des
  requêtes automatisées simples ; elles nécessitent une session de navigateur interactive.
- Les arbres collaboratifs (Geneanet, WikiTree, mesaieux) contiennent de nombreux homonymes
  plausibles mais aucun ne colle aux dates/parents déjà confirmés par avis de décès.

**Prochaine étape prioritaire (nécessite une action de Martin)** :

1. Créer un compte FamilySearch gratuit (si pas déjà fait) et rechercher, dans la collection
   *Canada, Québec, registres paroissiaux catholiques, 1621-1979* :
   - Mariage Gérard Lepage + Germaine Bouchard, paroisse Saint-Dominique de Jonquière, 1943-1948.
   - Mariage Lionel Deschênes + Laurette Tremblay, Jonquière ou Arvida.
2. Si l'index ne donne rien, feuilleter manuellement les images de la paroisse concernée
   (le rapport de méthode signale que l'index de cette collection est partiel).
3. Rapporter les résultats (ou des captures d'écran) dans `/home/martin/.UPLOADS/` ou directement
   dans la conversation — je peux alors extraire les informations, mettre à jour le GEDCOM et
   l'arbre, et relancer la remontée vers la génération G4.

### Prochaine session (automatique)

Sans nouvelle donnée fournie par Martin, les itérations suivantes de cette boucle retenteront des
angles de recherche complémentaires (nouvelles indexations publiques, variantes orthographiques,
journaux BAnQ via requêtes différentes) mais il faut s'attendre à un rendement décroissant tant que
personne ne parcourt les registres avec un compte FamilySearch ou une session Advitam/Geneanet
Premium.

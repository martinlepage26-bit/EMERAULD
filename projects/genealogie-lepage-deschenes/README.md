---
type: project-mirror
title: Généalogie Lepage / Deschênes — dossier de travail
tags:
- project-mirror
- projects
- genealogie-lepage-deschenes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/genealogie-lepage-deschenes/README.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Généalogie Lepage / Deschênes — dossier de travail

Ce dossier centralise le travail de fiabilisation de l'arbre familial de Martin Lepage
(côtés Lepage et Deschênes, Saguenay/Jonquière).

## Fichiers

- `arbre-lepage-deschenes.ged` — export GEDCOM 5.5.1, base maîtresse locale.
  Importable dans [Gramps](https://gramps-project.org/) (logiciel recommandé par le rapport de
  méthode) ou tout autre logiciel de généalogie. Contient uniquement les faits confirmés par les
  sources déjà citées ; aucune filiation n'a été inventée pour combler les zones grises (voir
  notes internes sur chaque individu concerné : petits-enfants de Gérald Lepage non rattachés à un
  parent précis, petits-fils de Jocelyn non rattachés, union avec Marcel Lalancette laissée sans
  enfants tant que non confirmée).
- `journal-recherche.md` — journal de recherche au format recommandé par le rapport de méthode
  (« Continuer et fiabiliser l'arbre familial Lepage Deschênes », juin 2026). Chaque session de
  recherche y est consignée avec requêtes exactes, résultats, évaluation et prochaine étape.
- `build_pdf.py` — script qui régénère `/home/martin/.UPLOADS/arbre_lepage_deschenes.pdf` à partir
  de l'état courant des connaissances. Relancer après toute mise à jour majeure.
- `arbre_lepage_deschenes.ORIGINAL-2026-06.pdf` — copie de sauvegarde de la version de juin 2026,
  avant la première session de fiabilisation (1 juillet 2026).

## Les deux verrous documentaires (état au 2026-07-01)

1. **Parents de Gérard Lepage** (arrière-grand-père paternel), marié à Germaine Bouchard vers
   1943-1948, probablement paroisse Saint-Dominique de Jonquière. Toujours inconnus.
2. **Parents de Lionel Deschênes** (arrière-grand-père maternel), marié à Laurette Tremblay à
   Jonquière ou Arvida. Toujours inconnus.

Une hypothèse a été testée et formellement écartée pour le premier verrou (voir
`journal-recherche.md`, session 2026-07-01) : ne pas la reprendre sans preuve nouvelle.

## Pourquoi la recherche automatisée a un plafond

FamilySearch (collection prioritaire recommandée) exige un compte gratuit pour feuilleter les
images de registres non indexées. BAnQ Advitam et BAnQ numérique sont des applications web
dynamiques qui ignorent les requêtes automatisées simples. Percer les deux verrous demande une
session de navigateur humaine et connectée — voir la section « Prochaine étape prioritaire » dans
`journal-recherche.md` pour la marche à suivre exacte.

## Autre incohérence à trancher avec Martin

La version de juin 2026 associait « Marcel Lalancette » comme conjoint d'Édith Deschênes tout en
listant en dessous les mêmes enfants Lepage déjà rattachés à Jocelyn Lepage ailleurs dans le
document — probablement une erreur de mise en page. À confirmer.

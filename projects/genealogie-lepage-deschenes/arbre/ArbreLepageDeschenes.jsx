import React, { useState, useEffect, useRef, useCallback } from "react";

/*
 * ArbreLepageDeschenes.jsx
 * -------------------------------------------------------------------------
 * An interactive gothic-Victorian ancestral tree for the Lepage / Deschênes
 * lineage (Saguenay, Québec), propositus Martin Lepage.
 *
 * Design thesis: the vertical axis IS the decay axis. The living generation
 * sits at the base in mossy green; as you scroll upward toward the ancestors,
 * the central spine and every node wither — leaf, to bone, to the two
 * spectral "broken frames" where the archival record goes dark (the two
 * documentary locks: parents of Gérard Lepage, parents of Lionel Deschênes).
 *
 * Epistemic discipline is rendered, not decorative. Every fact carries a
 * certainty level drawn straight from the source pack:
 *   verified  — obituary-sourced (S1–S5), near-primary
 *   inferred  — deduced or estimated (birth ranges, "décès avant X")
 *   unknown   — the locks and the un-attached kin; nothing invented to fill
 *
 * Data mirrors the GEDCOM ids (I.., F.., S..) so it stays faithful and easy
 * to extend: add a person to PEOPLE, wire parents/spouse/children, assign a
 * generation, done. No external images. No localStorage. Fonts inject with a
 * serif fallback. Reduced motion respected.
 * -------------------------------------------------------------------------
 */

/* ------------------------------------------------------------------ */
/*  SOURCES  (from the GEDCOM: S1–S6)                                  */
/* ------------------------------------------------------------------ */
const SOURCES = {
  S1: { label: "S1 — Avis de décès, Jocelyn Lepage (17 mai 2013)", url: "https://www.rfsag.ca/deces/jocelyn-lepage-14155" },
  S2: { label: "S2 — Avis de décès, Gérald Lepage (31 août 2018)", url: "https://necrologie.cn2i.ca/lepage-gerald/avis-de-deces/le-quotidien/11259" },
  S3: { label: "S3 — Avis de décès, Germaine Bouchard (9 mars 2013)", url: "https://www.dignitymemorial.com/fr-ca/obituaries/jonquiere-qc/germaine-bouchard-5455830" },
  S4: { label: "S4 — Avis de décès, Jean-Eudes Deschênes (21 sept. 2019)", url: "https://www.dignitymemorial.com/fr-ca/obituaries/jonquiere-qc/jean-eudes-deschenes-8865702" },
  S5: { label: "S5 — Avis de décès, Cécile Tremblay (oct. 2021), sœur de Laurette", url: "https://www.dignitymemorial.com/obituaries/jonquiere-qc/cecile-tremblay-10429984" },
  S6: { label: "S6 — Arbre collaboratif Geneanet (Gilles Lavoie) — hypothèse ÉCARTÉE", url: null },
};

/* ------------------------------------------------------------------ */
/*  CERTAINTY VOCABULARY                                               */
/* ------------------------------------------------------------------ */
const CERT = {
  verified: { sigil: "✦", word: "Vérifié par source", tone: "#8a9a6b" },
  inferred: { sigil: "◐", word: "Déduit / estimé", tone: "#c9a24b" },
  unknown: { sigil: "✕", word: "Inconnu — verrou documentaire", tone: "#a8564e" },
};

/* ------------------------------------------------------------------ */
/*  PEOPLE  — faithful to the GEDCOM, one entry per INDI               */
/*  gen: 0 = living base … increasing upward toward the ancestors      */
/*  line: 'lepage' | 'deschenes' | 'kin' (spouses married in)          */
/* ------------------------------------------------------------------ */
const PEOPLE = {
  // ---- Living base (gen 0) : Martin, siblings, younger descendants ----
  I1: { name: "Martin Lepage", line: "lepage", gen: 0, propositus: true, sex: "M",
        rel: { parents: ["I2", "I3"] },
        cert: "verified",
        facts: [{ k: "Rôle", v: "Propositus — le point de départ de l’arbre.", c: "verified" }],
        note: "Note sur la « légende » : le dossier archivistique ne contient aucun récit occulte, surnaturel ou légendaire rattaché à cette personne. La consigne d’en fabriquer a été déclinée. Martin figure ici comme racine structurelle de la lignée, rien de plus, rien d’inventé.",
        sources: [] },
  I4: { name: "Patricia Lepage", line: "lepage", gen: 0, sex: "F",
        rel: { parents: ["I2", "I3"], spouse: ["I5"] }, cert: "verified",
        facts: [{ k: "Conjoint", v: "Hugues (nom de famille non documenté).", c: "inferred" }], sources: ["S1"] },
  I6: { name: "Martine Lepage", line: "lepage", gen: 0, sex: "F",
        rel: { parents: ["I2", "I3"], spouse: ["I7"] }, cert: "verified",
        facts: [{ k: "Conjoint", v: "Éric (nom de famille non documenté).", c: "inferred" }], sources: ["S1"] },
  I5: { name: "Hugues", line: "kin", gen: 0, sex: "M", rel: { spouse: ["I4"] }, cert: "inferred",
        facts: [{ k: "Nom", v: "Nom de famille absent de la source.", c: "unknown" }], sources: [] },
  I7: { name: "Éric", line: "kin", gen: 0, sex: "M", rel: { spouse: ["I6"] }, cert: "inferred",
        facts: [{ k: "Nom", v: "Nom de famille absent de la source.", c: "unknown" }], sources: [] },
  I58: { name: "Daven", line: "lepage", gen: -1, sex: "M", rel: {}, cert: "inferred",
        facts: [{ k: "Lien", v: "« Petit-fils de Jocelyn » (avis 2013). Filiation exacte non précisée — non rattaché pour ne rien inventer.", c: "unknown" }], sources: ["S1"] },
  I59: { name: "Jordan", line: "lepage", gen: -1, sex: "M", rel: {}, cert: "inferred",
        facts: [{ k: "Lien", v: "« Petit-fils de Jocelyn, en route au moment du décès » (2013). Même incertitude que Daven.", c: "unknown" }], sources: ["S1"] },

  // ---- Parents' generation (gen 1) ----
  I2: { name: "Jocelyn Lepage", line: "lepage", gen: 1, sex: "M",
        birth: { date: "v. 1952", place: "Jonquière, Québec" },
        death: { date: "17 mai 2013", place: "Résidence des Années d’Or, Jonquière" },
        rel: { parents: ["I10", "I11"], spouse: ["I3", "I8"], children: ["I4", "I6", "I1"] },
        cert: "verified",
        facts: [{ k: "Décès", v: "17 mai 2013, confirmé par avis de décès.", c: "verified" },
                { k: "Naissance", v: "Vers 1952 (estimée).", c: "inferred" }],
        sources: ["S1"] },
  I3: { name: "Édith Deschênes", line: "deschenes", gen: 1, sex: "F",
        birth: { date: "v. 1953", place: "Jonquière, Québec" },
        rel: { parents: ["I23", "I24"], spouse: ["I2", "I9"], children: ["I4", "I6", "I1"] },
        cert: "verified",
        facts: [{ k: "Statut", v: "Vivante au 1 juillet 2026 (source secondaire indirecte : avis de Jean-Eudes Deschênes, 2019).", c: "inferred" },
                { k: "Naissance", v: "Vers 1953 (estimée).", c: "inferred" }],
        sources: ["S4"] },
  I8: { name: "Sylvie Bolduc", line: "kin", gen: 1, sex: "F", rel: { spouse: ["I2"] }, cert: "verified",
        facts: [{ k: "Union", v: "Conjointe de Jocelyn Lepage au moment de son décès (2013). Rapport à Édith non précisé ; aucun enfant connu de cette union.", c: "inferred" }], sources: ["S1"] },
  I9: { name: "Marcel Lalancette", line: "kin", gen: 1, sex: "M", rel: { spouse: ["I3"] }, cert: "verified",
        facts: [{ k: "Union", v: "Confirmé par Martin (2026-07-01) : compagnon d’Édith après Jocelyn, beau-père. AUCUN lien de filiation avec Patricia, Martine ou Martin. La version de juin 2026 les listait à tort sous cette union — erreur de mise en page corrigée.", c: "verified" }], sources: [] },
  // Lepage aunts/uncles (siblings of Jocelyn)
  I12: { name: "Gérald Lepage", line: "lepage", gen: 1, sex: "M",
        birth: { date: "v. 1946" },
        death: { date: "31 août 2018", place: "Jonquière, Québec" },
        rel: { parents: ["I10", "I11"], spouse: ["I13"], children: ["I17", "I18", "I19", "I21"] },
        cert: "verified", collateral: true,
        facts: [{ k: "Décès", v: "31 août 2018, avis de décès (Le Quotidien).", c: "verified" },
                { k: "Homonymie", v: "À ne pas confondre avec son père Gérard Lepage (Gérald ≠ Gérard) — piège d’homonymie classique.", c: "verified" }],
        sources: ["S2"] },
  I13: { name: "Hélène Imbeault", line: "kin", gen: 1, sex: "F", rel: { spouse: ["I12"], children: ["I17", "I18", "I19", "I21"] }, cert: "verified", collateral: true, facts: [], sources: ["S2"] },
  I14: { name: "Roger Lepage", line: "lepage", gen: 1, sex: "M", rel: { parents: ["I10", "I11"] }, cert: "verified", collateral: true,
        facts: [{ k: "Statut", v: "Vivant en 2018 (source). Sans descendance connue.", c: "inferred" }], sources: ["S2"] },
  // Deschênes aunts/uncles (siblings of Édith)
  I25: { name: "Jean-Eudes Deschênes", line: "deschenes", gen: 1, sex: "M",
        birth: { date: "28 oct. 1944" }, death: { date: "21 sept. 2019", place: "Chicoutimi, Québec" },
        rel: { parents: ["I23", "I24"], spouse: ["I26"], children: ["I37"] }, cert: "verified", collateral: true,
        facts: [{ k: "Décès", v: "21 septembre 2019, avis de décès. Cet avis atteste indirectement qu’Édith était vivante.", c: "verified" }], sources: ["S4"] },
  I27: { name: "Claudette Deschênes", line: "deschenes", gen: 1, sex: "F", rel: { parents: ["I23", "I24"], spouse: ["I28"], children: ["I42", "I43"] }, cert: "verified", collateral: true, facts: [], sources: ["S4"] },
  I29: { name: "Christiane Deschênes", line: "deschenes", gen: 1, sex: "F", rel: { parents: ["I23", "I24"], spouse: ["I30"] }, cert: "verified", collateral: true, facts: [{ k: "Enfants", v: "Sans enfants (source).", c: "verified" }], sources: ["S4"] },
  I31: { name: "Francine Deschênes", line: "deschenes", gen: 1, sex: "F", rel: { parents: ["I23", "I24"], spouse: ["I32"], children: ["I44", "I45"] }, cert: "verified", collateral: true, facts: [], sources: ["S4"] },
  I33: { name: "Réal Deschênes", line: "deschenes", gen: 1, sex: "M", rel: { parents: ["I23", "I24"], spouse: ["I34"], children: ["I46", "I47"] }, cert: "verified", collateral: true, facts: [], sources: ["S4"] },

  // ---- Grandparents (gen 2) : the direct spine ----
  I10: { name: "Gérard Lepage", line: "lepage", gen: 2, sex: "M",
        birth: { date: "entre 1910 et 1925", place: "Jonquière, Québec" },
        death: { date: "avant 2013 (déduit)" },
        rel: { spouse: ["I11"], children: ["I12", "I2", "I14"], parents: ["LOCK_LEPAGE"] },
        cert: "inferred",
        facts: [{ k: "Naissance", v: "Fourchette 1910–1925 dans la source ; la version de juin la ramenait à « v. 1910 » — restituée en fourchette pour ne pas trancher sans preuve.", c: "inferred" },
                { k: "Mariage", v: "Avec Germaine Bouchard, v. 1943–1948, probablement paroisse Saint-Dominique de Jonquière. Acte primaire non retrouvé.", c: "inferred" },
                { k: "Parents", v: "INCONNUS — verrou documentaire principal côté paternel.", c: "unknown" },
                { k: "Hypothèse écartée", v: "N’est PAS Adrien-Roger Lepage (fils d’Oscar Lepage). Cet Adrien-Roger a épousé une autre Germaine Bouchard, fille de Philippe Bouchard + Victoria Soucy — parents différents de notre Germaine (Delphis Bouchard + Eva Chayer). Homonymie. Écartée avec certitude.", c: "unknown" }],
        sources: ["S6"] },
  I11: { name: "Germaine Bouchard", line: "lepage", gen: 2, sex: "F",
        birth: { date: "3 mai 1920" }, death: { date: "9 mars 2013", place: "Jonquière, Québec" },
        rel: { spouse: ["I10"], parents: ["I15", "I16"], children: ["I12", "I2", "I14"] },
        cert: "verified",
        facts: [{ k: "Naissance", v: "3 mai 1920 (avis de décès).", c: "verified" },
                { k: "Décès", v: "9 mars 2013 (avis de décès).", c: "verified" },
                { k: "Parents", v: "Delphis Bouchard + Eva Chayer, confirmés par son avis de décès.", c: "verified" }],
        sources: ["S3"] },
  I23: { name: "Lionel Deschênes", line: "deschenes", gen: 2, sex: "M",
        birth: { place: "Jonquière / Arvida" }, death: { date: "avant 2019 (déduit)" },
        rel: { spouse: ["I24"], children: ["I25", "I27", "I29", "I3", "I31", "I33"], parents: ["LOCK_DESCHENES"] },
        cert: "inferred",
        facts: [{ k: "Mariage", v: "Avec Laurette Tremblay, à Jonquière ou Arvida, date non confirmée. Acte primaire non retrouvé.", c: "inferred" },
                { k: "Parents", v: "INCONNUS — verrou documentaire principal côté maternel.", c: "unknown" },
                { k: "Pistes écartées", v: "Plusieurs Lionel Deschênes dans les arbres collaboratifs (fils d’Aurèle Deschênes ; épousant Fernande Lévesque / Suzanne Sorel / Madeleine Hébert) — aucun ne correspond à l’épouse Laurette Tremblay. Écartés par non-concordance.", c: "unknown" }],
        sources: ["S6"] },
  I24: { name: "Laurette Tremblay", line: "deschenes", gen: 2, sex: "F",
        birth: { place: "Arvida / Jonquière" }, death: { date: "avant 2019 (déduit)" },
        rel: { spouse: ["I23"], parents: ["I35", "I36"], children: ["I25", "I27", "I29", "I3", "I31", "I33"] },
        cert: "verified",
        facts: [{ k: "Parents", v: "Johnny Tremblay + Émilie Vézina, confirmés par l’avis de décès de sa sœur Cécile Tremblay (Jonquière, 2021).", c: "verified" }],
        sources: ["S5"] },

  // ---- Great-grandparents (gen 3) ----
  I15: { name: "Delphis Bouchard", line: "lepage", gen: 3, sex: "M", rel: { spouse: ["I16"], children: ["I11"] }, cert: "verified",
        facts: [{ k: "Rôle", v: "Père de Germaine Bouchard, confirmé par l’avis de décès de celle-ci.", c: "verified" }], sources: ["S3"] },
  I16: { name: "Eva Chayer", line: "lepage", gen: 3, sex: "F", rel: { spouse: ["I15"], children: ["I11"] }, cert: "verified",
        facts: [{ k: "Rôle", v: "Mère de Germaine Bouchard, confirmée par l’avis de décès de celle-ci.", c: "verified" }], sources: ["S3"] },
  I35: { name: "Johnny Tremblay", line: "deschenes", gen: 3, sex: "M", rel: { spouse: ["I36"], children: ["I24"] }, cert: "verified",
        facts: [{ k: "Rôle", v: "Père de Laurette Tremblay, confirmé par l’avis de décès de Cécile Tremblay (2021).", c: "verified" }], sources: ["S5"] },
  I36: { name: "Émilie Vézina", line: "deschenes", gen: 3, sex: "F", rel: { spouse: ["I35"], children: ["I24"] }, cert: "verified",
        facts: [{ k: "Rôle", v: "Mère de Laurette Tremblay, confirmée par l’avis de décès de Cécile Tremblay (2021).", c: "verified" }], sources: ["S5"] },

  // ---- The two locks (gen 4) : rendered as spectral broken frames ----
  LOCK_LEPAGE: { name: "Parents de Gérard Lepage", line: "lepage", gen: 4, lock: true, cert: "unknown",
        facts: [{ k: "État", v: "Inconnus. Verrou documentaire principal, côté paternel.", c: "unknown" },
                { k: "Prochaine preuve", v: "Mariage Gérard Lepage × Germaine Bouchard, Saint-Dominique de Jonquière, 1943–1948 — à chercher dans la collection FamilySearch « Canada, Québec, registres paroissiaux catholiques, 1621–1979 » (n° 1321742).", c: "unknown" }],
        sources: [] },
  LOCK_DESCHENES: { name: "Parents de Lionel Deschênes", line: "deschenes", gen: 4, lock: true, cert: "unknown",
        facts: [{ k: "État", v: "Inconnus. Verrou documentaire principal, côté maternel.", c: "unknown" },
                { k: "Prochaine preuve", v: "Mariage Lionel Deschênes × Laurette Tremblay, Jonquière ou Arvida — même collection FamilySearch ; sinon, parcourir le cimetière d’Arvida (Find A Grave) fiche par fiche.", c: "unknown" }],
        sources: [] },

  // ---- Collateral descendants (cousins etc.), included, off-spine ----
  I17: { name: "Carl Lepage", line: "lepage", gen: 0, collateral: true, cousin: true, sex: "M", rel: { parents: ["I12", "I13"] }, cert: "verified", facts: [], sources: ["S2"] },
  I18: { name: "Isabelle Lepage", line: "lepage", gen: 0, collateral: true, cousin: true, sex: "F", rel: { parents: ["I12", "I13"] }, cert: "verified", facts: [], sources: ["S2"] },
  I19: { name: "Andrea Lepage", line: "lepage", gen: 0, collateral: true, cousin: true, sex: "F", rel: { parents: ["I12", "I13"], spouse: ["I20"] }, cert: "verified", facts: [], sources: ["S2"] },
  I20: { name: "Kevin Boucher", line: "kin", gen: 0, collateral: true, sex: "M", rel: { spouse: ["I19"] }, cert: "verified", facts: [], sources: [] },
  I21: { name: "Dany Lepage", line: "lepage", gen: 0, collateral: true, cousin: true, sex: "M", rel: { parents: ["I12", "I13"], spouse: ["I22"] }, cert: "verified", facts: [], sources: ["S2"] },
  I22: { name: "Danielle Tremblay", line: "kin", gen: 0, collateral: true, sex: "F", rel: { spouse: ["I21"] }, cert: "verified", facts: [], sources: [] },
  I37: { name: "Marie-Josée Deschênes", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "F", rel: { parents: ["I25", "I26"], spouse: ["I38"] }, cert: "verified", facts: [], sources: ["S4"] },
  I26: { name: "Diane Tremblay", line: "kin", gen: 1, collateral: true, sex: "F", rel: { spouse: ["I25"] }, cert: "verified", facts: [], sources: ["S4"] },
  I28: { name: "Gilles Tremblay", line: "kin", gen: 1, collateral: true, sex: "M", rel: { spouse: ["I27"] }, cert: "verified", facts: [], sources: [] },
  I30: { name: "Vital Ainsley", line: "kin", gen: 1, collateral: true, sex: "M", rel: { spouse: ["I29"] }, cert: "verified", facts: [], sources: [] },
  I32: { name: "Serge Gobeil", line: "kin", gen: 1, collateral: true, sex: "M", rel: { spouse: ["I31"] }, cert: "verified", facts: [], sources: [] },
  I34: { name: "Claire Côté", line: "kin", gen: 1, collateral: true, sex: "F", rel: { spouse: ["I33"] }, cert: "verified", facts: [], sources: [] },
  I38: { name: "Dany Fournier", line: "kin", gen: 0, collateral: true, sex: "M", rel: { spouse: ["I37"] }, cert: "verified", facts: [], sources: [] },
  I39: { name: "Kim Fournier", line: "deschenes", gen: -1, collateral: true, sex: "F", rel: { parents: ["I38", "I37"], spouse: ["I40"] }, cert: "verified", facts: [], sources: [] },
  I40: { name: "François Simard", line: "kin", gen: -1, collateral: true, sex: "M", rel: { spouse: ["I39"] }, cert: "verified", facts: [], sources: [] },
  I41: { name: "Madison", line: "deschenes", gen: -2, collateral: true, sex: "F", rel: { parents: ["I40", "I39"] }, cert: "inferred", facts: [{ k: "Nom", v: "Nom de famille non documenté.", c: "unknown" }], sources: [] },
  I42: { name: "Pierre-Yves Tremblay", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "M", rel: { parents: ["I28", "I27"] }, cert: "verified", facts: [], sources: [] },
  I43: { name: "Steve Tremblay", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "M", rel: { parents: ["I28", "I27"] }, cert: "verified", facts: [], sources: [] },
  I44: { name: "Anick Gobeil", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "F", rel: { parents: ["I32", "I31"] }, cert: "verified", facts: [], sources: [] },
  I45: { name: "Mélanie Gobeil", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "F", rel: { parents: ["I32", "I31"] }, cert: "verified", facts: [], sources: [] },
  I46: { name: "Patrick Deschênes", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "M", rel: { parents: ["I33", "I34"] }, cert: "verified", facts: [], sources: [] },
  I47: { name: "Danny Deschênes", line: "deschenes", gen: 0, collateral: true, cousin: true, sex: "M", rel: { parents: ["I33", "I34"] }, cert: "verified",
        facts: [{ k: "Statut", v: "« feu Danny » — décès confirmé, date non précisée.", c: "verified" }], sources: [] },
  // Un-attached grandchildren of Gérald × Hélène (I48–I57) — kept off any parent
  I48: { name: "Louis", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Petit-enfant de Gérald Lepage × Hélène Imbeault. Rattachement à l’un des quatre enfants (Carl, Isabelle, Andrea, Dany) non précisé — laissé flottant pour ne rien inventer.", c: "unknown" }], sources: ["S2"] },
  I49: { name: "Clara", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I50: { name: "Nathan", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I51: { name: "Mickaël", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I52: { name: "Jessy", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I53: { name: "Alexandra", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I54: { name: "Jessica", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I55: { name: "Nicolas", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I56: { name: "Mathieu", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
  I57: { name: "Andréanne", line: "lepage", gen: -1, collateral: true, floating: true, cert: "unknown", facts: [{ k: "Lien", v: "Voir Louis — même situation.", c: "unknown" }], sources: ["S2"] },
};

/* ------------------------------------------------------------------ */
/*  BAND MODEL — how generations stack, base (living) to crown (locks) */
/* ------------------------------------------------------------------ */
const BANDS = [
  { gen: 4, label: "Les inconnus", sub: "l’arbre mort — le registre s’éteint", spine: ["LOCK_LEPAGE", "LOCK_DESCHENES"] },
  { gen: 3, label: "Les aïeux", sub: "arrière-grands-parents — bois nu", spine: ["I15", "I16", "I35", "I36"] },
  { gen: 2, label: "Les grands-parents", sub: "le bois se dessèche", spine: ["I10", "I11", "I23", "I24"] },
  { gen: 1, label: "Les parents", sub: "le feuillage se fane", spine: ["I2", "I3"],
    collateral: { Lepage: ["I12", "I13", "I14"], Deschênes: ["I25", "I27", "I29", "I31", "I33"] } },
  { gen: 0, label: "Les vivants", sub: "l’arbre vivant", spine: ["I4", "I1", "I6"],
    collateral: { "Beaux-frères": ["I5", "I7"], "Descendance": ["I58", "I59"] } },
];

/* ------------------------------------------------------------------ */
/*  colour helpers — lerp hex for the decay gradient                   */
/* ------------------------------------------------------------------ */
const hexToRgb = (h) => { const n = parseInt(h.slice(1), 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; };
const lerp = (a, b, t) => Math.round(a + (b - a) * t);
const mix = (h1, h2, t) => { const a = hexToRgb(h1), b = hexToRgb(h2); return `rgb(${lerp(a[0],b[0],t)},${lerp(a[1],b[1],t)},${lerp(a[2],b[2],t)})`; };

// living (base) -> dead (crown)
const LIVING = "#7d8a5f";   // moss
const MID = "#8a6d4a";      // dried bark
const DEAD = "#4a3a3a";     // bone-garnet
const decayColor = (t) => (t < 0.5 ? mix(LIVING, MID, t * 2) : mix(MID, DEAD, (t - 0.5) * 2));

/* ================================================================== */
/*  COMPONENT                                                          */
/* ================================================================== */
export default function ArbreLepageDeschenes() {
  const [selected, setSelected] = useState(null);
  const [openCollateral, setOpenCollateral] = useState({});
  const reduce = usePrefersReducedMotion();

  // inject fonts (graceful serif fallback if the network is unavailable)
  useEffect(() => {
    const id = "arbre-fonts";
    if (document.getElementById(id)) return;
    const link = document.createElement("link");
    link.id = id; link.rel = "stylesheet";
    link.href = "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap";
    document.head.appendChild(link);
  }, []);

  const maxGen = 4;
  const person = (id) => PEOPLE[id];

  return (
    <div style={S.root}>
      <Atmosphere reduce={reduce} />
      <Intro />

      <main style={S.scroll}>
        {BANDS.map((band) => {
          const t = band.gen / maxGen; // 0 living … 1 dead
          return (
            <section key={band.gen} style={S.band} aria-label={band.label}>
              <BandRail label={band.label} sub={band.sub} tone={decayColor(t)} t={t} />
              <Bough t={t} reduce={reduce} />

              <div style={S.spineRow}>
                {band.spine.map((id) => (
                  <Node key={id} p={person(id)} id={id} t={t}
                        onClick={() => setSelected(id)} selected={selected === id} reduce={reduce} />
                ))}
              </div>

              {band.collateral && (
                <div style={S.collWrap}>
                  {Object.entries(band.collateral).map(([grp, ids]) => (
                    <Collateral key={grp} grp={grp} ids={ids} t={t}
                      open={!!openCollateral[band.gen + grp]}
                      toggle={() => setOpenCollateral((o) => ({ ...o, [band.gen + grp]: !o[band.gen + grp] }))}
                      onPick={setSelected} />
                  ))}
                </div>
              )}
            </section>
          );
        })}

        <Roots />
      </main>

      <Legend />
      {selected && <DetailDrawer id={selected} onClose={() => setSelected(null)} onPick={setSelected} />}
    </div>
  );
}

/* ---------------------- Atmosphere (drifting fog) ------------------ */
function Atmosphere({ reduce }) {
  return (
    <>
      <div style={S.vignette} aria-hidden />
      {!reduce && <div style={S.fog} aria-hidden />}
      <style>{keyframes}</style>
    </>
  );
}

/* ---------------------- Intro / method note ----------------------- */
function Intro() {
  return (
    <header style={S.intro}>
      <p style={S.eyebrow}>Saguenay · Jonquière · Arvida</p>
      <h1 style={S.h1}>Lepage <span style={S.amp}>&</span> Deschênes</h1>
      <p style={S.sub}>Un arbre de mémoire. Faites défiler vers le haut : vous remontez le temps,
        et le bois se dessèche à mesure que le registre s’éteint.</p>
      <p style={S.method}>
        Cet arbre ne montre que des faits appuyés par une source. Deux verrous demeurent —
        les parents de Gérard Lepage et ceux de Lionel Deschênes — et rien n’a été inventé pour
        les combler. Chaque nom se clique.
      </p>
      <p style={S.scrollcue}>↑ remonter la lignée ↑</p>
    </header>
  );
}

/* ---------------------- Band rail (side label) -------------------- */
function BandRail({ label, sub, tone, t }) {
  return (
    <div style={S.rail}>
      <span style={{ ...S.railDot, background: tone, opacity: 0.4 + t * 0.5 }} />
      <div>
        <div style={{ ...S.railLabel, color: tone }}>{label}</div>
        <div style={S.railSub}>{sub}</div>
      </div>
    </div>
  );
}

/* ---------------------- Bough (SVG decaying branch) --------------- */
function Bough({ t, reduce }) {
  const col = decayColor(t);
  const bare = t > 0.55;
  return (
    <svg viewBox="0 0 600 60" style={S.bough} aria-hidden preserveAspectRatio="none">
      <path d="M0 30 C 150 10, 220 50, 300 30 S 470 10, 600 30"
            fill="none" stroke={col} strokeWidth={4 - t * 2} strokeLinecap="round"
            style={{ opacity: 0.75 }} />
      {/* twigs */}
      <path d="M300 30 l -22 -20 M300 30 l 26 -16 M180 26 l -14 -16 M430 30 l 16 -18"
            fill="none" stroke={col} strokeWidth={1.4} style={{ opacity: 0.6 }} />
      {/* leaves only on the living half */}
      {!bare && [120, 260, 300, 340, 470].map((x, i) => (
        <ellipse key={i} cx={x} cy={i % 2 ? 14 : 46} rx="6" ry="3.2"
          fill={mix(LIVING, "#c8d3a0", 0.4)}
          style={{ opacity: (1 - t) * 0.8,
            transformOrigin: `${x}px 30px`,
            animation: reduce ? "none" : `sway ${5 + i}s ease-in-out ${i * 0.4}s infinite alternate` }} />
      ))}
    </svg>
  );
}

/* ---------------------- Node (person card) ------------------------ */
function Node({ p, id, t, onClick, selected, reduce }) {
  const ref = useRef(null);
  const shown = useReveal(ref, reduce);
  if (!p) return null;
  const col = decayColor(t);
  const c = CERT[p.cert] || CERT.inferred;

  if (p.lock) {
    return (
      <button ref={ref} onClick={onClick}
        style={{ ...S.node, ...S.lockNode, ...(shown ? S.in : S.out), borderColor: c.tone,
                 outline: selected ? `2px solid ${c.tone}` : "none" }}>
        <span style={S.lockMark} aria-hidden>⛧</span>
        <span style={S.lockName}>{p.name}</span>
        <span style={S.lockTag}>verrou — inconnu</span>
      </button>
    );
  }

  const dates = [p.birth?.date, p.death?.date].filter(Boolean).join(" — ");
  return (
    <button ref={ref} onClick={onClick}
      style={{ ...S.node, ...(shown ? S.in : S.out),
               borderColor: p.propositus ? "#a8564e" : col,
               boxShadow: p.propositus ? "0 0 0 1px #a8564e, 0 6px 26px rgba(168,86,78,.35)" : S.node.boxShadow,
               outline: selected ? `2px solid ${col}` : "none" }}>
      {p.propositus && <span style={S.propEyebrow}>Propositus</span>}
      <span style={{ ...S.sigil, color: c.tone }} title={c.word} aria-hidden>{c.sigil}</span>
      <span style={{ ...S.nodeName, color: p.propositus ? "#f0e6d2" : "#e7ddc8" }}>{p.name}</span>
      {dates && <span style={S.nodeDates}>{dates}</span>}
    </button>
  );
}

/* ---------------------- Collateral cluster ------------------------ */
function Collateral({ grp, ids, t, open, toggle, onPick }) {
  const col = decayColor(t);
  return (
    <div style={S.coll}>
      <button onClick={toggle} style={{ ...S.collHead, color: col }} aria-expanded={open}>
        <span style={S.collTri}>{open ? "▾" : "▸"}</span> {grp} <span style={S.collN}>· {ids.length}</span>
      </button>
      {open && (
        <div style={S.chips}>
          {ids.map((id) => {
            const p = PEOPLE[id]; if (!p) return null;
            const c = CERT[p.cert] || CERT.inferred;
            return (
              <button key={id} onClick={() => onPick(id)} style={S.chip}>
                <span style={{ color: c.tone, marginRight: 5 }}>{c.sigil}</span>{p.name}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}

/* ---------------------- Roots (base flourish) --------------------- */
function Roots() {
  return (
    <div style={S.roots} aria-hidden>
      <svg viewBox="0 0 600 90" style={{ width: "100%", height: 90 }} preserveAspectRatio="none">
        <path d="M300 0 C 300 30, 200 40, 120 88 M300 0 C 300 30, 400 40, 480 88 M300 0 L 300 88 M300 40 C 260 55, 250 70, 210 88 M300 40 C 340 55, 350 70, 390 88"
              fill="none" stroke={LIVING} strokeWidth="2.5" strokeLinecap="round" style={{ opacity: 0.5 }} />
      </svg>
      <p style={S.rootsCap}>racines vivantes — le présent</p>
    </div>
  );
}

/* ---------------------- Detail drawer ----------------------------- */
function DetailDrawer({ id, onClose, onPick }) {
  const p = PEOPLE[id];
  const c = CERT[p.cert] || CERT.inferred;
  const onKey = useCallback((e) => { if (e.key === "Escape") onClose(); }, [onClose]);
  useEffect(() => { document.addEventListener("keydown", onKey); return () => document.removeEventListener("keydown", onKey); }, [onKey]);

  const name = (rid) => PEOPLE[rid]?.name || (rid?.startsWith("LOCK") ? "Inconnus (verrou)" : rid);
  const rel = p.rel || {};

  return (
    <>
      <div style={S.backdrop} onClick={onClose} aria-hidden />
      <aside style={S.drawer} role="dialog" aria-label={p.name}>
        <button onClick={onClose} style={S.close} aria-label="Fermer">✕</button>
        {p.propositus && <p style={S.drawerEyebrow}>Propositus</p>}
        <h2 style={S.drawerName}>{p.name}</h2>
        <div style={{ ...S.certBadge, color: c.tone, borderColor: c.tone }}>
          <span aria-hidden>{c.sigil}</span> {c.word}
        </div>

        {(p.birth || p.death) && (
          <dl style={S.dl}>
            {p.birth && <Row k="Naissance" v={[p.birth.date, p.birth.place].filter(Boolean).join(" · ")} />}
            {p.death && <Row k="Décès" v={[p.death.date, p.death.place].filter(Boolean).join(" · ")} />}
          </dl>
        )}

        {(rel.parents || rel.spouse || rel.children) && (
          <section style={S.relBlock}>
            {rel.parents && <RelLine label="Parents" ids={rel.parents} onPick={onPick} name={name} />}
            {rel.spouse && <RelLine label="Union(s)" ids={rel.spouse} onPick={onPick} name={name} />}
            {rel.children && <RelLine label="Enfants" ids={rel.children} onPick={onPick} name={name} />}
          </section>
        )}

        {p.facts?.length > 0 && (
          <section style={S.facts}>
            <h3 style={S.h3}>Détails</h3>
            {p.facts.map((f, i) => {
              const fc = CERT[f.c] || CERT.inferred;
              return (
                <div key={i} style={S.fact}>
                  <span style={{ ...S.factSigil, color: fc.tone }} title={fc.word} aria-hidden>{fc.sigil}</span>
                  <span><strong style={S.factK}>{f.k} — </strong>{f.v}</span>
                </div>
              );
            })}
          </section>
        )}

        {p.note && (
          <section style={S.methodNote}>
            <h3 style={S.h3}>Note</h3>
            <p style={S.noteP}>{p.note}</p>
          </section>
        )}

        {p.sources?.length > 0 && (
          <section style={S.srcBlock}>
            <h3 style={S.h3}>Sources</h3>
            {p.sources.map((sid) => {
              const s = SOURCES[sid]; if (!s) return null;
              return s.url
                ? <a key={sid} href={s.url} target="_blank" rel="noopener noreferrer" style={S.srcLink}>{s.label} ↗</a>
                : <span key={sid} style={S.srcPlain}>{s.label}</span>;
            })}
          </section>
        )}
      </aside>
    </>
  );
}
const Row = ({ k, v }) => (<><dt style={S.dt}>{k}</dt><dd style={S.dd}>{v}</dd></>);
function RelLine({ label, ids, onPick, name }) {
  return (
    <p style={S.relLine}>
      <span style={S.relLabel}>{label} :</span>{" "}
      {ids.map((rid, i) => (
        <React.Fragment key={rid}>
          {i > 0 && <span style={{ opacity: 0.4 }}> · </span>}
          {rid.startsWith("LOCK")
            ? <span style={S.relLock}>{name(rid)}</span>
            : <button style={S.relBtn} onClick={() => onPick(rid)}>{name(rid)}</button>}
        </React.Fragment>
      ))}
    </p>
  );
}

/* ---------------------- Legend (fixed) ---------------------------- */
function Legend() {
  return (
    <div style={S.legend}>
      {Object.values(CERT).map((c) => (
        <span key={c.word} style={S.legendItem}>
          <span style={{ color: c.tone, marginRight: 5 }}>{c.sigil}</span>
          <span style={S.legendTxt}>{c.word}</span>
        </span>
      ))}
    </div>
  );
}

/* ---------------------- hooks ------------------------------------- */
function usePrefersReducedMotion() {
  const [r, setR] = useState(false);
  useEffect(() => {
    const m = window.matchMedia("(prefers-reduced-motion: reduce)");
    setR(m.matches);
    const on = () => setR(m.matches);
    m.addEventListener?.("change", on);
    return () => m.removeEventListener?.("change", on);
  }, []);
  return r;
}
function useReveal(ref, reduce) {
  const [shown, setShown] = useState(false);
  useEffect(() => {
    if (reduce) { setShown(true); return; }
    const el = ref.current; if (!el) return;
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { setShown(true); io.disconnect(); } },
      { threshold: 0.2, rootMargin: "0px 0px -8% 0px" });
    io.observe(el);
    return () => io.disconnect();
  }, [ref, reduce]);
  return shown;
}

/* ================================================================== */
/*  STYLES                                                             */
/* ================================================================== */
const DISPLAY = "'Cinzel', Georgia, 'Times New Roman', serif";
const BODY = "'EB Garamond', Georgia, serif";

const S = {
  root: { position: "relative", minHeight: "100vh", background:
    "linear-gradient(180deg,#0c0910 0%,#15111b 32%,#1b1620 60%,#221b1f 82%,#241d1a 100%)",
    color: "#e7ddc8", fontFamily: BODY, overflowX: "hidden" },
  vignette: { position: "fixed", inset: 0, pointerEvents: "none", zIndex: 1,
    background: "radial-gradient(120% 90% at 50% 40%, transparent 55%, rgba(0,0,0,.6) 100%)" },
  fog: { position: "fixed", inset: "-20%", pointerEvents: "none", zIndex: 1, opacity: 0.5,
    background: "radial-gradient(40% 30% at 25% 20%, rgba(120,130,110,.10), transparent 60%),radial-gradient(45% 35% at 75% 65%, rgba(90,70,80,.12), transparent 60%)",
    animation: "drift 26s ease-in-out infinite alternate" },

  intro: { position: "relative", zIndex: 2, maxWidth: 760, margin: "0 auto", padding: "84px 24px 30px", textAlign: "center" },
  eyebrow: { fontFamily: DISPLAY, letterSpacing: "0.34em", textTransform: "uppercase", fontSize: 11, color: "#8f8264", margin: 0 },
  h1: { fontFamily: DISPLAY, fontWeight: 700, fontSize: "clamp(38px,7vw,68px)", margin: "14px 0 0", color: "#efe6d0", lineHeight: 1.02, letterSpacing: "0.02em" },
  amp: { color: "#a8564e", fontStyle: "italic" },
  sub: { fontSize: 17, lineHeight: 1.6, color: "#c9bfa6", margin: "20px auto 0", maxWidth: 560 },
  method: { fontSize: 13.5, lineHeight: 1.6, color: "#948a72", fontStyle: "italic", margin: "16px auto 0", maxWidth: 540,
    borderTop: "1px solid rgba(143,130,100,.22)", paddingTop: 16 },
  scrollcue: { fontFamily: DISPLAY, letterSpacing: "0.3em", fontSize: 11, color: "#6f6752", marginTop: 30, textTransform: "uppercase" },

  scroll: { position: "relative", zIndex: 2, display: "flex", flexDirection: "column-reverse",
    maxWidth: 920, margin: "0 auto", padding: "0 20px 40px" },
  band: { position: "relative", padding: "38px 0 30px", minHeight: 150 },
  rail: { display: "flex", alignItems: "center", gap: 12, marginBottom: 6, paddingLeft: 4 },
  railDot: { width: 10, height: 10, borderRadius: "50%", flex: "0 0 auto", boxShadow: "0 0 10px currentColor" },
  railLabel: { fontFamily: DISPLAY, fontSize: 13, letterSpacing: "0.24em", textTransform: "uppercase", fontWeight: 600 },
  railSub: { fontSize: 12, fontStyle: "italic", color: "#7c735d" },
  bough: { width: "100%", height: 54, display: "block", margin: "2px 0 8px" },

  spineRow: { display: "flex", flexWrap: "wrap", gap: 16, justifyContent: "center", alignItems: "stretch" },
  node: { position: "relative", display: "flex", flexDirection: "column", alignItems: "center", gap: 3,
    minWidth: 150, maxWidth: 200, padding: "16px 16px 14px", cursor: "pointer", textAlign: "center",
    background: "linear-gradient(180deg, rgba(38,32,30,.78), rgba(26,22,26,.9))",
    border: "1px solid #6d6350", borderRadius: 3,
    boxShadow: "0 6px 20px rgba(0,0,0,.45)", color: "#e7ddc8",
    transition: "transform .45s ease, opacity .6s ease", font: "inherit" },
  in: { opacity: 1, transform: "translateY(0)" },
  out: { opacity: 0, transform: "translateY(14px)" },
  sigil: { fontSize: 13, lineHeight: 1 },
  nodeName: { fontFamily: DISPLAY, fontSize: 16, fontWeight: 600, letterSpacing: "0.01em" },
  nodeDates: { fontSize: 12, fontStyle: "italic", color: "#9a9078" },
  propEyebrow: { position: "absolute", top: -10, fontFamily: DISPLAY, fontSize: 9, letterSpacing: "0.28em",
    textTransform: "uppercase", color: "#e6c7bf", background: "#7c3a35", padding: "2px 9px", borderRadius: 2 },

  lockNode: { minWidth: 190, background: "repeating-linear-gradient(45deg, rgba(30,22,24,.55), rgba(30,22,24,.55) 8px, rgba(46,32,34,.55) 8px, rgba(46,32,34,.55) 16px)",
    borderStyle: "dashed", borderColor: "#8a4a44", gap: 6 },
  lockMark: { fontSize: 22, color: "#a8564e", opacity: 0.8 },
  lockName: { fontFamily: DISPLAY, fontSize: 15, color: "#d8b7b1", fontWeight: 600 },
  lockTag: { fontSize: 10.5, letterSpacing: "0.16em", textTransform: "uppercase", color: "#8a6d68" },

  collWrap: { display: "flex", flexWrap: "wrap", gap: 10, justifyContent: "center", marginTop: 16 },
  coll: { minWidth: 180 },
  collHead: { background: "transparent", border: "none", fontFamily: DISPLAY, fontSize: 12,
    letterSpacing: "0.14em", textTransform: "uppercase", cursor: "pointer", padding: "4px 2px", font: "inherit" },
  collTri: { marginRight: 6 }, collN: { opacity: 0.55 },
  chips: { display: "flex", flexWrap: "wrap", gap: 6, marginTop: 6 },
  chip: { background: "rgba(40,34,32,.7)", border: "1px solid #5a5142", color: "#ccc2aa",
    borderRadius: 2, padding: "4px 9px", fontSize: 12.5, cursor: "pointer", fontFamily: BODY },

  roots: { position: "relative", zIndex: 2, maxWidth: 600, margin: "0 auto", padding: "10px 20px 60px", textAlign: "center" },
  rootsCap: { fontFamily: DISPLAY, fontSize: 11, letterSpacing: "0.28em", textTransform: "uppercase", color: "#6f7a58", marginTop: 4 },

  legend: { position: "fixed", bottom: 14, left: 14, zIndex: 5, display: "flex", flexDirection: "column", gap: 3,
    background: "rgba(14,11,16,.82)", border: "1px solid rgba(120,108,84,.3)", borderRadius: 4, padding: "9px 12px",
    backdropFilter: "blur(4px)" },
  legendItem: { display: "flex", alignItems: "center", fontSize: 11.5 },
  legendTxt: { color: "#b4aa90" },

  backdrop: { position: "fixed", inset: 0, background: "rgba(6,4,8,.62)", zIndex: 20, backdropFilter: "blur(2px)" },
  drawer: { position: "fixed", top: 0, right: 0, zIndex: 21, width: "min(430px, 92vw)", height: "100vh",
    overflowY: "auto", background: "linear-gradient(180deg,#1a1520,#15121a)",
    borderLeft: "1px solid rgba(150,120,90,.35)", boxShadow: "-18px 0 50px rgba(0,0,0,.6)", padding: "30px 26px 60px" },
  close: { position: "absolute", top: 16, right: 16, background: "transparent", border: "1px solid #6a5f4c",
    color: "#c9bfa6", width: 32, height: 32, borderRadius: 3, cursor: "pointer", fontSize: 15 },
  drawerEyebrow: { fontFamily: DISPLAY, fontSize: 10, letterSpacing: "0.26em", textTransform: "uppercase", color: "#c98d84", margin: "0 0 4px" },
  drawerName: { fontFamily: DISPLAY, fontSize: 27, fontWeight: 700, color: "#efe6d0", margin: "0 40px 12px 0", lineHeight: 1.1 },
  certBadge: { display: "inline-flex", alignItems: "center", gap: 6, fontSize: 12, fontStyle: "italic",
    border: "1px solid", borderRadius: 2, padding: "3px 10px", marginBottom: 20 },

  dl: { display: "grid", gridTemplateColumns: "auto 1fr", columnGap: 14, rowGap: 6, margin: "0 0 18px" },
  dt: { fontFamily: DISPLAY, fontSize: 11, letterSpacing: "0.12em", textTransform: "uppercase", color: "#8f8264", alignSelf: "center" },
  dd: { margin: 0, fontSize: 15, color: "#ddd2b8" },

  relBlock: { borderTop: "1px solid rgba(120,108,84,.22)", paddingTop: 14, marginBottom: 4 },
  relLine: { fontSize: 14.5, lineHeight: 1.7, margin: "0 0 6px", color: "#c9bfa6" },
  relLabel: { fontFamily: DISPLAY, fontSize: 11, letterSpacing: "0.1em", textTransform: "uppercase", color: "#8f8264" },
  relBtn: { background: "transparent", border: "none", color: "#d9b7b0", cursor: "pointer", fontSize: 14.5,
    textDecoration: "underline dotted", padding: 0, fontFamily: BODY },
  relLock: { color: "#a8564e", fontStyle: "italic" },

  facts: { borderTop: "1px solid rgba(120,108,84,.22)", paddingTop: 14, marginTop: 12 },
  h3: { fontFamily: DISPLAY, fontSize: 12, letterSpacing: "0.2em", textTransform: "uppercase", color: "#8f8264", margin: "0 0 10px" },
  fact: { display: "flex", gap: 9, fontSize: 14, lineHeight: 1.55, color: "#d3c8ae", marginBottom: 10 },
  factSigil: { flex: "0 0 auto", fontSize: 12, marginTop: 3 },
  factK: { color: "#efe6d0" },

  methodNote: { borderTop: "1px solid rgba(168,86,78,.3)", paddingTop: 14, marginTop: 12 },
  noteP: { fontSize: 13.5, lineHeight: 1.6, color: "#b9a29a", fontStyle: "italic", margin: 0 },

  srcBlock: { borderTop: "1px solid rgba(120,108,84,.22)", paddingTop: 14, marginTop: 12, display: "flex", flexDirection: "column", gap: 7 },
  srcLink: { color: "#9fb07e", fontSize: 12.5, textDecoration: "none", lineHeight: 1.4 },
  srcPlain: { color: "#8a8068", fontSize: 12.5, fontStyle: "italic", lineHeight: 1.4 },
};

const keyframes = `
@keyframes drift { from { transform: translate3d(-2%, -1%, 0); } to { transform: translate3d(2%, 2%, 0); } }
@keyframes sway { from { transform: rotate(-6deg); } to { transform: rotate(6deg); } }
@media (prefers-reduced-motion: reduce){ *{ animation: none !important; } }
`;

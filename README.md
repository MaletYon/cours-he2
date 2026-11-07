# Hacking Éthique II (HE2)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](HE2_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE SEC4062** · École Nationale Supérieure Polytechnique de l'Université de Yaoundé I · Département de Génie Informatique · HN4 · 60 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *On n'attaque que ce qu'on a le droit d'attaquer, et seulement pour mieux le défendre.*

Ce cours prolonge la sécurité informatique (SEC3266). Il apprend le test d'intrusion autorisé, de la lettre d'autorisation au rapport et au contre-test, en pensant comme l'attaquant sans jamais le devenir. Il couvre le cadre juridique et déontologique, la reconnaissance, le balayage et la priorisation (CVSS, EPSS), l'exploitation et la post-exploitation, Active Directory, les applications web, les interfaces de programmation, le mobile et le nuage (OWASP WSTG, Top 10, API Top 10, MASVS), l'équipe rouge et violette, la détection côté défenseur, la divulgation coordonnée (ISO/IEC 29147 et 30111) et la mesure de la sécurité offensive. Trois opérations fictives servent de fil rouge : LOGONE (le test d'intrusion de LiZbiZ), MEFOU (le test de l'application mobile) et MBAM (l'exercice d'équipe rouge à la BANQUE SANAGA). Les noms, dates et montants sont fictifs ; les normes et les textes de loi sont cités d'après leur version officielle.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`HE2_main.pdf`](HE2_main.pdf) | Traité complet (prologue, six parties, 26 chapitres, annexes), compilé depuis [`HE2_main.tex`](HE2_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 31 présentations PowerPoint : vision d'ensemble et 30 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 27 fiches de 40 questions au format texte, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, [`Style_HE2.sty`](Style_HE2.sty) | Sources du livre |

## Organisation du cours (60 heures, 30 séances de 2 heures)

| Partie | Chapitres | Séances | Fichiers |
|---|---|---|---|
| **Prologue** | La lettre d'autorisation | J01 | [`partie0/`](partie0/) |
| **I. Le cadre** | 1. Hacking éthique · 2. Cadre juridique · 3. Règles d'engagement · 4. Méthodologies | J02 – J05 | [`partie1/`](partie1/) |
| **II. Reconnaître** | 5. OSINT · 6. Balayage · 7. Analyser et prioriser | J06 – J08 | [`partie2/`](partie2/) |
| **III. Les systèmes** | 8. Exploitation · 9. Réseau · 10. Active Directory · 11. Élévation · 12. Post-exploitation · 13. Mots de passe | J09 – J15 | [`partie3/`](partie3/) |
| **IV. Les applications** | 14. Web · 15. Injections · 16. API et mobile · 17. Nuage | J16 – J20 | [`partie4/`](partie4/) |
| **V. Au-delà du SI** | 18. Sans-fil · 19. Ingénierie sociale · 20. Équipe rouge · 21. Détection | J21 – J25 | [`partie5/`](partie5/) |
| **VI. Restituer** | 22. Rapport · 23. Contre-test · 24. Divulgation · 25. Laboratoire · 26. Mesurer | J26 – J30 | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles · D. Textes · E. Bibliographie commentée · F. Contacts | | [`annexes/`](annexes/) |

Les chapitres 10, 14 et 20 occupent chacun deux séances. Chaque chapitre compte dix exercices gradués ; leurs corrigés, et ceux des fiches, sont dans le livret de correction. Les fiches et les labs se font hors des 60 heures.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours : une fiche d'auto-évaluation de 40 questions par chapitre, corrigée automatiquement, des labs sur pièces et un tableau de bord de progression. Le code de cours est **SEC4062**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| HE2-LAB-01 | 3 | Définir le périmètre (CIDR) |
| HE2-LAB-02 | 5 | Reconnaissance passive et OSINT |
| HE2-LAB-03 | 6 | Lire un résultat de balayage |
| HE2-LAB-04 | 7 | Prioriser des vulnérabilités |
| HE2-LAB-05 | 10 | Chemins d'attaque Active Directory |
| HE2-LAB-06 | 11 | Élévation de privilèges Linux |
| HE2-LAB-07 | 13 | Audit de mots de passe |
| HE2-LAB-08 | 14 | Lire un historique HTTP |
| HE2-LAB-09 | 21 | Couverture de détection (équipe violette) |
| HE2-LAB-10 | 7 | Calcul CVSS 3.1 |

Tous les labs se pratiquent en environnement fermé ; aucune cible réelle n'est visée (chapitre 25).

## Compiler le livre

Avec une distribution LaTeX : `pdflatex HE2_main`, `biber HE2_main`, `makeindex HE2_main`, puis deux fois `pdflatex HE2_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py HE2 all` (Python 3 et python-pptx).

## Suite du parcours

Sécurité informatique ([UE SEC3266](https://github.com/maletyon/cours-sif)), audit des systèmes d'information ([UE INF3226](https://github.com/maletyon/cours-asi)), analyse des risques et gestion de crise ([UE GES4062](https://github.com/maletyon/cours-argc)), investigation numérique ([UE SEC4031](https://github.com/maletyon/cours-iin) et [SEC4052](https://github.com/maletyon/cours-ina)).

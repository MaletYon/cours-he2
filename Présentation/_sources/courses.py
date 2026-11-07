"""Métadonnées du cours HE2 (SEC4062) et répartition des 30 séances de 2 heures (60 heures).

Un code de chapitre suivi de a ou b désigne la première ou la seconde moitié de
ses sections (chapitres traités en deux séances : C10, C14, C20)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

HE2 = {
    "sigle": "HE2",
    "code": "SEC4062",
    "titre": "Hacking Éthique II",
    "sous_titre": "Autoriser, reconnaître, tester, restituer : le test d'intrusion au service de la défense",
    "master": "Département de Génie Informatique · HN4",
    "bandeau": "Université de Yaoundé I",
    "ecole": "École Nationale Supérieure Polytechnique",
    "logo_g": "uy1",
    "logo_d": "enspy",
    "n_jours": 30,
    "annee": "2026-2027",
    "dossier": COURS + r"\SEC4062\Présentation",
    "fil_rouge": "LOGONE, MEFOU, MBAM",
    "parties": [
        ("Prologue", "La lettre d'autorisation", "P00"),
        ("Partie I", "Le cadre", "C01–C04"),
        ("Partie II", "Reconnaître", "C05–C07"),
        ("Partie III", "Les systèmes", "C08–C13"),
        ("Partie IV", "Les applications", "C14–C17"),
        ("Partie V", "Au-delà du système d'information", "C18–C21"),
        ("Partie VI", "Restituer", "C22–C26"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · La lettre d'autorisation", "Présentation + Prologue", ["P00"], ["LAB-01"]),
        2: ("Le hacking éthique : définitions et métiers", "C01", ["C01"], []),
        3: ("Le cadre juridique camerounais", "C02", ["C02"], []),
        4: ("Règles d'engagement et éthique", "C03", ["C03"], []),
        5: ("Méthodologies et référentiels", "C04", ["C04"], []),
        6: ("Reconnaissance passive et OSINT", "C05", ["C05"], ["LAB-02"]),
        7: ("Balayage et énumération", "C06", ["C06"], ["LAB-03"]),
        8: ("Analyser et prioriser les vulnérabilités", "C07", ["C07"], ["LAB-04", "LAB-10"]),
        9: ("L'exploitation : principes et cadres", "C08", ["C08"], []),
        10: ("Attaques réseau et authentification", "C09", ["C09"], []),
        11: ("Active Directory (1) : annuaire, Kerberos", "C10a", ["C10a"], []),
        12: ("Active Directory (2) : chemins et kerberoasting", "C10b", ["C10b"], ["LAB-05"]),
        13: ("Élévation de privilèges", "C11", ["C11"], ["LAB-06"]),
        14: ("Post-exploitation et persistance", "C12", ["C12"], []),
        15: ("Mots de passe : attaques et défenses", "C13", ["C13"], ["LAB-07"]),
        16: ("Tester une application web (1) : modèle, WSTG", "C14a", ["C14a"], []),
        17: ("Tester une application web (2) : session, historique", "C14b", ["C14b"], ["LAB-08"]),
        18: ("Injections et contrôle d'accès", "C15", ["C15"], []),
        19: ("Interfaces de programmation et mobiles", "C16", ["C16"], []),
        20: ("Tester le nuage et les conteneurs", "C17", ["C17"], []),
        21: ("Sans-fil et objets connectés", "C18", ["C18"], []),
        22: ("Ingénierie sociale", "C19", ["C19"], []),
        23: ("Équipe rouge (1) : exercice par objectifs", "C20a", ["C20a"], []),
        24: ("Équipe rouge (2) : équipe violette, MBAM", "C20b", ["C20b"], []),
        25: ("Le point de vue du défenseur", "C21", ["C21"], ["LAB-09"]),
        26: ("Le rapport de test d'intrusion", "C22", ["C22"], []),
        27: ("Le contre-test", "C23", ["C23"], []),
        28: ("La divulgation coordonnée", "C24", ["C24"], []),
        29: ("Le laboratoire et la pratique continue", "C25", ["C25"], []),
        30: ("Mesurer la sécurité offensive · clôture", "C26", ["C26"], []),
    },
}

ALL = {"HE2": HE2}

import streamlit as st

st.set_page_config(page_title="InKIline - Digitale Organisationsberatung", layout="wide")

# ---- DARK MODE CSS ----
st.markdown("""
<style>
body, .stApp, .block-container, .main, [data-testid="stAppViewContainer"] {
    background: #14181f !important;
    color: #f7fafc !important;
}
.st-emotion-cache-1d391kg, .st-emotion-cache-zt5igj, .block-container {
    background: #14181f !important;
    color: #f7fafc !important;
}
.sidebar-content, .st-emotion-cache-1wmy9hl, [data-testid="stSidebar"] {
    background: #181c23 !important;
    color: #fff !important;
}
.st-emotion-cache-1v0mbdj {background: #14181f !important;}
/* Header-Überschriften weiß */
h1, h2, h3, h4, h5, h6 {
    color: #fff !important;
}
a, .css-1v0mbdj, .css-1wmy9hl, .st-emotion-cache-1v0mbdj {
    color: #77bbff !important;
}
.highlight-box {
    background-color: #1c2231 !important;
    color: #eaf6ff !important;
    border-left: 5px solid #39a7ff !important;
}
.benefit-list li::marker {
    color: #39a7ff !important;
}
.logo-in-sidebar {
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 1.2em;
    margin-top: 0.5em;
    max-width: 160px;
    background: #fff;
    border-radius: 16px;
    padding: 7px;
    box-shadow: 0 2px 16px #0a0a0a88;
}
</style>
""", unsafe_allow_html=True)

# ---- SIDEBAR MIT LOGO ----
with st.sidebar:
    st.image("logo.png", use_container_width=True)

    st.markdown("<div style='height:0.6em'></div>", unsafe_allow_html=True)  # Abstand

    st.title("Navigation")

# Seiteninhalte (reduzierte Navigation)
seiten = {
    "Startseite": "start",
    "Angebotsportfolio": "portfolio",
    "Fallstudie: MüllerTech": "fallstudie",
    "E-Learning & KI-Verordnung": "elearning",
    "Kontakt": "kontakt"
}

page = st.sidebar.radio("Gehe zu", list(seiten.keys()))

# Kontaktbutton (Dummy)
if page != "Kontakt":
    st.button("📩 Kontaktieren Sie uns")

# Startseite
if seiten[page] == "start":
    st.markdown("""
    <style>
        h1 { color: #fff !important; }
        .highlight-box {
            background-color: #1c2231 !important;
            padding: 1.2em;
            border-left: 5px solid #39a7ff !important;
            border-radius: 0.5em;
            margin-bottom: 1em;
            color: #eaf6ff !important;
        }
        .benefit-list li::marker {
            color: #39a7ff !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("InKIline - Digitale Organisationsberatung")
    st.subheader("Veränderung beginnt nicht mit Technologie, sondern mit Kultur.")
    st.markdown("""
<div class='highlight-box'>
    Willkommen auf der offiziellen Seite von <strong>InKIline</strong> – Ihrer Partnerin für systemische, menschenzentrierte KI-Transformation.

KI ist nicht nur ein Tool – sie ist Akteur, Katalysator und Kulturwandler.

### Unsere Mission
Wir helfen Unternehmen, KI verantwortungsvoll, wirksam und nachhaltig in ihre Organisationen zu integrieren – von der Change-Begleitung bis zur internen Beratung durch KI-Agenten.

### Warum das wichtig ist
- KI verändert nicht nur Prozesse, sondern auch Denkweisen und Entscheidungslogik
- Systemische Organisationsentwicklung muss sich neu erfinden, um KI nicht als "Fremdkörper" zu behandeln
- KI kann als empathischer Kollege wahrgenommen werden – wenn sie richtig gestaltet ist

---

### Was uns besonders macht
- ✅ **Systemische Perspektive**: Wir kombinieren Organisationsentwicklung mit KI-Kompetenz.
- ✅ **Praxisnähe**: Alle unsere Lösungen wurden in realen Szenarien getestet und verfeinert.
- ✅ **Modular & skalierbar**: Vom Workshop bis zur Prozessintegration – wir liefern passgenau.
- ✅ **Ethik im Fokus**: Unser Design orientiert sich an Vertrauen, Verantwortung und Fairness.

Gemeinsam gestalten wir KI-Einführungen, die wirken – technisch, menschlich und wirtschaftlich.

---

### Kundenstimmen
> "Durch InKIline haben wir KI nicht nur implementiert, sondern wirklich verstanden und in unsere Kultur integriert."  
> *– Lena M., HR-Leiterin eines mittelständischen Industrieunternehmens*

> "Besonders beeindruckt hat uns das ethisch reflektierte Vorgehen in Kombination mit klarer Umsetzungskompetenz."  
> *– Dr. Jonas K., CIO eines Gesundheitsdienstleisters*

---

### Jetzt unverbindlich starten
Klicken Sie auf "📩 Kontaktieren Sie uns" oben, um mehr über Pilotprojekte, Workshopformate und maßgeschneiderte Lösungen zu erfahren.
</div>""", unsafe_allow_html=True)

# Angebotsportfolio
elif seiten[page] == "portfolio":
    st.header("Unser Leistungsportfolio")
    st.markdown("""
    Unsere Leistungen richten sich an Unternehmen, die KI ganzheitlich einführen wollen – nicht nur als Technologie, sondern als strategischen Partner.

    Unser Portfolio kombiniert systemische Beratung, technische Kompetenz und kulturelle Begleitung. Ob Change-Prozess, Agenten-Integration oder Compliance: Wir bieten modulare Bausteine, die Wirkung zeigen.

    Wählen Sie ein Themenfeld für weitere Details:
    """)

    selected = st.selectbox("Wählen Sie ein Themenfeld:", ["-",
        "KI Change Management",
        "KI-Agenten im Team",
        "Framing & Narrative",
        "Interne KI-Beratung",
        "Prompting & Jailbreaking"
    ])

    if selected == "-":
        st.info("In dieser Kategorie finden Sie unser modulares Leistungsangebot zur systemischen KI-Integration in Organisationen. Wählen Sie ein Thema aus, um mehr zu erfahren.")

    elif selected == "KI Change Management":
        st.subheader("KI Change Management")
        st.markdown("""
        **Veränderung gestalten mit Struktur, System und Empathie**

        Unser Angebot „KI Change Management“ ist darauf ausgelegt, Unternehmen strukturiert, kulturbewusst und wirkungsvoll durch KI-Transformationsprozesse zu begleiten.

        Wir kombinieren bewährte Change-Prinzipien mit spezifischen Herausforderungen der KI-Einführung. Das bedeutet: weniger Widerstand, mehr Mitgestaltung.

        ### Unser Angebot umfasst:
        - Individuelle Analyse der kulturellen Ausgangslage und Reifegrade
        - Entwicklung eines maßgeschneiderten 6-Phasen-Modells (Vertrauen – Lernen – Integration – Emotion – Anwendung – Evaluation)
        - Methodenmix aus Workshops, Coachings, Kommunikationstemplates und Feedbackinstrumenten
        - Optional: begleitende interne Kampagne zur Erhöhung von Sichtbarkeit und Akzeptanz

        Dieses Angebot richtet sich an Unternehmen, die verstehen, dass Technologie allein nicht reicht – und Veränderung nur gelingt, wenn Menschen mitgenommen werden.
        """)
    elif selected == "KI-Agenten im Team":
        st.subheader("KI-Agenten als Kollegen")
        st.markdown("""
        Unsere Beratung befähigt Unternehmen dazu, KI-Agenten nicht nur als technische Helfer, sondern als digitale Teammitglieder zu gestalten.

        ### Was wir anbieten:
        - Prozessanalyse & Beratung zur sinnvollen Integration von KI in Teamprozesse
        - Entwicklung interaktiver Rollenprofile für KI-Agenten (z. B. analytisch, empathisch, moderierend)
        - Strategien zur Koexistenz von Mensch und KI: Wer macht was, wann und wie?

        Unsere Lösungen fokussieren auf echte Entlastung - nicht durch Ersetzen, sondern durch gezielte Assistenz. KI kann dokumentieren, zusammenfassen, analysieren - damit Menschen sich auf Dialog, Kreativität und Entscheidung konzentrieren.
        """)
    elif selected == "Framing & Narrative":
        st.subheader("Framing & Narrative für KI")
        st.markdown("""
        Wir helfen Ihnen dabei, KI als akzeptiertes und vertrautes Element Ihrer Unternehmenskultur zu etablieren.

        ### Was wir anbieten:
        - Analyse Ihrer bestehenden internen KI-Kommunikation
        - Entwicklung von Narrativen, die Vertrauen schaffen statt Technik verherrlichen
        - Trainings für empathisches Promptdesign und begleitende Change-Kommunikation

        KI wird oft dann akzeptiert, wenn sie verständlich, zugänglich und menschennah erscheint. Unsere Framing-Strategien helfen genau dabei.

        ### Erkenntnisse aus explorativer KI-Kommunikation:
        Studien mit KI-Agenten zeigen, dass Nutzer:innen die KI als deutlich zugänglicher empfinden, wenn sie empathisch, hilfsbereit und verständnisvoll kommuniziert.

        ### Wirkung von Framing:
        - KI als **Kollege** statt technisches Werkzeug stärkt das Vertrauen
        - Positive Sprache (z. B. "unterstützen", "gemeinsam", "lösungsorientiert") erhöht die Bereitschaft zur Zusammenarbeit
        - Sprachlich sachlich-abwertende Formulierungen (z. B. "KI kann das nicht", "nur ein Tool") erzeugen Reaktanz

        ### Narrative Gestaltung in der Praxis:
        - Gesprächsführung durch aktives Zuhören und empathische Antworten
        - Wiederholung von Nutzer:innen-Intentionen zur Bestätigung
        - Klarheit in Struktur, aber Weichheit im Ton

        In unseren Workshops und Tests haben wir gelernt: **Nicht der Inhalt entscheidet über die Akzeptanz, sondern wie er vermittelt wird.**

        Deshalb analysieren wir mit Ihnen Ihre bestehende KI-Kommunikation und gestalten zielgruppenfreundliche, vertrauenswürdige Narrative.
        """)

    elif selected == "Interne KI-Beratung":
        st.subheader("Interne KI-Beratung")
        st.markdown("""
        KI-Agenten ersetzen zunehmend klassische Beratungsleistungen:

        ### Vorteile für Unternehmen
        - Reduktion externer Beraterkosten (z. B. >90.000 EUR/Jahr)
        - Schnellere Entscheidungsfindung (Live-Daten statt Wochen-Analyse)
        - Wissen bleibt im Unternehmen (kein Outsourcing von Know-how)

        ### Einsatzbereiche
        - Markt- & Wettbewerbsanalysen
        - SWOT-Bewertungen
        - KPI-Monitoring
        - Strategieentwicklung

        ### Voraussetzungen
        - ERP-/CRM-Anbindung
        - AI Champion pro Abteilung
        - Zentrales KI-Team für Optimierung & Qualitätssicherung

        Unser Beratungspaket umfasst die technische Implementierung, Rollenkonzeption sowie Changemanagement zur Akzeptanzsicherung.
        """)

    elif selected == "Prompting & Jailbreaking":
        st.subheader("Prompting & Jailbreaking")
        st.markdown("""
        **Sicheres Promptdesign – menschlich, robust und verantwortungsvoll**

        LLMs bieten großartige Möglichkeiten – doch die Qualität der Ergebnisse hängt maßgeblich davon ab, wie sie angesprochen werden. Gleichzeitig steigt das Risiko für sogenannte Jailbreaks: gezielte Manipulation der Antwortlogik.

        Unser Angebot „Prompting & Jailbreaking“ vermittelt Ihrem Team:

        ### Was Sie erwartet:
        - Grundlagen des Prompt Engineerings und psychologisch wirksamer Sprachgestaltung
        - Hands-on-Training mit Testprompts, Eskalationsbeispielen und Rollentausch-Simulation
        - Jailbreak-Prävention: Was tun bei Risikoprompts, wie gestalten wir sichere Leitlinien?
        - Erstellung einer hausinternen Prompting-Guideline für ethische und leistungsstabile KI-Nutzung

        Dieses Modul richtet sich an Produktteams, Kommunikationsabteilungen, KI-Admins und alle, die systematisch mit LLMs arbeiten. Es ist auch einzeln buchbar als Intensiv-Workshop.
        """)

# Fallstudie
elif seiten[page] == "fallstudie":
    st.header("Fallstudie: KI als interner Berater bei MüllerTech GmbH")
    st.markdown("""
    Die **MüllerTech GmbH** (300 MA, industrielle Automatisierung) hat externe Beratungsleistungen durch einen internen KI-Agenten ersetzt.

    ### Ergebnisse
    - **Ersparnis:** bis zu 90.000 EUR pro Jahr
    - **Schnellere Entscheidungen** durch datenbasierte Empfehlungen
    - **Mehr Wissen im Unternehmen:** Aufbau interner Daten- und Entscheidungskompetenz

    ### Eingesetzte KI-Module
    - Markt- & Wettbewerbsanalysen
    - SWOT-Bewertungen
    - KPI-Reporting
    - Strategieentwicklung

    ### Organisatorische Umsetzung
    - Schulungen zu Prompt-Engineering
    - AI Champion pro Fachbereich
    - Zentrale Governance-Struktur (Datenschutz, Nachvollziehbarkeit)
    - Verankerung in Innovations- & Nachhaltigkeitsstrategie
    """)

# E-Learning
elif seiten[page] == "elearning":
    st.header("E-Learning & Compliance mit der KI-Verordnung")
    st.markdown("""
    Unser E-Learning-Angebot vermittelt alle Anforderungen der **EU-KI-Verordnung (ab 2025)** – und geht darüber hinaus.

    Ziel ist es, Mitarbeitende und Führungskräfte fit zu machen für den rechtssicheren, ethischen und verantwortungsvollen Umgang mit KI im Berufsalltag.

    Unsere Kurse berücksichtigen verschiedene Rollen im Unternehmen, setzen auf interaktive Lernformate und kombinieren rechtliche Anforderungen mit praxisnahen Beispielen.

    ### Vorteile unseres E-Learnings:
    - Rollenbasierte Lernpfade (für Mitarbeitende, Management, IT, Compliance)
    - KI-gestützter Lern-Coach mit Fortschritts-Tracking
    - Kompatibel mit bestehenden LMS-Systemen
    - Automatische Update-Mechanismen bei Gesetzesänderungen
    - Praxisnahe Checklisten, Use Cases und Selbsttests

    Wählen Sie ein Modul aus, um Details zu den jeweiligen Inhalten zu sehen:
    """)

    modul = st.selectbox("Wählen Sie ein Modul:", ["-",
        "Basismodul E-Learning",
        "Modul: Verantwortung",
        "Modul: Compliance"
    ])

    if modul == "-":
        st.info("In dieser Kategorie finden Sie unser E-Learning-Angebot zur EU-KI-Verordnung. Wählen Sie ein Modul aus, um Details und Inhalte zu entdecken.")

    elif modul == "Basismodul E-Learning":
        st.subheader("Basismodul E-Learning")
        st.markdown("""
        Dieses Modul richtet sich an alle Mitarbeitenden und vermittelt die grundlegenden Prinzipien der KI-Nutzung im Unternehmen:

        ### Inhalte
        - Einführung in die Begriffe der EU-KI-Verordnung (Art. 3-5)
        - Überblick über Risikoklassen (verboten, minimal, hoch)
        - Vermittlung ethischer Leitlinien: Fairness, Transparenz, Vertrauen
        - Risiken: Bias, Blackbox, Datenqualität

        ### Lernformate
        - Interaktive Fallbeispiele
        - Quizfragen zum Verständnis
        - Self-Checks zur Reflexion

        ### Zusätzlich enthalten:
        - „Dos and Don'ts“ im KI-Alltag (Praxisleitfaden)
        - Kommunikationsrichtlinien im Umgang mit KI-Agenten
        - Einführung in empathisches Prompting (für Anwender:innen)

        Ziel ist ein verantwortungsvoller Umgang mit KI und eine breite, praxisnahe Sensibilisierung für deren Chancen und Grenzen.
        """)

    elif modul == "Modul: Verantwortung":
        st.subheader("Modul Anwendung & Verantwortung")
        st.markdown("""
        Dieses Modul richtet sich an Führungskräfte, Projektleitende und Personen mit organisatorischer Verantwortung für KI-gestützte Prozesse.

        ### Inhalte
        - Delegation und Kontrolle: Wer trägt wann Verantwortung?
        - Umgang mit Hochrisiko-KI gemäß Art. 14, 17 und 29
        - Dokumentationspflichten und Meldewege bei Fehlverhalten
        - Risiko-Assessment: Bewertung von Einsatzszenarien
        - Beispiele für gelungene Verantwortungsübernahme durch KI-Begleitung

        ### Erweiterte Inhalte
        - Wie Führung in Mensch-KI-Kollaboration neu gedacht werden muss
        - Fallstricke bei unklaren Zuständigkeiten: juristische und ethische Perspektiven
        - Vorbereitung auf Audits & Compliance Reviews
        - Einführung von KI-Richtlinien auf Abteilungsebene

        ### Lernformate
        - Interaktive Rollenspiele zur Entscheidungssimulation
        - Bewertungsschemata für Risiko- und Verantwortungsverteilung
        - Reflexionsübungen zu ethischen Dilemmata

        Ziel ist die Stärkung von Urteilsvermögen, Rollenklarheit und Verantwortungsbewusstsein in digitalen Führungsstrukturen.
        """)

    elif modul == "Modul: Compliance":
        st.subheader("Modul Technologie & Compliance")
        st.markdown("""
        Dieses Modul richtet sich an Entwickler:innen, IT-Expert:innen und Data Scientists, die für KI-Systeme verantwortlich sind.

        ### Inhalte
        - Umsetzung der KI-Verordnung in technische Anforderungen (Art. 9, 10, 13)
        - Anforderungen an Trainingsdaten, Systemrobustheit und Datenqualität
        - Transparenzpflichten, technische Auditierbarkeit, Versionsmanagement
        - Integration in bestehende IT-Architekturen & MLOps-Prozesse
        - Grenzfälle, Herausforderungen und Lösungsansätze in der Praxis

        ### Erweiterte Inhalte
        - Umgang mit komplexen Datenabhängigkeiten & automatisierter Dokumentation
        - Strategien zur Nachvollziehbarkeit bei Deep Learning Modellen
        - Etablierung kontinuierlicher Prüf- & Updateprozesse
        - Zusammenarbeit zwischen IT, Datenschutz und Recht
        - Aufbau eines internen Auditleitfadens zur regelmäßigen Selbstüberprüfung

        ### Lernformate
        - Codebeispiele & Konformitäts-Checklisten
        - Hands-on-Übungen zur Datenverarbeitung & Risikobewertung
        - Szenarienbasierte Problemanalyse (Bias, Intransparenz, Fehlererkennung)
        - Fallstudien aus der Praxis inkl. Lessons Learned

        Ziel ist die rechtssichere und zukunftsorientierte Entwicklung sowie Überwachung von KI-Systemen im regulierten Umfeld.
        """)

# Kontakt
elif seiten[page] == "kontakt":
    st.header("Kontakt")
    st.markdown("""
    Sie möchten eine Demo, ein Beratungsgespräch oder direkt starten?

    **E-Mail:** kontakt@inkiline.ai  
    **Telefon:** +49 123 456 7890  
    **Adresse:** Innovationszentrum KI, Musterstadt

    Wir freuen uns auf den Austausch!
    """)


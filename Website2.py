import streamlit as st

st.set_page_config(page_title="InKIline - Digitale Organisationsberatung", layout="wide")

# --- CLEAN CSS ---
st.markdown("""
<style>
body, .stApp, .main, .block-container {
    background: #f6f9fc !important;
    color: #1a405d !important;
}
.navbar-inkiline {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2.6em;
    background: #fff !important;
    border-bottom: 1.5px solid #d7e8f6;
    padding: 0.85em 0 0.7em 0;
    margin-bottom: 2.1em;
}
.navbar-logo {
    font-weight: 900;
    color: #004D7A !important;
    font-size: 2.1em;
    letter-spacing: -1px;
    margin-right: 2.5em;
}
.navbar-link {
    font-size: 1.11em;
    color: #1a405d !important;
    text-decoration: none;
    font-weight: 600;
    letter-spacing: 0.5px;
    padding-bottom: 0.13em;
    border-bottom: 2.5px solid transparent;
    transition: border-color 0.2s, color 0.2s;
    background: none !important;
}
.navbar-link.selected, .navbar-link:focus, .navbar-link:hover {
    border-bottom: 2.5px solid #207abc;
    color: #207abc !important;
}
.contact-btn {
    margin-left: 2em;
    background: linear-gradient(90deg, #207abc 60%, #49a6e9 100%) !important;
    color: #fff !important;
    border-radius: 2em;
    padding: 0.54em 1.3em;
    font-weight: 700;
    font-size: 1.07em;
    text-decoration: none;
    box-shadow: 0 2px 16px #b8d7f8a0;
    border: none;
    display: flex;
    align-items: center;
    gap: 0.4em;
}
.content-card {
    background: #fff !important;
    border-radius: 1.1em;
    box-shadow: 0 3px 14px 0 #e2eefd8c;
    padding: 2.2em 2em 1.7em 2em;
    margin-bottom: 1.7em;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    color: #1a405d !important;
}
.highlight-box {
    background-color: #f0f9ff !important;
    color: #207abc !important;
    padding: 1.2em 1em;
    border-left: 5px solid #007ACC;
    border-radius: 0.55em;
    margin-bottom: 1.2em;
}
h1, h2, h3, h4, h5, h6 {
    color: #004D7A !important;
}
a, .navbar-link, .contact-btn {
    color: #207abc !important;
}
.benefit-list li::marker {
    color: #007ACC !important;
}
@media (max-width: 800px) {
    .navbar-inkiline {flex-direction: column; gap:1em;}
    .navbar-logo {margin-bottom:0.4em;}
}
@media (max-width: 600px) {
    .content-card {padding:1em;}
    .navbar-logo {font-size:1.2em;}
}
</style>
""", unsafe_allow_html=True)

# --- Menüstruktur ---
MENUS = [
    "Startseite",
    "Angebotsportfolio",
    "Fallstudie",
    "E-Learning & KI-Verordnung",
    "Kontakt"
]

# Menüstatus im Session State
if "page" not in st.session_state:
    st.session_state.page = MENUS[0]

def render_navbar(selected):
    navbar_html = '<div class="navbar-inkiline">'
    navbar_html += '<span class="navbar-logo">InKIline</span>'
    for menu in MENUS:
        is_selected = "selected" if menu == selected else ""
        navbar_html += f'<a class="navbar-link {is_selected}" href="#{menu}">{menu}</a>'
    # Kontaktieren-Button immer sichtbar (führt zur Kontaktseite)
    navbar_html += f'<a class="contact-btn" href="#Kontakt">📩 Kontaktieren</a>'
    navbar_html += '</div>'
    st.markdown(navbar_html, unsafe_allow_html=True)

# Navigation: Nach Klick auf Menü oder Button Seite wechseln
import urllib.parse
query_params = st.query_params if hasattr(st, "query_params") else {}
hash_page = query_params.get('', [''])[0] if '' in query_params else None
if hash_page:
    # Hash aus der URL holen und als aktives Menü setzen
    decoded = urllib.parse.unquote(hash_page.replace("#", ""))
    if decoded in MENUS:
        st.session_state.page = decoded

render_navbar(st.session_state.page)

# ----------- Inhalte -------------

if st.session_state.page == "Startseite":
    st.markdown("""
    <div class="content-card">
        <h1>InKIline – Digitale Organisationsberatung</h1>
        <h3 style="color:#207abc; font-weight:500; margin-bottom:1.4em;">Veränderung beginnt nicht mit Technologie, sondern mit Kultur.</h3>
        <div class="highlight-box">
            Willkommen auf der offiziellen Seite von <b>InKIline</b> – Ihrer Partnerin für systemische, menschenzentrierte KI-Transformation.<br><br>
            KI ist nicht nur ein Tool – sie ist Akteur, Katalysator und Kulturwandler.
            <br><br>
            <b>Unsere Mission</b><br>
            Wir helfen Unternehmen, KI verantwortungsvoll, wirksam und nachhaltig in ihre Organisationen zu integrieren – von der Change-Begleitung bis zur internen Beratung durch KI-Agenten.
            <br><br>
            <b>Was uns besonders macht</b>
            <ul class="benefit-list">
                <li><b>Systemische Perspektive:</b> Wir kombinieren Organisationsentwicklung mit KI-Kompetenz.</li>
                <li><b>Praxisnähe:</b> Alle unsere Lösungen wurden in realen Szenarien getestet und verfeinert.</li>
                <li><b>Modular & skalierbar:</b> Vom Workshop bis zur Prozessintegration – wir liefern passgenau.</li>
                <li><b>Ethik im Fokus:</b> Unser Design orientiert sich an Vertrauen, Verantwortung und Fairness.</li>
            </ul>
            Gemeinsam gestalten wir KI-Einführungen, die wirken – technisch, menschlich und wirtschaftlich.
            <hr>
            <b>Kundenstimmen</b><br>
            <i>"Durch InKIline haben wir KI nicht nur implementiert, sondern wirklich verstanden und in unsere Kultur integriert."<br>– Lena M., HR-Leiterin eines Industrieunternehmens</i><br>
            <i>"Besonders beeindruckt hat uns das ethisch reflektierte Vorgehen in Kombination mit klarer Umsetzungskompetenz."<br>– Dr. Jonas K., CIO eines Gesundheitsdienstleisters</i>
            <hr>
            <b>Jetzt unverbindlich starten:</b> Klicken Sie auf "📩 Kontaktieren", um mehr über Pilotprojekte, Workshopformate und maßgeschneiderte Lösungen zu erfahren.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Angebotsportfolio":
    st.markdown("""
    <div class="content-card">
        <h2>Unser Leistungsportfolio</h2>
        <p>
        Unsere Leistungen richten sich an Unternehmen, die KI ganzheitlich einführen wollen – nicht nur als Technologie, sondern als strategischen Partner.<br>
        Unser Portfolio kombiniert systemische Beratung, technische Kompetenz und kulturelle Begleitung.<br>
        Wählen Sie ein Themenfeld für weitere Details:
        </p>
    """, unsafe_allow_html=True)

    thema = st.selectbox("Themenfeld wählen", [
        "KI Change Management",
        "KI-Agenten im Team",
        "Framing & Narrative",
        "Interne KI-Beratung",
        "Prompting & Jailbreaking"
    ])

    if thema == "KI Change Management":
        st.markdown("""
        <div class="content-card">
            <h3>KI Change Management</h3>
            <p>
                Unser Angebot „KI Change Management“ ist darauf ausgelegt, Unternehmen strukturiert, kulturbewusst und wirkungsvoll durch KI-Transformationsprozesse zu begleiten.<br>
                <b>Unser Angebot umfasst:</b>
                <ul>
                    <li>Individuelle Analyse der kulturellen Ausgangslage und Reifegrade</li>
                    <li>Entwicklung eines maßgeschneiderten 6-Phasen-Modells</li>
                    <li>Methodenmix aus Workshops, Coachings, Kommunikationstemplates</li>
                    <li>Begleitende interne Kampagne zur Akzeptanzsteigerung (optional)</li>
                </ul>
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif thema == "KI-Agenten im Team":
        st.markdown("""
        <div class="content-card">
            <h3>KI-Agenten als Kollegen</h3>
            <p>
                Unsere Beratung befähigt Unternehmen dazu, KI-Agenten nicht nur als technische Helfer, sondern als digitale Teammitglieder zu gestalten.<br>
                <b>Wir bieten an:</b>
                <ul>
                    <li>Prozessanalyse & Beratung zur sinnvollen Integration von KI</li>
                    <li>Entwicklung interaktiver Rollenprofile für KI-Agenten</li>
                    <li>Strategien zur Koexistenz von Mensch und KI</li>
                </ul>
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif thema == "Framing & Narrative":
        st.markdown("""
        <div class="content-card">
            <h3>Framing & Narrative für KI</h3>
            <p>
                Wir helfen Ihnen dabei, KI als akzeptiertes und vertrautes Element Ihrer Unternehmenskultur zu etablieren.<br>
                <b>Wir bieten an:</b>
                <ul>
                    <li>Analyse Ihrer bestehenden internen KI-Kommunikation</li>
                    <li>Entwicklung von Narrativen, die Vertrauen schaffen</li>
                    <li>Trainings für empathisches Promptdesign</li>
                </ul>
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif thema == "Interne KI-Beratung":
        st.markdown("""
        <div class="content-card">
            <h3>Interne KI-Beratung</h3>
            <p>
                KI-Agenten ersetzen zunehmend klassische Beratungsleistungen.<br>
                <b>Vorteile für Unternehmen:</b>
                <ul>
                    <li>Reduktion externer Beraterkosten</li>
                    <li>Schnellere Entscheidungsfindung</li>
                    <li>Wissen bleibt im Unternehmen</li>
                </ul>
                <b>Einsatzbereiche:</b> Markt- & Wettbewerbsanalysen, SWOT, KPI-Monitoring, Strategieentwicklung.
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif thema == "Prompting & Jailbreaking":
        st.markdown("""
        <div class="content-card">
            <h3>Prompting & Jailbreaking</h3>
            <p>
                <b>Sicheres Promptdesign – menschlich, robust und verantwortungsvoll</b><br>
                Grundlagen des Prompt Engineerings, Hands-on-Training, Jailbreak-Prävention und hausinterne Prompting-Guidelines.
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "Fallstudie":
    st.markdown("""
    <div class="content-card">
        <h2>Fallstudie: KI als interner Berater bei MüllerTech GmbH</h2>
        <ul>
            <li><b>Ersparnis:</b> bis zu 90.000 EUR pro Jahr</li>
            <li><b>Schnellere Entscheidungen</b> durch datenbasierte Empfehlungen</li>
            <li><b>Mehr Wissen im Unternehmen:</b> Aufbau interner Kompetenz</li>
        </ul>
        <b>Umsetzung:</b>
        <ul>
            <li>Schulungen zu Prompt-Engineering</li>
            <li>AI Champion pro Fachbereich</li>
            <li>Zentrale Governance-Struktur</li>
            <li>Verankerung in Innovations- & Nachhaltigkeitsstrategie</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "E-Learning & KI-Verordnung":
    st.markdown("""
    <div class="content-card">
        <h2>E-Learning & Compliance mit der KI-Verordnung</h2>
        <p>
            Unser E-Learning-Angebot vermittelt alle Anforderungen der <b>EU-KI-Verordnung</b> (ab 2025) – und geht darüber hinaus.
            <br><br>
            <b>Vorteile:</b> Rollenbasierte Lernpfade, KI-gestützter Lern-Coach, LMS-kompatibel, automatische Updates, Praxis-Checklisten.
        </p>
    """, unsafe_allow_html=True)

    modul = st.selectbox("Wählen Sie ein Modul", [
        "Basismodul E-Learning",
        "Modul: Verantwortung",
        "Modul: Compliance"
    ])

    if modul == "Basismodul E-Learning":
        st.markdown("""
        <div class="content-card">
            <h3>Basismodul E-Learning</h3>
            <ul>
                <li>Grundlagen der KI-Verordnung</li>
                <li>Überblick über Risikoklassen</li>
                <li>Ethische Leitlinien</li>
                <li>Risiken: Bias, Blackbox, Datenqualität</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    elif modul == "Modul: Verantwortung":
        st.markdown("""
        <div class="content-card">
            <h3>Modul Anwendung & Verantwortung</h3>
            <ul>
                <li>Delegation und Kontrolle</li>
                <li>Umgang mit Hochrisiko-KI</li>
                <li>Dokumentationspflichten</li>
                <li>Risiko-Assessment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    elif modul == "Modul: Compliance":
        st.markdown("""
        <div class="content-card">
            <h3>Modul Technologie & Compliance</h3>
            <ul>
                <li>Technische Umsetzung der KI-Verordnung</li>
                <li>Anforderungen an Trainingsdaten & Robustheit</li>
                <li>Transparenzpflichten, Auditierbarkeit</li>
                <li>Integration in IT-Architekturen</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "Kontakt":
    st.markdown("""
    <div class="content-card">
        <h2>Kontakt</h2>
        <p>Sie möchten eine Demo, ein Beratungsgespräch oder direkt starten?</p>
        <b>E-Mail:</b> kontakt@inkiline.ai<br>
        <b>Telefon:</b> +49 123 456 7890<br>
        <b>Adresse:</b> Innovationszentrum KI, Musterstadt<br>
        <br>
        <i>Wir freuen uns auf den Austausch!</i>
    </div>
    """, unsafe_allow_html=True)

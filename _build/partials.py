"""Partials (Header, Footer, Meta) für die AFR-Website.

Hier zentral aenderbar. Nach Anpassung `python3 build.py` ausfuehren,
um alle HTML-Seiten neu zu generieren.
"""

SITE_NAME = "AFR Inkassokanzlei Joachim Siebert e.K."
SITE_TAGLINE = "Allgemeine Forderungs-Regulierung"
SITE_URL = "https://www.afr-inkasso.de"

CONTACT = {
    "company": "AFR Inkassokanzlei Joachim Siebert e.K.",
    "street": "Jeggener Str. 1a",
    "plz_city": "49143 Bissendorf",
    "tel": "+49 5402 9906-0",
    "tel_link": "tel:+4954029906-0",
    "fax": "+49 5402 9906-18",
    "mail": "info@afr-inkasso.de",
    "hours": [
        ("Montag – Donnerstag", "08:30 – 12:30 Uhr"),
        ("", "13:15 – 16:45 Uhr"),
        ("Freitag", "08:30 – 15:15 Uhr"),
    ],
}

NAV = [
    {"label": "Start", "href": "index.html", "file": "index.html"},
    {"label": "Leistungen", "href": "leistungen.html", "file": "leistungen.html",
     "sub": [
        {"label": "Forderungseinzug", "href": "leistungen.html#forderungseinzug"},
        {"label": "Auskünfte", "href": "leistungen.html#auskuenfte"},
        {"label": "Unternehmensberatung", "href": "leistungen.html#unternehmensberatung"},
        {"label": "Mahnservice", "href": "leistungen.html#mahnservice"},
        {"label": "Auslandsinkasso", "href": "leistungen.html#auslandsinkasso"},
     ]},
    {"label": "Auftragserteilung", "href": "auftragserteilung.html", "file": "auftragserteilung.html"},
    {"label": "Kosten", "href": "kosten.html", "file": "kosten.html"},
    {"label": "Über uns", "href": "ueber-uns.html", "file": "ueber-uns.html"},
    {"label": "Kontakt", "href": "kontakt.html", "file": "kontakt.html", "cta": True},
]


def head(title, description, page_file):
    canonical = f"{SITE_URL}/{page_file if page_file != 'index.html' else ''}"
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – AFR Inkassokanzlei Joachim Siebert</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<meta property="og:title" content="{title} – AFR Inkassokanzlei Joachim Siebert">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/logo.png">
<meta property="og:locale" content="de_DE">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="assets/css/styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "AFR Inkassokanzlei Joachim Siebert e.K.",
  "image": "{SITE_URL}/assets/img/logo.png",
  "url": "{SITE_URL}",
  "telephone": "+49 5402 9906-0",
  "email": "info@afr-inkasso.de",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Jeggener Str. 1a",
    "postalCode": "49143",
    "addressLocality": "Bissendorf",
    "addressCountry": "DE"
  }},
  "openingHoursSpecification": [
    {{ "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday"],
       "opens": "08:30", "closes": "16:45" }},
    {{ "@type": "OpeningHoursSpecification", "dayOfWeek": "Friday",
       "opens": "08:30", "closes": "15:15" }}
  ],
  "areaServed": "DE",
  "priceRange": "€€"
}}
</script>
</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
"""


def header():
    # Hauptnav (Desktop)
    nav_items = []
    for item in NAV:
        cls = "nav-cta" if item.get("cta") else "nav-link"
        attr = f'data-nav="{item.get("file","")}"'
        if "sub" in item:
            sub_lis = "\n".join(
                f'        <li><a class="nav-link" href="{s["href"]}">{s["label"]}</a></li>'
                for s in item["sub"]
            )
            nav_items.append(f"""    <li class="nav-item-has-sub">
      <a class="{cls}" {attr} href="{item['href']}">{item['label']}</a>
      <ul class="nav-sub">
{sub_lis}
      </ul>
    </li>""")
        else:
            nav_items.append(f'    <li><a class="{cls}" {attr} href="{item["href"]}">{item["label"]}</a></li>')
    desktop_nav = "\n".join(nav_items)

    # Mobile Nav
    mobile_items = []
    for item in NAV:
        attr = f'data-nav="{item.get("file","")}"'
        if "sub" in item:
            sub_lis = "\n".join(f'        <li><a {attr} href="{s["href"]}">{s["label"]}</a></li>' for s in item["sub"])
            mobile_items.append(f'      <li><a href="{item["href"]}" {attr}>{item["label"]}</a>\n        <ul>\n{sub_lis}\n        </ul>\n      </li>')
        else:
            mobile_items.append(f'      <li><a href="{item["href"]}" {attr}>{item["label"]}</a></li>')
    mobile_nav = "\n".join(mobile_items)

    return f"""<header class="site-header" role="banner">
  <div class="header-inner">
    <a class="brand" href="index.html" aria-label="Zur Startseite">
      <img src="assets/img/logo-300.png" alt="AFR Inkassokanzlei Logo" width="150" height="54">
      <div class="brand-text">{SITE_NAME.split(' ', 0)[0] if False else 'AFR Inkassokanzlei'}<small>Joachim Siebert e.K.</small></div>
    </a>
    <nav class="nav" aria-label="Hauptnavigation">
      <ul class="nav-list">
{desktop_nav}
      </ul>
    </nav>
    <button class="menu-toggle" aria-label="Menü öffnen" aria-expanded="false" aria-controls="mobile-nav">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
  </div>
  <nav id="mobile-nav" class="mobile-nav" aria-label="Mobile Navigation">
    <ul>
{mobile_nav}
    </ul>
  </nav>
</header>
"""


def footer():
    hours_rows = "\n".join(
        f"          <tr><td>{day}</td><td>{time}</td></tr>"
        for (day, time) in CONTACT["hours"]
    )
    return f"""<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo.png" alt="AFR Inkassokanzlei Logo" width="200">
        <p>Allgemeine Forderungs-Regulierung – fachmännisches Inkasso für Unternehmen, Gewerbetreibende und Freiberufler. Seit über 25 Jahren.</p>
      </div>
      <div>
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">Start</a></li>
          <li><a href="leistungen.html">Leistungen</a></li>
          <li><a href="auftragserteilung.html">Auftragserteilung</a></li>
          <li><a href="kosten.html">Kosten &amp; Gebühren</a></li>
          <li><a href="ueber-uns.html">Über uns</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
        </ul>
      </div>
      <div>
        <h4>Rechtliches</h4>
        <ul>
          <li><a href="agb.html">AGB</a></li>
          <li><a href="impressum.html">Impressum</a></li>
          <li><a href="datenschutz.html">Datenschutzerklärung</a></li>
          <li><a href="fragen-und-anregungen.html">Fragen &amp; Anregungen</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <p>
          <strong>{CONTACT['company']}</strong><br>
          {CONTACT['street']}<br>
          {CONTACT['plz_city']}<br>
          <br>
          Tel.: <a href="{CONTACT['tel_link']}">{CONTACT['tel']}</a><br>
          Fax: {CONTACT['fax']}<br>
          E-Mail: <a href="mailto:{CONTACT['mail']}">{CONTACT['mail']}</a>
        </p>
        <h4 style="margin-top:1.25rem">Bürozeiten</h4>
        <table class="hours-table" style="color:#cbd5e1">
{hours_rows}
        </table>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© <span id="year">2026</span> AFR Inkassokanzlei Joachim Siebert e.K. – Alle Rechte vorbehalten.</div>
      <div>
        <a href="impressum.html">Impressum</a> ·
        <a href="datenschutz.html">Datenschutz</a> ·
        <a href="agb.html">AGB</a>
      </div>
    </div>
  </div>
</footer>
<div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="Cookie-Hinweis">
  <strong>Cookies &amp; Datenschutz</strong>
  <p style="margin:0.5rem 0 0">
    Wir verwenden technisch notwendige Cookies. Weitere Informationen finden Sie in unserer
    <a href="datenschutz.html">Datenschutzerklärung</a>.
  </p>
  <div class="cookie-banner-actions">
    <button class="btn btn-primary" data-cookie-accept type="button">Verstanden</button>
  </div>
</div>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

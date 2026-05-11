# AFR Inkassokanzlei – Website

Statische Website für www.afr-inkasso.de. Reines HTML/CSS/JS, kein Backend nötig.

## Auf einen Blick

- **Tech-Stack:** statisches HTML, ein eigenes CSS-Stylesheet, eine kleine JS-Datei. Kein Build-Schritt nötig, um die Seite zu deployen.
- **11 Seiten:** Startseite, Leistungen (eine Seite mit 5 Abschnitten), Auftragserteilung, Kosten, Über uns, Kontakt, Impressum, Datenschutz, AGB, Fragen & Anregungen, 404.
- **Inhalte:** Übernommen aus dem Wayback-Machine-Snapshot vom 12.08.2025 (letzter erreichbarer Stand der alten WordPress-Seite). Layout/Design wurden neu gestaltet.

## Verzeichnisstruktur

```
site/
├── index.html
├── leistungen.html
├── auftragserteilung.html
├── kosten.html
├── ueber-uns.html
├── kontakt.html
├── impressum.html
├── datenschutz.html
├── agb.html
├── fragen-und-anregungen.html
├── 404.html
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   └── img/  (Logo + Favicons)
├── _build/   ← Generator-Skripte (NICHT mit hochladen, nur zur Pflege)
│   ├── build.py
│   └── partials.py
└── README.md (diese Datei)
```

## Lokal anschauen

```bash
cd site
python3 -m http.server 8765
# dann im Browser: http://localhost:8765/
```

## Inhalte ändern

**Variante A – einzelne Seite direkt im HTML bearbeiten (einfach):**

Jede `.html`-Datei im `site/`-Verzeichnis ist eigenständig und kann direkt im Editor bearbeitet werden. Suchen Sie z.B. nach „Jeggener Str.“ oder „05402“, um Kontaktdaten zu ändern.

**Variante B – über das Build-Skript (sauberer bei größeren Änderungen):**

Alle Inhalte und Komponenten liegen zentral in `_build/build.py` und `_build/partials.py`. Nach Änderungen:

```bash
cd site/_build
python3 build.py
```

Die HTML-Dateien werden dann komplett neu generiert.

## Deployment auf Hetzner konsoleH

1. In der Hetzner konsoleH **WebFTP** öffnen (oder einen FTP-Client wie FileZilla mit den FTP-Zugangsdaten benutzen).
2. In den Ordner `public_html/` wechseln.
3. **Inhalt des `site/`-Verzeichnisses** (ohne `_build/` und ohne diese README) komplett hochladen:
   - alle `.html`-Dateien
   - den `assets/`-Ordner mitsamt Unterordnern
4. Aufrufen: <https://www.afr-inkasso.de>.

**Wichtig:** Die `_build/`-Dateien NICHT hochladen. Sie werden auf dem Server nicht gebraucht und enthalten Generator-Code.

## To-Dos / mit Joachim zu klären

- [ ] **Postleitzahl:** In den alten Snapshots steht im Impressum **49143 Bissendorf**, in anderen Quellen (Suchergebnisse) jedoch **49139**. Aktuell verwendet die neue Seite **49143**. Bitte prüfen, was korrekt ist.
- [ ] **Herr Niebaum:** Auf der „Über uns“-Seite wird neben Joachim Siebert auch ein „Herr Niebaum“ als Volljurist genannt. Ist er noch in der Kanzlei tätig? Wenn nein, in `_build/build.py` bei der Funktion `ueber_uns_html` entfernen.
- [ ] **RDG-Aktenzeichen:** Az. beim Bundesamt für Justiz **2024 0001 0754** – noch aktuell?
- [ ] **Kontaktformular-Verarbeitung:** Aktuell öffnet das Kontaktformular das E-Mail-Programm des Nutzers (`mailto:`). Funktioniert in allen Browsern, ist aber für Nutzer ohne installiertes Mail-Programm umständlich. **Empfehlung:** auf einen Formular-Dienst wie [Formspree](https://formspree.io/) (kostenlos für geringe Volumen) oder [Web3Forms](https://web3forms.com/) umstellen. Ein kurzer Konfigurationsänderung in `kontakt.html` reicht dann.
- [ ] **AGB-Inhalte:** Die alten AGB konnten nicht vollständig rekonstruiert werden. Aktuell stehen sinnvolle Standardklauseln plus ein Hinweis, dass die verbindliche Fassung per E-Mail angefordert werden soll. Bitte vom alten AGB-PDF die echte Fassung übernehmen, sobald sie wieder verfügbar ist.
- [ ] **SSL-Zertifikat:** In Hetzner konsoleH ein Let's-Encrypt-Zertifikat für `afr-inkasso.de` und `www.afr-inkasso.de` aktivieren (kostenlos, ein Klick im Hetzner-Menü).
- [ ] **DNS / Domain:** Sicherstellen, dass die Domain auf den neuen Hetzner-Server zeigt.

## Browser-Support

Die Seite läuft in allen modernen Browsern (Chrome, Firefox, Safari, Edge ab 2020). IE11 wird **nicht** unterstützt — würde sich nicht lohnen.

## Performance

- Seitengröße: 8–17 KB pro Seite (HTML)
- 1 CSS-Datei (~9 KB)
- 1 JS-Datei (<1 KB)
- Logo als PNG (~150 KB für Hi-Res, ~16 KB für die kleine Version im Header)
- Keine externen Schriften oder Tracker

LCP/FCP sollten auf 4G unter 1 Sekunde liegen.

---

Bei Fragen / Anpassungswünschen: Victor.

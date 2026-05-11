"""Build-Skript für die AFR-Inkasso Website.

Alle inhaltlichen Texte stammen 1:1 aus dem Wayback-Machine-Snapshot
der alten Seite (zuletzt erreichbar 12.08.2025). Es werden KEINE
inhaltlichen Aussagen erfunden oder dazugedichtet.

Strukturelle/funktionale Texte (Buttons, Skip-Links, ARIA-Labels) sind
neutral formuliert.
"""

from pathlib import Path
import partials as P

OUT = Path(__file__).resolve().parent.parent  # site/


def page_header(breadcrumb_html, title, subtitle=""):
    sub = f'<p>{subtitle}</p>' if subtitle else ''
    return f"""<section class="page-header">
  <div class="container">
    <div class="breadcrumbs">{breadcrumb_html}</div>
    <h1>{title}</h1>
    {sub}
  </div>
</section>
"""


# -----------------------------------------------------------------------------
#  Page contents
# -----------------------------------------------------------------------------

def index_html():
    # Hero-Text ist 1:1 aus dem Original (siehe wayback/content/index.md)
    body = """<main id="main">
  <section class="hero">
    <div class="container hero-inner">
      <span class="hero-eyebrow">Allgemeine Forderungs-Regulierung</span>
      <h1>Inkassokanzlei Joachim Siebert</h1>
      <p class="hero-claim">Das Ziel stets fest im Blick</p>
    </div>
  </section>

  <section class="section">
    <div class="container container-narrow">
      <p class="lead"><strong>Willkommen bei der Inkassokanzlei Joachim Siebert; Volljurist.</strong></p>
      <p>Wir bieten Unternehmen, Gewerbetreibenden und Freiberuflern fachmännische Hilfe rund um das Inkasso. Mit unserem qualifizierten Team und individueller Bearbeitung Ihrer Forderungen erreichen wir bereits im vorgerichtlichen Bereich überdurchschnittliche Erfolgsquoten!</p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="grid grid-3">

        <article class="card">
          <h3><a href="leistungen.html" style="text-decoration:none; color:inherit">Leistungen</a></h3>
          <p>Forderungseinzug, Auskünfte, Unternehmensberatung, Mahnservice, Auslandsinkasso</p>
          <a class="card-link" href="leistungen.html">mehr</a>
        </article>

        <article class="card">
          <h3><a href="auftragserteilung.html" style="text-decoration:none; color:inherit">Auftragserteilung</a></h3>
          <p>In Ihrem Interesse gehen wir so unbürokratisch vor wie möglich! Sie haben mehrere Möglichkeiten.</p>
          <a class="card-link" href="auftragserteilung.html">mehr</a>
        </article>

        <article class="card">
          <h3><a href="kosten.html" style="text-decoration:none; color:inherit">Kosten &amp; Gebühren</a></h3>
          <p>Schlechtem Geld sollte man kein gutes hinterherwerfen!</p>
          <a class="card-link" href="kosten.html">mehr</a>
        </article>

      </div>
    </div>
  </section>
</main>
"""
    return P.head("Startseite", "AFR Inkassokanzlei Joachim Siebert – Allgemeine Forderungs-Regulierung. Bissendorf.", "index.html") + P.header() + body + P.footer()


def leistungen_html():
    # Alle Texte 1:1 aus den Original-Unterseiten (Forderungseinzug, Auskünfte, Unternehmensberatung, Mahnservice, Auslandsinkasso)
    body = """<main id="main">
""" + page_header('<a href="index.html">Start</a> · Leistungen', 'Leistungen') + """

  <section id="forderungseinzug" class="section">
    <div class="container container-narrow">
      <h2>Forderungseinzug</h2>
      <p>Pauschalierte Massenverfahren sind nicht unsere Sache! Wir setzen auf individuelle Bearbeitung und Beratung, um in jedem Einzelfall zu adäquaten Lösungen zu gelangen. Dies ist besonders im Business-To-Business-Bereich, aber auch im Zusammenhang mit anspruchsvollen Forderungen gegen Privatpersonen interessant.</p>

      <h3>Vorgerichtlicher Forderungseinzug</h3>
      <p><strong>Unsere Arbeitsweise:</strong></p>
      <ul>
        <li><strong>Individuell:</strong> Persönliche Kontaktaufnahme zum Schuldner unter Berücksichtigung seiner finanziellen Situation.</li>
        <li><strong>Kundenerhaltend:</strong> Auf Wunsch suchen wir gemeinsam mit Ihnen und Ihrem Schuldner nach einer Lösung und arbeiten – besonders im B2B-Bereich – unter größtmöglicher Schonung Ihrer Geschäftsbeziehung, ohne dabei den nötigen Nachdruck zu vernachlässigen.</li>
        <li><strong>Wirtschaftlich:</strong> Stetige Kosten-Nutzen-Kontrolle aus der Sicht des Mandanten.</li>
      </ul>

      <p><strong>Unsere Leistung – Ihr Vorteil:</strong></p>
      <ul>
        <li>Unbürokratische Auftragserteilung</li>
        <li>Unverzügliche Auftragserfassung und -bearbeitung</li>
        <li>Vereinbarung und Überwachung von Ratenzahlungen, Vergleichen, Stundungen etc.</li>
        <li>Zeitnahe Auskehrung eingezogener Beträge, auch bei Ratenzahlungen</li>
        <li>Sachstandsberichte (nach Bedarf) und telefonische Sachstandsauskünfte (jederzeit und kostenlos)</li>
        <li>Gerichtliche Titulierung nur nach vorheriger Abstimmung mit dem Mandanten und nach umfassender Vorabinformation über voraussichtliche Kosten und Erfolgsaussichten</li>
        <li>Zwangsvollstreckung in zuvor ermittelte Vermögenswerte</li>
        <li>Vorantreiben des Verfahrens bis zur Abrechenbarkeit mit dem Rückversicherer</li>
        <li>Forderungsanmeldung im Insolvenzverfahren des Schuldners</li>
        <li>Geltendmachung der Mandantenrechte aus dem Eigentumsvorbehalt oder anderen Sicherungsrechten</li>
        <li>Erstattung von Strafanzeigen</li>
      </ul>

      <h3>Nachgerichtlicher Forderungseinzug</h3>
      <p><strong>Langfristige Überwachung bisher erfolglos vollstreckter Forderungen.</strong></p>

      <p><strong>Unsere Arbeitsweise:</strong></p>
      <ul>
        <li><strong>Individuell:</strong> Persönliche Kontaktaufnahme zum Schuldner unter Berücksichtigung seiner finanziellen Situation.</li>
        <li><strong>Kundenerhaltend:</strong> Auf Wunsch suchen wir gemeinsam mit Ihnen und Ihrem Schuldner nach einer Lösung und arbeiten – besonders im B2B-Bereich – unter größtmöglicher Schonung Ihrer Geschäftsbeziehung, ohne dabei den nötigen Nachdruck zu vernachlässigen.</li>
        <li><strong>Wirtschaftlich:</strong> Stetige Kosten-Nutzen-Kontrolle aus der Sicht des Mandanten.</li>
      </ul>

      <p><strong>Unsere Leistung – Ihr Vorteil:</strong></p>
      <ul>
        <li>Unbürokratische Auftragserteilung</li>
        <li>Unverzügliche Auftragserfassung und -bearbeitung</li>
        <li>Vereinbarung und Überwachung von Ratenzahlungen, Vergleichen, Stundungen etc.</li>
        <li>Zeitnahe Auskehrung eingezogener Beträge, auch bei Ratenzahlungen</li>
        <li>Sachstandsberichte (nach Bedarf) und telefonische Sachstandsauskünfte (jederzeit und kostenlos)</li>
        <li>Übernahme des gesamten Kostenrisikos (für Ermittlungs-, Überwachungs-, Zwangsvollstreckungskosten etc.) durch uns</li>
        <li>Zwangsvollstreckung in zuvor ermittelte Vermögenswerte</li>
        <li>Vorantreiben des Verfahrens bis zur Abrechenbarkeit mit dem Rückversicherer</li>
        <li>Forderungsanmeldung im Insolvenzverfahren des Schuldners</li>
        <li>Geltendmachung der Mandantenrechte aus dem Eigentumsvorbehalt oder anderen Sicherungsrechten</li>
        <li>Erstattung von Strafanzeigen</li>
      </ul>
    </div>
  </section>

  <section id="auskuenfte" class="section section-alt">
    <div class="container container-narrow">
      <h2>Auskünfte</h2>
      <p>Aktualität ist Trumpf! Wir setzen nicht auf Datenbanken mit möglicherweise veraltetem Datenbestand, sondern auf Ermittlung des aktuellen Sachstands zum Anfragezeitpunkt.</p>
      <ul>
        <li>Einholung des Bonitätsstatus durch aktuelle Ermittlungen der uns angeschlossenen Wirtschaftsdetektei</li>
        <li>Personensuche</li>
        <li>Vermögenssuche</li>
      </ul>
    </div>
  </section>

  <section id="unternehmensberatung" class="section">
    <div class="container container-narrow">
      <h2>Unternehmensberatung</h2>
      <p>Nutzen Sie unser Know-How zur Optimierung Ihres Forderungsmanagements!</p>
      <ul>
        <li>Beratung, Optimierung und ggfls. Neustrukturierung des betrieblichen Mahnwesens</li>
        <li>Prüfung von Versicherungsverträgen unter Kosten-Nutzen-Gesichtspunkten</li>
        <li>Treuhänderische Vermögensverwaltung</li>
      </ul>
    </div>
  </section>

  <section id="mahnservice" class="section section-alt">
    <div class="container container-narrow">
      <h2>Mahnservice</h2>
      <p>Ein effektives und straff organisiertes Mahnwesen ist der erste Schritt zur Durchsetzung Ihrer Forderungen!</p>
      <p>Übernahme des betrieblichen Mahnwesens in verschiedenen Abstufungen als Angebot zum Outsourcing.</p>
    </div>
  </section>

  <section id="auslandsinkasso" class="section">
    <div class="container container-narrow">
      <h2>Auslandsinkasso</h2>
      <p>Andere Länder, andere Sitten! Wir verfolgen Ihre Ansprüche auch im Ausland.</p>
      <ul>
        <li>Forderungseinzug im gesamten EU-Gebiet</li>
        <li>Forderungseinzug in anderen Staaten nach Vereinbarung</li>
        <li>Gerichtliche Vertretung durch örtlich ansässige Wirtschaftskanzleien</li>
      </ul>
    </div>
  </section>
</main>
"""
    return P.head("Leistungen", "Forderungseinzug, Auskünfte, Unternehmensberatung, Mahnservice, Auslandsinkasso.", "leistungen.html") + P.header() + body + P.footer()


def auftragserteilung_html():
    # Struktur und Texte 1:1 aus dem Original (drei Wege: Online-Formular, Vollmachtsvorlage drucken, Übersendung von Unterlagen)
    body = f"""<main id="main">
{page_header('<a href="index.html">Start</a> · Auftragserteilung', 'Auftragserteilung')}

  <section class="section">
    <div class="container container-narrow">
      <p>Wir nehmen Aufträge nur von Unternehmen, Gewerbetreibenden und Freiberuflern entgegen. Aufträge von Verbrauchern werden nicht zur Bearbeitung angenommen.</p>
      <p>In Ihrem Interesse gehen wir so unbürokratisch vor wie möglich!</p>
      <p>Sie haben mehrere Möglichkeiten:</p>

      <hr>

      <h2>Online-Formular</h2>
      <p>Füllen Sie das hier bereitstehende Auftragsformular direkt am Bildschirm aus und versenden Sie es online.</p>
      <p>Unser Onlineformular ist sortiert nach den möglichen Rechtsformen Ihrer Schuldner/innen. Bitte wählen Sie zunächst die Rechtsform Ihres/r Schuldners/Schuldnerin:</p>

      <p><strong>Privatperson</strong></p>
      <ul>
        <li>Privatperson</li>
      </ul>

      <p><strong>Einzelfirma</strong></p>
      <ul>
        <li>Einzelfirma</li>
      </ul>

      <p><strong>Personengesellschaften</strong></p>
      <ul>
        <li>GbR</li>
        <li>OHG</li>
        <li>KG</li>
        <li>GmbH &amp; Co. KG</li>
      </ul>

      <p><strong>Kapitalgesellschaften</strong></p>
      <ul>
        <li>UG (haftungsbeschränkt)</li>
        <li>GmbH</li>
        <li>AG</li>
        <li>KGaA</li>
      </ul>

      <p><strong>Sonstige Rechtsformen</strong></p>
      <ul>
        <li>eG</li>
        <li>e.V.</li>
      </ul>

      <p><strong>Rechtsformen nach EU-Recht</strong></p>
      <ul>
        <li>EWIN/SUP</li>
        <li>SE</li>
        <li>SCE</li>
      </ul>

      <p>Formular „Nachgerichtliche Forderung" hier öffnen.</p>

      <p style="background:#fef3c7; border-left:4px solid #f59e0b; padding:0.9rem 1.1rem; border-radius:8px">
        <strong>Hinweis:</strong> Die Online-Auftragsformulare nach Rechtsform werden derzeit überarbeitet. Bitte erteilen Sie Ihren Auftrag in der Zwischenzeit per E-Mail an <a href="mailto:{P.CONTACT['mail']}">{P.CONTACT['mail']}</a>, per Fax an {P.CONTACT['fax']} oder per Post (Adresse siehe unten).
      </p>

      <p><em>Wir drucken das ausgefüllte Formular aus und übersenden es Ihnen – nach Prüfung Ihrer Angaben – zur Unterschrift. Aus rechtlichen Gründen kommt der Vertrag mit uns erst nach Eingang des unterschriebenen Formulars bei uns zustande. Wir übersenden Ihnen dann eine Auftragsbestätigung. Gleichzeitig werden erste Einziehungsmaßnahmen eingeleitet.</em></p>

      <hr>

      <h2>Formular ausdrucken</h2>
      <p>Drucken Sie die hier bereitstehende Vollmachtsvorlage aus und senden Sie sie uns ausgefüllt und unterschrieben per Fax oder per Post zu.</p>
      <p>(Hierzu benötigen Sie den <strong>Acrobat Reader</strong>. Sie können den Acrobat Reader kostenlos herunterladen und installieren.)</p>
      <p>Fügen Sie der Vollmachtsvorlage bitte stets eine Kopie des Dokuments bei – in der Regel der Rechnung –, aus der sich die Forderung ableitet. Bei komplexen Forderungen (etwa mit zahlreichen Teilforderungen oder zahlreichen bereits erfolgten Teilzahlungen) fügen Sie einfach eine Übersicht oder Ihre Offene-Posten-Liste bei.</p>
      <p><em>Wir prüfen Ihre Angaben und übersenden Ihnen eine Auftragsbestätigung. Gleichzeitig werden erste Einziehungsmaßnahmen eingeleitet.</em></p>

      <p style="background:#fef3c7; border-left:4px solid #f59e0b; padding:0.9rem 1.1rem; border-radius:8px">
        <strong>Hinweis:</strong> Die PDF-Vollmachtsvorlage muss nach dem Hosting-Wechsel neu hinterlegt werden. Bitte fordern Sie sie in der Zwischenzeit per E-Mail an <a href="mailto:{P.CONTACT['mail']}">{P.CONTACT['mail']}</a> an.
      </p>

      <hr>

      <h2>Übersendung von Unterlagen</h2>
      <p>Wenn Sie kein Auftragsformular zur Hand haben, übersenden Sie uns einfach die fragliche Rechnung, den Vertrag, Ihre Offene-Posten-Liste oder ähnliche Unterlagen, aus denen sich der Bestand der Forderung ergibt, per Fax oder Post. Vergessen Sie nicht Angaben zu den bereits erfolgten Mahnungen!</p>
      <p><em>Wir prüfen Ihre Unterlagen und übersenden Ihnen dann mit der Auftragsbestätigung ein entsprechendes Auftragsformular zur Unterschrift. Gleichzeitig werden erste Einziehungsmaßnahmen eingeleitet.</em></p>

      <hr>

      <p>Sämtliche Aufträge bearbeiten wir ausschließlich zu unseren <a href="agb.html">Allgemeinen Geschäftsbedingungen</a>, die Sie <a href="agb.html">hier</a> einsehen und herunterladen können.</p>
    </div>
  </section>
</main>
"""
    return P.head("Auftragserteilung", "So beauftragen Sie die AFR Inkassokanzlei: Online-Formular, Vollmachtsvorlage zum Ausdrucken oder Übersendung von Unterlagen.", "auftragserteilung.html") + P.header() + body + P.footer()


def kosten_html():
    # Strikt aus Original übernommen
    body = """<main id="main">
""" + page_header('<a href="index.html">Start</a> · Kosten &amp; Gebühren', 'Kosten &amp; Gebühren') + """

  <section class="section">
    <div class="container container-narrow">
      <p>Schlechtem Geld sollte man kein gutes hinterherwerfen!</p>
      <p>Unser Ziel ist, unsere Mandanten von zusätzlichen Aufwendungen, vor allem in Gestalt von Vorschüssen oder fallunabhängigen Beiträgen, möglichst freizuhalten. Unsere Kosten machen wir weitestgehend bei Ihrem Schuldner als Verzugsschaden geltend. Wo dies nicht möglich ist, bemühen wir uns um eine Verrechnung mit beim Schuldner eingezogenen Beträgen.</p>

      <h2>… beim vorgerichtlichen Forderungseinzug</h2>
      <p><strong>Ihr Vorteil:</strong></p>
      <ul>
        <li>Keine Mitgliedsbeiträge oder Vorschüsse!</li>
        <li>Auftragsgebühr von lediglich 16 EURO (netto) pro Auftrag, die nicht als Vorschuß zu entrichten ist, sondern mit eingezogenen Beträgen verrechnet wird.</li>
        <li>Erfolgsprovision von maximal 10 % der tatsächlich eingezogenen Beträge in schwierigen oder besonders langwierigen und/oder aufwändigen Verfahren (z.B. in Insolvenzverfahren oder bei Ratenzahlungsvereinbarungen mit sehr vielen kleinen Raten).</li>
        <li>Gebühren und Auslagen werden gemäß den gesetzlichen Vorgaben erhoben und dem Schuldner als Verzugsschaden auferlegt.</li>
      </ul>

      <h2>… beim nachgerichtlichen Forderungseinzug</h2>
      <p><strong>Ihr Vorteil:</strong></p>
      <ul>
        <li>Keine Mitgliedsbeiträge oder Vorschüsse!</li>
        <li>Auftragsgebühr von lediglich 16 EURO (netto) pro Auftrag, die nicht als Vorschuß zu entrichten ist, sondern mit eingezogenen Beträgen verrechnet wird.</li>
        <li>Übernahme des gesamten Kostenrisikos (für Ermittlungs-, Überwachungs-, Zwangsvollstreckungskosten etc.) durch uns.</li>
        <li>Erfolgshonorar von 45 % der tatsächlich eingezogenen Beträge. Soweit wir das Verfahren bereits vorgerichtlich betreut haben, beträgt das Erfolgshonorar lediglich 35 %.</li>
      </ul>

      <h2>… beim Auslandsinkasso</h2>
      <p>Wie beim <strong>vorgerichtlichen Forderungseinzug</strong> zuzüglich einer Auslandsprovision von 5 % auf alle eingezogenen Beträge.</p>
    </div>
  </section>
</main>
"""
    return P.head("Kosten & Gebühren", "Konditionen der AFR Inkassokanzlei: 16 € Auftragsgebühr, max. 10 % Erfolgsprovision vorgerichtlich, 35–45 % nachgerichtlich.", "kosten.html") + P.header() + body + P.footer()


def ueber_uns_html():
    # 1:1 Original
    body = """<main id="main">
""" + page_header('<a href="index.html">Start</a> · Über uns', 'Über uns') + """

  <section class="section">
    <div class="container container-narrow">
      <p>Die AFR Inkassokanzlei hat ihren Sitz in Bissendorf, einer niedersächsischen Gemeinde in der Nachbarschaft von Osnabrück.</p>
      <p>Wir sind eine inhabergeführte Kanzlei, die seit 25 Jahren für unsere Mandanten, die aus allen Bereichen der Wirtschaft stammen, tätig sein dürfen. Als Volljuristen sind Herr Siebert und Herr Niebaum Ihre kompetenten Ansprechpartner zu allen Fragen des Forderungseinzuges, von dem Verzug bis zur Verfolgung Ihrer Ansprüche in Insolvenzverfahren. Wir unterstützen Sie auch, wenn eingezogene Beträge in einem Insolvenzverfahren im Wege der Anfechtung zurückgefordert werden.</p>
      <p>Unser hochqualifiziertes Team besteht aus Juristen, Betriebswirten und Kaufleuten. Mit unserem Know-How erreichen wir im vorgerichtlichen Bereich Erfolgsquoten von – je nach Branche – 70 bis 85 %.</p>
      <p>Schwerpunkt unserer Tätigkeit ist der Forderungseinzug im B2B-Verhältnis. Hier sorgt unsere individuelle und kompetente Bearbeitung für hohe außergerichtliche Erfolgsquoten und gleichzeitig für große Akzeptanz bei den Verfahrensgegnern. Die meist von unseren Mandanten gewünschte Kundenerhaltung ist eine unmittelbare Folge.</p>
      <p>Die AFR Inkassokanzlei Joachim Siebert ist im Handelsregister des Amtsgerichts Osnabrück verzeichnet (HRA 5917) und unterliegt, wie alle seriösen Inkassobüros, der behördlichen Aufsicht.</p>
    </div>
  </section>
</main>
"""
    return P.head("Über uns", "Inhabergeführte Inkassokanzlei in Bissendorf bei Osnabrück.", "ueber-uns.html") + P.header() + body + P.footer()


def kontakt_html():
    body = f"""<main id="main">
{page_header('<a href="index.html">Start</a> · Kontakt', 'Kontakt')}

  <section class="section">
    <div class="container">
      <div class="contact-grid">
        <div class="contact-info" id="adresse">
          <h2>So erreichen Sie uns:</h2>
          <dl>
            <div>
              <dt>Anschrift</dt>
              <dd>
                AFR Inkassokanzlei Joachim Siebert e.K.<br>
                Jeggener Str. 1a<br>
                49139 Bissendorf
              </dd>
            </div>
            <div>
              <dt>Telefon</dt>
              <dd><a href="{P.CONTACT['tel_link']}">+49 / 05402 / 9906-0</a></dd>
            </div>
            <div>
              <dt>Fax</dt>
              <dd>+49 / 05402 / 9906-18</dd>
            </div>
            <div>
              <dt>E-Mail</dt>
              <dd><a href="mailto:{P.CONTACT['mail']}">{P.CONTACT['mail']}</a></dd>
            </div>
          </dl>

          <h3 style="margin-top:2rem">Bürozeiten</h3>
          <table class="hours-table">
            <tbody>
              <tr><td>Montag – Donnerstag:</td><td>08.30 Uhr bis 12.30 Uhr</td></tr>
              <tr><td></td><td>13.15 Uhr bis 16.45 Uhr</td></tr>
              <tr><td>Freitag:</td><td>08.30 Uhr bis 15.15 Uhr</td></tr>
            </tbody>
          </table>
        </div>

        <div>
          <h2>„Haben Sie Fragen an uns?"</h2>
          <p>Wir freuen uns auf den Kontakt mit Ihnen.</p>

          <form class="form" action="mailto:{P.CONTACT['mail']}" method="post" enctype="text/plain">
            <div class="form-field">
              <label for="nachricht">Ihre Nachricht *</label>
              <textarea id="nachricht" name="Nachricht" required></textarea>
            </div>

            <h3>Kontaktdaten</h3>
            <p class="form-note">Ihre Kontaktdaten werden von uns vertraulich behandelt und nicht an Dritte weitergegeben.</p>

            <div class="form-row two">
              <div class="form-field">
                <label for="vorname">Vorname *</label>
                <input id="vorname" name="Vorname" type="text" required>
              </div>
              <div class="form-field">
                <label for="nachname">Nachname *</label>
                <input id="nachname" name="Nachname" type="text" required>
              </div>
            </div>

            <div class="form-field">
              <label for="firma">Firma</label>
              <input id="firma" name="Firma" type="text">
            </div>

            <div class="form-field">
              <label for="strasse">Straße</label>
              <input id="strasse" name="Strasse" type="text">
            </div>

            <div class="form-row two">
              <div class="form-field">
                <label for="plz">PLZ</label>
                <input id="plz" name="PLZ" type="text">
              </div>
              <div class="form-field">
                <label for="ort">Ort</label>
                <input id="ort" name="Ort" type="text">
              </div>
            </div>

            <div class="form-field">
              <label for="land">Land</label>
              <input id="land" name="Land" type="text" value="Deutschland">
            </div>

            <div class="form-row two">
              <div class="form-field">
                <label for="telefon">Telefon</label>
                <input id="telefon" name="Telefon" type="tel">
              </div>
              <div class="form-field">
                <label for="email">E-Mail *</label>
                <input id="email" name="E-Mail" type="email" required>
              </div>
            </div>

            <div class="form-field">
              <label style="display:flex; align-items:flex-start; gap:0.5rem; font-weight:400; font-size:0.9rem">
                <input type="checkbox" required style="margin-top:0.25rem">
                <span>Einwilligung in die Datenübertragung * – Hiermit willige ich in die Übertragung, Speicherung und Weiterverarbeitung meiner persönlichen Daten zum Zwecke der Bearbeitung meiner Anfrage ein. <a href="datenschutz.html">Datenschutzerklärung</a></span>
              </label>
            </div>

            <div>
              <button class="btn btn-primary" type="submit">Nachricht senden</button>
            </div>
            <p class="form-note">* Pflichtfeld. Hinweis: Dieses Formular öffnet Ihr E-Mail-Programm mit den eingetragenen Angaben.</p>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    return P.head("Kontakt", "Kontaktdaten der AFR Inkassokanzlei in Bissendorf.", "kontakt.html") + P.header() + body + P.footer()


def impressum_html():
    body = f"""<main id="main">
{page_header('<a href="index.html">Start</a> · Impressum', 'Impressum')}

  <section class="section">
    <div class="container prose">

      <p>
        <strong>Allgemeine Forderungs-Regulierung<br>Inkassokanzlei</strong><br>
        Joachim Siebert e.K. (Volljurist)
      </p>
      <p>(Angaben gem. § 6 des Teledienstgesetzes – TDG – )</p>

      <p>
        Jeggener Str. 1 a<br>
        49143 Bissendorf<br>
        Tel.: +49 / 05402 / 9906-0<br>
        Fax: +49 / 05402 / 9906-18<br>
        E-Mail: <a href="mailto:{P.CONTACT['mail']}">{P.CONTACT['mail']}</a>
      </p>

      <p>Gesetzlicher Vertreter: Joachim Siebert<br>
        Handelsregister: HRA 5917 beim Amtsgericht Osnabrück</p>

      <p>Aufsichtsbehörde i.S.d. RDG (Rechtsdienstleistungsgesetz)<br>
        ist das Bundesamt für Justiz, Referat VII 5 /RDG,<br>
        Adenauerallee 99-103, 53113 Bonn<br>
        (Az. beim Bundesamt für Justiz: 2024 0001 0754)<br>
        E-Mail-Adresse: <a href="mailto:poststelle@bfj.bund.de">poststelle@bfj.bund.de</a></p>

      <p>Ursprüngliche Registrierungsbehörde:<br>
        Präsident des Amtsgerichts Osnabrück<br>
        Kollegienwall 29-31, 49074 Osnabrück</p>

      <p>Rechtsdienstleistungsregister:<br>
        AG Osnabrück, Az.: 9 S 24</p>

      <p>Datenschutzbeauftragter: Joachim Siebert</p>

      <p>WebDesign und Programmierung: <a href="https://www.kiel11.de" rel="noopener" target="_blank">kiel11.de</a></p>

      <p><strong>Hinweis:</strong></p>
      <p><em>Für alle von uns verlinkten Websites gilt: Für Inhalt und Aussage der Websites inklusive aller Unterseiten und deren Unterlinks oder anderer Weiterleitungsmechanismen sind wir nicht verantwortlich und haben auch keinen Einfluß darauf.</em></p>

      <p><strong>Rechtliche Hinweise:</strong></p>
      <p>Diese Website wurde mit größtmöglicher Sorgfalt zusammengestellt. Trotzdem kann keine Gewähr für die Fehlerfreiheit und Genauigkeit der enthaltenen Informationen übernommen werden.</p>
      <p>Deshalb wird Ihnen diese Website und das gesamte auf ihr enthaltene Material, sowie alle Informationen in der gegebenen Form und ohne eine ausdrückliche oder implizite Haftung seitens des oben genannten Anbieters zur Verfügung gestellt. Des weiteren behält sich der Anbieter das Recht vor, Änderungen oder Ergänzungen der bereitgestellten Informationen vorzunehmen. Zudem wird jegliche Haftung für Schäden, die direkt oder indirekt aus der Benutzung dieser Website entstehen, ausgeschlossen, soweit diese nicht auf Vorsatz oder grober Fahrlässigkeit beruhen. Die Haftung wegen fahrlässiger Verletzung von Leben, Körper und Gesundheit bleibt davon unberührt.</p>
      <p>Die Website kann Hyperlinks zu anderen Websites enthalten. Eine Haftung oder Garantie für die Aktualität, Richtigkeit und Vollständigkeit der Informationen, die in solchen Hypertextlinks oder anderen Websites enthalten sind, ist ausgeschlossen. Bei dem Inhalt der verlinkten Seiten handelt es sich um fremde Inhalte, die der Anbieter weder ausgewählt noch verändert hat. Der Zugriff auf solche Websites geschieht auf eigene Gefahr.</p>

      <p><strong>Copyright:</strong></p>
      <p>© Copyright Allgemeine Forderungs-Regulierung, Inkassokanzlei Joachim Siebert, Bissendorf (Deutschland). Alle Texte, Bilder, Grafiken, Ton-, Video- und Animationsdateien sowie ihre Arrangements unterliegen dem Urheberrecht und anderen Gesetzen zum Schutz geistigen Eigentums. Sie dürfen weder für Handelszwecke oder zur Weitergabe kopiert, noch verändert und auf anderen Websites ohne schriftliche Genehmigung vom o.g. Betreiber verwendet werden.</p>
      <p>Wir weisen zudem darauf hin, dass auf den Websites enthaltenen Inhalte teilweise dem Urheberrecht Dritter unterliegen.</p>

      <p><strong>Hinweise zum Datenschutz:</strong></p>
      <p><a href="datenschutz.html">Datenschutzerklärung anzeigen</a></p>
    </div>
  </section>
</main>
"""
    return P.head("Impressum", "Impressum der AFR Inkassokanzlei Joachim Siebert e.K., Bissendorf.", "impressum.html") + P.header() + body + P.footer()


def datenschutz_html():
    # KOMPLETT 1:1 aus dem Original-Snapshot (lange Datenschutzerklärung von activeMind AG, Version 2019-04-10)
    body = f"""<main id="main">
{page_header('<a href="index.html">Start</a> · Datenschutzerklärung', 'Datenschutzerklärung')}

  <section class="section">
    <div class="container prose">

      <p>Verantwortlicher im Sinne der Datenschutzgesetze, insbesondere der EU-Datenschutzgrundverordnung (DSGVO), ist:</p>
      <p>
        Allgemeine Forderungs-Regulierung<br>
        Inkassokanzlei<br>
        Joachim Siebert e.K. (Volljurist)
      </p>
      <p>(Angaben gem. § 6 des Teledienstgesetzes – TDG – )</p>
      <p>
        Jeggener Str. 1 a<br>
        49143 Bissendorf<br>
        Tel.: +49 / 05402 / 9906-0<br>
        Fax: +49 / 05402 / 9906-18<br>
        E-Mail: <a href="mailto:{P.CONTACT['mail']}">{P.CONTACT['mail']}</a>
      </p>
      <p>
        Gesetzlicher Vertreter: Joachim Siebert<br>
        Handelsregister: HRA 5917 beim Amtsgericht Osnabrück<br>
        Aufsichtsbehörde: Präsident des Amtsgerichts Osnabrück<br>
        Rechtsdienstleistungsregister: AG Osnabrück, Az.: 9 S 24
      </p>

      <h2>Ihre Betroffenenrechte</h2>
      <p>Unter den angegebenen Kontaktdaten unseres Datenschutzbeauftragten können Sie jederzeit folgende Rechte ausüben:</p>
      <ul>
        <li>Auskunft über Ihre bei uns gespeicherten Daten und deren Verarbeitung (Art. 15 DSGVO),</li>
        <li>Berichtigung unrichtiger personenbezogener Daten (Art. 16 DSGVO),</li>
        <li>Löschung Ihrer bei uns gespeicherten Daten (Art. 17 DSGVO),</li>
        <li>Einschränkung der Datenverarbeitung, sofern wir Ihre Daten aufgrund gesetzlicher Pflichten noch nicht löschen dürfen (Art. 18 DSGVO),</li>
        <li>Widerspruch gegen die Verarbeitung Ihrer Daten bei uns (Art. 21 DSGVO) und</li>
        <li>Datenübertragbarkeit, sofern Sie in die Datenverarbeitung eingewilligt haben oder einen Vertrag mit uns abgeschlossen haben (Art. 20 DSGVO).</li>
      </ul>
      <p>Sofern Sie uns eine Einwilligung erteilt haben, können Sie diese jederzeit mit Wirkung für die Zukunft widerrufen.</p>
      <p>Sie können sich jederzeit mit einer Beschwerde an eine Aufsichtsbehörde wenden, z. B. an die zuständige Aufsichtsbehörde des Bundeslands Ihres Wohnsitzes oder an die für uns als verantwortliche Stelle zuständige Behörde.</p>
      <p>Eine Liste der Aufsichtsbehörden (für den nichtöffentlichen Bereich) mit Anschrift finden Sie unter: <a href="https://www.bfdi.bund.de/DE/Infothek/Anschriften_Links/anschriften_links-node.html" rel="noopener" target="_blank">https://www.bfdi.bund.de/DE/Infothek/Anschriften_Links/anschriften_links-node.html</a>.</p>

      <h2>Erfassung allgemeiner Informationen beim Besuch unserer Website</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Wenn Sie auf unsere Website zugreifen, d.h., wenn Sie sich nicht registrieren oder anderweitig Informationen übermitteln, werden automatisch Informationen allgemeiner Natur erfasst. Diese Informationen (Server-Logfiles) beinhalten etwa die Art des Webbrowsers, das verwendete Betriebssystem, den Domainnamen Ihres Internet-Service-Providers, Ihre IP-Adresse und ähnliches.</p>
      <p>Sie werden insbesondere zu folgenden Zwecken verarbeitet:</p>
      <ul>
        <li>Sicherstellung eines problemlosen Verbindungsaufbaus der Website,</li>
        <li>Sicherstellung einer reibungslosen Nutzung unserer Website,</li>
        <li>Auswertung der Systemsicherheit und -stabilität sowie</li>
        <li>zu weiteren administrativen Zwecken.</li>
      </ul>
      <p>Wir verwenden Ihre Daten nicht, um Rückschlüsse auf Ihre Person zu ziehen. Informationen dieser Art werden von uns ggfs. statistisch ausgewertet, um unseren Internetauftritt und die dahinterstehende Technik zu optimieren.</p>
      <h3>Rechtsgrundlage:</h3>
      <p>Die Verarbeitung erfolgt gemäß Art. 6 Abs. 1 lit. f DSGVO auf Basis unseres berechtigten Interesses an der Verbesserung der Stabilität und Funktionalität unserer Website.</p>
      <h3>Empfänger:</h3>
      <p>Empfänger der Daten sind ggf. technische Dienstleister, die für den Betrieb und die Wartung unserer Webseite als Auftragsverarbeiter tätig werden.</p>
      <h3>Speicherdauer:</h3>
      <p>Die Daten werden gelöscht, sobald diese für den Zweck der Erhebung nicht mehr erforderlich sind. Dies ist für die Daten, die der Bereitstellung der Webseite dienen, grundsätzlich der Fall, wenn die jeweilige Sitzung beendet ist.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung der vorgenannten personenbezogenen Daten ist weder gesetzlich noch vertraglich vorgeschrieben. Ohne die IP-Adresse ist jedoch der Dienst und die Funktionsfähigkeit unserer Website nicht gewährleistet. Zudem können einzelne Dienste und Services nicht verfügbar oder eingeschränkt sein. Aus diesem Grund ist ein Widerspruch ausgeschlossen.</p>

      <h2>Cookies</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Wie viele andere Webseiten verwenden wir auch so genannte „Cookies". Bei Cookies handelt es sich um kleine Textdateien, die auf Ihrem Endgerät (Laptop, Tablet, Smartphone o.ä.) gespeichert werden, wenn Sie unsere Webseite besuchen.</p>
      <p>Hierdurch erhalten wir bestimmte Daten wie z. B. IP-Adresse, verwendeter Browser und Betriebssystem.</p>
      <p>Cookies können nicht verwendet werden, um Programme zu starten oder Viren auf einen Computer zu übertragen. Anhand der in Cookies enthaltenen Informationen können wir Ihnen die Navigation erleichtern und die korrekte Anzeige unserer Webseiten ermöglichen.</p>
      <p>In keinem Fall werden die von uns erfassten Daten an Dritte weitergegeben oder ohne Ihre Einwilligung eine Verknüpfung mit personenbezogenen Daten hergestellt.</p>
      <p>Natürlich können Sie unsere Website grundsätzlich auch ohne Cookies betrachten. Internet-Browser sind regelmäßig so eingestellt, dass sie Cookies akzeptieren. Im Allgemeinen können Sie die Verwendung von Cookies jederzeit über die Einstellungen Ihres Browsers deaktivieren. Bitte verwenden Sie die Hilfefunktionen Ihres Internetbrowsers, um zu erfahren, wie Sie diese Einstellungen ändern können. Bitte beachten Sie, dass einzelne Funktionen unserer Website möglicherweise nicht funktionieren, wenn Sie die Verwendung von Cookies deaktiviert haben.</p>
      <h3>Speicherdauer und eingesetzte Cookies:</h3>
      <p>Soweit Sie uns durch Ihre Browsereinstellungen oder Zustimmung die Verwendung von Cookies erlauben, können folgende Cookies auf unseren Webseiten zum Einsatz kommen:</p>
      <p>PHPSESSID wird für 24 Stunden gespeichert</p>
      <p>Soweit diese Cookies (auch) personenbezogene Daten betreffen können, informieren wir Sie darüber in den folgenden Abschnitten.</p>
      <p>Sie können über Ihre Browsereinstellungen einzelne Cookies oder den gesamten Cookie-Bestand löschen. Darüber hinaus erhalten Sie Informationen und Anleitungen, wie diese Cookies gelöscht oder deren Speicherung vorab blockiert werden können. Je nach Anbieter Ihres Browsers finden Sie die notwendigen Informationen unter den nachfolgenden Links:</p>
      <ul>
        <li>Mozilla Firefox: <a href="https://support.mozilla.org/de/kb/cookies-loeschen-daten-von-websites-entfernen" rel="noopener" target="_blank">https://support.mozilla.org/de/kb/cookies-loeschen-daten-von-websites-entfernen</a></li>
        <li>Internet Explorer: <a href="https://support.microsoft.com/de-de/help/17442/windows-internet-explorer-delete-manage-cookies" rel="noopener" target="_blank">https://support.microsoft.com/de-de/help/17442/windows-internet-explorer-delete-manage-cookies</a></li>
        <li>Google Chrome: <a href="https://support.google.com/accounts/answer/61416?hl=de" rel="noopener" target="_blank">https://support.google.com/accounts/answer/61416?hl=de</a></li>
        <li>Opera: <a href="http://www.opera.com/de/help" rel="noopener" target="_blank">http://www.opera.com/de/help</a></li>
        <li>Safari: <a href="https://support.apple.com/kb/PH17191?locale=de_DE&amp;viewlocale=de_DE" rel="noopener" target="_blank">https://support.apple.com/kb/PH17191?locale=de_DE&amp;viewlocale=de_DE</a></li>
      </ul>

      <h2>Erbringung kostenpflichtiger Leistungen</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Zur Erbringung kostenpflichtiger Leistungen werden von uns zusätzliche Daten erfragt, wie z.B. Zahlungsangaben, um Ihre Bestellung ausführen zu können.</p>
      <h3>Rechtsgrundlage:</h3>
      <p>Die Verarbeitung der Daten, die für den Abschluss des Vertrages erforderlich ist, basiert auf Art. 6 Abs. 1 lit. b DSGVO.</p>
      <h3>Empfänger:</h3>
      <p>Empfänger der Daten sind ggf. Auftragsverarbeiter.</p>
      <h3>Speicherdauer:</h3>
      <p>Wir speichern diese Daten in unseren Systemen bis die gesetzlichen Aufbewahrungsfristen abgelaufen sind. Diese betragen grundsätzlich 6 oder 10 Jahre aus Gründen der ordnungsmäßigen Buchführung und steuerrechtlichen Anforderungen.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung Ihrer personenbezogenen Daten erfolgt freiwillig. Ohne die Bereitstellung Ihrer personenbezogenen Daten können wir Ihnen keinen Zugang auf unsere angebotenen Inhalte und Leistungen gewähren.</p>

      <h2>Newsletter</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Ihre Daten werden ausschließlich dazu verwendet, Ihnen den abonnierten Newsletter per E-Mail zuzustellen. Die Angabe Ihres Namens erfolgt, um Sie im Newsletter persönlich ansprechen zu können und ggf. zu identifizieren, falls Sie von Ihren Rechten als Betroffener Gebrauch machen wollen.</p>
      <p>Für den Empfang des Newsletters ist die Angabe Ihrer E-Mail-Adresse ausreichend. Bei der Anmeldung zum Bezug unseres Newsletters werden die von Ihnen angegebenen Daten ausschließlich für diesen Zweck verwendet. Abonnenten können auch über Umstände per E-Mail informiert werden, die für den Dienst oder die Registrierung relevant sind (bspw. Änderungen des Newsletterangebots oder technische Gegebenheiten).</p>
      <p>Für eine wirksame Registrierung benötigen wir eine valide E-Mail-Adresse. Um zu überprüfen, dass eine Anmeldung tatsächlich durch den Inhaber einer E-Mail-Adresse erfolgt, setzen wir das „Double-opt-in"-Verfahren ein. Hierzu protokollieren wir die Bestellung des Newsletters, den Versand einer Bestätigungsmail und den Eingang der hiermit angeforderten Antwort. Weitere Daten werden nicht erhoben. Die Daten werden ausschließlich für den Newsletterversand verwendet und nicht an Dritte weitergegeben.</p>
      <h3>Rechtsgrundlage:</h3>
      <p>Auf Grundlage Ihrer ausdrücklich erteilten Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), übersenden wir Ihnen regelmäßig unseren Newsletter bzw. vergleichbare Informationen per E-Mail an Ihre angegebene E-Mail-Adresse.</p>
      <p>Die Einwilligung zur Speicherung Ihrer persönlichen Daten und ihrer Nutzung für den Newsletterversand können Sie jederzeit mit Wirkung für die Zukunft widerrufen. In jedem Newsletter findet sich dazu ein entsprechender Link. Außerdem können Sie sich jederzeit auch direkt auf dieser Website abmelden oder uns Ihren Widerruf über die am Ende dieser Datenschutzhinweise angegebene Kontaktmöglichkeit mitteilen.</p>
      <h3>Empfänger:</h3>
      <p>Empfänger der Daten sind ggf. Auftragsverarbeiter.</p>
      <h3>Speicherdauer:</h3>
      <p>Die Daten werden in diesem Zusammenhang nur verarbeitet, solange die entsprechende Einwilligung vorliegt. Danach werden sie gelöscht.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung Ihrer personenbezogenen Daten erfolgt freiwillig, allein auf Basis Ihrer Einwilligung. Ohne bestehende Einwilligung können wir Ihnen unseren Newsletter leider nicht zusenden.</p>

      <h2>Kontaktformular</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Die von Ihnen eingegebenen Daten werden zum Zweck der individuellen Kommunikation mit Ihnen gespeichert. Hierfür ist die Angabe einer validen E-Mail-Adresse sowie Ihres Namens erforderlich. Diese dient der Zuordnung der Anfrage und der anschließenden Beantwortung derselben. Die Angabe weiterer Daten ist optional.</p>
      <h3>Rechtsgrundlage:</h3>
      <p>Die Verarbeitung der in das Kontaktformular eingegebenen Daten erfolgt auf der Grundlage eines berechtigten Interesses (Art. 6 Abs. 1 lit. f DSGVO).</p>
      <p>Durch Bereitstellung des Kontaktformulars möchten wir Ihnen eine unkomplizierte Kontaktaufnahme ermöglichen. Ihre gemachten Angaben werden zum Zwecke der Bearbeitung der Anfrage sowie für mögliche Anschlussfragen gespeichert.</p>
      <p>Sofern Sie mit uns Kontakt aufnehmen, um ein Angebot zu erfragen, erfolgt die Verarbeitung der in das Kontaktformular eingegebenen Daten zur Durchführung vorvertraglicher Maßnahmen (Art. 6 Abs. 1 lit. b DSGVO).</p>
      <h3>Empfänger:</h3>
      <p>Empfänger der Daten sind ggf. Auftragsverarbeiter.</p>
      <h3>Speicherdauer:</h3>
      <p>Daten werden spätestens 6 Monate nach Bearbeitung der Anfrage gelöscht.</p>
      <p>Sofern es zu einem Vertragsverhältnis kommt, unterliegen wir den gesetzlichen Aufbewahrungsfristen nach HGB und löschen Ihre Daten nach Ablauf dieser Fristen.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung Ihrer personenbezogenen Daten erfolgt freiwillig. Wir können Ihre Anfrage jedoch nur bearbeiten, sofern Sie uns Ihren Namen, Ihre E-Mail-Adresse und den Grund der Anfrage mitteilen.</p>

      <h2>Verwendung von Scriptbibliotheken (Google Webfonts)</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Um unsere Inhalte browserübergreifend korrekt und grafisch ansprechend darzustellen, verwenden wir auf dieser Website „Google Web Fonts" der Google LLC (1600 Amphitheatre Parkway, Mountain View, CA 94043, USA; nachfolgend „Google") zur Darstellung von Schriften.</p>
      <p>Die Datenschutzrichtlinie des Bibliothekbetreibers Google finden Sie hier: <a href="https://www.google.com/policies/privacy/" rel="noopener" target="_blank">https://www.google.com/policies/privacy/</a></p>
      <h3>Rechtsgrundlage:</h3>
      <p>Rechtsgrundlage für die Einbindung von Google Webfonts und dem damit verbundenen Datentransfer zu Google ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
      <h3>Empfänger:</h3>
      <p>Der Aufruf von Scriptbibliotheken oder Schriftbibliotheken löst automatisch eine Verbindung zum Betreiber der Bibliothek aus. Dabei ist es theoretisch möglich – aktuell allerdings auch unklar ob und ggf. zu welchen Zwecken – dass der Betreiber in diesem Fall Google Daten erhebt.</p>
      <h3>Speicherdauer:</h3>
      <p>Wir erheben keine personenbezogenen Daten, durch die Einbindung von Google Webfonts.</p>
      <p>Weitere Informationen zu Google Web Fonts finden Sie unter <a href="https://developers.google.com/fonts/faq" rel="noopener" target="_blank">https://developers.google.com/fonts/faq</a> und in der Datenschutzerklärung von Google: <a href="https://www.google.com/policies/privacy/" rel="noopener" target="_blank">https://www.google.com/policies/privacy/</a>.</p>
      <h3>Drittlandtransfer:</h3>
      <p>Google verarbeitet Ihre Daten in den USA und hat sich dem EU_US Privacy Shield unterworfen <a href="https://www.privacyshield.gov/EU-US-Framework" rel="noopener" target="_blank">https://www.privacyshield.gov/EU-US-Framework</a>.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung der personenbezogenen Daten ist weder gesetzlich, noch vertraglich vorgeschrieben. Allerdings kann ggfs. die korrekte Darstellung der Inhalte durch Standardschriften nicht möglich sein.</p>
      <h3>Widerruf der Einwilligung:</h3>
      <p>Zur Darstellung der Inhalte wird regelmäßig die Programmiersprache JavaScript verwendet. Sie können der Datenverarbeitung daher widersprechen, indem Sie die Ausführung von JavaScript in Ihrem Browser deaktivieren oder einen JavaScript-Blocker installieren. Bitte beachten Sie, dass es hierdurch zu Funktionseinschränkungen auf der Website kommen kann.</p>

      <h2>Verwendung von Google Maps</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Auf dieser Webseite nutzen wir das Angebot von Google Maps. Google Maps wird von Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA (nachfolgend „Google") betrieben. Dadurch können wir Ihnen interaktive Karten direkt in der Webseite anzeigen und ermöglichen Ihnen die komfortable Nutzung der Karten-Funktion.</p>
      <p>Nähere Informationen über die Datenverarbeitung durch Google können Sie <a href="http://www.google.com/privacypolicy.html" rel="noopener" target="_blank">den Google-Datenschutzhinweisen</a> entnehmen. Dort können Sie im Datenschutzcenter auch Ihre persönlichen Datenschutz-Einstellungen verändern.</p>
      <p>Ausführliche Anleitungen zur Verwaltung der eigenen Daten im Zusammenhang mit Google-Produkten <a href="http://www.dataliberation.org/" rel="noopener" target="_blank">finden Sie hier</a>.</p>
      <h3>Rechtsgrundlage:</h3>
      <p>Rechtsgrundlage für die Einbindung von Google Maps und dem damit verbundenen Datentransfer zu Google ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
      <h3>Empfänger:</h3>
      <p>Durch den Besuch der Webseite erhält Google Informationen, dass Sie die entsprechende Unterseite unserer Webseite aufgerufen haben. Dies erfolgt unabhängig davon, ob Google ein Nutzerkonto bereitstellt, über das Sie eingeloggt sind, oder ob keine Nutzerkonto besteht. Wenn Sie bei Google eingeloggt sind, werden Ihre Daten direkt Ihrem Konto zugeordnet.</p>
      <p>Wenn Sie die Zuordnung in Ihrem Profil bei Google nicht wünschen, müssen Sie sich vor Aktivierung des Buttons bei Google ausloggen. Google speichert Ihre Daten als Nutzungsprofile und nutzt sie für Zwecke der Werbung, Marktforschung und/oder bedarfsgerechter Gestaltung seiner Webseite. Eine solche Auswertung erfolgt insbesondere (selbst für nicht eingeloggte Nutzer) zur Erbringung bedarfsgerechter Werbung und um andere Nutzer des sozialen Netzwerks über Ihre Aktivitäten auf unserer Webseite zu informieren. Ihnen steht ein Widerspruchsrecht zu gegen die Bildung dieser Nutzerprofile, wobei Sie sich zur Ausübung dessen an Google richten müssen.</p>
      <h3>Speicherdauer:</h3>
      <p>Wir erheben keine personenbezogenen Daten, durch die Einbindung von Google Maps.</p>
      <h3>Drittlandtransfer:</h3>
      <p>Google verarbeitet Ihre Daten in den USA und hat sich dem EU_US Privacy Shield unterworfen <a href="https://www.privacyshield.gov/EU-US-Framework" rel="noopener" target="_blank">https://www.privacyshield.gov/EU-US-Framework</a>.</p>
      <h3>Widerruf der Einwilligung:</h3>
      <p>Wenn Sie nicht möchten, dass Google über unseren Internetauftritt Daten über Sie erhebt, verarbeitet oder nutzt, können Sie in Ihrem Browsereinstellungen JavaScript deaktivieren. In diesem Fall können Sie unsere Webseite jedoch nicht oder nur eingeschränkt nutzen.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung Ihrer personenbezogenen Daten erfolgt freiwillig, allein auf Basis Ihrer Einwilligung. Sofern Sie den Zugriff unterbinden, kann es hierdurch zu Funktionseinschränkungen auf der Website kommen.</p>

      <h2>Eingebettete YouTube-Videos</h2>
      <h3>Art und Zweck der Verarbeitung:</h3>
      <p>Auf einigen unserer Webseiten betten wir YouTube-Videos ein. Betreiber der entsprechenden Plugins ist die YouTube, LLC, 901 Cherry Ave., San Bruno, CA 94066, USA (nachfolgend „YouTube"). Wenn Sie eine Seite mit dem YouTube-Plugin besuchen, wird eine Verbindung zu Servern von YouTube hergestellt. Dabei wird YouTube mitgeteilt, welche Seiten Sie besuchen. Wenn Sie in Ihrem YouTube-Account eingeloggt sind, kann YouTube Ihr Surfverhalten Ihnen persönlich zuzuordnen. Dies verhindern Sie, indem Sie sich vorher aus Ihrem YouTube-Account ausloggen.</p>
      <p>Wird ein YouTube-Video gestartet, setzt der Anbieter Cookies ein, die Hinweise über das Nutzerverhalten sammeln.</p>
      <p>Weitere Informationen zu Zweck und Umfang der Datenerhebung und ihrer Verarbeitung durch YouTube erhalten Sie in den Datenschutzerklärungen des Anbieters, Dort erhalten Sie auch weitere Informationen zu Ihren diesbezüglichen Rechten und Einstellungsmöglichkeiten zum Schutze Ihrer Privatsphäre (<a href="https://policies.google.com/privacy" rel="noopener" target="_blank">https://policies.google.com/privacy</a>). Google verarbeitet Ihre Daten in den USA und hat sich dem EU-US Privacy Shield unterworfen https://www.privacyshield.gov/EU-US-Framework</p>
      <h3>Rechtsgrundlage:</h3>
      <p>Rechtsgrundlage für die Einbindung von YouTube und dem damit verbundenen Datentransfer zu Google ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>
      <h3>Empfänger:</h3>
      <p>Der Aufruf von YouTube löst automatisch eine Verbindung zu Google aus.</p>
      <h3>Speicherdauer und Widerruf der Einwilligung:</h3>
      <p>Wer das Speichern von Cookies für das Google-Ad-Programm deaktiviert hat, wird auch beim Anschauen von YouTube-Videos mit keinen solchen Cookies rechnen müssen. YouTube legt aber auch in anderen Cookies nicht-personenbezogene Nutzungsinformationen ab. Möchten Sie dies verhindern, so müssen Sie das Speichern von Cookies im Browser blockieren.</p>
      <p>Weitere Informationen zum Datenschutz bei „YouTube" finden Sie in der Datenschutzerklärung des Anbieters unter: <a href="https://www.google.de/intl/de/policies/privacy/" rel="noopener" target="_blank">https://www.google.de/intl/de/policies/privacy/</a></p>
      <h3>Drittlandtransfer:</h3>
      <p>Google verarbeitet Ihre Daten in den USA und hat sich dem EU_US Privacy Shield unterworfen <a href="https://www.privacyshield.gov/EU-US-Framework" rel="noopener" target="_blank">https://www.privacyshield.gov/EU-US-Framework</a>.</p>
      <h3>Bereitstellung vorgeschrieben oder erforderlich:</h3>
      <p>Die Bereitstellung Ihrer personenbezogenen Daten erfolgt freiwillig, allein auf Basis Ihrer Einwilligung. Sofern Sie den Zugriff unterbinden, kann es hierdurch zu Funktionseinschränkungen auf der Website kommen.</p>

      <h2>SSL-Verschlüsselung</h2>
      <p>Um die Sicherheit Ihrer Daten bei der Übertragung zu schützen, verwenden wir dem aktuellen Stand der Technik entsprechende Verschlüsselungsverfahren (z. B. SSL) über HTTPS.</p>

      <h2>Änderung unserer Datenschutzbestimmungen</h2>
      <p>Wir behalten uns vor, diese Datenschutzerklärung anzupassen, damit sie stets den aktuellen rechtlichen Anforderungen entspricht oder um Änderungen unserer Leistungen in der Datenschutzerklärung umzusetzen, z.B. bei der Einführung neuer Services. Für Ihren erneuten Besuch gilt dann die neue Datenschutzerklärung.</p>

      <h2>Fragen an den Datenschutzbeauftragten</h2>
      <p>Wenn Sie Fragen zum Datenschutz haben, schreiben Sie uns bitte eine E-Mail oder wenden Sie sich direkt an die für den Datenschutz verantwortliche Person in unserer Organisation:</p>
      <p><em>Die Datenschutzerklärung wurde mithilfe der activeMind AG erstellt, den Experten für <a href="https://www.activemind.de/datenschutz/datenschutzhinweis-generator/" rel="noopener" target="_blank">externe Datenschutzbeauftragte</a> (Version #2019-04-10).</em></p>

      <hr>

      <h2>alte Datenschutzerklärung</h2>
      <p>Verantwortliche Stelle im Sinne der Datenschutzgesetze ist:</p>
      <p>
        Allgemeine Forderungs-Regulierung<br>
        Inkassokanzlei<br>
        Joachim Siebert e.K. (Volljurist)
      </p>
      <p>(Angaben gem. § 6 des Teledienstgesetzes – TDG – )</p>
      <p>
        Jeggener Str. 1 a<br>
        49143 Bissendorf<br>
        Tel.: +49 / 05402 / 9906-0<br>
        Fax: +49 / 05402 / 9906-18<br>
        E-Mail: <a href="mailto:{P.CONTACT['mail']}">{P.CONTACT['mail']}</a>
      </p>
      <p>
        Gesetzlicher Vertreter: Joachim Siebert<br>
        Handelsregister: HRA 5917 beim Amtsgericht Osnabrück<br>
        Aufsichtsbehörde: Präsident des Amtsgerichts Osnabrück<br>
        Rechtsdienstleistungsregister: AG Osnabrück, Az.: 9 S 24
      </p>

      <h3>Erfassung allgemeiner Informationen</h3>
      <p>Wenn Sie auf unsere Webseite zugreifen, werden automatisch Informationen allgemeiner Natur erfasst. Diese Informationen (Server-Logfiles) beinhalten etwa die Art des Webbrowsers, das verwendete Betriebssystem, den Domainnamen Ihres Internet Service Providers und Ähnliches. Hierbei handelt es sich ausschließlich um Informationen, welche keine Rückschlüsse auf Ihre Person zulassen. Diese Informationen sind technisch notwendig, um von Ihnen angeforderte Inhalte von Webseiten korrekt auszuliefern und fallen bei Nutzung des Internets zwingend an. Anonyme Informationen dieser Art werden von uns statistisch ausgewertet, um unseren Internetauftritt und die dahinterstehende Technik zu optimieren.</p>

      <h3>Cookies</h3>
      <p>Wie viele andere Webseiten verwenden wir auch so genannte „Cookies". Cookies sind kleine Textdateien, die von einem Webseitenserver auf Ihre Festplatte übertragen werden. Hierdurch erhalten wir automatisch bestimmte Daten wie z. B. IP-Adresse, verwendeter Browser, Betriebssystem über Ihren Computer und Ihre Verbindung zum Internet.</p>
      <p>Cookies können nicht verwendet werden, um Programme zu starten oder Viren auf einen Computer zu übertragen. Anhand der in Cookies enthaltenen Informationen können wir Ihnen die Navigation erleichtern und die korrekte Anzeige unserer Webseiten ermöglichen.</p>
      <p>In keinem Fall werden die von uns erfassten Daten an Dritte weitergegeben oder ohne Ihre Einwilligung eine Verknüpfung mit personenbezogenen Daten hergestellt.</p>
      <p>Natürlich können Sie unsere Website grundsätzlich auch ohne Cookies betrachten. Internet-Browser sind regelmäßig so eingestellt, dass sie Cookies akzeptieren. Sie können die Verwendung von Cookies jederzeit über die Einstellungen Ihres Browsers deaktivieren. Bitte verwenden Sie die Hilfefunktionen Ihres Internetbrowsers, um zu erfahren, wie Sie diese Einstellungen ändern können. Bitte beachten Sie, dass einzelne Funktionen unserer Website möglicherweise nicht funktionieren, wenn Sie die Verwendung von Cookies deaktiviert haben.</p>

      <h3>Registrierung auf unserer Webseite</h3>
      <p>Bei der Registrierung für die Nutzung unserer personalisierten Leistungen werden einige personenbezogene Daten erhoben, wie Name, Anschrift, Kontakt- und Kommunikationsdaten wie Telefonnummer und E-Mail-Adresse. Sind Sie bei uns registriert, können Sie auf Inhalte und Leistungen zugreifen, die wir nur registrierten Nutzern anbieten. Angemeldete Nutzer haben zudem die Möglichkeit, bei Bedarf die bei Registrierung angegebenen Daten jederzeit zu ändern oder zu löschen. Selbstverständlich erteilen wir Ihnen darüber hinaus jederzeit Auskunft über die von uns über Sie gespeicherten personenbezogenen Daten. Gerne berichtigen bzw. löschen wir diese auch auf Ihren Wunsch, soweit keine gesetzlichen Aufbewahrungspflichten entgegenstehen. Zur Kontaktaufnahme in diesem Zusammenhang nutzen Sie bitte die am Ende dieser Datenschutzerklärung angegebenen Kontaktdaten.</p>

      <h3>Erbringung kostenpflichtiger Leistungen</h3>
      <p>Zur Erbringung kostenpflichtiger Leistungen werden von uns zusätzliche Daten erfragt, wie z.B. Zahlungsangaben.</p>

      <h3>SSL-Verschlüsselung</h3>
      <p>Um die Sicherheit Ihrer Daten bei der Übertragung zu schützen, verwenden wir dem aktuellen Stand der Technik entsprechende Verschlüsselungsverfahren (z. B. SSL) über HTTPS.</p>

      <h3>Newsletter</h3>
      <p>Bei der Anmeldung zum Bezug unseres Newsletters werden die von Ihnen angegebenen Daten ausschließlich für diesen Zweck verwendet. Abonnenten können auch über Umstände per E-Mail informiert werden, die für den Dienst oder die Registrierung relevant sind (Beispielsweise Änderungen des Newsletterangebots oder technische Gegebenheiten).</p>
      <p>Für eine wirksame Registrierung benötigen wir eine valide E-Mail-Adresse. Um zu überprüfen, dass eine Anmeldung tatsächlich durch den Inhaber einer E-Mail-Adresse erfolgt, setzen wir das „Double-opt-in"-Verfahren ein. Hierzu protokollieren wir die Bestellung des Newsletters, den Versand einer Bestätigungsmail und den Eingang der hiermit angeforderten Antwort. Weitere Daten werden nicht erhoben. Die Daten werden ausschließlich für den Newsletterversand verwendet und nicht an Dritte weitergegeben.</p>
      <p>Die Einwilligung zur Speicherung Ihrer persönlichen Daten und ihrer Nutzung für den Newsletterversand können Sie jederzeit widerrufen. In jedem Newsletter findet sich dazu ein entsprechender Link. Außerdem können Sie sich jederzeit auch direkt auf dieser Webseite abmelden oder uns Ihren entsprechenden Wunsch über die am Ende dieser Datenschutzhinweise angegebene Kontaktmöglichkeit mitteilen.</p>

      <h3>Kontaktformular</h3>
      <p>Treten Sie per E-Mail oder Kontaktformular mit uns in Kontakt, werden die von Ihnen gemachten Angaben zum Zwecke der Bearbeitung der Anfrage sowie für mögliche Anschlussfragen gespeichert.</p>

      <h3>Löschung bzw. Sperrung der Daten</h3>
      <p>Wir halten uns an die Grundsätze der Datenvermeidung und Datensparsamkeit. Wir speichern Ihre personenbezogenen Daten daher nur so lange, wie dies zur Erreichung der hier genannten Zwecke erforderlich ist oder wie es die vom Gesetzgeber vorgesehenen vielfältigen Speicherfristen vorsehen. Nach Fortfall des jeweiligen Zweckes bzw. Ablauf dieser Fristen werden die entsprechenden Daten routinemäßig und entsprechend den gesetzlichen Vorschriften gesperrt oder gelöscht.</p>

      <h3>Verwendung von Google Maps</h3>
      <p>Diese Webseite verwendet Google Maps API, um geographische Informationen visuell darzustellen. Bei der Nutzung von Google Maps werden von Google auch Daten über die Nutzung der Kartenfunktionen durch Besucher erhoben, verarbeitet und genutzt. Nähere Informationen über die Datenverarbeitung durch Google können Sie <a href="http://www.google.com/privacypolicy.html" rel="noopener" target="_blank">den Google-Datenschutzhinweisen</a> entnehmen. Dort können Sie im Datenschutzcenter auch Ihre persönlichen Datenschutz-Einstellungen verändern.</p>
      <p>Ausführliche Anleitungen zur Verwaltung der eigenen Daten im Zusammenhang mit Google-Produkten <a href="http://www.dataliberation.org/" rel="noopener" target="_blank">finden Sie hier</a>.</p>

      <h3>Eingebettete YouTube-Videos</h3>
      <p>Auf einigen unserer Webseiten betten wir Youtube-Videos ein. Betreiber der entsprechenden Plugins ist die YouTube, LLC, 901 Cherry Ave., San Bruno, CA 94066, USA. Wenn Sie eine Seite mit dem YouTube-Plugin besuchen, wird eine Verbindung zu Servern von Youtube hergestellt. Dabei wird Youtube mitgeteilt, welche Seiten Sie besuchen. Wenn Sie in Ihrem Youtube-Account eingeloggt sind, kann Youtube Ihr Surfverhalten Ihnen persönlich zuzuordnen. Dies verhindern Sie, indem Sie sich vorher aus Ihrem Youtube-Account ausloggen.</p>
      <p>Wird ein Youtube-Video gestartet, setzt der Anbieter Cookies ein, die Hinweise über das Nutzerverhalten sammeln.</p>
      <p>Wer das Speichern von Cookies für das Google-Ad-Programm deaktiviert hat, wird auch beim Anschauen von Youtube-Videos mit keinen solchen Cookies rechnen müssen. Youtube legt aber auch in anderen Cookies nicht-personenbezogene Nutzungsinformationen ab. Möchten Sie dies verhindern, so müssen Sie das Speichern von Cookies im Browser blockieren.</p>
      <p>Weitere Informationen zum Datenschutz bei „Youtube" finden Sie in der Datenschutzerklärung des Anbieters unter: <a href="https://www.google.de/intl/de/policies/privacy/" rel="noopener" target="_blank">https://www.google.de/intl/de/policies/privacy/</a></p>

      <h3>Ihre Rechte auf Auskunft, Berichtigung, Sperre, Löschung und Widerspruch</h3>
      <p>Sie haben das Recht, jederzeit Auskunft über Ihre bei uns gespeicherten personenbezogenen Daten zu erhalten. Ebenso haben Sie das Recht auf Berichtigung, Sperrung oder, abgesehen von der vorgeschriebenen Datenspeicherung zur Geschäftsabwicklung, Löschung Ihrer personenbezogenen Daten. Bitte wenden Sie sich dazu an unseren Datenschutzbeauftragten. Die Kontaktdaten finden Sie ganz unten.</p>
      <p>Damit eine Sperre von Daten jederzeit berücksichtigt werden kann, müssen diese Daten zu Kontrollzwecken in einer Sperrdatei vorgehalten werden. Sie können auch die Löschung der Daten verlangen, soweit keine gesetzliche Archivierungsverpflichtung besteht. Soweit eine solche Verpflichtung besteht, sperren wir Ihre Daten auf Wunsch.</p>
      <p>Sie können Änderungen oder den Widerruf einer Einwilligung durch entsprechende Mitteilung an uns mit Wirkung für die Zukunft vornehmen.</p>

      <h3>Änderung unserer Datenschutzbestimmungen</h3>
      <p>Wir behalten uns vor, diese Datenschutzerklärung gelegentlich anzupassen, damit sie stets den aktuellen rechtlichen Anforderungen entspricht oder um Änderungen unserer Leistungen in der Datenschutzerklärung umzusetzen, z. B. bei der Einführung neuer Services. Für Ihren erneuten Besuch gilt dann die neue Datenschutzerklärung.</p>

      <h3>Fragen an den Datenschutzbeauftragten</h3>
      <p>Wenn Sie Fragen zum Datenschutz haben, schreiben Sie uns bitte eine E-Mail.</p>
      <p><em>Die Datenschutzerklärung wurde mit dem <a href="https://www.activemind.de/datenschutz/datenschutzhinweis-generator/" rel="noopener" target="_blank">Datenschutzerklärungs-Generator der activeMind AG erstellt</a>.</em></p>
    </div>
  </section>
</main>
"""
    return P.head("Datenschutzerklärung", "Datenschutzerklärung der AFR Inkassokanzlei Joachim Siebert e.K.", "datenschutz.html") + P.header() + body + P.footer()


def agb_html():
    # KOMPLETT 1:1 aus dem Wayback-Snapshot übernommen (Stand: 01.09.2002)
    body = """<main id="main">
""" + page_header('<a href="index.html">Start</a> · AGB', 'Allgemeine Geschäftsbedingungen (AGB)') + """

  <section class="section">
    <div class="container prose">
      <p>der AFR-Inkassokanzlei Joachim Siebert e.K.</p>
      <p>(Stand: 01.09.2002)</p>

      <h2>§ 1 Auftragsannahme</h2>
      <p>Der Inkassounternehmer nimmt nur solche Aufträge zur Forderungseinziehung an, die vollständig, verbindlich und nachvollziehbar unter Verwendung eines Formulars des Inkassounternehmers aufgestellt sind und als unbestritten und gemahnt übergeben werden. Im Rahmen des Auftrages verpflichtet sich der Inkassounternehmer so zu handeln, daß dem Auftraggeber kein Schaden erwächst. Insbesondere wird er sich im Umgang mit dem Schuldner streng an die Vorgaben der Rechtsordnung und an die guten Sitten halten.</p>

      <h2>§ 2 Inhalt und Umfang der Auftragserteilung</h2>
      <p>(1) Der Auftraggeber ist verpflichtet, über die zum Einzug abgetretene Forderung umfassend und wahrheitsgemäß Auskunft zu erteilen. Zweifel am rechtlichen Bestand der Forderung, hat er auch ohne Aufforderung mitzuteilen. Mit der Auftragserteilung übernimmt der Inkassounternehmer für den Auftraggeber die alleinige Forderungsverwaltung. Die zur Einziehung der Forderung notwendig erscheinenden Maßnahmen liegen im Ermessen des Inkassounternehmers. Dem Auftraggeber ist es auch nicht mehr gestattet, die Forderungssache selbst zu bearbeiten, oder durch Dritte bearbeiten zu lassen.</p>
      <p>(2) Mit der Auftragserteilung gestattet der Auftraggeber dem Inkassounternehmer, mit dem Schuldner neue Zahlungsziele oder Teilzahlungen zu vereinbaren. Der Inkassounternehmer ist ohne vorherige, ausdrückliche Erlaubnis des Auftraggebers nicht berechtigt, dem Schuldner Forderungen oder Teile davon zu erlassen. Im Falle titulierter Forderungen oder solcher, die aufgrund einer Vereinbarung zwischen dem Auftraggeber und dem Inkassounternehmer als uneinbringlich eingestuft wurden, darf der Inkassounternehmer dem Schuldner jedoch bei fristgemäßer Einhaltung einer vereinbarten Ratenzahlung die Inrechnungstellung weiterer Zinsen ab Aufnahme der Ratenzahlung bis zur Tilgung erlassen.</p>
      <p>(3) Werden gerichtliche Maßnahmen notwendig, ist die Forderungssache durch den Inkassounternehmer an einen Rechtsanwalt zu delegieren. Die Wahl des Rechtsanwalts obliegt dem Auftraggeber. Übt der Auftraggeber sein Wahlrecht nicht aus, werden bei Bedarf Vertragsanwälte des Inkassounternehmers tätig. Dem Inkassounternehmer ist es gestattet Rechtsanwälte im Namen des Auftraggebers zu beauftragen. Der Rechtsanwalt erhält in jedem Fall die unwiderrufliche Weisung, nach Durchführung der prozessualen Maßnahmen, die weitere Bearbeitung wieder an den Inkassounternehmer abzugeben. Das Recht und die Pflicht zur Forderungsverwaltung und Abrechnung wird nicht durch die Beauftragung eines Rechtsanwalts zur Weiterverfolgung der Forderung berührt.</p>
      <p>(4) Soweit es auf den Zeitpunkt der Auftragserteilung ankommt, ist der Tag des Auftragseingangs bei dem Inkassounternehmer maßgebend. Ein Auftrag gilt mit Eingang als bedingt auflösend angenommen.</p>
      <p>(5) Eine Verpflichtung verjährungsunterbrechende oder -hemmende Maßnahmen vorzunehmen oder vornehmen zu lassen, besteht ohne konkrete, schriftliche Weisung des Auftraggebers nicht. Dies gilt insbesondere dann, wenn der Aufenthaltsort von Schuldnern unbekannt ist oder eine erkennbare Zahlungsunfähigkeit vorliegt.</p>

      <h2>§ 3 Auftragsverfahren</h2>
      <p>(1) Der Inkassounternehmer ist verpflichtet, ein spezielles Konto einzurichten, auf welchem sämtliche Beträge, die für den Auftraggeber eingenommen werden, verbleiben. Der Inkassounternehmer ist nur berechtigt, über solche Beträge zu verfügen, die aufgrund der jeweils gültigen Gebühren- und Auslagentarifen des Inkassounternehmers und nach diesen Geschäftsbedingungen fällig geworden sind, dem Inkassounternehmer also selbst zustehen. Der Inkassounternehmer ist verpflichtet, mindestens einmal jeden Monat eingegangene Beträge, die der Auftraggeber beanspruchen kann, an diesen weiterzuleiten. Geringfügige Beträge unter EUR 50,- sind jedoch nur bei Abschluß des Auftrages, ansonsten nur auf Anforderung auszuzahlen.</p>
      <p>(2) Der Inkassounternehmer ist verpflichtet, in einem besonderen Register jeden Auftrag mittels Handakten zu erfassen, wobei die Handakten stets vollständig verfügbar sein müssen. Eine Verpflichtung, die Handakten länger als gesetzlich vorgesehen aufzubewahren, besteht nicht. Dem Auftraggeber ist auf Verlangen Einsicht in die Akten und in die Buchführung zu gewähren, soweit dies zur Überprüfung von Vorgängen notwendig ist. Im Falle der Geltendmachung dieses Einsichtsrechts, hat der Inkassounternehmer dem Auftraggeber in den folgenden acht Tagen einen Termin während der gewöhnlichen Bürozeiten zur Einsichtnahme zu benennen, wenn dies nicht ausnahmsweise für eine der Vertragsparteien unbillig ist.</p>
      <p>(3) Gebühren und Auslagen werden dem Auftraggeber nach dem jeweils gültigen Gebühren- und Auslagentarif in Rechnung gestellt. Gegenüber dem Schuldner dürfen im Rahmen eines Inkassomandats ebenfalls nur diese Beträge geltend gemacht werden. Gebührenansprüche werden in dem Umfang fällig, wie eine Verrechnungsmöglichkeit mit vom Schuldner erlangten Zahlungen des einzelnen Falles besteht. Jedoch werden bei Abschluß des Falles, bei Uneinbringlichkeit oder bei einer Kündigung des Auftrags seitens des Auftraggebers Gebührenansprüche sofort fällig. Auslagen werden mit Durchführung der Maßnahme, Erfolgsprovisionen mit Zahlungseingang fällig. Den Ansprüchen des Inkassounternehmers gegen den Auftraggeber steht nicht entgegen, daß Zahlungen auf die beizutreibende Forderung unmittelbar an den Auftraggeber geleistet werden. Jede Gutschrift des Auftraggebers zugunsten des Schuldners nach Auftragserteilung wird dem Auftragsverhältnis mit der entsprechenden Gebühren- bzw. Provisionsfolge zugeschrieben. Erfolgsprovisionen, sowie die Auftragsgebühr sind nicht vom Schuldner, sondern allein vom Auftraggeber zu erstatten. Änderungen der Gebühren- und Auslagentarife sind dem Auftraggeber mindestens einen Monat vor Wirksamkeit bekannt zugegeben. Änderungen der Auslagenpauschalen während der Laufzeit eines Inkassoauftrags sind nur möglich, soweit auch für die Neuaufträge die Auslagenpauschalen geändert werden. Die Änderungen gelten als genehmigt, wenn der Auftraggeber nicht binnen zwei Wochen nach Zugang schriftlich widerspricht. Hinsichtlich der Auslagenpauschalen ist der Inkassounternehmer vom Nachweis der Höhe der angefallenen Auslagen befreit.</p>
      <p>(4) Der Inkassounternehmer ist berechtigt, offene Forderungen gegenüber dem Auftraggeber auch mit eingehenden Zahlungen anderer Inkassoaufträge desselben Auftraggebers, aus denen diese Forderungen nicht resultieren, zu verrechnen. Anfallende Gerichts- und Anwaltskosten und sonstige Auslagen hat der Auftraggeber auf Anforderung unverzüglich zu erstatten; soweit dem Auftraggeber ein Guthaben zusteht, darf der Inkassounternehmer diese Kosten damit verrechnen.</p>

      <h2>§ 4 Haftung</h2>
      <p>(1) Der Inkassounternehmer haftet stets, insbesondere aber in bezug auf seine Mitarbeiter, nur für grobe Fahrlässigkeit und Vorsatz. Dies gilt auch bezüglich der im Rahmen des Auftrages seitens des Auftraggebers überlassenen Urkunden und sonstigen Papiere.</p>
      <p>(2) Der Auftraggeber ist verantwortlich für den rechtlichen Bestand der zur Einziehung übertragenen Forderung und haftet für die Folgen falscher oder unvollständiger Angaben. Im Rahmen dieser Haftung hat der Auftraggeber den Inkassounternehmer von eventuellen Schadensersatzforderungen freizustellen.</p>

      <h2>§ 5 Auftragsablehnung, Kündigung, Datenschutz, Gerichtsstand, Sonstiges</h2>
      <p>(1) Der Inkassounternehmer ist berechtigt Aufträge abzulehnen oder unerledigt zurückzugeben. In diesem Fall hat er keinen Anspruch auf Gebühren und ist nicht verpflichtet, auf laufende Verjährungsfristen hinzuweisen. Im Falle einer Auftragsablehnung oder -rückgabe binnen 20 Tagen gilt der Auftrag als von Anfang an abgelehnt.</p>
      <p>(2) Der Auftraggeber kann den Auftrag nur unter Einhaltung einer Frist von 2 Jahren zum Quartalsende kündigen.</p>
      <p>(3) Der Inkassounternehmer ist in den Fällen des § 4 Abs. 2 dieser Geschäftsbedingungen berechtigt, den Auftrag binnen eines Monats fristlos zu kündigen. Die Monatsfrist beginnt mit Kenntniserlangung des Kündigungsgrundes, spätestens jedoch ein Jahr nach dem Vertragsverstoß durch den Auftraggeber.</p>
      <p>(4) Die Angaben des Auftraggebers, sowie die der Schuldner werden vertraulich behandelt. Eine Weitergabe an Dritte ist nur statthaft, wenn das Gesetz dies vorschreibt oder die Einwilligung des Auftraggebers bzw. Schuldners vorliegt. Der Auftraggeber wird davon in Kenntnis gesetzt, daß seine Angaben und die Daten im Zusammenhang mit der Durchführung des Auftrags über EDV gespeichert und verwaltet werden.</p>
      <p>(5) Die eventuelle rechtliche Unwirksamkeit einzelner Klauseln, berührt die Wirksamkeit der übrigen nicht. Vielmehr verpflichten sich die Vertragsparteien, für diesen Fall eine rechtswirksame Vereinbarung zu treffen, die der unwirksamen Regelung wirtschaftlich am nächsten kommt. Soweit der Auftraggeber Vollkaufmann ist, ist als Gerichtsstand Osnabrück vereinbart. Für Verträge mit ausländischen Auftraggebern gilt das Recht der Bundesrepublik Deutschland.</p>
    </div>
  </section>
</main>
"""
    return P.head("AGB", "Allgemeine Geschäftsbedingungen der AFR Inkassokanzlei Joachim Siebert e.K. (Stand: 01.09.2002).", "agb.html") + P.header() + body + P.footer()


def fragen_html():
    body = f"""<main id="main">
{page_header('<a href="index.html">Start</a> · Fragen und Anregungen', 'Fragen und Anregungen')}

  <section class="section">
    <div class="container container-narrow">
      <p><strong>Ihre Meinung ist uns wichtig!</strong></p>
      <p>Sofern Sie mit unserer Leistung zufrieden waren oder Fragen, Anregungen oder Kritik anbringen möchten, schreiben Sie uns!</p>
      <p>Sie können dazu das folgende Formular verwenden:</p>

      <form class="form" action="mailto:{P.CONTACT['mail']}" method="post" enctype="text/plain">
        <div class="form-field">
          <label for="nachricht">Ihre Nachricht *</label>
          <textarea id="nachricht" name="Nachricht" required></textarea>
        </div>

        <h3>Kontaktdaten</h3>
        <p class="form-note">Ihre Kontaktdaten werden von uns vertraulich behandelt und nicht an Dritte weitergegeben.</p>

        <div class="form-row two">
          <div class="form-field">
            <label for="vorname">Vorname *</label>
            <input id="vorname" name="Vorname" type="text" required>
          </div>
          <div class="form-field">
            <label for="nachname">Nachname *</label>
            <input id="nachname" name="Nachname" type="text" required>
          </div>
        </div>

        <div class="form-field">
          <label for="firma">Firma</label>
          <input id="firma" name="Firma" type="text">
        </div>

        <div class="form-field">
          <label for="strasse">Straße</label>
          <input id="strasse" name="Strasse" type="text">
        </div>

        <div class="form-row two">
          <div class="form-field">
            <label for="plz">PLZ</label>
            <input id="plz" name="PLZ" type="text">
          </div>
          <div class="form-field">
            <label for="ort">Ort</label>
            <input id="ort" name="Ort" type="text">
          </div>
        </div>

        <div class="form-field">
          <label for="land">Land</label>
          <input id="land" name="Land" type="text" value="Deutschland">
        </div>

        <div class="form-row two">
          <div class="form-field">
            <label for="telefon">Telefon</label>
            <input id="telefon" name="Telefon" type="tel">
          </div>
          <div class="form-field">
            <label for="email">E-Mail *</label>
            <input id="email" name="E-Mail" type="email" required>
          </div>
        </div>

        <div class="form-field">
          <label style="display:flex; align-items:flex-start; gap:0.5rem; font-weight:400; font-size:0.9rem">
            <input type="checkbox" required style="margin-top:0.25rem">
            <span>Einwilligung in die Datenübertragung * – Hiermit willige ich in die Übertragung, Speicherung und Weiterverarbeitung meiner persönlichen Daten zum Zwecke der Bearbeitung meiner Anfrage ein. <a href="datenschutz.html">Datenschutzerklärung</a></span>
          </label>
        </div>

        <div>
          <button class="btn btn-primary" type="submit">Senden</button>
        </div>
      </form>
    </div>
  </section>
</main>
"""
    return P.head("Fragen und Anregungen", "Ihre Meinung ist uns wichtig! Schreiben Sie uns Ihre Fragen, Anregungen oder Kritik.", "fragen-und-anregungen.html") + P.header() + body + P.footer()


def notfound_html():
    body = """<main id="main">
  <section class="section" style="padding:6rem 0; text-align:center">
    <div class="container container-narrow">
      <p style="font-size:5rem; line-height:1; color:var(--color-primary); font-weight:700; margin:0">404</p>
      <h1>Seite nicht gefunden</h1>
      <p class="lead">Die aufgerufene Seite existiert nicht.</p>
      <p>
        <a class="btn btn-primary" href="index.html">Zur Startseite</a>
      </p>
    </div>
  </section>
</main>
"""
    return P.head("Seite nicht gefunden", "Die gesuchte Seite existiert nicht.", "404.html") + P.header() + body + P.footer()


# -----------------------------------------------------------------------------
#  Run
# -----------------------------------------------------------------------------

PAGES = {
    "index.html": index_html,
    "leistungen.html": leistungen_html,
    "auftragserteilung.html": auftragserteilung_html,
    "kosten.html": kosten_html,
    "ueber-uns.html": ueber_uns_html,
    "kontakt.html": kontakt_html,
    "impressum.html": impressum_html,
    "datenschutz.html": datenschutz_html,
    "agb.html": agb_html,
    "fragen-und-anregungen.html": fragen_html,
    "404.html": notfound_html,
}


def main():
    for fname, fn in PAGES.items():
        path = OUT / fname
        path.write_text(fn(), encoding="utf-8")
        size = path.stat().st_size
        print(f"  {fname:35s}  {size:>7,} bytes")


if __name__ == "__main__":
    main()

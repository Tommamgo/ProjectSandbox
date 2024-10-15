# Automatisierte Vertrags- und Gesetzesanalyse

## Projektidee

Die Idee zu diesem Projekt kam mir, nachdem ich selbst eine frustrierende Erfahrung mit meiner Haftpflichtversicherung gemacht habe. Ich hatte bei meiner Versicherung einen Schaden gemeldet, den ich bei meiner Freundin verursacht hatte. Die Versicherung lehnte den Schaden jedoch ab, mit der Begründung, dass wir zusammenwohnen und daher kein Anspruch bestünde. Das hat mich ziemlich geärgert. Daraufhin habe ich alle Vertragsunterlagen, Beschreibungen und E-Mails an ChatGPT übergeben und gefragt, ob es einen Weg gibt, wie die Versicherung den Schaden doch übernehmen könnte. Am Ende habe ich es tatsächlich geschafft, dass der Schaden erstattet wurde.

Daraus entstand die Idee, eine Plattform oder ein Machine-Learning-Modell zu entwickeln, das genau bei solchen Problemen hilft. Es soll Verträge und Gesetze analysieren und bei konkreten Fragen oder Streitfällen mögliche Lösungsansätze liefern. Wichtig dabei: Es geht nicht darum, eine rechtlich verbindliche Antwort zu geben, sondern eher um eine erste Orientierung – so wie man es von einer Erstberatung beim Anwalt kennt.

Ich habe mich auch mit einer Anwältin darüber unterhalten. Sie meinte, dass solche Tools grundsätzlich sinnvoll sein können und es bereits erste Ansätze gibt, aber Gesetze immer Interpretationsspielraum bieten und die Argumentation oft auf vergleichbaren Fällen basiert. Genau da könnten wir ansetzen: Gesetze und Urteile scrapen und daraus ein System aufbauen, das erste Einschätzungen zu Verträgen und rechtlichen Fragestellungen liefert.

## Ziel des Projekts

Das Hauptziel ist es, eine Plattform zu entwickeln, die Verträge und Gesetze automatisch analysiert und bei bestimmten rechtlichen Sachverhalten Unterstützung bietet. Die Anwendung soll nicht als Ersatz für eine Rechtsberatung dienen, sondern eher als Hilfsmittel, um die verschiedenen Möglichkeiten aufzuzeigen, wie man eine Situation angehen könnte – ähnlich einer ersten Beratung beim Anwalt.

## Geplante Funktionen

- **Vertrags- und Gesetzesanalyse**: Automatische Auswertung von Vertragsklauseln und gesetzlichen Bestimmungen.
- **Datenbeschaffung**: Scraping von Gesetzen und Urteilen aus dem Internet oder die Nutzung bestehender Datensätze, falls verfügbar.
- **Vergleichbare Fälle**: Einbindung von Präzedenzfällen und Urteilen, um mögliche Argumentationsstrategien aufzuzeigen.
- **Web-App**: Eine einfache Oberfläche, auf der Nutzer ihre Frage oder den Sachverhalt eingeben können und eine Einschätzung bekommen.

## Technische Umsetzung

- **Programmiersprache**: Python für das Machine-Learning-Modell.
- **Machine Learning**: Einsatz von Natural Language Processing (NLP) für die Analyse von Verträgen und Gesetzen.
- **Web-App**: Entwicklung einer Webseite, auf der Nutzer ihre Fragen eingeben und die Analyseergebnisse sehen können.
- **Datenbank**: MongoDB zur Speicherung der Gesetzestexte, Verträge und Präzedenzfälle.


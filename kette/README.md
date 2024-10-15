# Die Vibrierende Kette

## Projektbeschreibung

Die vibrierende Kette ist ein kleines IoT-Projekt, das auf einer Bluetooth-Verbindung zwischen einem ESP32-Mikrocontroller und einem Smartphone basiert. Die Kette ist mit einem Vibrationsmotor, einem ESP32-Chip und einer Batterie ausgestattet. Über eine App, die Requests an eine Datenbank sendet, wird die Kette aktiviert und beginnt zu vibrieren. Das Ziel des Projekts ist es, eine Verbindung zwischen zwei Personen zu schaffen, bei der sie sich gegenseitig "anpingen" können, indem sie einen Button in der App oder an der Kette drücken.

Die Grundidee ist ein einfaches, aber effektives Kommunikationsmittel, mit dem Partner sich gegenseitig signalisieren können, dass sie aneinander denken. Dies könnte ein liebevolles Zeichen der Verbundenheit sein, auch wenn sie räumlich getrennt sind.

## Features
- **Bluetooth-Verbindung**: Die Kette verbindet sich über Bluetooth mit einem Smartphone.
- **Vibration als Feedback**: Bei Empfang eines Requests über die App beginnt die Kette zu vibrieren.
- **Bidirektionale Kommunikation**: Über die App oder durch einen Button auf der Kette können Signale gesendet und empfangen werden.
- **Firebase-Integration**: Die Requests werden über eine Cloud-Datenbank (Firebase) abgewickelt.

## Komponenten

### Hardware
- **ESP32 (XIAO ESP32C3)**: Der Mikrocontroller, der die Bluetooth-Verbindung herstellt und die Vibration steuert.
  - [XIAO ESP32C3 Getting Started](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/)
- **Vibrationsmotoren**: Kleine Motoren, die das haptische Feedback durch Vibration geben.
  - [Link zu den Vibrationsmotoren](https://eckstein-shop.de/Motion-Vibration-Motoren)
- **Batterie**: Zur Stromversorgung der Kette (muss noch genauer spezifiziert werden).

### Software
- **App**: Entwickelt für Android in Kotlin oder mit Flutter (Dart), zur Steuerung und Kommunikation mit der Kette.
- **Backend**: Firebase wird für die Verwaltung der Requests und Datenbankverbindung genutzt.
- **Firmware**: Der ESP32 wird mit Arduino programmiert, um die Kommunikation mit der App und die Steuerung des Vibrationsmotors zu ermöglichen.

## Ablauf und Funktionalität

1. Die Kette wird über Bluetooth mit der App verbunden.
2. Die App sendet über das Internet einen Request an die Firebase-Datenbank.
3. Der ESP32 auf der Kette empfängt diesen Request und aktiviert den Vibrationsmotor.
4. Optional: Ein Button auf der Kette kann auch verwendet werden, um einen Request an die App zu senden, die dann das Signal an den Partner weiterleitet.

## Mögliche Erweiterungen
- Erweiterung der App für iOS.
- Hinzufügen weiterer Interaktionsmöglichkeiten, wie z. B. verschiedene Vibrationsmuster.

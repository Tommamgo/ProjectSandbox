from __future__ import print_function
from tqdm import tqdm
import json
import time
import oldp_client
from oldp_client.rest import ApiException
from pprint import pprint
import re

api_path = './apikey'

# Beispiel für die Verwendung der Funktion
name = "Urteil"


def read_api_key(filepath):
    """
    Liest den Inhalt der Datei 'apikey' und entfernt überflüssige Leerzeichen am Anfang und Ende.
    
    Args:
    filepath (str): Der Pfad zur Datei, die gelesen werden soll.

    Returns:
    str: Der getrimmte Inhalt der Datei.
    """
    try:
        with open(filepath, 'r') as file:
            api_key = file.read().strip()
            return api_key
    except FileNotFoundError:
        print(f"Die Datei {filepath} wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

def append_to_json(file_path, new_entries):
    # Datei öffnen und den vorhandenen Inhalt lesen
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            # Vorhandene Daten laden
            data = json.load(file)
            # Neue Einträge zu 'results' hinzufügen
            data['results'].extend(new_entries)
            
            # Dateiinhalt aktualisieren
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()
    except FileNotFoundError:
        # Datei neu erstellen, falls nicht vorhanden
        data = {
            "count": len(new_entries),
            "next": None,
            "previous": None,
            "results": new_entries
        }
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


# get the API key out of the file
api_key = read_api_key(api_path)


# Configure API key authorization: api_key
configuration = oldp_client.Configuration()
configuration.api_key['Authorization'] = api_key

#  create an instance of the API class
api_instance = oldp_client.LawsApi(oldp_client.ApiClient(configuration))
#book_id = 'book_id_example' # str |  (optional)
#book__latest = 'book__latest_example' # str |  (optional)
#book__revision_date = 'book__revision_date_example' # str |  (optional)
limit = 1 # int | Number of results to return per page. (optional)
offset = 0 # int | The initial index from which to return the results. (optional)
with tqdm(desc="Lade Einträge", unit=" Eintrag", unit_scale=True) as pbar:
    while True: 
        try:
            api_response = api_instance.laws_list(
                #book_id=book_id, 
                #book__latest=book__latest, 
                #book__revision_date=book__revision_date, 
                limit=limit, 
                #offset=offset
                )
            #print(type(api_response))
            #print(api_response)

            # Überprüfen, ob eine `to_dict()` Methode existiert
            if hasattr(api_response, 'to_dict'):
                parsed_data = api_response.to_dict()  # Konvertiert das Objekt in ein Dictionary
            else:
                # Fallback: Verwenden von `__dict__`, falls keine `to_dict()` Methode vorhanden ist
                parsed_data = api_response.__dict__

            append_to_json('/home/linus/output_data.json', [parsed_data])
            
            # Fortschrittsbalken um einen Eintrag erhöhen
            pbar.update(1)
            
            # Offset erhöhen, um den nächsten Datensatz zu holen
            offset += 1
            limit += 1

            # Test: Verzögerung einbauen, um den Fortschrittsbalken zu sehen (kann entfernt werden)
            time.sleep(0.5)

        except ApiException as e:
            print("Exception when calling LawsApi->laws_list: %s\n" % e)

from __future__ import print_function
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
#offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.laws_list(
            #book_id=book_id, 
            #book__latest=book__latest, 
            #book__revision_date=book__revision_date, 
            limit=limit, 
            #offset=offset
            )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LawsApi->laws_list: %s\n" % e)

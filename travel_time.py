import googlemaps
from datetime import datetime


def calculate_travel_times(api_key, postal_codes, university_address, mode='driving'):
    gmaps = googlemaps.Client(key=api_key)

    travel_times = []

    for postal_code in postal_codes:
        result = gmaps.distance_matrix(origins=postal_code,
                                       destinations=university_address,
                                       mode=mode,
                                       departure_time=datetime.now())

        duration = result['rows'][0]['elements'][0]['duration']['text']
        travel_times.append((postal_code, duration))

    return travel_times
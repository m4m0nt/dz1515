import json

country_capitals = {}


def add_country_capital(country, capital):
    country_capitals[country] = capital


def remove_country_capital(country):
    country_capitals.pop(country, None)


def search_capital(country):
    return country_capitals.get(country, "Capital not found.")


def edit_country_capital(country, new_capital):
    if country in country_capitals:
        country_capitals[country] = new_capital


def save_data(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(country_capitals, f)


def load_data(filename):
    global country_capitals
    with open(filename, 'r', encoding='utf-8') as f:
        country_capitals = json.load(f)


add_country_capital("Ukraine", "Kyiv")
add_country_capital("Poland", "Warsaw")
print(country_capitals)

music_bands = {}


def add_band_albums(band, albums):
    music_bands[band] = albums


def remove_band(band):
    music_bands.pop(band, None)


def search_albums(band):
    return music_bands.get(band, "Albums not found.")


def edit_band_albums(band, new_albums):
    if band in music_bands:
        music_bands[band] = new_albums


def save_data(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(music_bands, f)


def load_data(filename):
    global music_bands
    with open(filename, 'r', encoding='utf-8') as f:
        music_bands = json.load(f)


print(music_bands)

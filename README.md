# Folium — Interactive Maps

Generates interactive HTML maps with [Folium](https://python-visualization.github.io/folium/)
from Excel/JSON data sources. The output `.html` files can be opened in any browser.

## What it does (`Foulium.py`)

- **`trProvices`** — reads `tr-cities.xlsx` (city name + latitude/longitude) and
  places a marker for every Turkish city, saving the result to
  `Türkiye_ileçeler.html`.
- **`corona_virus`** — reads `world_coronavirus_cases.xlsx` and builds a
  multi-layer COVID-19 map with toggleable `FeatureGroup`s: total cases, death
  rate, active cases, test rate, and population, using circle size and color to
  encode magnitude.

## Layout

```
Foulium/
├── Foulium.py
├── tr-cities.xlsx
├── world_coronavirus_cases.xlsx
├── world.json / Istanbul_Airports.xlsx
└── *.html                 # generated maps
```

> Note: the file paths inside `Foulium.py` are relative to a `myCodes/mapStatistics/`
> directory — adjust them to match the local data files before running.

## Usage

```python
from Foulium import trProvices, corona_virus

trProvices()
corona_virus()
```

## Requirements

- Python 3.x
- `folium`, `pandas`, `openpyxl` (`pip install folium pandas openpyxl`)

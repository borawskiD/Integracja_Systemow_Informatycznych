#gdansk 54.372158, 18.638306
#warszawa 52.237049, 21.017532
#tokio 35.652832, longtitude: 139.839478
#nyc 40.730610, and the longitude is -73.935242
#rabat  34.020882, -6.841650

import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import matplotlib.pyplot as plt
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": [54.372158, 52.237049, 35.652832, 40.73061, 34.020882],
    "longitude": [18.638306, 21.017532, 139.839478, -73.935242, -6.84165],
    "hourly": "temperature_2m",
    "past_days": 14,
    "forecast_days": 16
}
responses = openmeteo.weather_api(url, params=params)

city_dataframes = []
cities = ["Gdansk", "Warszawa", "Tokio", "Nowy Jork", "Rabat"]

for i, response in enumerate(responses):
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    print(hourly_dataframe)
    plt.figure(figsize=(10, 6))
    plt.plot(hourly_dataframe["date"], hourly_dataframe["temperature_2m"], label=f"{cities[i]}")
    plt.title(f'Temperatura dla miasta {cities[i]}')
    plt.xlabel('Data')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'wykresy/{cities[i]}.png')
    plt.show()
    plt.close()
    city_dataframes.append(hourly_dataframe)

plt.figure(figsize=(10, 6))
for i, df in enumerate(city_dataframes):
    plt.plot(df["date"], df["temperature_2m"], label=f"{cities[i]}")

plt.title('Temperatura dla wszystkich miast')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'wykresy/wszystkie-miasta.png')
plt.show()
import requests

API_KEY = "fa131a3a8112addd99e490c0716e6564"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    if kind == "Temperetures":
        filtered_data = [dict["main"]["temp"]for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"]["temp"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo"))
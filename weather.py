import requests


def get_weather_desc_and_temp():
    api_key = "e80739840b62bd421d86d4e9431c1122"
    latitude = "49.245620"
    longitude = "-122.570790"
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&appid=" + api_key + "&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}


def main():
    # Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forcast is", weather_dict.get('description'))
    print('The minimum temperature is', weather_dict.get('temp_min'))
    print('The maximum temperature is', weather_dict.get('temp_max'))


main()

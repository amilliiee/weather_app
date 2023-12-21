import requests
API_KEY = '314f13556211f52a524ea3af7609a2d6'

def to_c(temp):
    return round(temp - 273.15, 1)

def to_f(temp):
    return round(to_c(temp) * 9 / 5 + 32, 1)

def main():
    city = input('Enter city name: ')

    temp_read = input('Would you like the reading in Celsius or Fahrenheit? (C or F) ')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    rsp = requests.get(url)

    if rsp.status_code == 200:
        data = rsp.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        feel = data['main']['feels_like']
        min_t = data['main']['temp_min']
        max_t = data['main']['temp_max']

        if temp_read == 'F' or temp_read == 'f':
            temp = to_f(temp)
            feel = to_f(feel)
            min_t = to_f(min_t)
            max_t = to_f(max_t)
        elif temp_read == 'C' or temp_read == 'c':
            temp = to_c(temp)
            feel = to_c(feel)
            min_t = to_c(min_t)
            max_t = to_c(max_t)

        print(f'Temperature: {temp} {temp_read}')
        print(f'Description: {desc}')
        print(f'Min / max temp: {min_t} {temp_read} / {max_t} {temp_read}')
        print(f'Feels like: {feel} {temp_read}')
    else:
        print('Error fetching data.')

main()
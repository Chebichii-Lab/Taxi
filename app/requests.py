from app import app
import urllib.request,json
from app.models import driver

Driver = driver.Driver

# Getting api key
api_key = app.config['GOOGLE_MAPS_API_KEY']

# Getting the movie base url
base_url = app.config["GOOGLE_MAPS_API_BASE_URL"]


def get_drivers(location):
    '''
    Function that gets the json response to our url request
    '''
    get_drivers_url = base_url.format(location,api_key)

    with urllib.request.urlopen(get_drivers_url) as url:
        get_drivers_data = url.read()
        get_drivers_response = json.loads(get_drivers_data)

        driver_results = None

        if get_drivers_response['results']:
            driver_results_list = get_drivers_response['results']
            driver_results = process_results(driver_results_list)


    return driver_results

def process_results(driver_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    driver_results = []
    for driver_item in driver_list:
        id = driver_item.get('id')
        name = driver_item.get('original_name')
        phone_number = driver_item.get('phone_number')
        image = driver_item.get('image_path')
        car_plate = driver_item.get('car_plate')
        car_brand = driver_item.get('car_number')
        car_colour = driver_item.get('car_colour')

        if image:
            driver_object = Driver(id,name,phone_number,image,car_plate,car_brand,car_colour)
            driver_results.append(driver_object)

    return driver_results


def get_driver(id):
    get_driver_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_driver_details_url) as url:
        driver_details_data = url.read()
        driver_details_response = json.loads(driver_details_data)

        driver_object = None
        if driver_details_response:
            id = driver_details_response.get('id')
            name = driver_details_response.get('original_name')
            phone_number = driver_details_response.get('phone_number')
            image = driver_details_response.get('image_path')
            car_plate = driver_details_response.get('car_plate')
            car_brand = driver_details_response.get('car_brand')
            car_colour = driver_details_response.get('car_colour')

            driver_object = Driver(id,name,phone_number,image,car_plate,car_brand,car_colour)

    return driver_object

def search_driver(driver_name):
    search_driver_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,driver_name)
    with urllib.request.urlopen(search_driver_url) as url:
        search_driver_data = url.read()
        search_driver_response = json.loads(search_driver_data)

        search_driver_results = None

        if search_driver_response['results']:
            search_driver_list = search_driver_response['results']
            search_driver_results = process_results(search_driver_list)


    return search_driver_results
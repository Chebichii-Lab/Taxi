from flask import render_template
from app import app
from app.requests import get_drivers,get_driver,search_driver


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    name_drivers = get_drivers('name')
    print(name_drivers)
    title = 'Home - Welcome to the Safe DADA website'
    return render_template('index.html', title = title,name = name_drivers)

@app.route('/driver/<int:id>')
def driver(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    driver = get_driver(id)
    name = f'{driver.name}'

    return render_template('driver.html',name = name,driver = driver)

@app.route('/search/<driver_name>')
def search(driver_name):
    '''
    View function to display the search results
    '''
    driver_name_list = driver_name.split(" ")
    driver_name_format = "+".join(driver_name_list)
    searched_drivers = search_driver(driver_name_format)
    title = f'search results for {driver_name}'
    return render_template('search.html',driver = searched_drivers)
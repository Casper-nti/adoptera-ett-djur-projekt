"""
  A Flask application for adopting pets.

  This application allows users to browse and adopt different types of pets such as dogs, cats, and rabbits.

  Attributes:
    pets (dict): A dictionary containing information about available pets.

  Routes:
    - `/`: The home page of the application.
    - `/animals/<int:pet_type>`: Displays a list of pets based on the specified pet type.
    - `/animals/<int:pet_type>/<int:pet_id>`: Displays information about a specific pet.

  """
from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the home page of the application.

    Returns:
      str: The HTML content of the home page.
    """
    return '''<h1>Adopt a Pet!</h1> 
  <p>Browse through the links below to find your new furry friend:</p> 
  <ul> 
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''


@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  """Generate HTML list of animals of a specific pet type.

  Args:
      pet_type (str): The type of pet (e.g., 'dog', 'cat', 'bird').

  Returns:
      str: The generated HTML code containing a list of animals of the specified pet type.
  """  
  html = f'''<h1>List of {pet_type}</h1>
  <ul>'''
  for id, pet in enumerate(pets[pet_type]):
    html += f'''<li><a href="/animals/{pet_type}/{id}">{pet["name"]}</a></li>'''

  html += '</ul>'
  return html

@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  """
  Display information about a pet.

  Args:
    pet_type (str): The type of pet.
    pet_id (int): The ID of the pet.

  Returns:
    str: HTML content representing the pet information.
  """  
  pet = pets[pet_type][pet_id]=pets[pet_type][pet_id]
  html = f'''<h1>{pet["name"]}</h1>
  <img src="{pet["url"]}">
  <p>{pet["description"]}</p>
  <ul>
    <li>age: {pet["age"]}</li>
    <li>breed: {pet["breed"]}</li>
  </ul>'''
  
  return html

app.run(debug=True, host="0.0.0.0")

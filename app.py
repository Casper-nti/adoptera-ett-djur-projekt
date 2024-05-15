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

@app.route('/animals/<str:pet_type>')
def animals(pet_type):
    """
    Renders a list of pets based on the specified pet type.

    Args:
      pet_type (int): The type of pet to display.

    Returns:
      str: The HTML content of the list of pets.
    """
    return f'''<h1>List of {pet_type}</h1>'''

@app.route('/animals/<int:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    """
    Renders information about a specific pet.

    Args:
      pet_type (int): The type of pet.
      pet_id (int): The ID of the pet.

    Returns:
      str: The HTML content of the pet information.
    """
    return f'''<h1>{pet_id} {pet_type}</h1>'''

  # Viktigt: Denna kodrad ska alltid placeras längst ner i filen.
  # Detta för att säkerställa en korrekt uppstart av servern.
app.run(debug=True, host="0.0.0.0")

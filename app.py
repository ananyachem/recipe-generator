import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = '3b40537ebc40431d8cf6bd611c73d9c7'

# Basic Recipe Search Function
def get_recipes(ingredients):
    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={API_KEY}'
    response = requests.get(url)
    recipes = response.json()
    return recipes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        recipes = get_recipes(ingredients)
        return render_template('index.html', recipes=recipes)
    return render_template('index.html', recipes=[])

if __name__ == '__main__':
    app.run(debug=True)

#Choose your own adventure
from app import app
from flask import render_template, request
from app.models import model, formopener
from app.models import branches

@app.route('/')
@app.route('/index')
def index():
    location = "beginning"
    return render_template('index.html', location = location)
@app.route('/play')
def play():
    return render_template('round1.html')

@app.route('/round1')
def locationCheck(): #Checks location and returns prompts based on location 
    location = "beginning"
    choice_a = ""
    choice_b = ""
    choice_c = ""
    prompt = ""
    if location == "beginning":
        choice_a = branches.choices[0]['a']
        choice_b = branches.choices[0]['b']
        choice_c = branches.choices[0]['c']
        prompt = branches.locations['beginning']
    elif location == "village":
        choice_a = branches.choices[1]['a']
        choice_b = branches.choices[1]['b']
        prompt = branches.locations['village']
    return render_template('round1.html', prompt = prompt, location = location, choice_a = choice_a, choice_b = choice_b, choice_c = choice_c)

app.route('/switch') #Changes location after an option is selected
def switchLocation():
    choice = ""
    if location == 'beginning' and choice == choice_a:
        location == 'village'
    elif location == 'beginning' and choice == choice_b:
        location ==
        
    

# @app.route('/round1')
# def round1():
#     prompt = "hello"
#     choice = "A choice"
#     return render_template('round1.html', prompt=prompt, choice=choice)
    
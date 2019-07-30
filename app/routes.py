#Choose your own adventure
from app import app
from flask import render_template, request
from app.models import model, formopener
from app.models import branches
from app.models import model


newPlayer = model.Player("beginning")

@app.route('/')
@app.route('/index')
def index():
    newPlayer = model.Player("beginning")
    return render_template('index.html')

#Was supposed to start play, but then I realized I could just use /round1 to zoop to beginning
# @app.route('/play')
# def play():
#     locationCheck()
#     return render_template('play.html')

@app.route('/round1')
def locationCheck(): #Checks location and returns prompts based on location 
    response = dict(request.args) #Checks values from round1 (ex, answer is a)
    choice = response['answer'] #Sets variable choice equal to the choice (a, b, c)
    choice_a = ""
    choice_b = ""
    choice_c = ""
    prompt = ""
    if choice == "play": 
        newPlayer.location = "beginning"
    if newPlayer.location == "beginning":
        choice_a = branches.choices[0]['a']
        choice_b = branches.choices[0]['b']
        choice_c = branches.choices[0]['c']
        prompt = branches.locations['beginning']
        print(choice)
        if choice == "a":
            newPlayer.location = "village"
            choice_a = branches.choices[1]['a']
            choice_b = branches.choices[1]['b']
            choice_c = ""
            prompt = branches.locations['village']
        if choice == "b":
            newPlayer.location = "forest"
            prompt = branches.locations['forest']
            choice_a = ""
            choice_b = ""
            choice_c = ""
        if choice == "c":
            newPlayer.location = "abandon"
            prompt = branches.locations['abandon']
            
    elif newPlayer.location == "village":
        choice_a = branches.choices[1]['a']
        choice_b = branches.choices[1]['b']
        prompt = branches.locations['village']
        if choice == "a":
            prompt = branches.locations['searchedVil']
            choice_a = ""
            choice_b = ""
            choice_c = ""
        elif choice == "b":
            prompt = branches.locations['abandon']
            choice_a = ""
            choice_b = ""
            choice_c = ""
    return render_template('round1.html', prompt = prompt, choice_a = choice_a, choice_b = choice_b, choice_c = choice_c, choice = choice)

# @app.route('/round2')
# def locationCheck2(): #Checks location and returns prompts based on location 
#     response = dict(request.args)
#     choice = response['answer']
#     choice_a = ""
#     choice_b = ""
#     choice_c = ""
#     prompt = ""

#     if newPlayer.location == "beginning":
#         choice_a = branches.choices[0]['a']
#         choice_b = branches.choices[0]['b']
#         choice_c = branches.choices[0]['c']
#         prompt = branches.locations['beginning']
#         if choice == "a":
#             newPlayer.location = "village"
#         if choice == "b":
#             newPlayer.location = "forest"
#             prompt = branches.locations['forest']
#             choice_a = ""
#             choice_b = ""
#             choice_c = ""
#         if choice == "c":
#             newPlayer.location = "abandon"
#             prompt = branches.locations['abandon']
#     if newPlayer.location == "village":
#         choice_a = branches.choices[1]['a']
#         choice_b = branches.choices[1]['b']
#         prompt = branches.locations['village']
#         if choice == "a":
#             prompt = branches.locations['searchedVil']
#             choice_a = ""
#             choice_b = ""
#             choice_c = ""
            
#         if choice == "b":
#             prompt = branches.locations['abandon']
#     return render_template('round2.html', prompt = prompt, choice_a = choice_a, choice_b = choice_b, choice_c = choice_c, choice = choice)

# app.route('/switch') #Changes location after an option is selected
# def switchLocation():
#     choice = ""
#     if location == 'beginning' and choice == choice_a:
#         location == 'village'
#     # elif location == 'beginning' and choice == choice_b:
#     #     location ==
        
    

# @app.route('/round1')
# def round1():
#     prompt = "hello"
#     choice = "A choice"
#     return render_template('round1.html', prompt=prompt, choice=choice)
    


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
        prompt = branches.locations['beginning']
        print(choice)
        if choice == "a":
            newPlayer.location = "village"
            # choice_a = branches.choices[13]['a']
            # choice_b = branches.choices[13]['b']
            # prompt = branches.locations['village']
            # if choice == "a":
            #     newPlayer.location = "peace"
                # choice_a = branches.choices[15]['a']
                # choice_b = branches.choices[15]['b']
                # prompt = branches.locations['peace']
        if choice == "b":
            newPlayer.location = "river"
            # newPlayer.location = "river"
            # prompt = branches.locations['forest']
            # choice_a = ""
            # choice_b = ""


    elif newPlayer.location == "village":
        choice_a = branches.choices[13]['a']
        choice_b = branches.choices[13]['b']
        prompt = branches.locations['village']
        if choice == "a":
            newPlayer.location = "peace"
        elif choice == "b":
            newPlayer.location = "mankind"

            
    elif newPlayer.location == "river":
        choice_a = branches.choices[2]['a']
        choice_b = branches.choices[2]['b']
        prompt = branches.locations['river']
        if choice == "a":
            newPlayer.location = "upstream"
        elif choice == "b":
            newPlayer.location = "downstream"
    
    elif newPlayer.location == "upstream":
        choice_a = branches.choices[3]['a']
        choice_b = branches.choices[3]['b']
        prompt = branches.locations['upstream']
        if choice == "a":
            newPlayer.location = "behindWaterfall"
        elif choice == "b":
            newPlayer.location = "waterfallDeath"
            prompt = branches.locations['waterfallDeath']
            
    elif newPlayer.location == "behindWaterfall":
        choice_a = branches.choices[4]['a']
        choice_b = branches.choices[4]['b']
        prompt = branches.locations['behindWaterfall']
        if choice == "a":
            newPlayer.location = "wfleft"
            prompt = branches.locations['wleft']
        elif choice == "b":
            newPlayer.location = "wfright"
            prompt = branches.locations['wright']
            
    elif newPlayer.location == "downstream":
        choice_a = branches.choices[5]['a']
        choice_b = branches.choices[5]['b']
        prompt = branches.locations['downstream']
        if choice == "a":
            newPlayer.location = "hunger"
        elif choice == "b":
            newPlayer.location = "abandon"
            prompt = branches.locations['abandon']
    
    elif newPlayer.location == "hunger":
        choice_a = branches.choices[6]['a']
        choice_b = branches.choices[6]['b']
        prompt = branches.locations['hunger']
        if choice == "a":
            newPlayer.location = "meat"
        elif choice == "b":
            newPlayer.location = "vegetarian"
    
    elif newPlayer.location == "meat":
        choice_a = branches.choices[7]['a']
        choice_b = branches.choices[7]['b']
        prompt = branches.locations['meat']
        if choice == "a":
            newPlayer.location = "ymeat"
        elif choice == "b":
            newPlayer.location = "nmeat"
    
    elif newPlayer.location == "ymeat":
        choice_a = branches.choices[8]['a']
        choice_b = branches.choices[8]['b']
        prompt = branches.locations['ymeat']
        if choice == "a":
            newPlayer.location = "deer"
            prompt = branches.locations['deer']
        elif choice == "b":
            newPlayer.location = "predator"
    
    elif newPlayer.location == "predator":
        choice_a = branches.choices[9]['a']
        choice_b = branches.choices[9]['b']
        prompt = branches.locations['predator']
        if choice == "a":
            newPlayer.location = "grill"
        elif choice == "b":
            newPlayer.location = "raw"
            prompt = branches.locations['raw']
    
    elif newPlayer.location == "grill":
        choice_a = branches.choices[11]['a']
        choice_b = branches.choices[11]['b']
        prompt = branches.locations['grill']
        if choice == "a":
            newPlayer.location = "path"
        elif choice == "b":
            newPlayer.location = "forest"
            prompt = branches.locations['forest']
    
    elif newPlayer.location == "nmeat":
        choice_a = branches.choices[7]['a']
        choice_b = branches.choices[7]['b']
        prompt = branches.locations['nmeat']
        if choice == "a":
            newPlayer.location = "ymeat"
        elif choice == "b":
            newPlayer.location = "nnmeat"
            prompt = branches.locations['nnmeat']
    
    elif newPlayer.location == "vegetarian":
        choice_a = branches.choices[10]['a']
        choice_b = branches.choices[10]['b']
        prompt = branches.locations['vegetarian']
        if choice == "a":
            newPlayer.location = "berries"
        elif choice == "b":
            newPlayer.location = "leaf"
    
    elif newPlayer.location == "berries":
        choice_a = branches.choices[7]['a']
        choice_b = branches.choices[7]['b']
        prompt = branches.locations['berries']
        if choice == "a":
            newPlayer.location = "berrydeath"
            prompt = branches.locations['berrydeath']
        elif choice == "b":
            newPlayer.location = "leaf"
    
    elif newPlayer.location == "leaf":
        choice_a = branches.choices[11]['a']
        choice_b = branches.choices[11]['b']
        prompt = branches.locations['leaf']
        if choice == "a":
            newPlayer.location = "path"
        elif choice == "b":
            newPlayer.location = "forest"
            prompt = branches.locations['forest']
            
    elif newPlayer.location == "path":
        choice_a = branches.choices[4]['a']
        choice_b = branches.choices[4]['b']
        prompt = branches.locations['path']
        if choice == "a":
            newPlayer.location = "pleft"
        elif choice == "b":
            newPlayer.location = "pright"
    
    elif newPlayer.location == "pright":
        choice_a = branches.choices[24]['a']
        choice_b = branches.choices[24]['b']
        prompt = branches.locations['pright']
        if choice == "a":
            newPlayer.location = "deathawaits"
            prompt = branches.locations['deathawaits']
        elif choice == "b":
            newPlayer.location = "lost"
    
    elif newPlayer.location == "lost":
        choice_a = branches.choices[13]['a']
        choice_b = branches.choices[13]['b']
        prompt = branches.locations['lost']
        if choice == "a":
            newPlayer.location = "peace"
        elif choice == "b":
            newPlayer.location = "mankind"
    
    elif newPlayer.location == "peace":
        choice_a = branches.choices[15]['a']
        choice_b = branches.choices[15]['b']
        prompt = branches.locations['peace']
        if choice == "a":
            newPlayer.location = "stay"
            prompt = branches.locations['stay']
        elif choice == "b":
            newPlayer.location = "leave"
    
    elif newPlayer.location == "leave":
        choice_a = branches.choices[2]['a']
        choice_b = branches.choices[2]['b']
        prompt = branches.locations['leave']
        if choice == "a":
            newPlayer.location = "upstream"
        elif choice == "b":
            newPlayer.location = "drown"
            prompt = branches.locations['drown']
    
    elif newPlayer.location == "mankind":
        choice_a = branches.choices[14]['a']
        choice_b = branches.choices[14]['b']
        prompt = branches.locations['mankind']
        if choice == "a":
            newPlayer.location = "havoc"
        elif choice == "b":
            newPlayer.location = "lightning"
            prompt = branches.locations['lightning']
    
    elif newPlayer.location == "havoc":
        choice_a = branches.choices[16]['a']
        choice_b = branches.choices[16]['b']
        prompt = branches.locations['havoc']
        if choice == "a":
            newPlayer.location = "dog"
            prompt = branches.locations['dog']
        elif choice == "b":
            newPlayer.location = "run"
    
    elif newPlayer.location == "run":
        choice_a = branches.choices[4]['a']
        choice_b = branches.choices[4]['b']
        prompt = branches.locations['run']
        if choice == "a":
            newPlayer.location = "lleft"
        elif choice == "b":
            newPlayer.location = "lright"
    
    elif newPlayer.location == "lleft":
        choice_a = branches.choices[12]['a']
        choice_b = branches.choices[12]['b']
        prompt = branches.locations['lleft']
        if choice == "a":
            newPlayer.location = "ruin"
        elif choice == "b":
            newPlayer.location = "ghost"
            prompt = branches.locations['ghost']
    
    elif newPlayer.location == "pleft":
        choice_a = branches.choices[12]['a']
        choice_b = branches.choices[12]['b']
        prompt = branches.locations['pleft']
        if choice == "a":
            newPlayer.location = "ruin"
        elif choice == "b":
            newPlayer.location = "ghost"
    
    elif newPlayer.location == "ruin":
        choice_a = branches.choices[17]['a']
        choice_b = branches.choices[17]['b']
        prompt = branches.locations['ruin']
        if choice == "a":
            newPlayer.location = "statues"
        elif choice == "b":
            newPlayer.location = "painting"
    
    elif newPlayer.location == "painting":
        choice_a = branches.choices[7]['a']
        choice_b = branches.choices[7]['b']
        prompt = branches.locations['painting']
        if choice == "a":
            newPlayer.location = "ypainting"
        elif choice == "b":
            newPlayer.location = "npainting"
            prompt = branches.locations['npainting']
            
    elif newPlayer.location == "ypainting":
        choice_a = branches.choices[7]['a']
        choice_b = branches.choices[7]['b']
        prompt = branches.locations['ypainting']
        if choice == "a":
            newPlayer.location = "rleft"
        elif choice == "b":
            newPlayer.location = "rright"
            prompt = branches.locations['rright']
    
    elif newPlayer.location == "rleft":
        choice_a = branches.choices[18]['a']
        choice_b = branches.choices[18]['b']
        prompt = branches.locations['rleft']
        if choice == "a":
            newPlayer.location = "dragon"
        elif choice == "b":
            newPlayer.location = "dstatues"
            prompt = branches.locations ['dstatues']
    
    elif newPlayer.location == "dragon":
        choice_a = branches.choices[19]['a']
        choice_b = branches.choices[19]['b']
        prompt = branches.locations['dragon']
        if choice == "a":
            newPlayer.location = "contract"
            prompt = branches.locations['contract']
        elif choice == "b":
            newPlayer.location = "treasure"
    
    elif newPlayer.location == "treasure":
        choice_a = branches.choices[20]['a']
        choice_b = branches.choices[20]['b']
        prompt = branches.locations['treasure']
        if choice == "a":
            newPlayer.location = "excalibur"
            prompt = branches.locations['excalibur']
        elif choice == "b":
            newPlayer.location = "aegis"
            prompt = branches.locations['aegis']
            
    elif newPlayer.location == "statues":
        choice_a = branches.choices[21]['a']
        choice_b = branches.choices[21]['b']
        prompt = branches.locations['statues']
        if choice == "a":
            newPlayer.location = "summon"
        elif choice == "b":
            newPlayer.location = "panic"
            prompt = branches.locations['panic']
    
    elif newPlayer.location == "summon":
        choice_a = branches.choices[22]['a']
        choice_b = branches.choices[22]['b']
        prompt = branches.locations['summon']
        if choice == "a":
            newPlayer.location = "cat"
        elif choice == "b":
            newPlayer.location = "chimera"
            prompt = branches.locations['chimera']
    
    elif newPlayer.location == "cat":
        choice_a = branches.choices[23]['a']
        choice_b = branches.choices[23]['b']
        prompt = branches.locations['cat']
        if choice == "a":
            newPlayer.location = "pride"
            prompt = branches.locations['pride']
        elif choice == "b":
            newPlayer.location = "decline"
            
    elif newPlayer.location == "decline":
        choice_a = branches.choices[7]['a']
        choice_b = branches.choices[7]['b']
        prompt = branches.locations['decline']
        if choice == "a":
            newPlayer.location = "rleft"
        elif choice == "b":
            newPlayer.location = "rright"
            prompt = branches.location['rright']

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
    


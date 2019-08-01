#List of options
choices = [
    {"a": "Follow the path.", "b": "Follow the sound of water."},
    {"a": "Search the village.", "b": "Leave."},
    {"a": "Go upstream.", "b": "Go downstream.", "c": "Cut across the river."},
    {"a": "Search the area around the waterfall.", "b": "Climb the rocks next to the waterfall."},
    {"a": "Go left.", "b": "Go right."},
    {"a": "Dang I'm hungry, I need to eat!", "b": "I'm done with this treasure crap. Lemme out."},
    {"a": "Meat sounds nice.", "b": "I'm a vegetarian."},
    {"a": "Yes.", "b":"No."},
    {"a": "Deer.", "b": "The fiercest predator in this forest!"},
    {"a": "Grill it.", "b":"Eat it raw!"},
    {"a": "Berries.", "b": "lef."},
    {"a": "Path.", "b": "Forest."},
    {"a": "Explore the ruin!", "b": "Bruh, that thing looks haunted. I'm out."},
    {"a": "Get to know the locals.", "b": "Teach them the ways of mankind."},
    {"a": "Cry 'Havoc!,' and let slip the dogs of war!", "b": "Lightning, heed my call!"},
    {"a": "Stay.", "b": "Leave."},
    {"a": "Heck yeah! Come, my fluffy companions!", "b":"Cynophobia... activating..."},
    {"a": "The gallery of creepy statues.", "b": "The strange paintings on the wall."},
    {"a": "Tell the dragon that the statues dishonored its family.", "b": "Tell the statues that the dragon dislikes their helmets."},
    {"a": "Form a contract with the dragon.", "b": "Inquire about the treasure."},
    {"a": "Excalibur!", "b":"Aegis"},
    {"a": "Screw it, I'll summon something! Anything!", "b": "NOOOOOOOOOO!"},
    {"a": "A cat?", "b": "A chimera?"},
    {"a": "Hakuna Matata!", "b": "Decline."},
    {"a": "Death awaits.", "b": "The word lost does not exist in my dictionary!"}
]

#Dictionary of locations 
locations = {
    "beginning": "You're in the forest. Where do you want to go?",
    "village": "You follow the path and arrive at a village.",
    "forest": "How can you eat without feeding the doggos? You encounter a wolf and die.",
    "abandon": "You're just not feeling the treasure today? See you next time.",
    "searchedVil": "You search the village and find the treasure! Good job!", 
    "river": "You follow the sound of water and arrive at a river.",
    "drown": "You slip and fall into the river. The current carries you away and smashes you against rocks. The world grows dark around you.",
    "upstream": "You arrive at a waterfall.",
    "waterfallDeath": "Due to the spray from the waterfall, you slip on the rocks and fall. Ouch.",
    "behindWaterfall": "You find a secret cave behind the waterfall.",
    "wfleft": "Woah! You've found the treasure! Nice, hope you make it home safely.",
    "wfright": "Ever heard of vampire bats? Usually, you'd be okay, but these guys are reaaaally hungry. Goodnight.",
    "downstream": "You go downstream for a long time, but haven't found anything. What will you do?",
    "hunger": "You decide to search for some food. What are you in the mood for?",
    "meat": "You realize that you have to hunt in order to get meat, right?",
    "ymeat": "Okay. What're you hunting?",
    "deer": "Deer would be a safe bet, right? No. You're run over by a stampede.",
    "predator": "You use the force of your hunger to scare a wolf to death. Neat. How're you cooking it?",
    "grill": "You skin the wolf and grill it. Yum. Now that you're full, where to next?",
    "raw": "You eat it raw like a barbarian and get a stomachache. Actually, you're seriously dying here. Best to leave before it's too late.",
    "nmeat": "Are you really going to be okay? Anyway, are you still gonna eat meat?",
    "nnmeat": "Probably for the best. You decide to end for today and leave the forest.",
    "vegetarian": "So, you're a vegetarian. Pick your pois--leaf. Pick your leaf.",
    "berries": "Uh, you sure those aren't poisonous?",
    "berrydeath": "Yeah, they were poisounous. Farewell.",
    "leaf": "You eat the leaves, which were, surprisingly, edible and quite filling. Where to next?",
    "path": "You follow the path and arrive at a fork. Which way?",
    "pleft": "You arrive at an ancient ruin.",
    "mankind": "They don't appreciate the fact that you're trying to undermine their traditions. You're tied to a stake. Any last words before you burn?",
    "peace": "You decide to get to know the locals. Actually, you're liking it here.",
    "stay": "Sometimes, the true treasures are the friends we find along the way. You spend the rest of your days in the village.",
    "leave": "Treasure calls. After a tearful farewell, you leave the village and find a river.",
    "havoc": "The dogs of war have come! AKA wolves! They rout the villagers and come to you with wagging tails.",
    "lightning": "You summon lightning! Well, since you suck at it though, you strike yourself. Ouch.",
    "dog": "You adopt the wolves and take them all home. They give you love in return for the occasional treat. The best ending.",
    "run": "You panic and run away from the village. Great. Now you're lost.",
    "lleft": "You come across some ancient ruins.",
    "lright": "You come across a cave.",
    "ruin": "You aren't scared of ghosts, or so you convince yourself. Which way?",
    "painting": "Uh... did that painting of a dragon just look at you?",
    "ypainting": "A dragon manifests out of the painting! Run!",
    "npainting": "You turn away, but you feel a sharp slash across your back before the world fades to black.",
    "rleft": "You dart left into the gallery of statues. Obligatory moving statues, that is. Now you're stuck between a dragon and statues.",
    "dstatues": "Unfortunately for you, the statues don't like their helmets either. They execute you together with the dragon.",
    "dragon": "The dragon immediately destroys the statues and thanks you for satisfying its grudge.",
    "contract": "Who needs treasure when you can have a fricking dragon? You go on many adventures together and live happily ever after.",
    "treasure": "Following the dragon's instructions. You find a sword in a stone.",
    "excalibur": "Pleased to hear its name, the sword vows its allegiance. Neat.",
    "aegis": "Irate, the sword cuts you down while screaming that it's not an aegis.",
    "statues": "What?! The statues started moving. You run into a chamber that looks like it's made for human sacrifices.",
    "summon": "You scatter your blood around desparately. To your surprise, something actually appears. What is it?",
    "cat": "The cat transforms into Simba. He destroys the statues and invites you back to Pride Rock.",
    "pride": "Screw treasure! You return to Pride Rock with Simba.",
    "decline": "You bid farewell to Simba and go to the hall with paintings. Wait, did that painting just move?",
    "chimera": "The chimera destroys all the statues, and you with them. Sayonara.",
    "pright": "You go right, but after walking for a while, you realize you're lost. What do you do?",
    "deathawaits": "And so it does. Enjoy your slumber.",
    "panic": "Yeah, screaming doesn't do much. The statues sacrifice you.",
    "lost": "Miraculously, you somehow run into a village after declaring your lack of vocabulary. So?",
    "ghost": "Yeah, you're not messing with any ghosts today.",
    "rright": "You run right... right into a corner. The smell of ash and flames haunts you."
}
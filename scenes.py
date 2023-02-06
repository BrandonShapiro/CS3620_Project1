import interaction
import PlayerClass

def startAdventure():
  print('\n\n------------------------------------------------')
  print('               High Seas Survival                   ')
  print('------------------------------------------------\n\n')
  print('You wake up with a pounding headache unable to remember anything...')
  print('...')
  print('The first thing you notice is the smell of seawater and the sound of the ocean.')
  print('You appear to be on some kind of old sail boat. You stand up and look around but can\'t see anything but ocean in every direction.')
  print('...')
  print('"Where am I? What am I doing here? How long have I been here?" you ask yourself.')
  print('You struggle to remember anything at all and eventually decide to focus on your name.')

  name = input('\n"What\'s my name again?" (Enter your name): ')
  player = PlayerClass.Player(name)

  print('"That\'s right, my name is {}\n"'.format(player.getName()))
  print('Just as you start to feel a little better you notice that the ocean seems to have gotten closer since the last time you looked.')
  print('Suddenly you realize that the ship is slowly sinking. You don\'t have much time!')

  options = ['scream for help', 'look around the deck']
  functions = [screamForHelp, mainDeck]
  interaction.get_user_input('What do you do next? ', options, functions, player)


def screamForHelp(player):
  print('\n\n------------------------------------------------')
  print('                Scream for help                  ')
  print('------------------------------------------------\n\n')
  print('You start screaming at the top of your lungs. "HEEEEEELLLLLLPPPP! CAN ANYBODY HELP ME?!"')
  print('After a couple of moments of silence, you realize that you are completely alone. The only answer is the terrifying sound of the ship slowly groaning as it continues to sink.')
  print('You need to act fast if you want to survive...')

  options = ['look around the deck']
  functions = [mainDeck]
  interaction.get_user_input('What do you do next? ', options, functions, player)


def mainDeck(player):
  print('\n\n------------------------------------------------')
  print('                  Main Deck                    ')
  print('------------------------------------------------\n\n')
  if(not player.hasRaftMaterials()):
    print('You look around the deck for anything that could help you. With the ship sinking you need to stay afloat somehow...') 
    print('Perhaps you could build a raft, but with what?')
    print('...')
    print('As you look around you notice a trap door to below deck, perhaps there could be something useful down there? Or maybe I explore the deck more?')

    options = ['explore the forward deck', 'explore the back of the deck', 'explore below deck']
    functions = [exploreDeckForward, exploreDeckBack, belowDeck]
    interaction.get_user_input('Where do you want to look? ', options, functions, player)
  else:
    print('You have all the materials you need to build a raft, but do you have what you need to survive on the ocean?')
    print('Who knows how long you could be stranded...')
    options = ['build the raft and set out', 'keep looking around the ship']
    functions = [buildRaft, continueExploring]
    interaction.get_user_input('The ship has almost sunk, what will you do? ', options, functions, player)

def exploreDeckForward(player):
  print('\n\n------------------------------------------------')
  print('           Explore Main Deck Forward                ')
  print('------------------------------------------------\n\n')
  print('You begin to walk around the forward deck and explore it some more.')
  if(not player.rope):
    print('You notice a small pile of old ropes laying near the main mast. These could be useful...')
    options = ['pick it up', 'go back to main deck']
    functions = [pickUpRope, mainDeck]
  else:
    print('You don\'t find anything new this time')
    options = ['go back']
    functions = [mainDeck]
  
  interaction.get_user_input('What will you do? ', options, functions, player)

def exploreDeckBack(player):
  print('\n\n------------------------------------------------')
  print('           Explore Back of Main Deck                ')
  print('------------------------------------------------\n\n')
  print('You walk to the back of the main deck and look around.')
  if(not player.lantern):
    print('You find a small lantern on a pole. It\'s still lit, but you\'re not sure how much longer it will last.')
    options = ['take it', 'go back to main deck']
    functions = [pickUpLight, mainDeck]
  else:
    print('Looks like there\'s nothing else to find here.')
    options = ['go back']
    functions = [mainDeck]
  
  interaction.get_user_input('What will you do? ', options, functions, player)


def pickUpRope(player):
  print('\n\n------------------------------------------------')
  print('                 Pick up rope                   ')
  print('------------------------------------------------\n\n')
  player.rope = True
  print('** ROPE ADDED TO INVENTORY **\n')
  print('Hopefully these will come in handy later...')
  print('You go back to explore the deck some more.')
  mainDeck(player)

def pickUpLight(player):
  print('\n\n------------------------------------------------')
  print('                 Pick up light                   ')
  print('------------------------------------------------\n\n')
  player.lantern = True
  print('** LIGHT ADDED TO INVENTORY **\n')
  print('This could be helpful to explore dark areas...')
  print('You go back to explore the deck some more.')
  mainDeck(player)

def belowDeck(player):
  print('\n\n------------------------------------------------')
  print('                 Below Deck                   ')
  print('------------------------------------------------\n\n')
  print('You open the trap door and descend the stairs. The water is up to your ankles already, you don\'t have much time left...')
  print('The sound of splashing echoes around you as you step into the cold water. Maybe this was a mistake...')

  options=['go back to main deck', 'look around']
  functions=[mainDeck, lookAroundBelowDeck]
  interaction.get_user_input('What will you do? ', options, functions, player)

def lookAroundBelowDeck(player):
  print('\n\n------------------------------------------------')
  print('               Explore Below Deck                   ')
  print('------------------------------------------------\n\n')
  if(not player.lantern):
    print('It\'s too dark to see anything. You need to go back and find a light that you could use.')
    print('You ascend back up to the main deck')
    mainDeck(player)
  else:
    print('It\'s dark down here. Good thing you found that lantern earlier. You hold it out in front of you and look around.')
    print('You find yourself in a narrow hallway. In the dim light you can see a couple of doorways around you.')
    
    options = ['go back to main deck', 'go left', 'go right', 'continue down the hallway',]
    functions = [mainDeck, crewQuarters, kitchen, hallway]
    interaction.get_user_input('What do you want to do? ', options, functions, player)

def crewQuarters(player):
  print('\n\n------------------------------------------------')
  print('                  Crew Quarters                     ')
  print('------------------------------------------------\n\n')
  print('This room looks like it was used as the crew\'s living quarters. Where did everyone go? Maybe someone left something behind that you could use?')
  options = ['go back to hallway', 'snoop around']
  functions = [lookAroundBelowDeck, exploreCrewQuarters]
  interaction.get_user_input('What do you want to do? ', options, functions, player)


def exploreCrewQuarters(player):
  print('\n\n------------------------------------------------')
  print('              Explore Crew Quarters                 ')
  print('------------------------------------------------\n\n')
  if(not player.bottle):
    print('It looks like someone ransacked this place.... There\'s nothing left but an old wine bottle.')
    options = ['take it', 'go back to hallway']
    functions = [pickUpBottle, lookAroundBelowDeck]
  else:
    print('You search again but don\'t find anything new.')
    options = ['go back']
    functions = [lookAroundBelowDeck]
  interaction.get_user_input('What will you do? ', options, functions, player)

   
def pickUpBottle(player):
  print('\n\n------------------------------------------------')
  print('              Pick up wine bottle                 ')
  print('------------------------------------------------\n\n')
  player.bottle = True
  print('** BROKEN BOTTLE ADDED TO INVENTORY **\n')
  print('Not sure how I could use this yet...')
  print('You return to the hallway confused.')
  lookAroundBelowDeck(player)


def kitchen(player):
  print('\n\n------------------------------------------------')
  print('                     Kitchen                        ')
  print('------------------------------------------------\n\n')
  print('This must be the kitchen. There\'s not much left in here...')
  options = ['go back to hallway', 'look around']
  functions = [lookAroundBelowDeck, exploreKitchen]
  interaction.get_user_input('What do you want to do? ', options, functions, player)

def exploreKitchen(player):
  print('\n\n------------------------------------------------')
  print('                 Explore Kitchen                    ')
  print('------------------------------------------------\n\n')
  print('You begin to rummage around the kitchen in the dim light of your lantern.')
  if(not player.knife):
    print('You notice something shining on the counter.')
  print('To your left there is a shelf with a small box on it.')
  options = ['take a closer look at the counter', 'check out the shelf', 'get out of here']
  functions = [kitchenCounter, kitchenShelf, lookAroundBelowDeck]
  interaction.get_user_input('What will you do? ', options, functions, player)

def kitchenCounter(player):
  print('\n\n------------------------------------------------')
  print('                  Kitchen Counter                   ')
  print('------------------------------------------------\n\n')
  if(not player.knife):
    print('You move a little closer and see that your light is reflecting off of a knife on the counter.')
    options = ['take it', 'I don\'t need it']
    functions = [pickUpKnife, exploreKitchen]
  else:
    print('It\'s just an empty counter. You can\'t find anything useful.')
    options = ['go back']
    functions = [exploreKitchen]
  interaction.get_user_input('What do you want to do? ', options, functions, player)

def pickUpKnife(player):
  print('\n\n------------------------------------------------')
  print('                 Pick up knife                   ')
  print('------------------------------------------------\n\n')
  player.knife = True
  print('** KNIFE ADDED TO INVENTORY **\n')
  print('This could be a valuable tool...')
  print('You continue to explore the kitchen...')
  exploreKitchen(player)

def kitchenShelf(player):
  print('\n\n------------------------------------------------')
  print('                  Kitchen Shelf                     ')
  print('------------------------------------------------\n\n')
  if(not player.rations):
    print('You approach the shelf and open the box. Looks like some food rations. It doesn\'t look very appetizing...')
    options = ['take it anyways', 'leave it']
    functions = [pickUpRations, exploreKitchen]
  else:
    print('It\'s just an empty counter. You can\'t find anything else useful.')
    options = ['go back']
    functions = [exploreKitchen]
  interaction.get_user_input('What do you want to do? ', options, functions, player)

def pickUpRations(player):
  print('\n\n------------------------------------------------')
  print('                 Pick up rations                   ')
  print('------------------------------------------------\n\n')
  player.rations = True
  print('** FOOD RATIONS ADDED TO INVENTORY **\n')
  print('"I hope I don\'t have to eat this, but it\'s better than nothing I guess.."')
  print('You continue to explore the kitchen...')
  exploreKitchen(player)


def hallway(player):
  print('\n\n------------------------------------------------')
  print('                Below Deck Hallway                  ')
  print('------------------------------------------------\n\n')
  if(not player.door):
    print('You continue down the hallway and come to a door that is partially off the hinges. Looks like someone broke this door down to get in.')
    options = ['go back to the stairs', 'examine the door', 'enter the room']
    functions = [lookAroundBelowDeck, examineDoor, storageHull]
  else:
    print('You enter the hallway and look around.')
    options = ['explore below deck some more', 'enter the room']
    functions = [lookAroundBelowDeck, storageHull]
  interaction.get_user_input('What do you want to do?', options, functions, player)

def examineDoor(player):
  print('\n\n------------------------------------------------')
  print('                   Hallway Door                     ')
  print('------------------------------------------------\n\n')
  print('"This door is almost off it\'s hinges. If I had a tool, maybe I could remove it...I wonder if it floats?"')
  if(player.knife):
    options = ['use knife to remove the door', 'return to hallway']
    functions = [pickUpDoor, hallway]
  else:
    options = ['keep looking around']
    functions = [hallway]
  interaction.get_user_input('What will you do? ', options, functions, player)

def pickUpDoor(player):
  print('\n\n------------------------------------------------')
  print('                    Take door                       ')
  print('------------------------------------------------\n\n')
  player.door = True
  print('** DOOR ADDED TO INVENTORY **\n')
  print('"Let\'s hope this thing floats... It looks sturdy enough to hold me."')
  print('You continue to explore the hallway')
  hallway(player)

def storageHull(player):
  print('\n\n------------------------------------------------')
  print('                   Storage Hull                     ')
  print('------------------------------------------------\n\n')
  print('You enter the room and see barrels and some wooden planks floating around. This must have been the storage hull. "I wonder what was so valuable in here?"')
  print('I wonder if I could salvage anything in here to help build a raft?')
  options = ['return to hallway', 'take the barrels', 'take the wooden planks', 'explore the room more']
  functions = [hallway, pickUpBarrels, pickUpPlanks, exploreStorageHull]
  interaction.get_user_input('What\'s your next move? ', options, functions, player)

def pickUpBarrels(player):
  print('\n\n------------------------------------------------')
  print('                  Pick up barrel                    ')
  print('------------------------------------------------\n\n')
  print('You try to pick up one of the barrels, but it\'s far too heavy to lift... This probably won\'t work...')
  print('You look around for other options.')
  storageHull(player)

def pickUpPlanks(player):
  print('\n\n------------------------------------------------')
  print('                  Pick up planks                    ')
  print('------------------------------------------------\n\n')
  player.planks = True
  print('** PLANKS ADDED TO INVENTORY **\n')
  print('"These definitely float, but how can I use these?"')
  print('You continue to look around the storage hull')
  storageHull(player)

def exploreStorageHull(player):
  print('\n\n------------------------------------------------')
  print('               Explore Storage Hull                 ')
  print('------------------------------------------------\n\n')
  if(not player.medallion):
    print('The water is definitely deeper down here and rising quickly. A faint shine below the surface catches your eye.')
    options = ['I don\'t have time, head back to the hallway', 'investigate']
    functions = [hallway, pickUpMedallion]
  else:
    print('You can\'t find anything else useful. Better not spend too much time down here.')
    options = ['Go back to the hallway']
    functions = [hallway]
  interaction.get_user_input('Time is short, what will you do? ', options, functions, player)

def pickUpMedallion(player):
  print('\n\n------------------------------------------------')
  print('                 Pick up medallion                  ')
  print('------------------------------------------------\n\n')
  player.medallion = True
  print('** MEDALLION ADDED TO INVENTORY **\n')
  print('"This must be what they were after, I guess they dropped this one. Maybe it will help me later..."')
  print('You continue to look around the storage hull')
  storageHull(player)
  
def continueExploring(player):
  print('\n\n------------------------------------------------')
  print('                    Main Deck                       ')
  print('------------------------------------------------\n\n')
  print('Time is running dangerously short, maybe I should just leave?')
  options = ['build the raft and leave', 'explore the forward deck', 'explore the back of the deck', 'explore below deck']
  functions = [buildRaft, exploreDeckForward, exploreDeckBack, belowDeck]
  interaction.get_user_input('Where do you want to look? ', options, functions, player)

def buildRaft(player):
  print('\n\n------------------------------------------------')
  print('                   Build Raft                       ')
  print('------------------------------------------------\n\n')
  print('You quickly build a makeshift raft out of the materials you\'ve managed to scrounge together. You use the knife to cut the rope into pieces and tie the door and planks together.')
  print('You leave one plank untied to use as a sort of row and rudder.')
  print('It doesn\'t look very sturdy, but hopefully it will stay afloat...')
  if(player.bottle):
    print('You carefully place the bottle you found on the raft, this might be the only way to collect rainwater. Can\'t lose it!')
  if(player.rations):
    print('Still unsure if you have the stomach to eat it, you carefully stash the rations aboard your makeshift raft.')
  print('')
  setAfloat(player)

def setAfloat(player):
  print('\n\n------------------------------------------------')
  print('                 The High Seas                      ')
  print('------------------------------------------------\n\n')
  print('After setting afloat you found yourself floating for what seemed like an eternity.')
  print('Days passed and nothing seemed to change.')
  print('You begin to realize you would need some sort of food and water to survive this journey.')
  if(not player.bottle):
    print('Unfortunately, in your haste to create a raft, you neglected to find something to collect rain water and perished on the ocean.')
    result(player)
  if(not player.rations):
    print('In your panic, you forgot to find food aboard the sinking ship and now you begin to suffer and lose energy.')
    print('After a few days a ship passes by, but you don\'t have the energy to shout or motion for help.')
    print('You end up dying on the ocean within yelling distance of another ship and are eventaully found by some fishermen. You were so close')
    result(player)
  else:
    print('Luckily for you, you found a bottle to collect rainwater and some food rations to help you keep you alive.')
    print('Although malnourished and on the verge of giving up, eventually you hear a ship approaching through fog...')
    pirateEncounter(player)

def pirateEncounter(player):
  print('\n\n------------------------------------------------')
  print('                Approaching Ship                    ')
  print('------------------------------------------------\n\n')
  print('You can\'t see the approaching ship yet, but you can definitely hear voices getting louder and moving in your direction.')
  options = ['yell for help', 'wait just a little bit...']
  functions = [pirateCapture, avoidPirates]
  interaction.get_user_input('Desperate to get out of the ocean, what will you do? ', options, functions, player)

def pirateCapture(player):
  print('\n\n------------------------------------------------')
  print('               Captured by Pirates                  ')
  print('------------------------------------------------\n\n')
  print('"Help! Help!" you yell as loud as you can.\nAs the ship comes into view you realize that it is a pirate ship, perhaps the very one that attacked your ship in the first place.')
  print('The pirates drag you aboard and search you...')
  if(not player.medallion):
    print('Finding nothing of value, they decide to enslave you.')
    print('Eventually you die from a combination of being overworked and contracting scurvy.')
    result(player)
  else:
    print('You offer them the medallion in exchange for safe passage to the nearest port.')
    print('They accept your offer and you survive, but barely.')
    player.survived = True
    result(player)

def avoidPirates(player):
  print('\n\n------------------------------------------------')
  print('          Close encounter with Pirates              ')
  print('------------------------------------------------\n\n')
  print('Just as you are about to yell for help, the ship comes into view and you realize to your dismay that it is pirates!')
  print('Good thing you didn\'t yell for help! You slip by unnoticed in the fog...\n')
  print('"If there are pirates around, surely there must be others nearby" you think to yourself.')
  print('After a few more hours the fog clears and without cover you hope that the next ship to come by will be friendly')
  print('Just as you begin to lose hope, another ship approaches...')
  rescued(player)

def rescued(player):
  print('\n\n------------------------------------------------')
  print('                     Rescued!                       ')
  print('------------------------------------------------\n\n')
  print('This time, it is some friendly fishermen. They take you aboard and generously give you food and water.')
  print('They nourish you back to health and drop you off at the nearest port')
  if(player.medallion):
    print('You manage to sell the gold medallion you found for a small fortune and never have to sail on the ocean again for the rest of your life!')
  player.survived = True
  result(player)

def result(player):
  if(player.survived):
    print('\n\n------------------------------------------------')
    print('                   YOU SURVIVED                     ')
    print('------------------------------------------------\n\n')
  else:
    print('\n\n------------------------------------------------')
    print('                     YOU DIED                       ')
    print('------------------------------------------------\n\n')
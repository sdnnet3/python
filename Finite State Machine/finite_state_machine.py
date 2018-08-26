from random import randint
from time import clock

##=========================================
            ##Base State classes##
##=========================================

State = type("State",(object,),{})
#create state base class
#other classes will inherit


#inherit from state base class
class LightOn(State):
    def Execute(self):
        print ("Light is on!")

#inherit from state base class
class LightOff(State):
    def Execute(self):
        print ("Light is off!")

##=========================================
            ## Transision Class##
##=========================================

class transition(object):

#when constructed, we pass in a toState (what it's transitioning too)
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print ("transitioning...")
        

##=========================================
            ## Finite State Machine
##=========================================

class simpleFSM(object):

#char passed in when the object is created
    def __init__(self,char):
        self.char = char

#create dict, store all of our states here
        self.states = {}
#create dict, for all transitions
        self.transitions = {}
#store our current state
        self.curState = None
#current transition
        self.trans = None

#fucntion that will look for string passed in within states dict line 48
# paired with state name to instance of the state. how we set current state
# to the passed in state.
    def setState(self, stateName):
        self.curState = self.states[stateName]

#same as above, sets transitions state
    def transition (self, transName):
        self.trans = self.transitions[transName]
        self.Execute()

#if there is a transition stored within self.trans, we will execute transition
# and set current state to whatever that is, then reset current state to None

    def Execute(self):
        if (self.trans):
            self.setState(self.trans.toState)
            self.trans = None
        self.curState.Execute()

##=========================================
            ## Create a character object
##=========================================
# all attributes would go here, stuff for your character, helmets etc.

#create char object class
class Char(object):
    def __init__(self):
        #create an instance of the FSM within the character class
        #when character class is initialized
        self.FSM = simpleFSM(self)
        #start with the light on
        self.LightOn = True


##=========================================
            ##Create and Run
##=========================================

#Create and instance of the character
if __name__ == "__main__":
    light = Char()

    #create instance of the light on state, created above
    #then store it in the states dictionary inside the FSM
    light.FSM.states["On"] = LightOn()

    #same as above, dict now has on/off key/value pairs
    light.FSM.states["Off"] = LightOff()

    #create instance that is stored in the transitions dictionary within the FSM
    #dictionary now has turningOff/turningOn k/v pairs
    light.FSM.transitions["toOn"] = transition("On")
    light.FSM.transitions["toOff"] = transition("Off")

## when transition("On") string is passed into light.FSM.states[], "On" goes
## into light.FSM.states["On"] which = output fuction execution of LightOn()

#set the initial state of the FSM
    light.FSM.setState("On")

    for i in range(20):
        startTime = clock()
        timeInterval = 1

        #while we haven't passed 1 second, we loop
        while (startTime + timeInterval > clock()):
            pass

        #0 or 1 picked. 0 skips below, and wont transition
        if (randint(0,2)):
            #if rand int = 1, we transition from current state to opposite
            #state. if LightOn = True, set transition toOff, set LightOn = False
            if (light.LightOn):
                light.FSM.transition("toOff")
                light.LightOn = False
            else:
                #if light is already off, turn it on
                light.FSM.transition("toOn")
                light.LightOn = True
        light.FSM.Execute()


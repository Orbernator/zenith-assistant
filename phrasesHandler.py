import zenithConfig
import random as rnd

def greetings():
    greetrnd = rnd.randint(1, 6):
    if greetrnd == 1:
        return('Hello, ' + zenithConfig.userName + ', how are you?')
    elif greetrnd == 2:
        return('Hiya, ' + zenithConfig.userName + ', whats going on?')
    elif greetrnd == 3:
        return('Hey there, ' + zenithConfig.userName + ', what can I help you with?')
    elif greetrnd == 4:
        rudeGreet = rnd.randint(1, 50)
        rudeGreet2 = rnd.randint(1, 50)
        if rudeGreet == rudeGreet2:
            return('What do you want, you little sh*t?')
        else:
            return('Wasup' + zenithConfig.userName + '? How can I help you?')
    elif greetrnd == 5:
        return('Hi there,' + zenithConfig.userName + 'what can I help you with?')
    elif greetrnd == 6:
        return('Aloha! How may I assist you today!')
    else:
        return('A Fatal Error Occurred. Error Code 0001')

def goodbyes():
    byernd = rnd.randint(1,6)
    if byernd == 1:
        return('See you later!')
    elif byernd == 2:
        return('Bye, have a good day!')
    elif byernd == 3:
        return('Goodbye, ' + zenithConfig.userName + '. Have a nice rest of your day.')
    elif byernd == 4:
        return('Going so soon? Bye then!')
    elif byernd == 5:
        return('Adios Amigo!')
    
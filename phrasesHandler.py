import zenithConfig
import random as rnd

def greetings():
    greetrnd = rnd.randint(1, 2)
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

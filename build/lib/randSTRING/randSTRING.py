from math import ceil

import string
import random

class randSTRgen:
    '''
    This is a generator class which creates a random variable string with preset variables.
    
    '''
    
    optionDict = {'lower letters':string.ascii_lowercase,
                  'upper letters':string.ascii_uppercase,
                'numbers':string.digits,
                'punctuation':string.punctuation}
    optionLS = [chars for keys, chars in optionDict.items()]
    
    defaultLength = 10    
    defaultOption = 1
    
    def __init__(self,option = defaultOption):
        if option >3:
            self.option = 3
        elif option <0:
            self.option = 0
        else:
            self.option = option
    
    def strGen(self,length = defaultLength):
        #indexLS = [i for i in range(length)]
        noLS = []
        
        for i in range(self.option + 1):
            noLS.append(random.random())
        
        charLS =[]
        i = 0
        
        for no in noLS:
            if no != noLS[-1]:
                count = int(no/sum(noLS)*(length-3))
            else:
                count = int(length - sum(noLS[:-2]))
            for c in range(count):
                charLS.append(random.choice(self.optionLS[i]))
            i +=1

        result = ''
        for i in range(length):
            character = random.choice(charLS)
            result += character
            charLS.remove(character)
            
        return result
    
    def changeOption(self,option = defaultOption):
        self.option = option
    
    def __eq__(self,other):
        return (self.option == other.option) and (type(self) == type(other))
    
if __name__ = '__main__':
    testGEN = randSTRgen()
    print('Random String:',testGEN.strGen())
class Calculator(object):
  
  def read(self):
    """Read input from stdin"""
    return input()
        
  def eval(self, string):
    
    splitted=string.split(" ")
    vocab=["/", "*", "-", "+"]
    
    """Checking for minuses and division by zero"""
    for check in splitted:
      if check not in vocab and check.startswith("-"):
        splitted[splitted.index(check)]=int(check)
      elif (check=="/" and int(splitted[splitted.index(check)+1])==0):
        return("Division by zero")
    
    """Checking for wrong input"""
    for check in splitted:
      if (check not in vocab and isinstance(check, str) and check.isdigit()==False):
        return("Wrong operator")
    
    """Checking from passages starting from "-" """  
    if (splitted[0]=="-"):
      splitted.pop(0)
      first = 0 - int(splitted.pop(0))
      splitted.insert(0, first)
    
    """Checking for operations under negatives"""
    for minus in splitted:
      if minus=="-" and splitted[splitted.index(minus)-1] in vocab:
        splitted[splitted.index(minus)+1]=0-splitted[splitted.index(minus)+1]
        splitted.pop(splitted.index(minus))
      
    i=0
    while(len(splitted)>1):
      if (splitted[i]=="*"):
        result=float(splitted[i-1])*float(splitted[i+1])
        splitted.pop(i+1)
        splitted.pop(i)
        splitted.pop(i-1)
        splitted.insert(i-1, result)
        i=0
      elif (splitted[i]=="/"):
        result=float(splitted[i-1])/float(splitted[i+1])
        splitted.pop(i+1)
        splitted.pop(i)
        splitted.pop(i-1)
        splitted.insert(i-1, result)
        i=0
      elif ("*" not in splitted and "/" not in splitted and splitted[i]=="+"):
        result=float(splitted[i-1])+float(splitted[i+1])
        splitted.pop(i+1)
        splitted.pop(i)
        splitted.pop(i-1)
        splitted.insert(i-1, result)
        i=0
      elif ("*" not in splitted and "/" not in splitted and splitted[i]=="-"):
        result=float(splitted[i-1])-float(splitted[i+1])
        splitted.pop(i+1)
        splitted.pop(i)
        splitted.pop(i-1)
        splitted.insert(i-1, result)
        i=0
      elif (i<len(splitted)):
        i+=1
      else:
        i=0
      
    if ( (float(splitted[0]) - int(splitted[0])) == 0):
      splitted[0]=int(splitted[0])
          
    return splitted[0]

  def loop(self):
    line = self.read()
    while line != "quit":
      value = self.eval(line)
      print(value)
      # Read next line of input
      line = self.read()    
            
if __name__ == '__main__':
  calc = Calculator()
  calc.loop()

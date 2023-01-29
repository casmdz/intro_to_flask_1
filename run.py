from app import app 
#defining the variable from another file 
#when you just import something, it runs ALL the code from the file

if __name__ == "__main__":  #the if statement lets people know that this is our starting point
    app.run() #anything under the if statement is being run
    
    #open  if __name__ == "__main__" 
    #as a way to store code that should only run when your file is executed as a script
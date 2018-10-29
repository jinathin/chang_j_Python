# print a message to the terminal window
print("Rules that govern the state of water")

# set up a variable to hold the temperature we input
current_tempt = False 

while current_tempt is False:
	# make this a number and clean the code up (DRY it out)
    current_tempt = input("Enter a temperature:\n")
    # see what current temp is
    print("you input:", current_tempt)

    # if the current temp is at freezing or below, water is solid
    if (int(current_tempt) < 0 or (int(current_tempt) == 0)):
       print("water is a solid! cuz it's at or below freezing")
       current_tempt = False
     # else check another condition. if it's not freezing, is below boiling?	
	elif (int(current_tempt) < 100):
		print("water is a liquid, because it's above freezing and below boiling")
	      current_tempt = False

	elif (int(current_tempt) > 100 or (int(current_tempt)	== 100)):
	 	 print("water is a gas. Cuz it's, like, really hot")
	 	  current_tempt = False

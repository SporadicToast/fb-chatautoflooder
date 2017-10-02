import time
import os
ver = "Beta 0.1"
repeat = True

os.system("cls")
os.system("title Facebook Chatflooder {}".format(ver))
print("======== Info ========")
print("Programmed by Marc Macaraeg - Python 3 - Sikuli 1.1.0")
print("Alias - SporadicToast")
print("")
print("You require Java IDE 7 (or above), Python 3 and Sikuli to run")
print("Current program version :{}".format(ver))
print("")
print("Program Logs:")
print("")
popup("Now, open the Facebook chat page before closing.\nMake sure that if you are using mini chat, only one is open.", "Facebook Chatflooder {}".format(ver))
if exists("messengerinit.png"):
	popup("New Messenger Box Detected!")
	print("[Notify] Chatstyle - New Messenger Box Format Detected")	
	while repeat == True:
		cycle = 0
		print("[Notify] Cycle set to {}".format(cycle))
		totype = str(input("Enter what to type repeatably:"))
		print("[Notify] Chat repetition set to the following : {}".format(totype))
		times = int(input("How many times are we to input this?:"))
		print("[Notify] Chat repetition set to {}".format(times))
		chatbox = "messengerboxb.png"
		if not exists(chatbox):
			popup("The chatbox {} does not exist on screen!".format(chatbox))
			chatbox = "messengerboxb.png"
		while cycle < times:
			type(chatbox, totype + Key.ENTER)
			cycle += 1
			print("[Operation] Current cycle: {}".format(cycle))
			
elif exists("fbchatinit2.png"):
	print("[Notify] Chatstyle - Large Chatbox Detected")
	while repeat == True:
		cycle = 0
		print("[Notify] Cycle set to {}".format(cycle))
		totype = str(input("Enter what to type repeatably:"))
		print("[Notify] Chat repetition set to the following : {}".format(totype))
		times = int(input("How many times are we to input this?:"))
		print("[Notify] Chat repetition set to {}".format(times))
		chatbox = "textbox.png"
		while cycle < times:
			type(chatbox, totype + Key.ENTER)
			cycle += 1
			print("[Operation] Current cycle: {}".format(cycle))
			
elif exists("fbminichatinit.png"):
	popup("Detected Smallscale Chat")
	print("[Notify] Chatstyle - Smallscale Chatbox Detected")	
	while repeat == True:
		cycle = 0
		print("[Notify] Cycle set to {}".format(cycle))
		totype = str(input("Enter what to type repeatably:"))
		print("[Notify] Chat repetition set to the following : {}".format(totype))
		times = int(input("How many times are we to input this?:"))
		print("[Notify] Chat repetition set to {}".format(times))
		chatbox = "minichatbox.png"
		hover("minichatbox.png")
		while cycle < times:
			type(chatbox, totype + Key.ENTER)
			cycle += 1
			print("[Operation] Current cycle: {}".format(cycle))
			

else:
	print("[Error] Exception Handle 01! - No chat detected.")
	popup("No such chat exists - please check if the browser is in top screen. Closing application.")
	
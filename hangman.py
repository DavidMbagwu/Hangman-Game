#David Mbagwu CSI 180-A Program2. 14th November 2023.
#This program aims to simulate a 'Hangman Game' utilizing user input

#Introduction to the program
import random 
from graphics import *  #This imports the graphics library necessary for animation



def main():
	pass
	print("Program 2")

	print("")

	print("This program simulates the 'Hangman Game'")
	print("The Aim is to test your vocabulary and your critical thinking skills")
	print("")

	print("Make sure to get a pen and paper!")
	print("")

	print("Play the H A N G M A N Game")
	print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

	
	while True: 

		#open a file for reading
		inputfile = open("Hangman.txt", "r")

		#reads a random line of the file
		lines = inputfile.readline().splitlines()
		random_word = random.choice(list(open('Hangman.txt')))

		#Turn the word into a list
		random_word_list = list(random_word)
		random_word_list.pop(-1)
		num_of_words = len(random_word_list)
		num_of_tries = num_of_words + 7
		print(random_word)
		#print(random_word_list)
		#print("You have ", num_of_tries, "tries Left.")

		#Create Platform for guessing
		new_list = []

		for x in range(num_of_words):
			new_list.append("_")

		#print(new_list)


		#Create a graphics window with game introduction at the top of the screen
		win = GraphWin("Hangman Game", 900, 720) 
		win.setBackground("grey")

		#Introductory text
		message = Text(Point(450, 56), "Play the HANGMAN Game")
		message.setSize(20)
		message.setFace("courier")
		message.setStyle("bold")
		message.setTextColor('black')
		message.draw(win)

		#Draw button to the window
		button = Text(Point(600, 300), "Continue")
		button.draw(win)
		button = Text(Point(400, 300), "Click to start")
		button.draw(win)
		Rectangle(Point(700, 350), Point(500, 250)).draw(win)

		def display(n):
			sumOf = 0
			trials = 0
			used_word = []
			num_of_tries = 7
			# #create textbox object from the Entry class & draw to the window
			# inputText = Entry(Point(700,400),5)
			# #inputText.setText("")
			# inputText.draw(win)
			# #return inputText
			#Wait for a mouse click
			win.getMouse()
			
			def aline1(pt1,pt2,pt3,pt4):
				aLine = Line(Point(pt1,pt2), Point(pt3,pt4))
				aLine.draw(win)
				aLine.setWidth(8)
				aLine.setFill("black")

			def circ1(pt11,pt12,pt13):
				cir1 = Circle(Point(pt11, pt12), pt13)  #The values 100 and 120 are the center of the circle while 70 is the radius
				# cir1.setFill("yellow") # You can get color RGB codes from the Paint app
				cir1.draw(win)

			for i in range(n):
				
				# #create textbox object from the Entry class & draw to the window
				# inputText = Entry(Point(700,400),5)
				# #inputText.setText("")
				# inputText.draw(win)
				# #return inputText
				# #Wait for a mouse click
				# win.getMouse()
				# word = str(inputText.getText())    #input("Enter a letter: ")
				# #print("")

				print("You have ", num_of_tries, "tries Left.")
				print("Word: "," ".join(str(e) for e in new_list), "Guesses:", sumOf, "Wrong:",trials, "Tried:", used_word)
				
				if num_of_tries > 0 and new_list == random_word_list:
					print("Congratulations!! You got it in ", sumOf, "guesses.")
					end_scene = Text(Point(450, 100), "Congratulations!! You got it")
					end_scene1 = Text(Point(450, 200), "The word was :"+ random_word)
					end_scene.setSize(20)
					end_scene.setFace("courier")
					end_scene.setStyle("bold")
					end_scene.setTextColor('black')
					end_scene1.setSize(20)
					end_scene1.setFace("courier")
					end_scene1.setStyle("bold")
					end_scene1.setTextColor('black')
					end_scene.draw(win)
					end_scene1.draw(win)	
					break

				word = input("Enter a letter: ")
				word = word.lower()
				print("")

				if word in random_word_list:
					for i, s in enumerate(random_word_list):
						if s == word:
							new_list[i] = word

				elif trials == 6:
					aline1(180,420,220,460)
					print("Sorry you lost.")
					print("The word was:", random_word)
					end_scene = Text(Point(450, 100), "Game Over!")
					end_scene1 = Text(Point(450, 200), "The word was :"+ random_word)
					end_scene.setSize(20)
					end_scene.setFace("courier")
					end_scene.setStyle("bold")
					end_scene.setTextColor('black')
					end_scene1.setSize(20)
					end_scene1.setFace("courier")
					end_scene1.setStyle("bold")
					end_scene1.setTextColor('black')
					end_scene.draw(win)
					end_scene1.draw(win)		
					break

				elif trials == 0 and word != "":
					circ1(180,300,40)
					#textbox(500,600,5)
					trials += 1
					num_of_tries -= 1

				elif trials == 1 and trials > 0 and word != "":
					aline1(180,340,180,380)
					#textbox(500,600,5)
					trials += 1
					num_of_tries -= 1

				elif trials == 2 and trials > 1 and word != "":
					aline1(140,340,180,380)
					#textbox(500,600,5)
					trials += 1
					num_of_tries -= 1

				elif trials == 3 and trials > 2 and word != "":
					aline1(220,340,180,380)
					#textbox(500,600,5)
					trials += 1
					num_of_tries -= 1

				elif trials == 4 and trials > 3 and word != "":
					aline1(180,380,180,420)
					#textbox(500,600,5)
					trials += 1
					num_of_tries -= 1

				elif trials == 5 and trials > 4 and word != "":
					aline1(180,420,140,460)
					#textbox(500,600,5)
					trials += 1
					num_of_tries -= 1

				else:
					pass
					# circ1(800,300,70)
					# #textbox(500,600,5)
					# trials += 1
					# num_of_tries -= 1

				# sumOf += 1
				if word not in used_word and word != "":
					sumOf += 1
					used_word.append(word)
				#textbox(500,600,5)
	

		#Set the initial object of the window
		def aline(pt1,pt2,pt3,pt4):
			aLine = Line(Point(pt1,pt2), Point(pt3,pt4))
			aLine.draw(win)
			aLine.setWidth(8)
			aLine.setFill("black")


		#draw a circle
		def circ(pt1,pt2,pt3):
			cir1 = Circle(Point(pt1, pt2), pt3)  #The values 100 and 120 are the center of the circle while 70 is the radius
			cir1.setFill("yellow") # You can get color RGB codes from the Paint app
			cir1.draw(win)

		#draw a rectangle
		def rec(pt1,pt2,pt3,pt4):
			rect = Rectangle(Point(pt1,pt2), Point(pt3,pt4))  
			rect.setFill(color_rgb(98, 49, 0))  #Fills the shape with the solid color 
			rect.setOutline("black") #Fills the outline of the shape 
			rect.setWidth(5) #You can set the width of the shapes outline 
			rect.draw(win)

		
		#Function for the random word


		
		aline(80,160,180,160)
		aline(180,160,180,260)
		circ(800,120,70)
		rec(20,158,80,620)
		rec(10,600,620,620)
		display(num_of_tries)
		#textbox(500,600,5)
		win.getMouse()
		win.close()

		check = input("Do you want to quit or start again? enter Y to restart or N to end: ")
		if check.upper() == "Y": #go back to the top
			continue
    
		else:
			break

	print("")

	#End of the program
	print("Terminating Program")

	print("")

	print("End")




main()
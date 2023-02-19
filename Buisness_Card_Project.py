# Website referenced  for how to use python: https://realpython.com/beginners-guide-python-turtle/#customizing-in-one-line
#Website referenced for Colors: https://www.webucator.com/article/python-color-constants-module/
#Website refrenced for colored text: https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
#Website refrenced for ANSII colors: https://www.geeksforgeeks.org/print-colors-python-terminal/ 

# P.G.R
# Game and Simulation Programing
#2/18-20/23
# Proffesor Gooch

import turtle

u = input(" Enter the password to access the buissnes card : ")
if u == "Skadooch":

#______FRONT CARD____________FRONT CARD____________FRONT CARD_______#
    
    #making turtle in t for more simple syntax
    t = turtle.Turtle()

    #hide the turtle
    t.ht()

    #speeding up the speed of the pen
    t.speed(5)

    #_______________Creating the actual Card___________________#

    #Setting the pen size and the colorfill of the card on the edges
    t.pensize(2)
    t.fillcolor("gray7")

    #Making the rectangle for the card and begining and ending fill 
    t.begin_fill()
    t.fd(500)
    t.rt(90)

    t.fd(250)
    t.rt(90)

    t.fd(500)
    t.rt(90)

    t.fd(250)
    t.end_fill()

    #filling picking the color for the body of the card
    t.fillcolor("gray9")# original color gray10

    #making the top left traingle
    t.pu()
    t.bk(25)
    t.rt(45)
    t.fd(5)

    # begining to fill the inside of the card
    t.begin_fill()

    #continue making the top left traingle
    t.pd()
    t.fd(25)

    #making the top line to make it look fancier
    t.pu()
    t.rt(45)
    t.pd()
    t.fd(455)

    #making the top right traingle
    t.pu()
    t.pd()
    t.rt(45)
    t.fd(30)

    #Right side line going down of the traingle
    t.rt(45)
    t.fd(200)

    #Bottom Right Traingle
    t.rt(45)
    t.fd(30)

    #bottom line going across
    t.rt(45)
    t.fd(451)

    #bottom left traingle
    t.rt(45)
    t.fd(30)

    # Line going up on the left side
    t.rt(45)
    t.fd(204)

    #End the filling of the inside of the card
    t.end_fill()

    #Test to see if line are on the line
    #t.rt(90)
    #t.fd(500)
    #They are on the same line

    #pushing the turtle to the left side to be able see the turtle print out the text needed for the card
  #  t.pu()

   # t.rt(270)
   # t.fd(200)

    #t.pd()

    #______________Creating the Font outputting the company card name and color _________#
    t.pensize(2)
    t.pu()
    t.bk(125)
    t.rt(90)
    t.fd(350)

    t.color("red")
    style = ('Helvetica',14,'bold')
    t.write("Palaxium Shadow Gov. LLC.\n" "Email : Palaxium@gmail.com\n" "Phone: (666) 420 - 6969 ", font = style, align = 'center')

    #bring back color to normal
    t.color("black")
    
 ##_____________________Creating the Company Logo_____________________#

    #pushing the turtle  to create the logo
    #DONT CHANGE THE RIGHT ON THIS PORTION!!!!!!#
    t.pu()
    t.rt(180)

    t.fd(175)
    t.rt(45)
    t.fd(100)

    #Create the inside of the logo 
    t.circle(25)

    #getting the inner left line in place#
    #CHANGE RT TO CORRECTLY ALIGN LOGO#
    ##This right is the one that change the location of the entire logo#
    t.rt(225) 
    t.fd(10)


    t.rt(90) 

    #moving the diamond to connect to the circle
    t.bk(-44)

    ####DONT CHANGE ANYTHING BELOW HERE!!!!!!!!!!!!!!!#
    #Actual line being created for the logo and begin filling in the inner diamond
    t.fillcolor("red")
    t.begin_fill()

    t.pd()
    t.fd(25)

    #Putting the inner right line in place
    t.pu()
    t.rt(180) 
    t.fd(75)

    #printing the line on the right side for the logo
    t.pd()
    t.fd(25)

    #getting the inner bottom line in place
    t.pu()
    t.bk(50)
    t.rt(91)
    t.fd(30)

    #printing the actual bottom inner line
    t.pd()
    t.fd(50)

    #getting the top inner line in place
    t.pu()
    t.rt(180)
    t.fd(100)

    #printing the actual top inner line
    t.pd()
    t.fd(30)

    #connecting the top inner line to the inner left line
    t.rt(-135)
    t.fd(75)

    #connecting inner left to inner bottom
    t.rt(-80)
    t.fd(92)

    #connecting the inner bottom to the inner right
    t.rt(-110)
    t.fd(92)

    #connecting the inner right to the inner middle and ending filling
    t.rt(-80)
    t.fd(75)
    #t.end_fill()

    #making the outer area of the diamond and connecting it to the inner left
    t.fillcolor("firebrick3")
    t.rt(-80)
    t.fd(95)

    t.rt(-145) 
    t.fd(26)

    # connecting bottom outer area of diamond to  the middle area
    t.pu()
    t.bk(25)

    t.pd()
    t.rt(55)

    t.fd(138)
    t.rt(-145)
    t.fd(45)

    #Connecting the middle portion of the right side of the diamond
    t.pu()
    t.bk(45)

    t.pd()
    t.rt(35)
    t.fd(139)

    t.rt(-125) 
    t.fd(35)

    #Connecting the outer right side to the top inner side
    t.pu()
    t.bk(35)

    t.pd()
    t.rt(34) 

    t.fd(101)
    t.end_fill()

    #Creating the inner circle and begining to color fill it
    t.pu()
    t.rt(-125)

    t.fd(84)
    t.rt(-90)

    t.pd()
    t.fillcolor("tomato1")#tomato1
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    
##    #The logo has finally been completed !

#____END OF FRONT CARD____END OF FRONT CARD_____END OF FRONT CARD_______#



#___START OF BACK CARD____START OF BACK CARD____START OF BACK CARD______#

    #moving the turtle to be able to create the card
    t.up()
    t.fd(500)

        #_______________Creating the actual Card___________________#

    #Setting the pen size and the colorfill of the card on the edges
    t.pensize(2)
    t.fillcolor("gray7")

    #Making the rectangle for the card and begining and ending fill 
    t.begin_fill()
    t.fd(500)
    t.rt(90)

    t.fd(250)
    t.rt(90)

    t.fd(500)
    t.rt(90)

    t.fd(250)
    t.end_fill()

    #filling picking the color for the body of the card
    t.fillcolor("gray9")# original color gray10

    #making the top left traingle
    t.pu()
    t.bk(25)
    t.rt(45)
    t.fd(5)

    # begining to fill the inside of the card
    t.begin_fill()

    #continue making the top left traingle
    t.pd()
    t.fd(25)

    #making the top line to make it look fancier
    t.pu()
    t.rt(45)
    t.pd()
    t.fd(455)

    #making the top right traingle
    t.pu()
    t.pd()
    t.rt(45)
    t.fd(30)

    #Right side line going down of the traingle
    t.rt(45)
    t.fd(200)

    #Bottom Right Traingle
    t.rt(45)
    t.fd(30)

    #bottom line going across
    t.rt(45)
    t.fd(451)

    #bottom left traingle
    t.rt(45)
    t.fd(30)

    # Line going up on the left side
    t.rt(45)
    t.fd(204)

    #End the filling of the inside of the card
    t.end_fill()

        #______________Creating the Font outputting the company card name and color _________#
    t.pensize(2)
    t.pu()
    t.bk(125)
    t.rt(90)
    t.fd(350)
    
    t.write("")

    #bring back color to normal
    t.color("black")
    

     ##_____________________Creating the Company Logo_____________________#

    #pushing the turtle  to create the logo
    #DONT CHANGE THE RIGHT ON THIS PORTION!!!!!!#
    t.pu()
    t.rt(180)

    t.fd(25)
    t.rt(45)
    t.fd(100)

    #Create the inside of the logo 
    t.circle(25)

    #getting the inner left line in place#
    #CHANGE RT TO CORRECTLY ALIGN LOGO#
    ##This right is the one that change the location of the entire logo#
    t.rt(225) 
    t.fd(10)


    t.rt(90) 

    #moving the diamond to connect to the circle
    t.bk(-44)

    ####DONT CHANGE ANYTHING BELOW HERE!!!!!!!!!!!!!!!#
    #Actual line being created for the logo and begin filling in the inner diamond
    t.fillcolor("red")
    t.begin_fill()

    t.pd()
    t.fd(25)

    #Putting the inner right line in place
    t.pu()
    t.rt(180) 
    t.fd(75)

    #printing the line on the right side for the logo
    t.pd()
    t.fd(25)

    #getting the inner bottom line in place
    t.pu()
    t.bk(50)
    t.rt(91)
    t.fd(30)

    #printing the actual bottom inner line
    t.pd()
    t.fd(50)

    #getting the top inner line in place
    t.pu()
    t.rt(180)
    t.fd(100)

    #printing the actual top inner line
    t.pd()
    t.fd(30)

    #connecting the top inner line to the inner left line
    t.rt(-135)
    t.fd(75)

    #connecting inner left to inner bottom
    t.rt(-80)
    t.fd(92)

    #connecting the inner bottom to the inner right
    t.rt(-110)
    t.fd(92)

    #connecting the inner right to the inner middle and ending filling
    t.rt(-80)
    t.fd(75)
    #t.end_fill()

    #making the outer area of the diamond and connecting it to the inner left
    t.fillcolor("firebrick3")
    t.rt(-80)
    t.fd(95)

    t.rt(-145) 
    t.fd(26)

    # connecting bottom outer area of diamond to  the middle area
    t.pu()
    t.bk(25)

    t.pd()
    t.rt(55)

    t.fd(138)
    t.rt(-145)
    t.fd(45)

    #Connecting the middle portion of the right side of the diamond
    t.pu()
    t.bk(45)

    t.pd()
    t.rt(35)
    t.fd(139)

    t.rt(-125) 
    t.fd(35)

    #Connecting the outer right side to the top inner side
    t.pu()
    t.bk(35)

    t.pd()
    t.rt(34) 

    t.fd(101)
    t.end_fill()

    #Creating the inner circle and begining to color fill it
    t.pu()
    t.rt(-125)

    t.fd(84)
    t.rt(-90)

    t.pd()
    t.fillcolor("tomato1")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    #creating the bottom text for the back of card

    t.pu()
    t.rt(90)
    t.fd(110)

    t.pd()
    t.color("red")
    style = ('Helvetica',14,'bold')
    t.write("Never over shadow us pal.",font = style, align = 'center')
    
else:
    print(" Ask the owner for the password.")

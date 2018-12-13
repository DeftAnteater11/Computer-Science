import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

show = pg.prompt("What is your favorite show? ")

if show == "Family Guy":
    points += 200
    t.sleep(5)
    pg.alert("That is a really good show!")
elif show == "Big Ten Football and Beyond":
    wb.open("https://www.bing.com/videos/search?q=Big+Ten+Football+and+Beyond&&view=detail&mid=26D353CA3497CA632D1626D353CA3497CA632D16&&FORM=VRDGAR")
    points += 100
    t.sleep(3)
    pg.alert("I love football!")
elif show == "Ceeday":
    points += 300
    t.sleep(4) 
    pg.alert("Good man!")
elif show == "The Office UK":
    points += -200,000
    t.sleep(5)
    pg.alert("Dwight is doodoo")
elif show == "First Take":
    wb.open("https://www.bing.com/videos/search?q=stephen+a+smith+screaming&view=detail&mid=846A6E79064A34F93121846A6E79064A34F93121&FORM=VIRE")
    points += 50
    t.sleep(3)
    pg.alert("Noice")
elif show == "Spongebob":
    points += 400
    t.sleep(3)
    pg.alert("I loved that show as well!")
else:
    pg.alert("Your favorite show is " + show)

team = pg.prompt("What is your favorite college team?")

if team == "Michigan":
    wb.open("https://www.bing.com/videos/search?q=michigan+football+&&view=detail&mid=8AA915E73B34A2D21B828AA915E73B34A2D21B82&&FORM=VRDGAR")
    points += 500,000
    t.sleep(3)
    pg.alert("Wow they are so good. They are ten times better than Ohio State and Michigan and much more prestigous then either. Wow they are so great hopefully they can beat Maryland who is actually a solid team this year and show them that we are ready to take the leap into one of the teams contending this year")
elif team == "Ohio State":
    wb.open("https://www.youtube.com/watch?v=kmCx36Mtf7Y")
    points += -750,000
    t.sleep(3)
    pg.alert("Just no, I hope Michigan wipes the floor with them")
elif team == "Penn State":
    wb.open("https://www.youtube.com/watch?v=UIxkaGOyVHQ")
    points += -500
    pg.alert("I hope you suffer while you watch this video")
elif team == "Oklahoma":
    points += -400
    t.sleep(3)
    pg.alert("Get a defense before you try to compete with the big boys")
elif team == "Alabama":
    points += -750
    t.sleep(3)
    pg.alert("BANDWAGON BANDWAGON BANDWAGON")
elif team == "Slippery Rock":
    points += 300
    t.sleep(3)
    pg.alert("VERY GOOD")
else:
    pg.alert("As long as your team isn't Michigan State, Notre Dame, Ohio State, or Penn State, I shall respect you")
food = pg.prompt("What is your favorite food? ")

if food == "Tacos":
    wb.open("https://www.bing.com/videos/search?q=every+loss+in+the+urban+meyer+era&qs=PF&cvid=cfaa5f13dba040938d14abf98cd747c5&cc=US&setlang=en-US&PC=LSJS&ru=%2fsearch%3fq%3devery%2bloss%2bin%2bthe%2burban%2bmeyer%2bera%26form%3dEDGEAR%26qs%3dPF%26cvid%3dcfaa5f13dba040938d14abf98cd747c5%26cc%3dUS%26setlang%3den-US%26PC%3dLSJS&view=detail&mmscn=vwrc&mid=C1419F2C823734B0018CC1419F2C823734B0018C&FORM=WRVORC")
    pg.alert("You're doodoo, Tapioca is actually god tier and so is Ohio State not Michigan stupid.. ")
elif food == "Cotton Candy":
        wb.open("https://www.bing.com/images/search?q=cotton+candy&FORM=HDRSC2")
        points += 200
        t.sleep(3)
        pg.alert("Now that actually makes sense!")
elif food == "Pizza":
        points += 200
        t.sleep(5)
        pg.alert("That is SOLID!")
elif food == "Pasta":
    points += 200
    t.sleep(3)
    pg.alert("I respect it")
elif food == "Cringle":
    points += 300
    t.sleep(3)
    pg.alert("Yes.")
elif food == "Cookies":
    points += 200
    t.sleep(3)
    pg.alert("Aight")
else:
    pg.alert("Your favorite food is" + food)
game = pg.prompt("What is your favorite video game? ")

if game == "Call of Duty Black Ops 4":
    wb.open("https://www.youtube.com/watch?v=6kqe2ICmTxc")
    points += 500,000
    t.sleep(4) 
    pg.alert("Well that is just an amazing game! ")
elif game == "Fortnite":
    wb.open("https://www.youtube.com/watch?v=Y8Ij9xboreA")
    points += -500
    t.sleep(4)
    pg.alert("That game is more dead than the dinosaurs... ")
elif game == "Fallout 76":
    t.sleep(3)
    pg.alert("G_o_O-D!")
else:
    pg.alert("Well that is just a terrible game.... ")
      
book = pg.prompt("What is your favorite book? ")

if book == "Diary of a Wimpy Kid":
    wb.open("https://www.youtube.com/watch?v=6VYRAiXB-h0")
    points += -1
    pg.alert("You're probably 6 years old and just spray the compact smg in fortnite trash can.")
elif book == "Fearless":
    wb.open("https://www.youtube.com/watch?v=3EstBFhiXO8")
    points += 400
    t.sleep(3)
    pg.alert("Now that actually is actually a very very very good book. ")
elif book == "Harry Potter":
     points += 200
     t.sleep(3)
     pg.alert("I like that series as well!")
elif book == "Cherub":
     wb.open("https://images-na.ssl-images-amazon.com/images/I/61xe86R4AAL.jpg")
     points += 25
     t.sleep(3)
     pg.alert("I heard it is good")
else:
    pg.alert("Your favorite book is " + book)
          
          

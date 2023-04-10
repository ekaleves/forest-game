print('''
 .. ........... .............  ........... . ..... ........ .......
 ......  ....................%.... .... ..... .........%............
 .@@@ ........ @@.... @@@@  . ............................  *  .....
 ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
 .....\@\....@ .... @ ............................. #  .. *****  ...
  @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
 ....@-@..@ ..@......@@@\...... %...... ....... <## ####>********
   @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********
 ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
 ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
 ...... .  @@ .. ..v.. .. . { } ............<###############>*******
 ......... @@ .... ........ {^^,     .......   {## ######}***** ****
 ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
 . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
 .... ... @@ ... ..   /(______); .. ....<################  #####>***
 . .... ..@@@ ...... (         (  .........{##################}*****
 ......... @@@  ....  |:------( )  .. <##########################>**
  @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****
 @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
print("Welcome to Surviving the forest.")
print("Your mission is to get out of the forest, and find the city.")
print("You went to the forest to have a picnic, and a wild animal scared you. You ran deep into the forest. now you realized that you are lost.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

firstCommand = input("You look in front of you, and there is two options to choose. go to the 'left', or go to the 'right'. which one do you choose? ")

firstCommand = firstCommand.lower()

if firstCommand == "left":
  print("You choose the left path... You start to walk, when suddenly a pack of wolfs attack you. You're dead! game over!!!")
  
elif firstCommand == "right":
  print("You start to walk.... there is a lot of beautiful trees and it is a warm and sunny day. In the end of this path, you find a lake.")
  secondCommand = input("The lake looks beautiful in the sun light, you wandering what is best choice. 'Swim' or 'find another path'? ")
  secondCommand = secondCommand.lower()
  
  if secondCommand == "swim":
    print("It is a warm day, and you decided that was to much for walk under the heavy sun. So you go inside the lake and starts to swim. When carnivorous piranhas apper and start to biting you. You bleed to much and die. Game over!!")

  elif secondCommand == "find another path":
    print("You decided to walk, even with the warm day, around the lake. you walk for a few kilometers until you find 3 big trees. The trees have doors on it, and again you are forced to make a choice.")
    thirdCommand = input("which door do you choose? 'Red', 'blue', or 'yellow'? ")
    thirdCommand = thirdCommand.lower()

    if thirdCommand == "red":
      print("The red door takes you to a different realm, a realm full of ugly beasts and one eats you alive. Game over!!")

    elif thirdCommand == "blue":
      print("The blue door takes you to a different realm. The Fairy Kingdom it is beautiful and full of amazing colors, there's magical critures living there, and they receive you with love and gracious. But it is impossible to come back to the forest, so you have to live the rest of your days playing with fairies. Game over!!!")

    elif thirdCommand == "yellow":
      print("The yellow door, when you open, takes you back to your living room, where you can sit confortably and enjoy your day. YOU WIN!!! ")
  
    else:
      print("Wrong command. Game over!!")

  else:
    print("Wrong command. Game over!!")
  
else:
  print("Wrong command. Game over!!")
  
  

  


  


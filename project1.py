# pprint allows us to print lists in a nicer manner
from pprint import pprint

# create an empty list called pictures
pictures = []

# on Windows replace back slash (\) with foward slash (/)
pathToImages = "c:/Users/Avner/Desktop/my205Project1/Project1Images/" 

firstImage = pathToImages + "1.png"

for image in range(1,10):
	# we have to cast our counter (image) to a string for concatenation here
	myImage = pathToImages + str(image) + ".png"
	
	"""
	In each iteration of the loop, add picture to the end of the list.
	makePicture() is a JES function which returns a picture object.
	"""
	pictures.append(makePicture(myImage))


pprint(pictures)
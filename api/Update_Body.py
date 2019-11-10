from PIL import Image, ImageDraw, ImageOps


def findColor(condition):
	if condition == "Good": return "green"
	if condition == "Okay": return "orange"
	if condition == "Bad": return "red"



def update():
	# Data
	areas = {"neck":[300, 200, "red"], "left wrist":[70, 800, "red"],
	 "left ankle":[240, 1550, "red"], "right wrist":[540,800, "red"],
	 "right ankle":[370, 1550, "red"], "left knee":[240, 1205, "orange"], 
	 "right knee":[370, 1205, "orange"]}


	# Initialize
	img = Image.open("human.png")
	pen = ImageDraw.Draw(img)

	
	# Draw some stuff
	for joint in areas:
		color = areas[joint][2]
		x, y = areas[joint][0], areas[joint][1]
		pen.ellipse([x, y, x+50, y+50], fill=color)
	

	# Paste some stuff
	'''
	for joint in areas:
		image = Image.open(areas[joint][2]+".png", 'r')
		w, h = 50, 50
		offset = areas[joint][0], areas[joint][1]
		img.paste(image, offset, image.convert('RGBA'))
	'''

	# Save the image
	img.save("humanOut.png")

if __name__ == "__main__":
	update()
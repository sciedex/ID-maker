from PIL import Image, ImageDraw, ImageFont

#Data Collection
name = input("type in your full name: ")  
print ("is " , name, "correct?" )
namecheck = input("y/n ")
if namecheck == "y":
    namecheck = "correct"
elif namecheck == "n":
    name = input("enter your name: ")

print ("Hello ", name, ", this is a data collection and ID making for the Livgardet coorps.")  
print ("Please note that you cannot change your data after this point. Becareful when entering your data.")
id_number = input("Please enter your ID number: ")
sex = input("Please enter your sex: ")
height = input("Please enter your height in Centimeters: ")
weight = input("Please enter your Weight in Kilograms: ")

photo_path = "desktop/Unknown.jpeg"  # Path to the photo
template_path = "desktop/id_template.png"  # Path to the ID card template

# Load template and photo
template = Image.open(template_path)
photo = Image.open(photo_path)
photo = photo.resize((250, 300))  # Resize the photo as needed

# Paste photo onto template
template.paste(photo, (50, 50))

# Initialize drawing context
draw = ImageDraw.Draw(template)

# Load font
font_path = "desktop/typewriter.ttf"  # Path to a font file
font = ImageFont.truetype(font_path, 50)

# Draw text onto template
draw.text((50, 350), f"Name  : {name}", fill="black", font=font)
draw.text((50, 400), f"ID    : {id_number}", fill="black", font=font)
draw.text((50, 450), f"Sex   : {sex}", fill="black", font=font)
draw.text((50, 500), f"Height: {height}", fill="black", font=font)
draw.text((50, 550), f"Weight: {weight}", fill="black", font=font)

# Save or display the ID card
template.show()
# template.save("generated_id.png")  # Save the ID card as an image file
template.save("SubjectID.png")
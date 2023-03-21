import face_recognition
photo_1= face_recognition.load_image_file('./photos/Amlo.jpg','RGB')
photo_2= face_recognition.load_image_file('./photos/Ghandi.jpeg','RGB')
photo_3= face_recognition.load_image_file('./photos/Mark.jpg')

print("The shape of the color photos file are: ")
print("Photo 1: ",photo_1.shape)
print("Photo 2: ",photo_2.shape)
print("Photo 3: ",photo_3.shape)
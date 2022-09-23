import PIL.Image
import PIL.ImageDraw
import face_recognition #this gives an access to face detection model in dlib
#load image file into numpy array using face recognition lib
image = face_recognition.load_image_file(r"images/person1.jpg")
'''find all faces in the image by pretrained HOG face detector using face_recognition function'''
face_recog = face_recognition.face_locations(image)
no_of_faces = len(face_recog)
print('total no. of faces are: ', no_of_faces)
#now load image into PIL library to draw box on the top of image
pil_image = PIL.Image.fromarray(image)
for i in face_recog:
    top, right, bottom, left = i
    #draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle((left, top , right, bottom), outline = 'red')

pil_image.show()

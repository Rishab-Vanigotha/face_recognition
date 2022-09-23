import PIL.Image
import PIL.ImageDraw
import face_recognition
from matplotlib.pyplot import fill #this gives an access to face detection model in dlib
#load image file into numpy array using face recognition lib
image = face_recognition.load_image_file(r"images/person1.jpg")
face_recog = face_recognition.face_landmarks(image)
no_of_faces = len(face_recog)
print('total no. of faces are: ', no_of_faces)
#now load image into PIL library to draw box on the top of image
pil_image = PIL.Image.fromarray(image)
#create pil drawing object
draw = PIL.ImageDraw.Draw(pil_image)
#loop over each face
for face_landmarks in face_recog:
    #loop over each facial feature
    for names, list_of_points in face_landmarks.items():
        #print the location of each facial feature in the image
        print("the {} in this face has the following points {}".format(names, list_of_points))
        #tracing out the facial feature by drawing line on the landmarks
        draw.line(list_of_points,fill = "red",width=2)
    

pil_image.show()

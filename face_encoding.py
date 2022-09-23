import face_recognition
#load images
person1=face_recognition.load_image_file(r"images/person1.jpg")
person2=face_recognition.load_image_file(r"images/person2.jpg")
person3=face_recognition.load_image_file(r"images/person4.jpg")

#get face encoding of each person
face1 = face_recognition.face_encodings(person1)[0]
face2 = face_recognition.face_encodings(person2)[0]
face3 = face_recognition.face_encodings(person3)[0]
#create a list of all three face encodings
known = [face1,face2,face3]
#now load unkown image you want to check
unknown = face_recognition.load_image_file(r"C:\Users\DELL\Documents\5th sem\machine learning projects\unknown.jpg")
# unknown face encodings
unknown_encodings = face_recognition.face_encodings(unknown)
# loop over each photos as ther might be more than one same person's photos
for i in unknown_encodings:
    results = face_recognition.compare_faces(known, i)

    name = 'unknown'

    if results[0]:
        name = 'person1'
    elif results[1]:
        name = 'person2'
    elif results[2]:
        name = 'person3' 
    print("found {} in photo".format(name)) 

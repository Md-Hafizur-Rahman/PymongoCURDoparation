connectingString='mongodb+srv://HafizurRahman15-1979:hafizur1979@cluster0.jt70izk.mongodb.net/test'
import pymongo
from pymongo import MongoClient

def deleteDocument():
    collection.delete_many({'math_marks': 100})
def updateDocument():
    #collection.update_one({'section':3}, {'$inc': {'section':111}})
    collection.update_many({}, {'$inc': {'math_marks':1}})
def insertDocument():
    studentInfo={
        "name":"hafsa-123",
        "section":3,
        "math_marks":100,
        "get_marks":95
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f'student this {student_id} id hass been created!')
if __name__ == '__main__':
    client =MongoClient(connectingString,connect=False)
    db = client['Collectorate_school_and_college']
    # creating a collection
    collection = db.class1
    # CURD operation => create,update,read,delete
    insertDocument()

    # read the document more than one
    for mystudent in collection.find({'section':'A'}):
        print(mystudent)
    # update
    #updateDocument()
    # delete the document
    deleteDocument()
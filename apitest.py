import requests
import json 

def getreq(url):
    try:
        res=requests.get(url)
        return json.dumps(res.json(),indent=4)
    except Exception as ee:
        return f"message:{ee}"
def postreq(url,data):
    try:
        res=requests.post(url,json=data)
        return json.dumps(res.json(),indent=4)
    except Exception as er:
        return (f"message:{er}")
if __name__== '__main__':
    while True:
        try:
           choice=int(input("1.get\n 2.post \n 3.exit\n Enter choice:"))
           if choice==1:
                url1= input("enter a valid url")
                print(getreq(url1))
           elif choice == 2:
               url_inp = input("Enter a valid get url : ")
               data_inp = {"name": input("Name : "),"email": input("Email : "),"work": input("Work : "),"age": input("Age : ")}
               print(postreq(url_inp, data_inp))
                 
           elif choice == 3:
                exit(0)
                 
        except Exception as e:
            print("Error : ", e)

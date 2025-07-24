# My CLI project
import time

print("Բարի Գալուստ օգտատեր !:")

time.sleep(3)

name = input("Մուտքագրեք ձեր անունը: ")
surname = input("Մուտքագրեք ձեր ազգանունը: ")
age = input("Մուտքագրեք ձեր տարիքը: ")
city = input("Մուտքագրեք որտեղ էք ապրում։ ")
student = input("Դուք ստուդենտ եք ? (yes/no): ")

if student.lower() == "yes":
    student = True
else:
    student = False

class user:
    def __init__(self,name,surname,age,city,student):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.student = student

    def greet(self):
        about = input(f"Ես {self.name} {self.surname} եմ :Ես {self.age} տարեկան եմ ,ապրում եմ {self.city}: Ստուդենտ {self.student},ճիշտ է՞(yes/no): ")
        if about.lower() == "yes":
            print(f"Բարի Գալուստ {self.name} {self.surname} !")

            data = input("📄 Տվյալները հաջողությամբ գրանցվեցին user_data.txt ֆայլում!, ցույց տալ ֆայլը՞(yes/no) ")
            if data.lower() == "yes":
              with open("user_data.txt", "w", encoding="utf-8") as f:
               f.write(f"Անուն: {name}\n")
               f.write(f"Ազգանուն: {surname}\n")
               f.write(f"Տարիք: {age}\n")
               f.write(f"Ապրում է: {city}\n")
               f.write(f"Ստուդենտ: {student}\n")
    
              with open("user_data.txt", "r", encoding="utf-8") as f:
               content = f.read()
               print("💾 Ձեր պահված տվյալները՝")
              print(content)
            else:
             print(f"{name}, շնորհակալություն ձեր տվյալները մուտքագելու համար ! ...")
        else:
         print("Error: նորից կրկնեք մուտքագրումը....")

User = user(name,surname,age,city,student)
User.greet()
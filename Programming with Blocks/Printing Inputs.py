# 1. This is a basic program that ask the user certain information about him/her This information can be used in different ways, it can also be stored in a database and later displayed with different purposes. I did not programmed this store any information so feel free to answer these questions!
# 2. The following is a simple design of a questionnaire with simple questions such as "What is your...". In the questionnaire i added justifying questions like "Why..." where the user justifies his/her previous answer.
name = input("What is your First Name?")
print("Thas a nice Name", name,"!")
last_name = input("What is your Last Name?")
print("Nice last Name too!")
print("So,", name, last_name, "let me ask you some questions about you...")
Language = input("What is your primary language?")
print("Thats so cool!")
hobbies = input("Do you have any Hobbies? (Yes/No)")
if hobbies == "yes":
  Whobbies = input("What is your favorite thing to do then?")
  why_hobbies = input(f"Why do you enjoy {Whobbies} ?" )
  print("It seem you really enjoy doing it!")
elif hobbies == "No":
    print("There are lots of fun things to do, You should try something you find fun!")
favorite_book = input("What is your favorite book?")
print("cool")
why_book = input(f"Why '{favorite_book}' is yor favorite book?")
print("Cool!")
favorite_color = input("What is your Favorite Color?")
print(f"your favorite color is", favorite_color)
print("Thats a good color!")
programming = input("Do know any progrming languages? (Yes/No)")
if programming == "yes" or programming == "Yes": 
    projects = input("Have you done any major projects with those languages?")
    print("Thats way Cool!")
else:
    print("Programming languages are fun you should try it!")


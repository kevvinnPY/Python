gay=0
name = input("What is your name?: ")
gender = input("What is your gender?: ")
if gender == "male":
  q1 = input("Question 1: Do you like boys?: ")
  if q1 == "yes":
    gay += 20
  q2 = input("Question 2: Have you ever kissed a boy?: ")
  if q2 == "yes":
    gay += 50
  q3 = input("Question 3: Do you have a dad?: ")
  if q3 == "no":
    gay += 10
  q4 = input("Question 4: Do you like girls?: ")
  if q4 == "no":
    gay += 15
  q5 = input("Question 5: Do you like pastel colors?: ")
  if q5 == "yes":
    gay += 5

if gender == "female":
  q1 = input("Question 1: Do you like girls?: ")
  if q1 == "yes":
    gay += 20
  q2 = input("Question 2: Have you ever kissed a girl?: ")
  if q2 == "yes":
    gay += 50
  q3 = input("Question 3: Do you have a dad?: ")
  if q3 == "no":
    gay += 10
  q4 = input("Question 4: Do you like boys?: ")
  if q4 == "no":
    gay += 15
  q5 = input("Question 5: Do you like pastel colors?: ")
  if q5 == "yes":
    gay += 5

if gay >= 50:
  print("Oh no! you are", gay, "% gay.")
if gay <=50:
  print("Congratulations! You are", gay, "% gay")
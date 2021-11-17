import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


select_name = random.randint(0, (len(names) - 1))
name_selected = names[select_name]

print(f"{name_selected} is going to buy the meal today!")


#We can use choice() function insted of all this code.

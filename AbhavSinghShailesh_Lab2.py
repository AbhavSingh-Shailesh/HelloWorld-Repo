'''
AbhavSInghShailesh
9/6/2024
'''
#This line of the code takes the human age.
human_age = float (input("Enter your age:"))

#This line of the code takes the human age and multiplies it by 7 which is dog years.
dog_age = int(human_age * 7)

#This line cal the months by getting the dog age * 12 for months
dog_month = int ((human_age*7-dog_age)*12)

#This line cal the days by gettting the moths and diving a year in 12 months
dog_days = int ((dog_month * 360)%30)

print(f"Your age in dog years is: {dog_age} years, {dog_month} months, {dog_days} days")





#This line gets the human age dividing that by 9 to get cat age
cat_age = int(human_age / 9)

#Calculates the months by getting the cat age * 12 for months
cat_months = int((human_age / 9 - cat_age)*12)

#Calculates the days by gettting the moths and diving a year in 12 months
cat_days = int(((human_age / 9 - cat_age) *12 - cat_months)*(360/12))

print(f"The age of your cat is: {cat_age} years, {cat_months} months, {cat_days} days")


#This line takes human age and uses the horse age formula to calculate the horse years.
horse_age = int(3 * ((((human_age ** 2) - 47) / 7) + 12))

horse_months = int ((human_age * 6.46428 - horse_age)*12)

horse_days =  int(((human_age * 6.46428 - horse_age) *12 - horse_months)*(360/12))


print(f"Your horse age is: {horse_age} years,{horse_months} months,{horse_days} days")













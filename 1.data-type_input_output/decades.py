age = int(input("How old are you?\n"))
year = age%10
# decades = (int)((age - year)/10)
decades = age // 10 

print(f"You are {decades} decades and {year} year(s) old.")

score_in_int = input("Enter your Mark: ")

# Use 'and' instead of '&', and check for an empty string first
if score_in_int == '' or int(score_in_int) > 100:
    print("Enter a valid number")
else:
    score = int(score_in_int)
# score = 80
    # if you break or exit the program in your condition then use exit() or break()then your condition is not satified then your program stop 
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else:
        grade = "F"

    print("Grade:", grade)
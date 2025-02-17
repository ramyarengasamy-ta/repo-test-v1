score = int(input(" enter the student's score. "))
if score >= 90:
    print(str(score) + " is an A.")
else:
    if score >= 80:
        print(str(score) + " is a B.")
    else:
        if score >= 70:
            print(str(score) + " is a C.")
        else:
            if score >= 60:
                print( str(score) + " is a D.")
            else:
                print(str(score) + " is a F.")

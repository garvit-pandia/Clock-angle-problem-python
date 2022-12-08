print("\tGreetings Ma'am\n"
      "\tThis Project Is Submitted By :- \t Garvit Pandia (Roll no = 53)\n"
      "\tSection = K22KS\n")
print("\tClock Angle Problem")
hour = int(input("\tEnter The Time In Hours =\t"))
minutes = int(input("\tEnter The Time In Minutes =\t"))
if 12 < hour < 24:
    if minutes >= 0 and minutes <= 60:
        min_deg = (minutes * 6)
        hour_deg = ((hour + minutes / 60) / 12) * 360 % 360
        print("\tThe Angle Between ", hour, " : ", minutes, " = ",
              min(abs(min_deg - hour_deg), 360 - (abs(min_deg - hour_deg))), "°", sep="")
        print("\n"
              "\tTHANK YOU")
    elif minutes > 60 and minutes < 0:
        print("\tInvalid")
elif hour >= 1 and hour <= 12:
    if minutes >= 0 and minutes <= 60:
        b = input("\tAm or Pm = ")
        min_deg = (minutes * 6)
        hour_deg = ((hour + minutes / 60) / 12) * 360 % 360
        print("\tThe Angle Between ", hour, " : ", minutes, " ", b, " = ",)


        print("\n"
              "\tTHANK YOU")
    elif minutes > 60 or minutes < 0:
        print("\tInvalid")
elif hour > 23 or hour < 1:
    print("\tInvalid")
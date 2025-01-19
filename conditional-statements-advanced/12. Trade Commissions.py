# Град      0 ≤ s ≤ 500     500 < s ≤ 1 000     1 000 < s ≤ 10 000      s > 10 000
#
# Sofia     5%              7%                  8%                          12%
#
# Varna     4.5%            7.5%                10%                         13%
#
# Plovdiv    5.5%              8%               12%                         14.5%

city = input()
sales = float(input())
comission = 0
error_data = False


if city == "Sofia":
        if 0<= sales <= 500:
            comission = sales*0.05
        elif 500<sales<=1000:
            comission = sales*0.07
        elif 1000<sales<=10000:
            comission = sales*0.08
        elif sales>10000:
            comission = sales*0.12
        else:
            error_data = True

elif city == "Varna":
        if 0 <= sales <= 500:
             comission = sales * 0.045
        elif 500 < sales <= 1000:
             comission = sales * 0.075
        elif 1000 < sales <= 10000:
            comission = sales * 0.1
        elif sales > 10000:
            comission = sales * 0.13
        else:
            error_data = True

elif city == "Plovdiv":

        if 0 <= sales <= 500:
            comission = sales * 0.055
        elif 500 < sales <= 1000:
            comission = sales * 0.08
        elif 1000 < sales <= 10000:
            comission = sales * 0.12
        elif sales > 10000:
            comission = sales * 0.145
        else:
            error_data = True
else:
    error_data = True

if error_data == False:
    print(f"{comission:.2f}")
else:
    print("error")
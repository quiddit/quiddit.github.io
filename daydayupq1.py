# DayDayUpQ1.py
dayup1 = pow(1.005, 365)
dayup2 = pow(1.01, 365)
daydown1 = pow(0.995, 365)
daydown2 = pow(0.99, 365)
a = input()
print("向上1：{:.2f}，向上2：{:.2f}，向下1：{:.2f}，向下2：{:.2f}".format(dayup1, dayup2, daydown1, daydown2))

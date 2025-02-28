print("Enter the marks obtain in 4 subjects : ")
math =int(input("maths : "))
science =int(input("science : "))
sinhala =int(input("sinhala : "))
English =int(input("English : "))

sum = science+math+sinhala+English
print("sum of science,math,sinhala,English")

perc=(sum/400)*100

print(end="percantage mark = ")
print(perc)
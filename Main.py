import div_u
import mul

print("Enter two space seperated numbers")
a,b = map(int,input().split())

f = open("result.txt", "w")
f.write(div_u._div(a,b)+"\n")
f.write("--------------------"+"\n")
f.write(mul.mul(a,b)+"\n")
f.close()

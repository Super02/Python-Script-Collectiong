user_input=int(input("Indtast et tal du vil omvende: "))
_rev=0
while(user_input>0):
  dig=user_input%10
  _rev=_rev*10+dig
  user_input=user_input//10
print("Det omvendte tal er: ",_rev)

#

# get input value for total number of friends 
total_friends=int(input("enter no of frnds:"))
total_bill=int(input("enter bill:"))
# calculate the tax amount
tax = total_bill*0.20
final=tax+total_bill
bill=final/total_friends
print(bill)




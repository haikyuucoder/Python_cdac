inv_amt=float(input("Enter the investment amount: "))
time=int(input("Enter the number of years: "))
rate=float(input("Enter the rate as a%: "))
amt=inv_amt
t=time
r=rate
interest=(inv_amt*r*1)/100
end_bal=amt+interest
for i in range(time+1):
	if(i==0):
		print("%5s"%'Year',"%17s"%'Starting Balance',"%10s"%'Interest',"%16s"%'Ending Balance')
	else:
		print("%5d"%i,"%17.2f"%amt,"%10.2f"%interest,"%16.2f"%end_bal)
		end_bal=amt+interest
		amt=end_bal
		interest=(amt*r*1)/100
print("Ending Balance: Rs %0.2f"%amt)
print("Total Interest Earned: Rs %0.2f"%(amt-inv_amt))
	

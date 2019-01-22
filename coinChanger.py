def changer(cost, paid):
	#Calculate chage
	change = paid - cost

	#break down
	dollars = int(change)
	cents = 100*(change - dollars)
	round(cents)

	denom_dollars = [50, 20, 10, 5, 1]
	count_dollars = []
	denom_change = [25, 10, 5, 1]
	count_cents = []
	count = 0

	for denom in denom_dollars:
	    while dollars >= denom:
	        dollars = dollars - denom
	        count += 1
	    count_dollars.append(count)
	    count = 0

	for denom in denom_change:
	    while cents >= denom:
	        cents = cents - denom
	        count += 1
	    count_cents.append(count)
	    count = 0

	print("Change: \n")
	print("Fifties:", count_dollars[0])
	print("Twenties:", count_dollars[1])
	print("Tens:", count_dollars[2])
	print("Fives:", count_dollars[3])
	print("Ones:", count_dollars[4], "\n")

	print("Quarters:", count_cents[0])
	print("Dimes:", count_cents[1])
	print("Nickels:", count_cents[2])
	print("Pennies:", count_cents[3])

changer(25.76, 50)
per_unit_price = int(input("Enter The Price Of Petrol\n"))
mileage = int(input("Enter The Mileage\n"))
price_per_dis = per_unit_price / mileage
total_distance = int(input("Enter The Total Distance You Want To Travel\n"))
total_price = price_per_dis * total_distance
print("Total Price Of Petrol : ",total_price)
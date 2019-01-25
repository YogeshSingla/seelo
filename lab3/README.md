# Project - Transport Automation Vehicle System
## Description
A transport company requires to automate its various operations. The company has a fleet of vehicles.  
Currently the company has the following vehicles :  
1. Ambassadors : 10 Non-AC, 2 AC
2. Tata Sumo : 5 Non-AC, 5 AC
3. Maruti Omni : 10 Non-AC
4. Maruti Esteem : 10 AC
5. Mahindra Armada : 10 Non-AC  

The company rents out vehicles to customers. When a customer requests for a car, the company lets them
know what types of vehicles are available, and the charges for each car. For every car, there is a per hour
charge, and a per kilometer charge. A car can be rented for a minimum of 4 hours. The amount chargeable
to a customer is the maximum of (per hour charge for the car times the number of hours used, and per
kilometer charge times the number of kilometers run) subject to a minimum amount decided by the charge
for 4 hours use of the car. An AC vehicle of a particular category is charged 50% more than a non-AC vehicle of the same category. There is a charge of Rs 150 for every night halt regardless of the type of the vehicle.
When a customer books a car, he has to deposit an advance amount. The customer also informs the company when he expects to return the car. When the car is returned, depending on the usage, either the
customer is refunded some amount, or he has to pay additional amount to cover the cost incurred.
The company can acquire new vehicles and add them to the fleet of its vehicles. Cars may be condemned
and sold off. A car which is currently with the company can be in one of these three states: it may have
gone for repair, it may be available, it may be rented out. If it is rented out, the company records the data
and time when it has been rented out, and the mile-meter reading of the car at that time. The company
also wants to maintain the amount of maintenance expense each vehicle incurs.
The company wants to collect statistics about various types of vehicles : the price of the car, average amount
of money spent on repairs for the car, average demand, revenue earned by renting out the car, and fuel
consumption of the car. Based on these statistics, the company may take a decision about which vehicles
are more profitable. The statistics can also be used to decide the charge for different types of vehicles.

## Preliminary Requirements
*Primary : A transport company requires to automate its various operations.*

1. Rents out vehicles to customers. 
    1. customer requests for a car
        1. the company lets them know what types of vehicles are available, and the charges for each car.   
        2. The amount chargeable to a customer is the maximum of (per hour charge for the car times the number of hours used, and per kilometer charge times the number of kilometers run) subject to a minimum amount decided by the charge for 4 hours use of the car.  
    2. customer books a car
        1. he has to deposit an advance amount. 
        2. informs the company when he expects to return the car. 
    3. car is returned
        1. depending on the usage, either the customer is refunded some amount, or he has to pay additional amount to cover the cost incurred.

2. Car management
    1. The company can acquire new vehicles and add them to the fleet of its vehicles. 
    2. Cars may be condemned and sold off. 
    3. A car which is currently with the company can be in one of these three states: 
        1. it may have gone for repair, 
        2. it may be available, 
        3. it may be rented out. 
            1. the company records the data and time when it has been rented out, and the mile-meter reading of the car at that time. 

3. Data Collections and Analysis
    1. The company also wants to maintain the amount of maintenance expense each vehicle incurs.
    2. The company wants to collect statistics about various types of vehicles : 
        1. the price of the car, 
        2. average amount of money spent on repairs for the car, 
        3. average demand, 
        4. revenue earned by renting out the car, and 
        5. fuel consumption of the car. 
    3. Determine profitability and decide charges for each type of vehicle.

### Constraints
1. A car can be rented for a minimum of 4 hours.
2. An AC vehicle of a particular category is charged 50% more than a non-AC vehicle of the same category.
3. For every car, there is a per hour
charge, and a per kilometer charge.
4. There is a charge of Rs 150 for every night halt regardless of the type of the vehicle.
# Ricky Bui
# Student ID: 010738347
# C950

import csv
import datetime
import Truck
import Package

from HashTable import CreateHashMap
from Package import Packages
## Testing hash ##
#HashMap = CreateHashMap()
#print(HashMap.list_all())

# Read the file with the distance information
with open("Distance_File.csv") as csvfile:
    CSV_Distance = csv.reader(csvfile)
    CSV_Distance = list(CSV_Distance)

# Read the file with the address information
with open("Address_File.csv") as csvfile1:
    CSV_Address = csv.reader(csvfile1)
    CSV_Address = list(CSV_Address)

# Read the file with the package information
with open("Package_File.csv") as csvfile2:
    CSV_Package = csv.reader(csvfile2)
    CSV_Package = list(CSV_Package)


# Load package files from CSV into a hash table: Package_hash_table
def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for packages in package_data:
            pID = int(packages[0])
            pAddress = packages[1]
            pCity = packages[2]
            pState = packages[3]
            pZipcode = packages[4]
            pDeadline_time = packages[5]
            pWeight = packages[6]
            pStatus = "At Hub"
            pDepartureTime = None
            pDeliveryTime = None
            pCurrentStatus = None

            # Package object
            p = Packages(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus, pDepartureTime, pDeliveryTime, pCurrentStatus)

            # Insert data into hash table
            package_hash_table.insert(pID, p)



# Finding distance between two address
def distance_in_between(addy1, addy2):
    distance = CSV_Distance[addy1][addy2]
    if distance == '':
        distance = CSV_Distance[addy2][addy1]

    return float(distance)


# Method to get address number
def extract_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])

# Manually load trucks
# Truck 1 #13, 14, 15, 16,19, and 20 must all be together
truck1 = Truck.Truck(16, 18, None, [1, 2, 4, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Truck 2 #3, 18, 36,and 38 must be on truck 2
truck2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 21, 23, 24, 25, 26, 27, 32, 33, 36, 38], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=0))

# Truck 3 #6, 25, 28, and 32 cannot leave before 9:05am
truck3 = Truck.Truck(16, 18, None, [5, 7, 8, 9, 10, 11, 22, 28, 35, 39], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=11, minutes=0))

# Create hash table
package_hash_table = CreateHashMap()
#print(package_hash_table.list_all())

# Load packages into hash table
load_package_data("Package_File.csv", package_hash_table)

# Method for ordering packages on a given truck using the nearest neighbor algo
# Calculate truck milage driven
def delivering_packages(truck):
    # Place all packages into an array to be delivered
    notDelivered = []
    for packageID in truck.packages:
        package = package_hash_table.lookup(packageID)
        notDelivered.append(package)
    # Clear the package list of a given truck so the packages can be placed back into the truck in the order
    truck.packages.clear()

    # While there are packages left to be delivered, algorithm will continue to run
    while len(notDelivered) > 0:
        next_address = 1000
        next_package = None
        for package in notDelivered:
            if distance_in_between(extract_address(truck.address), extract_address(package.address)) <= next_address:
                next_address = distance_in_between(extract_address(truck.address), extract_address(package.address))
                next_package = package
        # Adds next closest package to list
        truck.packages.append(next_package.ID)
        # Removes the same package from not delivered list
        notDelivered.remove(next_package)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.mileage += next_address
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_package.address
        # Updates the time it took for the truck to drive to the nearest package
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time


# Put the trucks through the loading process
delivering_packages(truck1)
delivering_packages(truck2)
# Truck 3 will not leave until either truck 1 or truck 2 is finished delivering their packages
truck3.depart_time = min(truck1.time, truck2.time)
delivering_packages(truck3)


class Main:
    # User Interface
    # Below is used to check the status of the package at a certain time or of all the packages
    print("Western Governors University Parcel Service (WGUPS)")
    # Print total mileage of all the trucks combine
    print(f"The total milage for Western Governors University Parcel Service (WGUPS)   {truck1.mileage + truck2.mileage + truck3.mileage}")
    # To check the status of of the packages the user will be asked to input "status"
    status = input("To start please type the word 'status' (Anything other than 'status' will cause the program to exit the program). ")
    # The program will prompt the user to be able to check the status of certain packages or all
    if status == "status":
        try:
            # The user will be asked to enter a specific time
            userTime = input(
                "Please enter a time to see the status of each package. Format: HH:MM. ")
            (h, m) = userTime.split(":")
            timeChange = datetime.timedelta(hours=int(h), minutes=int(m))
            # The user will be prompt to check the status of a single package or all the packages
            second_input = input("To view the status of an individual package please type 'one'. For a rundown of all"
                                 " packages please type 'all'. ")
            # Prompt the user to enter "one" to look up a package
            if second_input == "one":
                try:
                    # The user will be asked to input a package ID. Invalid entry will cause the program to quit
                    solo_input = input("Enter the numeric package ID ")
                    package = package_hash_table.lookup(int(solo_input))
                    package.update_status(timeChange)
                    print(str(package))
                except ValueError:
                    print("Invalid Entry. Closing program.")
                    exit()
            # Prompt the user to enter all to check the status of all the package
            elif second_input == "all":
                try:
                    for packageID in range(1, 41):
                        package = package_hash_table.lookup(packageID)
                        package.update_status(timeChange)
                        print(str(package))
                except ValueError:
                    print("Invalid entry. Closing program.")
                    exit()
            else:
                exit()
        except ValueError:
            print("Invalid entry. Closing program.")
            exit()
    elif input != " ":
        print("Invalid entry. Closing program.")
        exit()
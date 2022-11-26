from option import message_display
from outrow import thank_you
from clock import countdown
from perfumery import perfumes_site
from pharmacy import medicine_site
from cosomtics import cosmo_site
cosmo_ticket_number = cosmo_site()
medicines_ticket_number = medicine_site()
perfumes_ticket_number = perfumes_site()
count = 0
timer = 1
exit_point = "Stop"
# using id
idnum_dawit = "987654321"
idnum_yonas = "123456789"
id_list = [idnum_dawit, idnum_yonas]


# while exit_point != "stop" and count < 3:
def main_page():
    global count
    while count < 3:
        idnum = input("Please Enter Valid Id: ")
        if idnum in id_list:
            message_display()
            customer = input("Please Choose Which Site you went to visit--> ")
            if customer == "c" or customer == "C" or customer == "cosmetic" or customer == "COSMETIC":
                print("\n\t\t\t\t Your Ticket Number is C-", next(cosmo_ticket_number))
                print("\t\t\t\t Please wait and someone will assist you shortly.")
                print("===================================================================================")
            elif customer == "p" or customer == "P" or customer == "perfume" or customer == "PERFUME":
                print("\n\t\t\t\t Your Ticket Number is P-", next(perfumes_ticket_number))
                print("\t\t\t\t Please wait and someone will assist you shortly.")
            elif customer == "m" or customer == "M" or customer == "medicine" or customer == "MEDICINE":
                print("\n\t\t\t\t Your Ticket Number is M-", next(medicines_ticket_number))
                print("\t\t\t\t Please wait and someone will assist you shortly.")
            else:
                print("\t\t\t\t Please choose correct valid site you went to visit--> ")
                continue
            other_site = input("\nDo you went to continue seeing other sites yes/no: ")
            if other_site == "y" or other_site == "Y" or other_site == "Yes" or other_site == "YES":
                continue
            elif other_site == "":
                print("You didn't Enter valid input, Please enter valid value ")
                other_site = input("Do you went to continue seeing other sites y/n")
            else:
                thank_you()
                break
        else:
            count += 1
            continue
    else:
        print("\nYou Enter invalid ID so many time , please try other time")
        countdown()

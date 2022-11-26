# Define medicine site ticket generator
def medicine_site():
    medicine_queue_num = 1
    medicine_ticket_num = 0
    while True:
        yield medicine_queue_num
        medicine_queue_num, medicine_ticket_num = medicine_queue_num + 1, medicine_ticket_num + 1

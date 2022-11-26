# Define cosmetic site ticket generator
def cosmo_site():
    cosmo_queue_num = 1
    cosmo_ticket_num = 0
    while True:
        yield cosmo_queue_num
        cosmo_queue_num, cosmo_ticket_num = cosmo_queue_num + 1, cosmo_ticket_num + 1

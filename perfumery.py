# Define perfumes site ticket generator
def perfumes_site():
    perfume_queue_num = 1
    perfume_ticket_num = 0
    while True:
        yield perfume_queue_num
        perfume_queue_num, perfume_ticket_num = perfume_queue_num + 1, perfume_ticket_num + 1

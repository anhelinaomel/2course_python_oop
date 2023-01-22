# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price. There are four types
# of tickets: regular ticket, advance ticket (purchased 60 or more days before the event), late ticket (purchased fewer
# than 10 days before the event) and student ticket. Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.

from random import randint
from datetime import date

class Event:
    def __init__(self, event_name = "", date = None, time = None):
        self.event_name = event_name
        self.event_date = date
        self.event_time = time
        self.tickets_set = set()

    def ticket_add(self, ticket):
        self.tickets_set.add(ticket)
    
    def print_event_tickets(self):
        for ticket in self.tickets_set:
            ticket.print_ticket()

class Ticket:
    price = 150
    def __init__(self, buyer_name = "", buyer_surname = ""):
        self.buyer_name = buyer_name
        self.buyer_surname = buyer_surname

    def set_name(self, name = "", surname = ""):
        self.buyer_name = name
        self.buyer_surname = surname

    def get_price(self):
        return self.price * self.coeff

    def number(self):
        if self.number_ != 0:
            return str(self.num_base) + str(self.number_)
        else:
            while True:
                n = randint(1000, 9999)
                if not n in self.numbers:
                    break
            self.numbers.append(n)
            self.number_ = n
            return str(self.num_base) + str(self.number_)

    def number_remove(self):
        self.numbers.remove(self.number_)

    def print_ticket(self):
        print("---------------------------------")
        print(f'TICKET #{self.number()}')
        print(f'VISITOR NAME: {self.buyer_name} {self.buyer_surname}\nPRICE: {self.get_price()}')
        print("---------------------------------")

class RegularTicket(Ticket):
    def __init__(self, number=0):
        self.coeff = 1
        self.num_base = 101
        self.numbers = []
        self.name = 'Regular'
        self.number_ = number

class StudentTicket(Ticket):
    def __init__(self, number=0):
        self.coeff = 0.5
        self.num_base = 102
        self.numbers = []
        self.name = 'Student'
        self.number_ = number

class AdvanceTicket(Ticket):
    def __init__(self, number=0):
        self.coeff = 0.6
        self.num_base = 103
        self.numbers = []
        self.name = 'Advance'
        self.number_ = number

class LateTicket(Ticket):
    def __init__(self, number=0):
        self.coeff = 1.1
        self.num_base = 104
        self.numbers = []
        self.name = 'Late'
        self.number_ = number

events = []
Tech_Talent_Day = Event("Tech Talent Day", date(2023, 3, 1), "11:00")
Innovative_Products = Event("Innovations", date(2023, 4, 17), "19:00")
Ai = Event("Artificial Intelligence Startups", date(2023, 4, 23), "20:00")
Career_Fair = Event("Career fair", date(2023, 5, 13), "13:00")

events.append(Tech_Talent_Day)
events.append(Innovative_Products)
events.append(Ai)
events.append(Career_Fair)

while True:
    answer = input("""\nEnter:
    1 - to buy a new ticket
    2 - to see your current tickets
    3 - to quit\n""")
    if answer == "1":
        print("Current events:\n")
        i = 1
        for ev in events:
            print(f'{i}.', ev.event_date, ev.event_name)
            i += 1
        chosen_event = input("Enter the number of event to buy ticket: ")
        if int(chosen_event) > len(events):
            print("Input error!")
        else:
            ticket = None
            stdnt_ticket = input("Student ticket? yes/no\n")
            if stdnt_ticket == "yes":
                ticket = StudentTicket()
            elif stdnt_ticket == "no":
                today = date.today()
                diff_dates = abs(events[int(chosen_event)-1].event_date-today).days
                if diff_dates < 10:
                    ticket = LateTicket()
                elif diff_dates < 60:
                    ticket = RegularTicket()
                elif diff_dates > 60:
                    ticket = AdvanceTicket()
                else:
                    print("Can't buy ticket for this event.")
                    continue
            else:
                print("Wrong input!")
                continue
            name = input("Enter first name: ")
            surname = input("Enter last name: ")
            ticket.set_name(name, surname)
            ticket.print_ticket()
            buying = input("Confirm buying a ticket: yes/no\n")
            if buying == "yes":
                events[int(chosen_event)-1].ticket_add(ticket)
            else:
                ticket.number_remove()
    elif answer == "2":
        i = 1
        for ev in events:
            print(f'{i}.', ev.event_date, ev.event_name)
            ev.print_event_tickets()
            i += 1
    elif answer == "3":
        break
    else:
        print("Input error!")
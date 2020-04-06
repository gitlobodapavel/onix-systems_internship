import datetime
import random
import string


def number_in_list(number, list_of_nums):
    counter = 0

    while counter < list_of_nums.__len__():
        if list_of_nums[counter] == number:
            return True
        counter = counter + 1

    return False


def get_random_divisors(start_number=100, end_number=999, divisor=5, number_of_divisors=3):
    divisors_list = []

    while divisors_list.__len__() < number_of_divisors:
        current_random = random.randrange(start_number, end_number)
        if current_random % divisor == 0:
            if not number_in_list(current_random, divisors_list):
                divisors_list.append(current_random)

    return divisors_list


def generate_ticket():
    return random.randint(1000000000, 1999999999)


def get_tickets(num=100):
    tickets = []

    for i in range(num):
        current_ticket = generate_ticket()

        if not number_in_list(current_ticket, tickets):
            tickets.append(current_ticket)
    return tickets


def choose_winners(num, list_of_tickets):
    winners_list = []
    while winners_list.__len__() < num:
        current_winner = random.choice(list_of_tickets)
        if not number_in_list(current_winner, winners_list):
            winners_list.append(current_winner)
    return winners_list


def get_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def divide(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "[ Warning ]: Cant divide by 0"
    finally:
        pass


if __name__ == "__main__":

    """Datetime module"""

    # getting current date and time from datetime module
    current_datetime = datetime.datetime.now()
    print("[ Log ]: Current date and time is --> " + str(current_datetime))

    # adding one day to current datetime obj
    day_delta = datetime.timedelta(days=1)
    new_datetime = current_datetime + day_delta
    print("[ Log ]: Current datetime + 1 day is --> " + str(new_datetime))

    # converting datetime obj to string
    new_datetime = new_datetime.strftime('%d-%m-%Y %H:%S')
    print("[ Log ]: String converted from datetime obj --> " + new_datetime + " and has type " + str(type(new_datetime)))

    # converting string to datetime obj
    date_time_str = '2020-02-03 09:18:36.000'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    print("[ Log ]: Datetime obj from string --> " + str(date_time_obj))

    # getting data from datetime

    day = date_time_obj.strftime("%d")
    month = date_time_obj.strftime("%m")
    year = date_time_obj.strftime("%Y")
    hours = date_time_obj.strftime("%H")
    seconds = date_time_obj.strftime("%S")

    print("[ Log ]: Data from datetime object: \n")

    print("DAY --> " + day)
    print("MONTH -- > " + month)
    print("YEAR --> " + year)
    print("HOURS -->  " + hours)
    print("SECONDS --> " + seconds)

    """Random module"""

    # generating 3 random divisors in range

    print("\nDivisors:\n")

    print(get_random_divisors(100, 999, 5, 3))

    # random string

    print("\nRandom string: \n")

    print(get_random_string(10))

    # lottery

    print("\nLottery:\n")

    tickets = get_tickets(100)
    print("[ Log ]: Tickets generated: " + str(tickets))
    print("[ Log ]: Winners chosen: " + str(choose_winners(2, tickets)))

    """Try / Expect / Finally"""

    print("\n" + str(divide(3, 0)))

else:
    print("[ Warning ]: Run " + __name__ + " as script (NOT MODULE) !")

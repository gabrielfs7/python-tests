import time
from datetime import datetime

hosts = "/etc/hosts"

forbidden_addresses = [
    'www.facebook.com',
    'facebook.com',
    'youtube.com',
    'www.youtube.com',
    'mail.google.com'
]


def is_current_time_between(start_hour, start_min, end_hour, end_min):
    """ Check current time within the provided range """
    now = datetime.now()
    start = datetime(year=now.year, month=now.month, day=now.day, hour=start_hour, minute=start_min, second=0)
    end = datetime(year=now.year, month=now.month, day=now.day, hour=end_hour, minute=end_min, second=59)

    return now >= start and now <= end


def is_address_blocked(file_content, address):
    """ Verify if site was already blocked """
    if address in file_content:
        return True
    return False


def unblock_addresses(hosts_file_path, forbidden_addresses):
    """ Clear forbidden addresses """
    with open(hosts_file_path, "r+") as hosts_file:
        lines = hosts_file.readlines()

        hosts_file.seek(0)

        for line in lines:
            if not any(forbidden_address in line for forbidden_address in forbidden_addresses):
                hosts_file.write(line)

        hosts_file.truncate()  # Clear everything was written before


def block_address(hosts_file_path, forbidden_addresses):
    """ Deny or release access for sites """
    with open(hosts_file_path, "r+") as hosts_file:
        file_content = hosts_file.read()

        for forbidden_address in forbidden_addresses:
            if not is_address_blocked(file_content, forbidden_address):
                hosts_file.write("127.0.0.1 " + str(forbidden_address) + "\n")


while True:
    is_fun_time = not is_current_time_between(9, 0, 19, 0)

    if is_fun_time:
        unblock_addresses(hosts, forbidden_addresses)

        print("You can have fun! :)")

    if not is_fun_time:
        block_address(hosts, forbidden_addresses)

        print("You should be working... :(")

    time.sleep(1)
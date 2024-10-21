from faker import Faker

fake = Faker()


def generate_random_name():
    return fake.name()


def generate_random_email():
    return fake.email()


def generate_random_password():
    return fake.password()

from faker import Faker

fake = Faker()


def email_generator():
    email_fake = fake.email()
    return email_fake


email = email_generator()
print(email)

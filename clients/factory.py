from fake import Faker

def create_fake_client():
    fake = Faker()
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "cpf": fake.cpf()
    }
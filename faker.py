import hashlib
from faker import Faker

fake = Faker()

def consistent_fake(val, field):
    seed = int(hashlib.sha256(str(val).encode()).hexdigest(), 16) % (10 ** 9)
    Faker.seed(seed)
    fake = Faker()
    if field == 'name':
        return fake.name()
    elif field == 'email':
        return fake.email()
    elif field == 'phone':
        return fake.phone_number()
    
df['fullname'] = df['fullname'].apply(lambda x: consistent_fake(x, 'name'))
df['email'] = df['email'].apply(lambda x: consistent_fake(x, 'email'))
df['phone'] = df['phone'].apply(lambda x: consistent_fake(x, 'phone'))

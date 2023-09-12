from faker import Faker

fake = Faker()


def fake_names(n, lastname=False):
    for _ in range(n):
        name, surname = fake.name().split()
        if lastname:
            print(f"('{name}', '{surname}'),")
        else:
            print(f"('{name}'),")


def fake_addresses(n):
    ids = set()
    while len(ids) != n:
        ids.add(fake.pyint(1, 20))
    iter_ids = iter(ids)
    for _ in range(n):
        print(f"({next(iter_ids)}, '{fake.city()}', '{fake.country()}'),")


fake_names(5)
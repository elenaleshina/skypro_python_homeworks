from Address import Address
from Mailing import Mailing

to_address = Address("636785", "Красноярск", "Алексеева", "33", "65")
from_address = Address("678910", "Томск", "Мира", "26", "77")
mailing = Mailing(to_address, from_address, 7000, "FAS123")

print(f" Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}"
      f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}"
      f" {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")

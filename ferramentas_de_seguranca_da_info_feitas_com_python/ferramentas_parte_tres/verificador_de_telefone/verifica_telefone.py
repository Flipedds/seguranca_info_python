import phonenumbers

from phonenumbers import geocoder, timezone

telefone = input('digite o número de telefone no formato: +551140028922: ')

numero_telefone = phonenumbers.parse(telefone)

# mostra o estado do número de telefone
print(geocoder.description_for_number(numero_telefone, 'pt'))
# mostra a zona de hora do número
print(timezone.time_zones_for_number(numero_telefone))

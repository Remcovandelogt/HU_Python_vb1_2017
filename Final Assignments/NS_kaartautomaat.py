stations = ['Schagen', 'Heerhugowaard', 'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation=input('vul hier je beginstation in: ')
eindstation=input('vul hier je eindstation in: ')
if beginstation and eindstation in stations:
    print('stations komen voor')
    print('jou station beginstation bevindt zich in rang {} in het traject en je eindstation in rang {} '.format(stations[beginstation],stations[eindstation]))
else:
    beginstation = input('vul hier je beginstation in: ')
    eindstation = input('vul hier je eindstation in: ')

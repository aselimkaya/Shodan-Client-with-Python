#!/usr/bin/python3
import shodan

SHODAN_API_KEY = "enter_shodan_api_key_here"

api = shodan.Shodan(SHODAN_API_KEY)

# Search Shodan
results = api.search('product:MySQL country:TR', page=100)

# Show the results
print('Results found: {}'.format(results['total']))
print('Matches length: {}'.format(len(results['matches'])))

for result in results['matches']:
    print('IP: {}'.format(result['ip_str']))
    print(result['data'])
    print('')
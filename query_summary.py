#!/usr/bin/python3

import shodan
import sys

# Configuration
API_KEY = "enter_shodan_api_key_here"

# The list of properties we want summary information on
FACETS = [
    'org',
    'domain',
    'port',
    'asn',
]

FACET_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'asn': 'Top 5 Autonomous Systems',
}

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)
    query = 'product:MongoDB country:TR'
    result = api.count(query, facets=FACETS)

    print('Shodan Summary Information')
    print('Query: %s' % query)
    print('Total Results: %s\n' % result['total'])

    # Print the summary info from the facets
    for facet in result['facets']:
        print(FACET_TITLES[facet])

        for term in result['facets'][facet]:
            print('%s: %s' % (term['value'], term['count']))
        print('')
except Exception as e:
        print('Error: %s' % e)
        sys.exit(1)

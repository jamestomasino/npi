"""Script to gather NPI data."""
import sys
import urllib.request
import json
from hcp import hcp

API_URL = "https://npiregistry.cms.hhs.gov/api/?number="

def main():
    """Main entry point for the script."""
    try:
        npi = sys.argv[1]
    except:
        npi = ""
    data = get_npi_data(npi)
    if not check_error(data):
        doc = hcp(data)
        print (doc.get_first_name())
        print (doc.get_last_name())
        print (doc.is_active())
        print (doc.last_updated())
        print (doc.get_addresses())
    else:
        print ("No record found for NPI")

def check_error(data):
    if "Errors" in data:
        return True
    else:
        return False

def get_npi_data(npi):
    with urllib.request.urlopen(API_URL + npi) as url:
        data = json.loads(url.read().decode())
    return data

if __name__ == '__main__':
    sys.exit(main())

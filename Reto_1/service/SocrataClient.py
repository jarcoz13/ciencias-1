from sodapy import Socrata

class SocrataClient:

    def __init__(self):
        self.client = Socrata("www.datos.gov.co", None)


    def getDataset(self):
        # Unauthenticated client only works with public data sets. Note 'None'
        # in place of application token, and no username or password:

        # Example authenticated client (needed for non-public datasets):


        # First 2000 results, returned as JSON from API / converted to Python list of
        # dictionaries# client = Socrata(www.datos.gov.co,
        #         #                  MyAppToken,
        #         #                  userame="user@example.com",
        #         #                  password="AFakePassword") by sodapy.
        results = self.client.get("gt2j-8ykr", limit=1000)
        return results
import requests

class PostCode():

    def __init__(self, postcode):
        self.postcode = postcode

        def getPostcodeInfo(postcode):
            post_code_req = requests.get(
                f"http://api.postcodes.io/postcodes/{postcode}")
            self.postcodeDict = (post_code_req.json()['result'])
            result = self.postcodeDict
            return result

        self.postcodeDict = getPostcodeInfo(self.postcode)






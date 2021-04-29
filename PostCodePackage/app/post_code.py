import requests


class PostCode:

    def __init__(self, postcode):
        self.result = self.get_post_code_info(postcode)
        
    def get_post_code_info(self, postcode):
        post_code_req = requests.get(
          f"http://api.postcodes.io/postcodes/{postcode}")
        post_code_dict = (post_code_req.json()['result'])
        result = post_code_dict
        return result
    
    def country(self):
        nation = self.result['country']
        return nation
      
    def admin_district(self):
        district = self.result['admin_district']
        return district
      
    def admin_ward(self):
        ward = self.result['admin_ward']
        return ward
      
    def region(self):
        reg = self.result['region']
        return reg
      
    def post_code(self):
        postcode = self.result['postcode']
        return postcode

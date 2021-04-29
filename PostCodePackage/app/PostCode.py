class PostCode:
    #def __init__(self,post_code_req):
        #self.p=post_code_req
       # self.result=self.p['result']
    def country(self):
        nation=self.result['country']
        return nation
    def admin_district(self):
        district=self.result['admin_district']
        return district
    def admin_ward(self):
        ward=self.result['admin_ward']
        return ward
    def region(self):
        reg=self.result['region']
        return reg
    def post_code(self):
        postcode=self.result['postcode']
        return postcode
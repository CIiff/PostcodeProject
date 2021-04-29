from PostCodePackage.app.post_code import PostCode
import configparser

# Read local `config.ini` file.
config = configparser.ConfigParser()
config.read('config.ini')

post_code = config.get('INPUT', 'POSTCODE')
post_code_data = PostCode(post_code)

print("Country: "+post_code_data.country())
print("Admin District: "+post_code_data.admin_district())
print("Admin Ward: "+post_code_data.admin_ward())
print("Region: "+post_code_data.region())
print("Post Code: "+post_code_data.post_code())

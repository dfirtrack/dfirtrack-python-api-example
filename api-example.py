from pprint import pprint
import time
import dfirtrackapi_client
from dfirtrackapi_client.api import api_api
from dfirtrackapi_client.model.tag import Tag
from dfirtrackapi_client.model.tagcolor import Tagcolor


# here we can setup the configuration for the api client 
configuration = dfirtrackapi_client.Configuration()
configuration.host = "http://localhost"
# configuration.username = "admin"
# configuration.password = "forensics"
configuration.access_token = "f692c7e4b71a6dd38be6f742fc9276daa35c70df"
# This needs to be set if you're working with a self-signed certs
# Please do only use this in dev environment!!!
configuration.verify_ssl = False
# configuration.api_key_prefix = {'Bearer': 'Token'}

client = dfirtrackapi_client.ApiClient(configuration=configuration)
api_instance = api_api.ApiApi(client)
try:
    tc = api_instance.list_tagcolors()
    tmp = tc[3]
    test = tmp['tagcolor_id']
    pprint(tmp['tagcolor_id'])
    pprint(tc)
    
    t = Tag(
        tag_name="firs-bearer-api-6",
        tagcolor=test,
    )

    pprint(t)
    temp2=t
    pprint(type(t))
    r = api_instance.create_tag(tag=t)
    pprint(r)
    # r = api_instance.create_auth_token("admin", 'forensics')
    # r = api_instance.list_systemstatus()
except dfirtrackapi_client.ApiException as e:
    print(e)

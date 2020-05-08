from defines import makeApiCalls, getCreds

def getUserPages(params):
    endpointPar=dict()
    endpointPar['access_token']=params['access_token']

    url=params['endpoint_base']+'me/accounts'
    return makeApiCalls(url,endpointPar,params['debug'])

params=getCreds()
params['debug']='yes'
response=getUserPages(params)

print ("\n---- FACEBOOK PAGE INFO ----\n") # section heading
print ("Page Name:") # label
print (response['json_data']['data'][0]['name']) # display name
print ("\nPage Category:") # label
print (response['json_data']['data'][0]['category']) # display category
print ("\nPage Id:") # label
print (response['json_data']['data'][0]['id']) # display id

print(response['json_data'].keys())
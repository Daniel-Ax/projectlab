from defines import getCreds,makeApiCalls
import datetime

def debugAccessToken(params):
    endpointParams=dict()
    endpointParams['input_token']=params['access_token']
    endpointParams['access_token']=params['access_token']

    url=params['graph_domain']+'/debug_token'

    return makeApiCalls(url,endpointParams,params['debug'])


params=getCreds()
params['debug']='yes'
response=debugAccessToken(params)
# print("\nExpires at: ")
# print (datetime.datetime.fromtimestamp( response['json_data']['data']['data_access_expires_at'] ))
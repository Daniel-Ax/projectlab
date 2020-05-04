import requests
import json

def getCreds():
    creds=dict()
    creds['access_token']='EAAL1IUfKDNUBAFKOjaE6sDx9ae5ZAuJz3r7spKZBaxJsEXyAjO9d8SIadEwMb5XJd6lpGwauwWnxWKJhxoZABfN5oKawgUiy' \
                          'WSO3lbomcYRWytuunQIb1WpZASAGmFJie2eRPW95MbcGUiUM1AP1UA1AIl9DAblKooLrjsUDQ0Qnh8iMYl3RVFQssn1ZCHU0XSe7gGMd807IDdYW1UUlQtLfC8GJx4ZBcZD'
    creds['client_id']='832473240571093'
    creds['client_secret']='3b4b20b769d9b96e047fa7734ba9646c'
    creds['graph_domain']='https://graph.facebook.com/'
    creds['graph_version']='v6.0'
    creds['endpoint_base']=creds['graph_domain']+creds['graph_version']+'/'
    creds['debug']='no'

    return creds

def makeApiCalls(url,endpointPar,debug='no'):
    data=requests.get(url,endpointPar)

    response=dict()
    response['url']=url
    response['enpoint_params']=endpointPar
    response['endpoint_params_pretty']=json.dump(endpointPar,indent=4)
    response['json_data']=json.loads(data.content)
    response['json_data_pretty'] = json.dump(response['json_data'], indent=4)

    if('yes'==debug):
        displayApiData(response)


def displayApiData(response):
    print ("\nURL: ")
    print (response['url']   )
    print("\nEndpoint Params: ")
    print(response['endpoint_params_pretty'])
    print("\nResponse: ")
    print(response['json_data_pretty'])
from defines import getCreds, makeApiCalls

def getLongLivedAccess(params):
    """ Get long lived access token

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['grant_type'] = 'fb_exchange_token'  # tell facebook we want to exchange token
    endpointParams['client_id'] = params['client_id']  # client id from facebook app
    endpointParams['client_secret'] = params['client_secret']  # client secret from facebook app
    endpointParams['fb_exchange_token'] = params['access_token']  # access token to get exchange for a long lived token

    url = params['endpoint_base'] + 'oauth/access_token'  # endpoint url
    return makeApiCalls(url, endpointParams, params['debug'])  # make the api call


params = getCreds()  # get creds
params['debug'] = 'yes'  # set debug
response = getLongLivedAccess(params)

import os, requests, uuid, json,Sub_Key,endP

def init_key(sub_key):
    key_var_name = sub_key
    if not key_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
    subscription_key = os.environ[key_var_name]
    return subscription_key

def init_endpoint(endpoint):
    endpoint_var_name = endpoint
    if not endpoint_var_name in os.environ:
        raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
    endpoint = os.environ[endpoint_var_name]
    return endpoint

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-dictionary-lookup
if __name__ == "__main__":
    path = '/dictionary/lookup?api-version=3.0'
    params = '&from=hu&to=es';
    constructed_url = init_endpoint(endP.endpoint) + path + params
    print(constructed_url)
    headers = {
        'Ocp-Apim-Subscription-Key': init_key(Sub_Key.key),
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': '에서 파티를 취소했다고요. 제가 이제 여기 이제 왕자가 형이라고 얘기를 할 겸 워낙 친해서 문자를 나누다가 너무 잘 하고 있으니까 제가 아휴 시간도 안 먹고 이러고 있는데 베이커가 나온다고 있기 때문에 오늘이 크리스마스거든요. 25일 맞아요.\n다 취소하고 바로 나왔죠. 안녕하세요. 오랜만에 뵙습니다. 먼저.안녕하세요.이 게임은 진짜로 리빙 레전드예요 잠긴다. 일처리도 조직을 놓고 진짜 이 분은 최고로 어느 정도 이제 개그맨의 꿈을 가진 친구들이 이국진영을 바라보듯이. 저는. 그. 이후에 최고의 풋풋했던. 나이가 드신 게 옛날 같으면 가만인데 제발 가만있을 만한 결혼생활에 너무 행복해.선수가 손흥민 선수라 해서 함께 한국을 알리는으로도.'
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))
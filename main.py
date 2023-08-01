import requests
import json
 
class Claude:
  def __init__(self,org_uuid,con_uuid,cookie):
    self.org_uuid = org_uuid
    self.con_uuid = con_uuid
    self.cookie = cookie
  def send_message(self, query):
    url = "https://claude.ai/api/append_message"
    payload = json.dumps({
      "completion": {
        "prompt": query,
        "timezone": "Asia/Singapore",
        "model": "claude-2",
        "incremental": True
      },
      "organization_uuid": self.org_uuid,
      "conversation_uuid": self.con_uuid,
      "text": query,
      "attachments": []
    })
    headers = {
      'Accept': 'text/event-stream, text/event-stream',
      'Accept-language': 'zh-CN,zh',
      'Content-type': 'application/json',
      'Cookie': self.cookie,
      'Origin': 'https://claude.ai',
      'DNT': '1',
      'Connection': 'keep-alive',
      'Referer': 'https://claude.ai/chat/ecc769bc-427b-466b-843c-1b7bf9b44295',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
      'TE': 'trailers'
    }
 
    try:
      response = requests.request("POST", url, headers=headers, data=payload,stream = True)
    except Exception as error:
      print(error)
      return False
 
    if len(response.text) >=60:
      return True
    return False
  def chat_conversation_history(self):
    url = f"https://claude.ai/api/organizations/{self.org_uuid}/chat_conversations/{self.con_uuid}"
 
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Accept-Encoding":"gzip, deflate, br",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Referer': 'https://claude.ai/chats',
        'Content-Type': 'application/json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',
        'Cookie': f'{self.cookie}'
    }
 
    response = requests.request("GET", url, headers=headers)
 
    print(type(response))
    response.encoding = 'utf-8'
    # List all the conversations in JSON
    return response.json()
if __name__ == '__main__':
    org_uuid= 填写你的orguuid
    con_uuid= 填写你的con uuid
    cookie = 填写cookie
 
    claude = Claude(org_uuid, con_uuid,cookie)
    while True:
      query = input("human:")
      result = claude.send_message(query)
      if result:
        print("send success")
      else:
        continue
 
      history = claude.chat_conversation_history()
      print(history["chat_messages"][-1]["text"])

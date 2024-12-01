import requests

class ChatService:

    def __init__(self, model):
        self.model = model
    
    def askOllama(self, promptMessage): 

        url = "http://localhost:11434/api/chat"
        ##Payload may have to be adjusted for more complex models than just text
        ##Ref model docs for payload
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": promptMessage}],
            "stream" : False
        }
        headers = {"Content-Type": "application/json"}

        try:
            APIresponse = requests.post(url, json=payload, headers=headers)
            
            if APIresponse.status_code == 200:
                res = APIresponse.json()
                return res["message"]["content"]
            else:
                return f"Error: Received unexpected status code {APIresponse.status_code}"
        
        except Exception as e:
            return f"An error occurred: {e}"


    def chatInteraction(self):
        while True:
            userPrompt = input("Ask Away: ")

            if userPrompt.lower() != "/bye":
                print("Humm..")
                ollamaResponse = self.askOllama(promptMessage=userPrompt)
                print(ollamaResponse)
            else:
                break


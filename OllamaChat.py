import requests


class ChatService:

    def __init__(self, model):
        self.model = model

    def askOllama(self, promptMessage):

        url = "http://localhost:11434/api/chat"
        visionModels = ["llama3.2-vision:11b"]
        payload = {}
        headers = {"Content-Type": "application/json"}

        if self.model not in visionModels:
            payload = {
                "model": self.model,
                "messages": [{"role": "user", "content": promptMessage}],
                "stream": False,
            }

        else:
            payload = {
                "model": self.model,
                "messages": [{"role": "user", "content": promptMessage}],
                "stream": False,
                "images": [
                    "TestImages\\testImg1.jpg"
                ],  ##maybe take an option imgs arg for askOllama????
            }

        try:
            APIresponse = requests.post(url, json=payload, headers=headers)

            if APIresponse.status_code == 200:
                res = APIresponse.json()
                return res["message"]["content"]
            else:
                return (
                    f"Error: Received unexpected status code {APIresponse.status_code}"
                )

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


if __name__ == "__main__":
    chat = ChatService("llama3.1:latest ")

    chatting = True
    while chatting:

        prompt = input("Ask way...")

        if prompt == "/bye":
            chatting = False
        else:
            res = chat.askOllama(promptMessage=prompt)
            print(res)

    quit()

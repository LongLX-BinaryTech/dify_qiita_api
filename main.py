from fastapi import FastAPI, Header, HTTPException
import requests

app = FastAPI()

@app.get("/check_qiita_user")
def check_qiita_user(authorization: str = Header(...)):
    headers = {
        "Authorization": authorization,
    }
    response = requests.get("https://qiita.com/api/v2/authenticated_user", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

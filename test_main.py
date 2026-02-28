from fastapi.testclient import TestClient
from main import app
client = TestClient(app)



def test_main():
    response = client.post("/",json={"city":"istanbul"})
    assert response.status_code == 200
    assert response.json()["outfit_advice"] != None
import requests as req

parameters = {
    "amount" : 10 ,
    "category" : 21 ,
    "type" : "boolean",
}
api = "https://opentdb.com/api.php"
resp = req.get(api, params=parameters)
question_data = resp.json()["results"]
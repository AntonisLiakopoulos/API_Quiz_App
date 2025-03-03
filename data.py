import requests


def get_data(num,dif):
    parameters = {
        "amount":num,
        "type":"boolean",
        "difficulty":dif
    }

    response = requests.get(f"https://opentdb.com/api.php?amount={num}&difficulty={dif}&type=boolean",params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data= data["results"]
    return question_data

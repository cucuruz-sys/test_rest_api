import requests

# 1
url = "http://127.0.0.1:8000/process_text/"
input_text = "FastAPI is an amazing framework for building APIs quickly and easily!"

response = requests.post(url, json={"text": input_text})

if response.status_code == 200:
    print("Processed text:", response.json()["processed_text"])
else:
    print("Error:", response.status_code, response.text)


# 2
url_search = "http://127.0.0.1:8000/search_text/"
search_query = "text similarity using TF-IDF"

response = requests.post(url_search, json={"text": search_query})

if response.status_code == 200:
    print("Top search results:")
    for result in response.json()["top_results"]:
        print(f"Text: {result['text']}, Score: {result['score']:.2f}")
else:
    print("Error:", response.status_code, response.text)

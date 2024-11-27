import json
from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

with open("text_database.json", "r", encoding="utf-8") as f:
    text_database = json.load(f)["texts"]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(text_database)


class TextRequest(BaseModel):
    text: str


@app.post("/process_text/")
def process_text(request: TextRequest):
    doc = nlp(request.text)

    processed_tokens = [
        token.lemma_.lower() for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return {"processed_text": processed_tokens}


@app.post("/search_text/")
def search_text(request: TextRequest):
    query = request.text
    query_vector = tfidf_vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[-3:][::-1]
    results = [{"text": text_database[idx], "score": cosine_similarities[idx]} for idx in top_indices]
    return {"top_results": results}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

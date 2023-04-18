from fastapi import FastAPI, Request
import openai

openai.api_key = "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"

async def generate_answer(question):
    "Generate using Gpt3"
    completions = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = question,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return completions.choices[0].text

app = FastAPI()

@app.post("/get_sentiment")
async def return_sentiment(request: Request):
    data = await request.json()
    template = f"""Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: "{data['text']}"
Sentiment:"""
    answer = await generate_answer(template)
    return {"Result" : answer}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("WaleeSentimentAnalyzer:app", reload=True)
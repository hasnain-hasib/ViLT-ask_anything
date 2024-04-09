# ViltQA-FastAPI

This is a FastAPI-based web application that uses the VILT (Vision-and-Language Transformer) model for question-answering on images.

## Features

- Provides an API endpoint `/ask` to accept a question and an image, and returns the answer to the question.
- Uses the pre-trained `ViltForQuestionAnswering` model from the Transformers library.
- Serves a simple HTML-based frontend for interacting with the API.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ViltQA-FastAPI.git
   ```

2. Change to the project directory:
   ```
   cd ViltQA-FastAPI
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

2. Open your web browser and visit `http://localhost:8000`. You should see the frontend interface.

3. Enter a question and upload an image, then click the "Ask" button to get the answer.

## API Endpoint

The `/ask` endpoint accepts a `POST` request with the following parameters:

- `question`: The question to be answered.
- `image`: The image file to be used for the question-answering task.

The response will be a JSON object with the following structure:

```json
{
  "answer": "The answer to the question."
}
```

## Dependencies

- FastAPI
- Pillow
- Transformers
- Starlette

## License

This project is licensed under the [MIT License](LICENSE).

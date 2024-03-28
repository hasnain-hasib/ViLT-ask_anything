# ViLT-ask_anything



# FastAPI Question Answering App

This is a simple FastAPI application that allows users to ask questions and get answers based on an uploaded image. The application uses the VILT (Vision and Language Transformer) model for question answering.

## Requirements

Make sure you have Python installed on your system. You can install it from [python.org](https://www.python.org/).

To install the required Python packages, run:


## Usage

1. Clone this repository:


2. Install the required dependencies using the command mentioned in the Requirements section.

3. Run the FastAPI server:


4. Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the application.

5. You will be presented with a form where you can enter a question and upload an image. Click on the "Get Answer" button to submit the form.

## Endpoints

- `/`: The home page of the application. It serves the HTML form for asking questions and uploading images.
- `/ask`: This endpoint handles the form submission. It accepts a question and an image file, processes them using the VILT model, and returns the answer.

## File Structure

- `main.py`: Contains the FastAPI application code.
- `requirements.txt`: Lists all the Python packages required by the application.
- `static/`: Directory containing static files, including the HTML template for the user interface.

## Credits

- FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Hugging Face Transformers: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
- PyTorch: [https://pytorch.org/](https://pytorch.org/)
- Uvicorn: [https://www.uvicorn.org/](https://www.uvicorn.org/)

## License

This project is licensed under the [MIT License](LICENSE).

To run the FastAPI app with Uvicorn, we need to use the nbconvert tool from the Jupyter Notebook project. This tool can convert your Jupyter Notebook into a Python script that Uvicorn can understand.
First, install nbconvert if you haven't already:


Copy code
pip install nbconvert
Then, convert your Jupyter Notebook to a Python script:


Copy code
jupyter nbconvert --to script main.ipynb
This will create a new file called main.py in the same directory as your notebook.

Finally, you can run the converted Python script with Uvicorn:

Copy code
uvicorn main:app --reload
Note that when using --reload, Uvicorn will monitor the main.py file for changes and automatically reload the server. However, if you make changes to the original main.ipynb file, you'll need to convert it to main.py again before the changes take effect.



# AI Website Summarize and Tweet Generator
This project utilizes OpenAI's GPT-3.5 Turbo model and DALL-E-2 to generate professional-sounding tweets for Twitter based on a provided website. The generated tweets are accompanied by images created by the DALL-E-2 model. The entire process is orchestrated through a Flask-based RESTful API.

Prerequisites
Before running the project, make sure you have the necessary dependencies installed. You can install them using the following:

bash
Copy code
pip install openai flask requests tweepy
Additionally, create a .env file in the project directory and add the required API keys:

makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
X_API_KEY=your_twitter_api_key
X_API_SECRET_KEY=your_twitter_api_secret_key
X_ACCESS_TOKEN=your_twitter_access_token
X_ACCESS_TOKEN_SECRET_KEY=your_twitter_access_token_secret
Getting Started
Run the Flask server:
bash
Copy code
python Flask_Server.py
The server will be hosted at http://127.0.0.1:5000/.

Make a GET request to the /tweets endpoint with the desired website service:
bash
Copy code
curl http://127.0.0.1:5000/tweets?service=sagemaker
Replace sagemaker with the desired service.

API Endpoints
/tweets (GET)
Parameters:
service: The name of the website service to summarize.
This endpoint triggers the process of generating a tweet and image based on the provided website service. The resulting tweet and image are then posted on Twitter.

Notes
Ensure that your Twitter API keys are correctly set in the .env file.
The OpenAI GPT-3.5 Turbo model is used for generating tweet summaries, while the DALL-E-2 model is used for creating images.
The Flask server handles communication between the client and OpenAI API.
For troubleshooting, check the console output for detailed information.

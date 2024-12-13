# Customer Supportbot Chatbot
This is a Flask-based chatbot designed to assist customers using the Bitext Sample Pre-built Customer Support Dataset for English. The chatbot uses a fine-tuned transformer model to classify user intents and provide predefined responses.

## Features:
1. **Intent Recognition:** Identifies user intents based on natural language queries.
2. **Predefined Responses:** Returns relevant answers based on the detected intent. 
3.**Logging:** Logs user queries, predicted intents, and confidence scores for analysis.
4. **Feedback Systems:** Allows users to provide feedback to improve the chatbot.

## Technologies Used:
-**Flask:** Backend framework for handling requests and routing.
-**Transformers(Hugging Face):** For intent classification.
-**Torch:** Supporting framework for deep learning.
-**HTML/CSS/JavaScript:** Frontend design of the chatbot.

## How It Works:
-**User Query:** Users input a message via the frontend (HTML form).
-**Intent Classification:** The query is processed using the fine-tuned model to predict the intent.
-**Predefined Responses:** Based on the predicted intent, the chatbot returns a response from the responses.json file.
-**Feedback Logging:** Feedback provided by users is saved for further improvements.

## Future Enhancements:
-**Deployment:** Deploy the chatbot to a cloud platform.
-**Interactive Interface:** Improve the frontend UI for better user experience.
-**Dynamic Responses:** Generate more personalized responses using GPT-based models.
-**Multilingual Support:** Extend support for multiple languages.

## Acknowledgments:
-**Bitext Sample Dataset:** Used as the training dataset for intent classification.
-**Hugging Face Transformers:** Powering the intent recognition pipeline.

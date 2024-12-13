# Customer Supportbot Chatbot
This is a Flask-based chatbot designed to assist customers using the Bitext Sample Pre-built Customer Support Dataset for English. The chatbot uses a fine-tuned transformer model to classify user intents and provide predefined responses.

## Features:
1. **Intent Recognition:** Identifies user intents based on natural language queries.
2. **Predefined Responses:** Returns relevant answers based on the detected intent.
3. **Logging:** Logs user queries, predicted intents, and confidence scores for analysis.
4. **Feedback Systems:** Allows users to provide feedback to improve the chatbot.

## Technologies Used:
1. **Flask:** Backend framework for handling requests and routing.
2. **Transformers(Hugging Face):** For intent classification.
3. **Torch:** Supporting framework for deep learning.
4. **HTML/CSS/JavaScript:** Frontend design of the chatbot.

## How It Works:
1. **User Query:** Users input a message via the frontend (HTML form).
2. **Intent Classification:** The query is processed using the fine-tuned model to predict the intent.
3. **Predefined Responses:** Based on the predicted intent, the chatbot returns a response from the responses.json file.
4. **Feedback Logging:** Feedback provided by users is saved for further improvements.

## Future Enhancements:
1. **Deployment:** Deploy the chatbot to a cloud platform.
2. **Interactive Interface:** Improve the frontend UI for better user experience.
3. **Dynamic Responses:** Generate more personalized responses using GPT-based models.
4. **Multilingual Support:** Extend support for multiple languages.

## Acknowledgments:
1. **Bitext Sample Dataset:** Used as the training dataset for intent classification.
2. **Hugging Face Transformers:** Powering the intent recognition pipeline.

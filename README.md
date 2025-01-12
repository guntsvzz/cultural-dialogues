# Cultural Dialogues

This project synthetics a conversation from normbank settings. 

## Requirements
- Python 3.8+
- Required Python libraries:
  - `langchain`
  - `langchain-openai`
  - `dotenv`
  - `argparse`
  - `pydantic`
  
To install the required libraries, you can use the following command:
```bash
pip install -r requirements.txt
```

## Setup
1. **Azure OpenAI Setup:**
   - You need to have an Azure OpenAI account and obtain the API key, version, and endpoint.
   - Create a `.env` file in the project directory to store these values:

   Example `.env` file:

   ```
   AZURE_OPENAI_API_KEY=your_api_key_here
   OPENAI_API_VERSION=your_openai_api_version_here
   AZURE_OPENAI_ENDPOINT=your_azure_endpoint_here
   ```


## How to run
```bash
python3 main.py --country Germany --num_sample 10
```

## Contribution

Feel free to fork the repository, contribute, or open an issue for any bugs or improvements.

---

This `README.md` provides the necessary information for users to understand the project setup, running the simulation, and contributing to the project.
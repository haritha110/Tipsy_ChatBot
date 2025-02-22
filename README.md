# Tipsy Chatbot

This repository contains the code for a customer support ticket processing system. It uses asynchronous programming and incorporates agent-based architecture for ticket analysis and response generation.

![Screenshot 2025-02-22 at 6 50 28 AM](https://github.com/user-attachments/assets/3348286f-6c7e-4b42-8d71-81cb8c533c78)

## Table of Contents

- [Introduction](#introduction)
- [Setup Instructions](#setup-instructions)
- [Design Decisions](#design-decisions)
- [Testing Approach](#testing-approach)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Usage](#usage)


## Introduction

The Tipsy Chatbot is designed to automate the processing of customer support tickets. It analyzes ticket content, determines the appropriate category and priority, and generates a suitable response.  This system is built using Python and leverages asynchronous programming for efficient handling of multiple tickets.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone [https://github.com/haritha110/Tipsy_ChatBot.git]
   cd tipsy-chatbot

2. Create a virtual environment (recommended):

    ```bash
    python3 -m venv .venv  # Create a virtual environment
    source .venv/bin/activate  # Activate the environment (Linux/macOS)
    .venv\Scripts\activate  # Activate the environment (Windows)

  (Create requirements.txt by running pip freeze > requirements.txt after installing all the necessary packages.)

3. Install dependencies:

    ```bash
     pip install -r requirements.txt

4. Set up environment variables (if needed):

    Create a .env file in the project root and add any necessary environment variables.  For example:

       # .env file
        DATABASE_URL=your_database_url
        API_KEY=your_api_key

5. Configure Response Templates:

    The response templates are stored in `templates/response_templates.py`. You can modify these templates to customize the chatbot's responses.


## Design Decisions

- **Agent-based Architecture:** The system uses separate agents for ticket analysis and response generation. This modular design allows for easier maintenance and scalability.
- **Asynchronous Programming:** Asynchronous programming with `asyncio` is used to handle multiple tickets concurrently, improving performance.
- **Data Models:** Dataclasses (`@dataclass`) are used to define the structure of data objects like `SupportTicket`, `TicketAnalysis`, and `ResponseSuggestion`, promoting code clarity and reducing boilerplate.
- **Enum for Categories and Priority:** Enums (`Enum`) are used for defining ticket categories and priorities, improving code readability and preventing invalid values.
- **Template Engine**: The system uses string formatting (`.format()`) for response generation, making it easy to create and modify templates.

## Testing Approach
  The project currently uses basic print statements for testing and demonstration.  A more robust testing approach should be implemented using a testing framework like `pytest` and/or `unittest`. I used Pycharm tool and Python 3.11.
  
- **Unit Tests:** Unit tests should be written for each agent (`TicketAnalysisAgent`, `ResponseAgent`) to ensure they function correctly in isolation.  These tests should cover various scenarios, including edge cases and error handling.
- **Integration Tests:** Integration tests should verify the interaction between the different components of the system, particularly the `TicketProcessor`.  These tests should simulate real-world ticket processing scenarios.
- **Test Data:** Use a variety of test data, including valid and invalid tickets, to thoroughly test the system's behavior.

## Project Structure
```bash
tipsy-chatbot/
├── agents/
│   ├── agent_orchestration.py        #Orchestration agent and handle logics
│   ├── response_generation_agent.py  #Handle response generation
│   └── ticket_analysis_agent.py      #Handle ticket analysis
├── data_models.py                    #Enums for categories and priority
├── main.py                           #Entry point
├── requirements.txt                  #List of dependencies
├── templates/
│   └── response_templates.py         #Response templates
├── .env                              #.env file contains APIKey and localhost 
└── README.md                         #Documentation
```

## Dependencies

- Python 3.11
- `asyncio`
- `dataclasses`
- `enum`
- `typing`
- `python-dotenv` (for environment variables)
- `streamlit` (if using the Streamlit app)

## Usage

1. Run the main script:
    ```bash
   python main.py

2. Run the Streamlit app:
   ```bash
   streamlit run streamline_app.py

3. Then check the localhost:
  
        `localhost[http://localhost:8501]`
  
  

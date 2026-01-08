# Company Policy AI

## Overview

Company Policy AI is an LLM-based intelligent agent system designed to answer company policy questions and provide policy guidance. This project leverages advanced language models, document intelligence, and policy engines to deliver accurate and contextual policy information.

## Features

- **Intelligent Policy Engine**: FastAPI-based REST API for policy query handling
- **LLM Integration**: Leverages large language models for natural language understanding
- **Policy Explainer**: Provides detailed explanations and reasoning for policy decisions
- **Document Processing**: Integrates with LLM Explainer for intelligent document analysis
- **Easy Integration**: Simple API endpoints for policy queries and responses

## Project Structure

```
company-policy-ai/
├── main.py                 # FastAPI application and core endpoints
├── policy_engine.py        # Core policy evaluation logic
├── policy_explainer.py     # LLM-based policy explanation module
├── llm_explainer.py        # LLM integration and document intelligence
├── policies.py             # Policy definitions and rules
├── requirements.txt        # Python dependencies
└── start.sh               # Startup script for deployment
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pavvaru-droid/company-policy-ai.git
cd company-policy-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the API

```bash
./start.sh
# or
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Ask Policy Question

**POST** `/ask`

Request body:
```json
{
  "question": "What is the company vacation policy?"
}
```

Response:
```json
{
  "answer": "Policy details here...",
  "policy_key": "vacation_policy",
  "policy_data": { /* full policy details */ }
}
```

## Core Components

### main.py
FastAPI application with the main `/ask` endpoint that processes policy queries.

### policy_engine.py
Contains the `get_policy_answer()` function that processes questions and retrieves relevant policies.

### policy_explainer.py  
Provides the `explain_policy()` function that generates detailed explanations using LLM technology.

### llm_explainer.py
Integrates with language models to process and explain policy documents intelligently.

### policies.py
Defines the company policy structure and rules.

## Configuration

See `requirements.txt` for Python dependencies configuration.

## Deployment

This project is configured for deployment with deployments tracked in the repository settings. Check the Deployments section for active deployments.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or support, please open an issue in the GitHub repository or contact the maintainers.

# MCP Project

This project demonstrates a simple MCP (Multi-Component Platform) server and client setup with OpenAI integration.

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd mcp_project
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

## Usage

- **Start the server:**
  ```sh
  python server.py
  ```

- **Run the client:**
  ```sh
  python client.py
  ```

## Notes

- The server exposes example tools (`get_weather`, `web_search`) for demonstration.
- You can extend the server with more tools as needed.
- Make sure your OpenAI API key is valid and has access to the required endpoints.
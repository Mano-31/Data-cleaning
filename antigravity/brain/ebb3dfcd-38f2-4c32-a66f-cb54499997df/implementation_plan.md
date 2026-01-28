# Implement Chatbot Feature

The goal is to add a chatbot to the "Mano data clean" Streamlit application. This chatbot will assist users by providing information about the uploaded dataset (e.g., row count, column names, missing values) and potentially guiding them through the cleaning process.

## User Review Required

> [!IMPORTANT]
> This implementation will use a **rule-based** approach initially to demonstrate functionality without requiring external API keys (like OpenAI or Gemini). It will be able to answer questions about the current dataset using the internal dataframe state.
> If you wish to connect to an external LLM, please provide the API key and preferred provider.

## Proposed Changes

### `data_wizard`

#### [MODIFY] [app.py](file:///c:/Users/MANO/.gemini/antigravity/scratch/data_wizard/app.py)

- Add a new section 4: "Chat with Data Wizard" (or a Sidebar chat)
- Initialize `st.session_state.messages` to store chat history.
- Implement `st.chat_input` and `st.chat_message` loop.
- Implement a `generate_response(prompt)` function:
    - Check if a dataframe is loaded (`st.session_state.df`).
    - Support keywords like "rows", "columns", "missing", "summary", "shape".
    - Fallback response for unknown queries.

## Verification Plan

### Manual Verification
- Run the app using `streamlit run app.py`.
- Upload a sample CSV or Excel file.
- Navigate to the Chat section (or sidebar).
- Type "How many rows?" -> Verify it returns the correct row count.
- Type "Show columns" -> Verify it lists columns.
- Type "hello" -> Verify it greets back.

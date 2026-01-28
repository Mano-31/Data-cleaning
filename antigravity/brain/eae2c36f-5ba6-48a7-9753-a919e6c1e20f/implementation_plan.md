# Data Wizard Implementation Plan

## Goal Description
Build a web-based tool collecting user datasets (CSV/Excel), performing automated cleaning (handling missing values, duplicates), and providing interactive visualizations.

## Proposed Changes
### Project Structure
- `app.py`: Main Streamlit application.
- `requirements.txt`: Dependencies.

### Features
1.  **Upload**: Support CSV and Excel files.
2.  **Cleaning**:
    - Show basic stats (rows, columns, missing values).
    - Drop duplicates.
    - Fill missing values (Mean/Median/Mode).
3.  **Visualization**:
    - Histograms for numerical columns.
    - Bar charts for categorical columns.
    - Correlation heatmap.
    - Scatter plots.
4.  **Chatbot**:
    -   Simple interface to ask questions about the data.
    -   Supports basic queries: "shape", "columns", "summary", "head".

## Verification Plan
### Manual Verification
- Run `streamlit run app.py`
- Upload a sample CSV.
- Test distinct cleaning operations.
- Verify charts render correctly.
- Test chatbot with questions like "What are the columns?" or "Show me the head".

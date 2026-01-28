# Data Wizard Walkthrough

The Data Wizard application is now ready! It allows you to upload datasets, clean them, and create visualizations.

## How to Run
1.  Open your terminal.
2.  Navigate to the project folder:
    ```bash
    cd C:\Users\MANO\.gemini\antigravity\scratch\data_wizard
    ```
3.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Features
-   **Upload**: Supports CSV and Excel files.
-   **Clean**:
    -   Remove Duplicates.
    -   Fill missing numerical values (Mean, Median, Zero).
-   **Visualize**:
    -   Histograms
    -   Box Plots
    -   Scatter Plots
    -   Bar Charts
    -   Correlation Heatmaps

## Troubleshooting
### "File does not exist: app.py"
If you see this error, you are likely in the wrong folder. Make sure to `cd` into the project directory first:
```bash
cd C:\Users\MANO\.gemini\antigravity\scratch\data_wizard
```

### "ModuleNotFoundError: No module named 'streamlit'"
If you see this error, install the dependencies:
```bash
pip install pandas streamlit plotly openpyxl
```

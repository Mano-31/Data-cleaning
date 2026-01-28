import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Data Clean House", page_icon="🧙‍♂️", layout="wide")

# Title and Description
st.title("🧙‍♂Data Clean House")
st.markdown("""
Welcome to Data Clean House! 
1. **Upload** your dataset (CSV or Excel).
2. **Clean** your data (Handle missing values, duplicates).
3. **Visualize** your insights.
""")

# --- 1. Upload Section ---
st.header("1. Upload Data")
uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load data
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Save to session state to prevent reloading on every widget interaction
        if 'df' not in st.session_state:
            st.session_state.df = df
        
        # Use simple variable for easier access in this run
        df = st.session_state.df
        
        st.success("Data uploaded successfully!")
        st.write("### Raw Data Preview")
        st.dataframe(df.head())
        
        # --- 2. Data Cleaning Section ---
        st.header("2. Data Cleaning")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Original Shape:** {df.shape[0]} rows, {df.shape[1]} columns")
            if st.button("Remove Duplicates"):
                st.session_state.df = df.drop_duplicates()
                st.success("Duplicates removed!")
                st.rerun()

        with col2:
            st.write("**Missing Values:**")
            st.write(df.isna().sum()[df.isna().sum() > 0])
            
            fill_method = st.selectbox("Fill Missing Numerical Values With:", ["None", "Mean", "Median", "Zero"])
            if st.button("Apply Fill"):
                numeric_cols = df.select_dtypes(include=['number']).columns
                if fill_method == "Mean":
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                elif fill_method == "Median":
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
                elif fill_method == "Zero":
                    df[numeric_cols] = df[numeric_cols].fillna(0)
                
                st.session_state.df = df
                st.success(f"Missing values filled with {fill_method}!")
                st.rerun()

        st.write("### Cleaned Data Preview")
        st.dataframe(st.session_state.df.head())

        # --- 3. Visualization Section ---
        st.header("3. Visualization")
        df_clean = st.session_state.df
        
        all_columns = df_clean.columns.tolist()
        numeric_columns = df_clean.select_dtypes(include=['number']).columns.tolist()
        categorical_columns = df_clean.select_dtypes(include=['object', 'category']).columns.tolist()

        viz_type = st.selectbox("Choose Visualization Type", 
                                ["Histogram", "Box Plot", "Scatter Plot", "Bar Chart", "Correlation Heatmap"])

        if viz_type == "Histogram":
            col = st.selectbox("Select Column", numeric_columns)
            if col:
                fig = px.histogram(df_clean, x=col, title=f"Histogram of {col}")
                st.plotly_chart(fig)

        elif viz_type == "Box Plot":
            col = st.selectbox("Select Column", numeric_columns)
            if col:
                fig = px.box(df_clean, y=col, title=f"Box Plot of {col}")
                st.plotly_chart(fig)

        elif viz_type == "Scatter Plot":
            x_col = st.selectbox("X Axis", numeric_columns)
            y_col = st.selectbox("Y Axis", numeric_columns, index=min(1, len(numeric_columns)-1))
            color_col = st.selectbox("Color (Optional)", ["None"] + categorical_columns)
            
            if x_col and y_col:
                c = None if color_col == "None" else color_col
                fig = px.scatter(df_clean, x=x_col, y=y_col, color=c, title=f"{x_col} vs {y_col}")
                st.plotly_chart(fig)

        elif viz_type == "Bar Chart":
            col = st.selectbox("Select Categorical Column", categorical_columns)
            if col:
                counts = df_clean[col].value_counts().reset_index()
                counts.columns = [col, 'Count']
                fig = px.bar(counts, x=col, y='Count', title=f"Count of {col}")
                st.plotly_chart(fig)
        
        elif viz_type == "Correlation Heatmap":
            if len(numeric_columns) > 1:
                corr = df_clean[numeric_columns].corr()
                fig = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
                st.plotly_chart(fig)
            else:
                st.warning("Not enough numerical columns for correlation heatmap.")

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Awaiting file upload...")

# --- 4. Chatbot Section ---
st.markdown("---")
st.header("4. Chat with Data Clean House 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Data Clean House assistant. Upload a dataset and ask me questions about it! 🧙‍♂️"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask something about your data..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Response Logic
    response = ""
    
    # Check if dataframe is loaded
    if 'df' in st.session_state:
        df_chat = st.session_state.df
        prompt_lower = prompt.lower()
        
        # Simple Rule-Based Logic
        if "row" in prompt_lower or "record" in prompt_lower or "how many" in prompt_lower:
            response = f"The dataset has **{df_chat.shape[0]} rows**."
        
        elif "column" in prompt_lower:
            response = f"The dataset has **{df_chat.shape[1]} columns**: \n\n" + ", ".join([f"`{c}`" for c in df_chat.columns])
            
        elif "shape" in prompt_lower:
            response = f"The shape of the dataset is **{df_chat.shape}**."
            
        elif "missing" in prompt_lower or "null" in prompt_lower or "empty" in prompt_lower:
            missing_count = df_chat.isna().sum().sum()
            if missing_count > 0:
                response = f"There are **{missing_count} missing values** in total.\n\nBreakdown:\n"
                response += str(df_chat.isna().sum()[df_chat.isna().sum() > 0])
            else:
                response = "There are **no missing values** in the dataset! 🎉"
                
        elif "summary" in prompt_lower or "describe" in prompt_lower or "stats" in prompt_lower:
            response = "Here is a statistical summary of the numerical columns:\n\n"
            st.dataframe(df_chat.describe()) # Direct render for complex objects
            response += "Check the table above for details."

        elif "head" in prompt_lower or "first" in prompt_lower:
            st.dataframe(df_chat.head())
            response = "Here are the first 5 rows."
            
        elif "hello" in prompt_lower or "hi" in prompt_lower:
             response = "Hello there! ready to analyze your data? 🚀"
        
        else:
            response = "I'm not sure how to answer that yet. Try asking about 'rows', 'columns', 'missing values', or 'summary'."
            
    else:
        response = "Please **upload a dataset** first so I can analyze it! 📂"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

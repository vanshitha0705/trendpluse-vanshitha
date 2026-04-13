import pandas as pd
import numpy as np
import os

def analyze_trends():
    # --- Task 1: Load and Explore ---
    file_path = os.path.join('data', 'trends_clean.csv')
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please run Task 2 first.")
        return

    # Load the cleaned CSV
    df = pd.read_json(file_path) if file_path.endswith('.json') else pd.read_csv(file_path)
    
    print(f"Loaded data: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())

    # Calculate global averages using Pandas
    avg_score = df['score'].mean()
    avg_comments = df['num_comments'].mean()
    
    print(f"\nAverage score   : {avg_score:,.0f}")
    print(f"Average comments: {avg_comments:,.0f}")

    # --- Task 2: Basic Analysis with NumPy ---
    print("\n--- NumPy Stats ---")
    
    # Converting columns to NumPy arrays for calculations
    scores = df['score'].to_numpy()
    
    mean_score = np.mean(scores)
    median_score = np.median(scores)
    std_score = np.std(scores)
    max_score = np.max(scores)
    min_score = np.min(scores)

    print(f"Mean score   : {mean_score:,.0f}")
    print(f"Median score : {median_score:,.0f}")
    print(f"Std deviation: {std_score:,.0f}")
    print(f"Max score    : {max_score:,.0f}")
    print(f"Min score    : {min_score:,.0f}")

    # Category with the most stories
    # value_counts() returns a Series; we can use idxmax() to find the top category
    top_category = df['category'].value_counts().idxmax()
    cat_count = df['category'].value_counts().max()
    print(f"Most stories in: {top_category} ({cat_count} stories)")

    # Story with most comments
    # Using np.argmax to find the index of the maximum value in the comments array
    comments_array = df['num_comments'].to_numpy()
    max_comm_idx = np.argmax(comments_array)
    top_story_title = df.iloc[max_comm_idx]['title']
    top_story_comments = df.iloc[max_comm_idx]['num_comments']
    
    print(f"Most commented story: \"{top_story_title}\" — {top_story_comments:,} comments")

    # --- Task 3: Add New Columns ---
    
    # Formula: engagement = num_comments / (score + 1)
    # Adding 1 prevents division by zero errors
    df['engagement'] = df['num_comments'] / (df['score'] + 1)

    # is_popular: True if score > average score, else False
    df['is_popular'] = df['score'] > avg_score

    # --- Task 4: Save the Result ---
    output_path = os.path.join('data', 'trends_analysed.csv')
    df.to_csv(output_path, index=False)
    
    print(f"\nSaved to {output_path}")

if __name__ == "__main__":
    analyze_trends()

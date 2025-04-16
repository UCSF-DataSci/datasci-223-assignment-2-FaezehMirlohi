#!/usr/bin/env python3
"""
Patient Data Cleaner

This script standardizes and filters patient records according to specific rules:

Data Cleaning Rules:
1. Names: Capitalize each word (e.g., "john smith" -> "John Smith")
2. Ages: Convert to integers, set invalid ages to 0
3. Filter: Remove patients under 18 years old
4. Remove any duplicate records

Input JSON format:
    [
        {
            "name": "john smith",
            "age": "32",
            "gender": "male",
            "diagnosis": "hypertension"
        },
        ...
    ]

Output:
- Cleaned list of patient dictionaries
- Each patient should have:
  * Properly capitalized name
  * Integer age (≥ 18)
  * Original gender and diagnosis preserved
- No duplicate records
- Prints cleaned records to console

Example:
    Input: {"name": "john smith", "age": "32", "gender": "male", "diagnosis": "flu"}
    Output: {"name": "John Smith", "age": 32, "gender": "male", "diagnosis": "flu"}

Usage:
    python patient_data_cleaner.py
"""

import json
import os
import pandas as pd

def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    # BUG: No error handling for file not found
    # FIX: Giving warning if file is not found
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Warning: File not found!")
        return None

def clean_patient_data(patients):
    """
    Clean patient data by:
    - Capitalizing names
    - Converting ages to integers
    - Filtering out patients under 18
    - Removing duplicates
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        list: Cleaned list of patient dictionaries
    """
    cleaned_patients = []
    
    for patient in patients:
        # Change patient into a dataframe
        patient = pd.DataFrame([patient])

        # BUG: Typo in key 'nage' instead of 'name'
        # FIX: Change 'nage' with 'name'
        patient['name'] = patient['name'].str.title()
        
        # BUG: Wrong method name (fill_na vs fillna)
        # FIX: Change fill_na with fillna
        patient['age'] = int(patient['age'].fillna(0))
        
        # BUG: Wrong method name (drop_duplcates vs drop_duplicates)
        # FIX: Change drop_duplcates with drop_duplicates
        patient = patient.drop_duplicates()
        

        # BUG: Wrong comparison operator (= vs ==)
        # FIX: Change = with => 
        if patient['age'].item() >= 18:
            # BUG: Logic error - keeps patients under 18 instead of filtering them out
            # FIX: Change = with => to filter out patients under 18
            cleaned_patients.append(patient.to_dict(orient="records")[0])
    
    # BUG: Missing return statement for empty list
    # FIX: Add print the empty list 
    if not cleaned_patients:
        print("There is no patients info in the cleaned list!")
        return None
    
    return cleaned_patients

def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'raw', 'patients.json')
    
    # BUG: No error handling for load_patient_data failure
    # FIX: Add try and except for the data
    try:
        patients = load_patient_data(data_path)
    except Exception as e:
        print("Error loading patient data:", e)
        return

    # Clean the patient data
    cleaned_patients = clean_patient_data(patients)
    
    # BUG: No check if cleaned_patients is None
    # FIX: Prints "Empty list" if cleaned_patients is None
    if cleaned_patients:
        # Print the cleaned patient data
        print("Cleaned Patient Data:")
        for patient in cleaned_patients:
            # BUG: Using 'name' key but we changed it to 'nage'
            # FIX: We changed the 'nage' to 'name' on top, also added the gender
            print(f"Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
    else:
        print("Empty list!")
    # Return the cleaned data (useful for testing)
    return cleaned_patients

if __name__ == "__main__":
    main()
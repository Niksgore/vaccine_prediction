import pandas as pd

def check_vaccination_status(dataset, unique_id):
    # Filter the dataset based on the unique ID
    person_data = dataset[dataset['unique_id'] == unique_id]

    # Check if the person is vaccinated or not
    if not person_data.empty:
        vaccination_status = person_data.iloc[0]['h1n1_vaccine']
        if vaccination_status == 1:
            return f"Person with ID {unique_id} is vaccinated."
        elif vaccination_status == 0:
            return f"Person with ID {unique_id} is not vaccinated."
    else:
        return f"Person with ID {unique_id} not found in the dataset."

csv_file_path = "h1n1_vaccine_prediction.csv"
df = pd.read_csv(csv_file_path)

# Take user input for unique ID
user_input_id = int(input("Enter the unique ID to check vaccination status: "))

# Example usage
result = check_vaccination_status(df, user_input_id)
print(result)


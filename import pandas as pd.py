import pandas as pd

# Load the .csv file
csv_file = "baseplate.csv"
csv_data = pd.read_csv(csv_file)

# Load the .xlsx file
xlsx_file = "form.xlsx"
xlsx_data = pd.read_excel(xlsx_file)

csv_column = "Email"  # Column name for email in .csv file
xlsx_column = "Email"  # Column name for email in .xlsx file

# Find attendees in the .csv file but not in the .xlsx file
csv_not_in_xlsx = csv_data[~csv_data[csv_column].isin(xlsx_data[xlsx_column])]

# Find attendees in the .xlsx file but not in the .csv file
xlsx_not_in_csv = xlsx_data[~xlsx_data[xlsx_column].isin(csv_data[csv_column])]

# Extract only the emails and save them
csv_not_in_xlsx_emails = csv_not_in_xlsx[[csv_column]]
xlsx_not_in_csv_emails = xlsx_not_in_csv[[xlsx_column]]

# Save results to new files
csv_not_in_xlsx_emails.to_csv("not_registered_in_form.csv", index=False)
xlsx_not_in_csv_emails.to_csv("not_registered_in_baseplate.csv", index=False)

# Extract the emails from the .csv file
csv_emails = csv_data[[csv_column]]

# Extract the emails from the .xlsx file
xlsx_emails = xlsx_data[[xlsx_column]]

csv_emails.to_csv("emails_from_baseplate.csv", index=False)
xlsx_emails.to_csv("emails_from_form.csv", index=False)

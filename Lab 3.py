#CIS 117 Lab 3
#A script that creates .csv region files that contain the countries that reside within them.
#Ethan Ishii

import csv

# Input CSV file name
input_csv = 'country_full.csv'
# Set a specific file path to save files
file_path = "C:/college work/CIS 117 Python/Lab 3/CREATED FILES/"
# Dictionary to group countries by region
regions = {}

# Reading the input file
try:
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row.get('name')
            region = row.get('region')

            if not country or not region:
                continue

            # Checks if the region key exists
            if region not in regions:
                regions[region] = []
            regions[region].append({'name': country, 'region': region})

except FileNotFoundError:
    print("The file doesn't exist! I can't sort a nonexistent file!")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit(1)

# Try writing the output files
for region, country_list in regions.items():
    filename = f"{region.replace(' ', '_')}.csv"
    output_file_path = file_path + filename # Concentrating the file paths

    try:
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['name', 'region']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(country_list)

        print(f"{filename} Created!")

    except PermissionError:
        print(f"Error: Permission denied when trying to write '{filename}'.")
    except IOError as e:
        print(f"IOError: An error occurred while writing '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing '{filename}': {e}")

print("Done! All files were written!")

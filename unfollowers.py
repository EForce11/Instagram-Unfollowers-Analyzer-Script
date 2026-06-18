import json
import pandas as pd

# Define file paths (assuming files are in the same directory as the script)
followers_file = 'followers_1.json'
following_file = 'following.json'

try:
    with open(followers_file, "r", encoding="utf-8") as f:
        followers_data = json.load(f)

    with open(following_file, "r", encoding="utf-8") as f:
        following_data = json.load(f)
except FileNotFoundError:
    print(f"[-] Error: Please ensure '{followers_file}' and '{following_file}' are in the same directory as this script.")
    exit()

# 1. Collect followers into a set for fast lookup
followers_set = set()
for item in followers_data:
    try:
        # In 'followers_1.json', the username is stored under the 'value' key
        username = item["string_list_data"][0]["value"]
        followers_set.add(username)
    except (KeyError, IndexError):
        pass

# 2. Iterate through following list and find unfollowers
unfollowers_data = []
following_list = following_data.get("relationships_following", [])

for item in following_list:
    try:
        # NOTE: In 'following.json', the username is stored under the 'title' key!
        username = item["title"]
        profile_link = item["string_list_data"][0]["href"]
        
        # If the person we follow is not in our followers set, add them to the list
        if username not in followers_set:
            unfollowers_data.append({
                "Username": username,
                "Profile Link": profile_link
            })
    except (KeyError, IndexError):
        pass

# Convert the list of dictionaries to a pandas DataFrame
df_unfollowers = pd.DataFrame(unfollowers_data)

print(f"\n[+] Analysis Complete! A total of {len(df_unfollowers)} people are not following you back.")

# Export the results to an Excel file
output_excel_name = "unfollowers_report.xlsx"
try:
    # index=False prevents pandas from writing row numbers into the file
    df_unfollowers.to_excel(output_excel_name, index=False)
    print(f"[+] Results have been successfully saved to '{output_excel_name}'.")
except Exception as e:
    print(f"[-] An error occurred while creating the Excel file: {e}")

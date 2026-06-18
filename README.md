# Instagram Unfollowers Analyzer 🕵️‍♂️

A secure, local, and fault-tolerant Python script to find out who isn't following you back on Instagram. 

Forget about sketchy third-party apps, password sharing, or API limits. This script relies entirely on your official Instagram data export (JSON) and processes everything locally on your machine. It even handles Instagram's inconsistent data structures (`value` vs. `title` keys) without crashing!

## ✨ Features
* **100% Secure:** No passwords, no session cookies, no third-party APIs. You don't even need to be connected to the internet to run it.
* **Fault-Tolerant:** Safely skips deactivated or deleted accounts without throwing `KeyError` exceptions.
* **Smart Data Parsing:** Automatically resolves the structural differences between Instagram's `followers_1.json` and `following.json` files.
* **Excel Export:** Generates a beautifully formatted Excel report (`.xlsx`) with clickable profile links and timestamps.

## 🛠️ Prerequisites
You need Python installed on your system. You also need the following libraries:
`bash
pip install pandas openpyxl
`

## 🚀 How to Use

**Step 1: Request Your Data from Instagram**
1. Open Instagram on your phone or browser.
2. Go to **Settings > Accounts Center > Your information and permissions > Download your information**.
3. Choose **Download or transfer information**.
4. Select your Instagram profile and choose **Some of your information**.
5. Select **Followers and following** ONLY ⚠️.
6. **Crucial:** Set the format to **JSON** and create the file.

**Step 2: Run the Script**
1. Once Instagram emails your data, extract the `.zip` file.
2. Locate `followers_1.json` and `following.json` inside the extracted folder.
3. Place both files in the same directory as this script.
4. Run the script:
   `bash
   python find_unfollowers.py
   `
5. Check your directory for the generated `unfollowers_report.xlsx` file!

## 📝 Output Details
The generated Excel file includes:
* **Username:** The exact Instagram handle.
* **Profile Link:** A clickable hyperlink directly to their profile.
* **Following Since:** The date and time you started following them (converted from the raw timestamp).

---
*Developed by [Emir Furkan Ulu](https://emirfurkan.com)*

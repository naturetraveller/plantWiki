import subprocess
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the scripts to run
scripts = [
    "02_deleteAll_rows.py", 
    "01A_initalImport_wikiPlants_excel.py", 
    "03A_export_wikiPlants_txt.py",
    "03B_export_wikiPlants_html.py"
    "03C_export_wikiPlants_xhtml.py"
]

# Execute the scripts one after the other
for script in scripts:
    script_path = os.path.join(current_directory, script)
    subprocess.run(["python", script_path])

print("All scripts executed.")
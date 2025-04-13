
import os
import pandas as pd

def extract_indentation_data(folder_path):
    extracted_data = {}

    for filename in os.listdir(folder_path):
        if not (filename.endswith(".txt") and filename.startswith("force-save-")):
            continue
        
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        in_indent_segment = False
        data_started = False
        columns = []
        data_rows = []

        for line in lines:
            line = line.strip()

            if line.startswith("# segment:"):
                segment_type = line.split(":")[1].strip()
                in_indent_segment = (segment_type == "extend")
                data_started = False  # reset when switching segments
                continue

            if in_indent_segment and line.startswith("# columns:"):
                columns = line.split(":", 1)[1].strip().split()
                data_started = True
                continue

            if data_started:
                if not(line.startswith("#")):
                #     break  # reached next metadata block
                    values = line.split()
                    if len(values) == len(columns):
                        data_rows.append(values)
        
        if columns and data_rows:
            df = pd.DataFrame(data_rows, columns=columns).astype(float)
            name = f"force_depth{filename[10:-4]}"
            extracted_data[name] = df[['verticalTipPosition', 'vDeflection']]
    
    return extracted_data


folder = "/home/joeashton/Sync/Obsidian/SuperVault/Projects/Uni Projects/Individual project/Workspace/Curves/txt-export/Control/wide_fit-2025.04.08-10.54.23/"

data = extract_indentation_data(folder)

for fname, df in data.items():
    df.to_csv(f"{fname}.csv", index=False)


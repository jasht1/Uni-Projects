import os
import pandas as pd

def get_paths(relative_paths):
    workspace = os.path.dirname(__file__).split("Scripts")[0]
    paths = {}
    for path in relative_paths:
        paths[path] = os.path.join(workspace,relative_paths[path])

    return paths

# relative_paths = {
#     'Control': "Curves/txt-export/HK2 Control/HK2 Control_processed-2025.04.18-16.35.00.tsv",
#     'Treated': "Curves/txt-export/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)_processed-2025.04.18-16.25.25.tsv"
# }
# paths = get_paths(relative_paths)

def get_path(relative_path):
    workspace = os.path.dirname(__file__).split("Scripts")[0]
    path = os.path.join(workspace,relative_path)

    return path

def extract_indentation_datasets(folder_path):  # Rips force vs indentation data from txt to csv
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
            name = f"force-depth{filename[10:-4]}"
            extracted_data[name] = df[['verticalTipPosition', 'vDeflection']]
    
    return extracted_data

# txt_path = get_paths("Curves/txt-export/HK2 Control/processed_curves-2025.04.18-16.35.00")
# txt_path = get_path("Curves/txt-export/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)/processed_curves-2025.04.18-16.25.25")
# data = extract_indentation_datasets(txt_path)
# for fname, df in data.items():
#     df.to_csv(f"{fname}.csv", index=False)

def get_csv_datasets(folder_path):
    extracted_data = {}

    for filename in os.listdir(folder_path):
        if not (filename.endswith(".csv") and filename.startswith("force-depth-")):
            continue
        
        filepath = os.path.join(folder_path, filename)
        df = pd.read_csv(filepath)

        if 'verticalTipPosition' in df.columns and 'vDeflection' in df.columns:
            df = df[['verticalTipPosition', 'vDeflection']].astype(float)
            name = filename[:-4]  # remove .csv
            extracted_data[name] = df

    return extracted_data

# csv_path = '/home/joeashton/Sync/Obsidian/SuperVault/Projects/Uni Projects/Individual project/Workspace/Curves/csv-force-indentation/untreated/'
# data = get_csv_datasets(csv_path)

def get_csv_dataset(filename, group="Control"):
    extracted_data = {}

    if not (filename.endswith(".csv") and filename.startswith("force-depth-")):
        if filename.startswith("force-save-") and filename.endswith(".jpk-force"):
            # curve_date = filename.split("-")[1].strip()
            curve_date = filename[11:-10]
            filename = f"force-depth-{curve_date}.csv"
        else:
            print(f"bad csv filename {filename}")
            return 0

    folder_path = get_path(f"Curves/csv-force-indentation/{group}")
    filepath = os.path.join(folder_path, filename)
    df = pd.read_csv(filepath)

    if 'verticalTipPosition' in df.columns and 'vDeflection' in df.columns:
        df = df[['verticalTipPosition', 'vDeflection']].astype(float)
        name = filename[:-4]  # remove .csv
        extracted_data[name] = df

    return extracted_data

def get_jpk_batch_data(paths='default', relative_paths=False):

    if relative_paths:
        paths = get_paths(paths)

    else: 
        rpaths = {
            'Control': "Curves/txt-export/HK2 Control/HK2 Control_processed-2025.04.18-16.35.00.tsv",
            'Treated': "Curves/txt-export/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)_processed-2025.04.18-16.25.25.tsv"
        }
        if paths == 'default':
            paths = get_paths(rpaths)

        # elif paths == 'Control':
        #     return pd.read_csv(rpaths['Control'],sep='\t')
        # elif paths == 'Treated':
        #     return pd.read_csv(rpaths['Treated'],sep='\t')
    data = {}

    for path in paths:
        df = pd.read_csv(paths[path],sep='\t')  # JPK outputs a tsv summarising batch processes
        data[path] = df

    return data

# data = get_jpk_batch_data(paths) # Use w prev example

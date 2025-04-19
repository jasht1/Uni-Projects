import pandas
# import matplotlib

paths = {
    'Control': "/home/joeashton/Sync/Obsidian/SuperVault/Projects/Uni Projects/Individual project/Workspace/Curves/txt-export/HK2 Control/HK2 Control_processed-2025.04.18-16.35.00.tsv",
    'Treated': "/home/joeashton/Sync/Obsidian/SuperVault/Projects/Uni Projects/Individual project/Workspace/Curves/txt-export/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)/HK2 Diseased (TGF-beta1- 10ng per mL, 48h)_processed-2025.04.18-16.25.25.tsv"
}

def get_jpk_batch_data(paths):
    data = {}

    for path in paths:
        df = pandas.read_csv(paths[path],sep='\t')  # JPK outputs a tsv summarising batch processes
        data[path] = df

    return data

data = get_jpk_batch_data(paths)

print('yay')

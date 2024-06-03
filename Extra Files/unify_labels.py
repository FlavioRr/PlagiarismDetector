import pandas as pd

# Define paths to the alphanumeric and numeric data files
path_alphanumeric = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\data\conplag_version_2\versions\labels.csv'
path_numeric_qrel = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\data\fire14-source-code-training-dataset\fire14-source-code-training-dataset\SOCO14-java.qrel'

# Define the destination path for the unified label file
destination_path = r'C:\Users\droid\Documents\Aplicaciones_Avanzadas\Proyecto\PlagiarismDetector\finalDataset\unify_labels\javafiles_labels.csv'

# Load the alphanumeric dataset
df_alphanumeric = pd.read_csv(path_alphanumeric)
# Drop the 'problem' column from the alphanumeric dataset
if 'problem' in df_alphanumeric.columns:
    df_alphanumeric.drop(columns=['problem'], inplace=True)
# Ensure veredict is integer
df_alphanumeric['veredict'] = df_alphanumeric['veredict'].astype(int)

# Read the numeric .qrel file and assign a default veredict of 1
df_numeric = pd.read_csv(path_numeric_qrel, sep="\s+", header=None, names=["sub1", "sub2"])
df_numeric['veredict'] = 1

# Concatenate both dataframes
unified_df = pd.concat([df_alphanumeric, df_numeric])

# Save the unified dataset
unified_df.to_csv(destination_path, index=False)

print("Unified labels have been saved to:", destination_path)
import os
import pandas as pd
import re

# Get the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Read the Excel files
all_AKI_genes = pd.read_excel('./AMIA2024/20240901_NewDignetResults/AKI_gene_pairs_updated_with_percentages.xlsx',dtype=str)
all_CKD_genes = pd.read_excel('./AMIA2024/20240901_NewDignetResults/CKD_gene_pairs_updated_with_percentages.xlsx',dtype=str)

# Function to extract numeric part
def extract_numeric(value):
    match = re.search(r'\d+(\.\d+)?', str(value))
    return match.group() if match else value

# Apply the function to the 4th column (index 3)
all_AKI_genes.iloc[:, 3] = all_AKI_genes.iloc[:, 3].apply(extract_numeric)
all_CKD_genes.iloc[:, 3] = all_CKD_genes.iloc[:, 3].apply(extract_numeric)

# Remove rows with NaN in gene1 or gene2 for both AKI and CKD dataframes
all_AKI_genes = all_AKI_genes.dropna(subset=[all_AKI_genes.columns[1], all_AKI_genes.columns[2]])
all_CKD_genes = all_CKD_genes.dropna(subset=[all_CKD_genes.columns[1], all_CKD_genes.columns[2]])

# Check the sizes of the resulting lists
print("------------------------------------------------");
print("! all AKI genes: "+str(all_AKI_genes.shape))
print("! all CKD genes: "+str(all_CKD_genes.shape))

# Filter by the number of hits (in the fourth column)
# currently, minimum 3 papers for reliable gene pairs
filtered_AKI_genes = all_AKI_genes[all_AKI_genes.iloc[:, 3].astype(float) >= 3].iloc[:, 1:4]
filtered_CKD_genes = all_CKD_genes[all_CKD_genes.iloc[:, 3].astype(float) >= 3].iloc[:, 1:4]

# Check the sizes of the resulting lists
print("---- after filtering by minimum # of papers ----");
print("! all AKI genes filtered: "+str(filtered_AKI_genes.shape))
print("! all CKD genes filtered: "+str(filtered_CKD_genes.shape))


# To get the list of all unique genes in each gene set
# Select the second and third columns and combine into one list
AKI_genes = list(pd.concat([filtered_AKI_genes.iloc[:, 0], filtered_AKI_genes.iloc[:, 1]]).unique())
CKD_genes = list(pd.concat([filtered_CKD_genes.iloc[:, 0], filtered_CKD_genes.iloc[:, 1]]).unique())

# Check the total numbers of unique genes in each dataset
print("------------------------------------------------");
print(f"Number of all AKI genes: {len(AKI_genes)}")
print(f"Number of all CKD genes: {len(CKD_genes)}")

# save AKI_genes and CKD_genes to csv
pd.DataFrame(AKI_genes, columns=['AKI_genes']).to_csv('./AMIA2024/20240901_NewDignetResults/AKI_genes_updated_filtered.csv', index=False)
pd.DataFrame(CKD_genes, columns=['CKD_genes']).to_csv('./AMIA2024/20240901_NewDignetResults/CKD_genes_updated_filtered.csv', index=False)

# Analyze the overlap between the two gene sets
unique_genes_to_AKI = set(AKI_genes) - set(CKD_genes)
unique_genes_to_CKD = set(CKD_genes) - set(AKI_genes)
common_genes = set(AKI_genes) & set(CKD_genes)

# print("Genes unique to AKI:", unique_to_AKI)
# print("Genes unique to CKD:", unique_to_CKD)
# print("Genes common to both AKI and CKD:", common_genes)
print("------------------------------------------------");
print(f"Number of genes unique to AKI: {len(unique_genes_to_AKI)}")
print(f"Number of genes unique to CKD: {len(unique_genes_to_CKD)}")
print(f"Number of genes common to both: {len(common_genes)}")





################################################################################################################################################
## GENE PAIRS
################################################################################################################################################

# Initialize lists to store unique gene pairs for each group
AKI_pairs = []
CKD_pairs = []

# Process AKI gene pairs
for _, row in filtered_AKI_genes.iterrows():
    AKI_pairs.append(set(row.iloc[0:2]))  # Assuming gene pairs are in columns 2 and 3

# Process CKD gene pairs
for _, row in filtered_CKD_genes.iterrows():
    CKD_pairs.append(set(row.iloc[0:2]))  # Assuming gene pairs are in columns 2 and 3

# # Sort gene pairs before comparison
# AKI_pairs = [tuple(sorted(group)) for group in AKI_pairs]
# CKD_pairs = [tuple(sorted(group)) for group in CKD_pairs]

# Sort gene pairs before comparison, ensuring all elements are strings
AKI_pairs = [tuple(sorted(map(str, group))) for group in AKI_pairs]
CKD_pairs = [tuple(sorted(map(str, group))) for group in CKD_pairs]

# # Saving AKI and CKD groups to csv
# pd.DataFrame(AKI_pairs).to_csv('./AMIA2024/20240901_NewDignetResults/AKI_gene_pairs_updated.csv', index=False)
# pd.DataFrame(CKD_pairs).to_csv('./AMIA2024/20240901_NewDignetResults/CKD_gene_pairs_updated.csv', index=False)

# Concatenate the two columns into a single column for each pair
AKI_pairs_concatenated = [f"{pair[0]}_{pair[1]}" for pair in AKI_pairs]
CKD_pairs_concatenated = [f"{pair[0]}_{pair[1]}" for pair in CKD_pairs]

# Saving AKI and CKD groups to csv
pd.DataFrame(AKI_pairs_concatenated, columns=['AKI_gene_pairs']).to_csv('./AMIA2024/20240901_NewDignetResults/AKI_gene_pairs_updated_filtered.csv', index=False)
pd.DataFrame(CKD_pairs_concatenated, columns=['CKD_gene_pairs']).to_csv('./AMIA2024/20240901_NewDignetResults/CKD_gene_pairs_updated_filtered.csv', index=False)

# Find unique and common groups
unique_to_AKI_pairs = [group for group in AKI_pairs if group not in CKD_pairs]
unique_to_CKD_pairs = [group for group in CKD_pairs if group not in AKI_pairs]
common_pairs = [group for group in AKI_pairs if group in CKD_pairs]

# print("\nPairs unique to AKI:", unique_to_AKI_pairs)
# print("\nPairs unique to CKD:", unique_to_CKD_pairs)
# print("\nPairs common to both AKI and CKD:", common_pairs)

print("------------------------------------------------");
print(f"Number of pairs unique to AKI: {len(unique_to_AKI_pairs)}")
print(f"Number of pairs unique to CKD: {len(unique_to_CKD_pairs)}")
print(f"Number of pairs common to both: {len(common_pairs)}")


# # Optionally, save the results to CSV files
# # pd.DataFrame(unique_to_AKI).to_csv('./AMIA2024/20240901_NewDignetResults/unique_AKI_pairs.csv', index=False)
# # pd.DataFrame(unique_to_CKD).to_csv('./AMIA2024//20240901_NewDignetResults/unique_CKD_pairs.csv', index=False)
# # pd.DataFrame(common_groups).to_csv('./AMIA2024//20240901_NewDignetResults/common_groups.csv', index=False)


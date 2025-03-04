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

# # Print the first 3 rows of the DataFrame
print(all_AKI_genes.shape)
print(all_CKD_genes.shape)

# Filter by the number of hits (in the fourth column)
# And only keep up to fourth column
filtered_AKI_genes = all_AKI_genes[all_AKI_genes.iloc[:, 3].astype(float) >= 3].iloc[:, 1:4]
filtered_CKD_genes = all_CKD_genes[all_CKD_genes.iloc[:, 3].astype(float) >= 3].iloc[:, 1:4]


# Select the second and third columns and combine into one list
AKI_genes = list(pd.concat([filtered_AKI_genes.iloc[:, 0], filtered_AKI_genes.iloc[:, 1]]).unique())
CKD_genes = list(pd.concat([filtered_CKD_genes.iloc[:, 0], filtered_CKD_genes.iloc[:, 1]]).unique())

print(len(AKI_genes))
print(len(CKD_genes))

# # Print the size (dimensions) of the filtered DataFrame
# print("Size of filtered_AKI_genes:", filtered_AKI_genes.shape)


# print(len(AKI_genes))
# print(len(CKD_genes))


#print(all_AKI_genes)


unique_to_AKI = set(AKI_genes) - set(CKD_genes)
unique_to_CKD = set(CKD_genes) - set(AKI_genes)
common_genes = set(AKI_genes) & set(CKD_genes)

# # # save AKI_genes and CKD_genes to csv
# pd.DataFrame(AKI_genes, columns=['AKI_genes']).to_csv('./AMIA2024/20240901_NewDignetResults/AKI_genes_updated_filtered.csv', index=False)
# pd.DataFrame(CKD_genes, columns=['CKD_genes']).to_csv('./AMIA2024/20240901_NewDignetResults/CKD_genes_updated_filtered.csv', index=False)


# print("Genes unique to AKI:", unique_to_AKI)
# print("Genes unique to CKD:", unique_to_CKD)
# print("Genes common to both AKI and CKD:", common_genes)

print(f"\nNumber of genes unique to AKI: {len(unique_to_AKI)}")
print(f"Number of genes unique to CKD: {len(unique_to_CKD)}")
print(f"Number of genes common to both: {len(common_genes)}")

################################################################################################################################################
##       PAIRS
##
################################################################################################################################################


# # Initialize lists to store unique genes for each group
AKI_groups = []
CKD_groups = []

# Process AKI gene groups
for _, row in filtered_AKI_genes.iterrows():
    AKI_groups.append(set(row.iloc[0:2]))  # Assuming gene pairs are in columns 2 and 3

# Process CKD gene groups
for _, row in filtered_CKD_genes.iterrows():
    CKD_groups.append(set(row.iloc[0:2]))  # Assuming gene pairs are in columns 2 and 3

# Find unique and common groups
unique_to_AKI_pairs = [group for group in AKI_groups if group not in CKD_groups]
unique_to_CKD_pairs = [group for group in CKD_groups if group not in AKI_groups]
common_pairs = [group for group in AKI_groups if group in CKD_groups]

# print("\nPairs unique to AKI:", unique_to_AKI_pairs)
# print("\nPairs unique to CKD:", unique_to_CKD_pairs)
# print("\nPairs common to both AKI and CKD:", common_pairs)

print(f"\nNumber of pairs unique to AKI: {len(unique_to_AKI_pairs)}")
print(f"Number of pairs unique to CKD: {len(unique_to_CKD_pairs)}")
print(f"Number of pairs common to both: {len(common_pairs)}")



# # Optionally, save the results to CSV files
# # pd.DataFrame(unique_to_AKI).to_csv('./AMIA2024/unique_AKI_groups.csv', index=False)
# # pd.DataFrame(unique_to_CKD).to_csv('./AMIA2024/unique_CKD_groups.csv', index=False)
# # pd.DataFrame(common_groups).to_csv('./AMIA2024/common_groups.csv', index=False)

# # Saving AKI and CKD groups to csv
# pd.DataFrame(AKI_groups).to_csv('./AMIA2024/20240901_NewDignetResults/AKI_gene_pairs_updated.csv', index=False)
# pd.DataFrame(CKD_groups).to_csv('./AMIA2024/20240901_NewDignetResults/CKD_gene_pairs_updated.csv', index=False)
# import pandas as pd

# # Read the Excel files
# all_AKI_genes = pd.read_excel('./AMIA2024/AKI gene pairs.xlsx',dtype=str)
# all_CKD_genes = pd.read_excel('./AMIA2024/CKD gene pairs.xlsx',dtype=str)

# # # Check for the specific datetime value in the second and third columns
# # if (all_AKI_genes.iloc[:, 1].isin([pd.Timestamp('2024-03-08')]).any() or 
# #     all_AKI_genes.iloc[:, 2].isin([pd.Timestamp('2024-03-08')]).any()):
# #     print("The datetime value 'datetime.datetime(2024, 3, 8, 0, 0)' exists in the DataFrame.")
# # else:
# #     print("The datetime value does not exist in the DataFrame.")


# # Select the second and third columns and combine into one list
# AKI_genes = list(pd.concat([all_AKI_genes.iloc[:, 1], all_AKI_genes.iloc[:, 2]]).unique())
# CKD_genes = list(pd.concat([all_CKD_genes.iloc[:, 1], all_CKD_genes.iloc[:, 2]]).unique())

# # print(len(AKI_genes))
# # print(len(CKD_genes))



# #print(all_AKI_genes)

# # AKI_genes = list(all_AKI_genes[1, 2])
# # CKD_genes = list(all_CKD_genes[1, 2])

# unique_to_AKI = set(AKI_genes) - set(CKD_genes)
# unique_to_CKD = set(CKD_genes) - set(AKI_genes)
# common_genes = set(AKI_genes) & set(CKD_genes)

# # save AKI_genes and CKD_genes to csv
# #pd.DataFrame(AKI_genes, columns=['AKI_genes']).to_csv('./AMIA2024/AKI_genes.csv', index=False)
# #pd.DataFrame(CKD_genes, columns=['CKD_genes']).to_csv('./AMIA2024/CKD_genes.csv', index=False)


# print("Genes unique to AKI:", unique_to_AKI)
# print("Genes unique to CKD:", unique_to_CKD)
# print("Genes common to both AKI and CKD:", common_genes)

# print(f"\nNumber of genes unique to AKI: {len(unique_to_AKI)}")
# print(f"Number of genes unique to CKD: {len(unique_to_CKD)}")
# print(f"Number of genes common to both: {len(common_genes)}")

##########################################################################################
# |
# |    Gene pairs code
# V
##########################################################################################

import pandas as pd

# Read the Excel files
all_AKI_genes = pd.read_excel('./AMIA2024/AKI gene pairs.xlsx', dtype=str)
all_CKD_genes = pd.read_excel('./AMIA2024/CKD gene pairs.xlsx', dtype=str)

# Initialize lists to store unique genes for each group
AKI_groups = []
CKD_groups = []

# Process AKI gene groups
for _, row in all_AKI_genes.iterrows():
    AKI_groups.append(set(row.iloc[1:3]))  # Assuming gene pairs are in columns 2 and 3

# Process CKD gene groups
for _, row in all_CKD_genes.iterrows():
    CKD_groups.append(set(row.iloc[1:3]))  # Assuming gene pairs are in columns 2 and 3

# Find unique and common groups
unique_to_AKI = [group for group in AKI_groups if group not in CKD_groups]
unique_to_CKD = [group for group in CKD_groups if group not in AKI_groups]
common_groups = [group for group in AKI_groups if group in CKD_groups]

print("\nPairs unique to AKI:", unique_to_AKI)
print("\nPairs unique to CKD:", unique_to_CKD)
print("\nPairs common to both AKI and CKD:", common_groups)

print(f"\nNumber of pairs unique to AKI: {len(unique_to_AKI)}")
print(f"Number of pairs unique to CKD: {len(unique_to_CKD)}")
print(f"Number of pairs common to both: {len(common_groups)}")

# Optionally, save the results to CSV files
# pd.DataFrame(unique_to_AKI).to_csv('./AMIA2024/unique_AKI_groups.csv', index=False)
# pd.DataFrame(unique_to_CKD).to_csv('./AMIA2024/unique_CKD_groups.csv', index=False)
# pd.DataFrame(common_groups).to_csv('./AMIA2024/common_groups.csv', index=False)

# Saving AKI and CKD groups to csv
pd.DataFrame(AKI_groups).to_csv('./AMIA2024/AKI_groups.csv', index=False)
pd.DataFrame(CKD_groups).to_csv('./AMIA2024/CKD_groups.csv', index=False)
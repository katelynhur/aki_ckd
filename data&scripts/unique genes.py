import pandas as pd

# Read the Excel files
all_AKI_genes = pd.read_excel('./AMIA2024/AKI_genes_updated.xlsx',dtype=str)
all_CKD_genes = pd.read_excel('./AMIA2024/CKD gene pairs.xlsx',dtype=str)

# # Check for the specific datetime value in the second and third columns
# if (all_AKI_genes.iloc[:, 1].isin([pd.Timestamp('2024-03-08')]).any() or 
#     all_AKI_genes.iloc[:, 2].isin([pd.Timestamp('2024-03-08')]).any()):
#     print("The datetime value 'datetime.datetime(2024, 3, 8, 0, 0)' exists in the DataFrame.")
# else:
#     print("The datetime value does not exist in the DataFrame.")


# Select the second and third columns and combine into one list
AKI_genes = list(pd.concat([all_AKI_genes.iloc[:, 1], all_AKI_genes.iloc[:, 2]]).unique())
CKD_genes = list(pd.concat([all_CKD_genes.iloc[:, 1], all_CKD_genes.iloc[:, 2]]).unique())

# print(len(AKI_genes))
# print(len(CKD_genes))



#print(all_AKI_genes)

AKI_genes = list(all_AKI_genes[1, 2])
# CKD_genes = list(all_CKD_genes[1, 2])

# unique_to_AKI = set(AKI_genes) - set(CKD_genes)
# unique_to_CKD = set(CKD_genes) - set(AKI_genes)
# common_genes = set(AKI_genes) & set(CKD_genes)

# save AKI_genes and CKD_genes to csv
pd.DataFrame(AKI_genes, columns=['AKI_genes']).to_csv('./AMIA2024/AKI_genes_updated.csv', index=False)
# pd.DataFrame(CKD_genes, columns=['CKD_genes']).to_csv('./AMIA2024/CKD_genes.csv', index=False)


# print("Genes unique to AKI:", unique_to_AKI)
# print("Genes unique to CKD:", unique_to_CKD)
# print("Genes common to both AKI and CKD:", common_genes)

# print(f"\nNumber of genes unique to AKI: {len(unique_to_AKI)}")
# print(f"Number of genes unique to CKD: {len(unique_to_CKD)}")
# print(f"Number of genes common to both: {len(common_genes)}")
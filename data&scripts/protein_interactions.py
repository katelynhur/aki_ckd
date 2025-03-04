import matplotlib.pyplot as plt
from matplotlib_venn import venn2

import pandas as pd
AKI_genes = pd.read_excel('AKI gene pairs.xlsx')
CKD_genes = pd.read_excel('CKD gene pairs.xlsx')

# Define sets of genes for AKI and CKD
# Replace these with your actual gene lists
#aki_genes = set(['GENE1', 'GENE2', 'GENE3', 'GENE4', 'GENE5'])
#ckd_genes = set(['GENE3', 'GENE4', 'GENE5', 'GENE6', 'GENE7'])
#aki_genes = set(AKI_genes['Gene 1'])
#ckd_genes = set(CKD_genes['Gene 1'])

# Create the Venn diagram
plt.figure(figsize=(10, 6))
venn2([AKI_genes, CKD_genes], set_labels=('Acute Kidney Injury', 'Chronic Kidney Disease'))

# Add title
plt.title("Gene Overlap between AKI and CKD")

# Save the figure
plt.savefig('aki_ckd_venn_diagram.png')

# Display the diagram (optional, remove if running on a server without display)
plt.show()

# Print some statistics
print(f"Number of genes in AKI: {len(AKI_genes)}")
print(f"Number of genes in CKD: {len(CKD_genes)}")
print(f"Number of overlapping genes: {len(AKI_genes.intersection(CKD_genes))}")


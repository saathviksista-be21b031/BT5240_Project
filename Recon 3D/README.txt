Workflow for project

Model
MATLAB script 'gene_Desc' to get gene names from model nomenclature to descriptive names used in drugbank db

DrugBank
Data_Processing1 script (first half)
Then filter drugs such that only the drugs whose drug targets are present in our model are retained (in same script)

SIDER
has drug names in PubChem cid, need to get drug names in drugbank id
(Script in part 2 of DataProcessing1)
also remove all entries with type as 'indication'
(script in part 2 of dataprocessing1)
Now keep only records where the drugs are in list of drugs of the file drugbank_inhibitor_gsmm.csv
(script in dataprocessing2)
Generate reverse index list (script in dataprocessing2)
Generate drug-gene target mapping to then inactivate (last two scripts in dataprocessing2)

FVA
Data_prcoessing_FVA script
2 parts, first iterates through each drug and inactivates that drugs gene targets and then does FVA and saves bounds to csv file, 2nd part of script normalizes the bounds

SVM_training script
Trains SVM (or an MPP) for each side effect
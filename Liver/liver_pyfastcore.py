from pyfastcore import Fastcore
import cobra
import pandas as pd
from optlang import gurobi_interface

# Load CSV
data = pd.read_csv('C:/Users/Saathvik/Documents/MATLAB/Project_Liver/data/GSMMs/C_liver_Recon1_rxns.csv')

# Convert to list if needed
python_list = data.iloc[:, 0].tolist()
model_x=cobra.io.read_sbml_model("C:/Users/Saathvik/Documents/MATLAB/Project_Liver/data/GSMMs/RECON1.xml")
model_Recon3D=cobra.io.read_sbml_model("C:/Users/Saathvik/Documents/MATLAB/Project_Liver/data/GSMMs/Recon3D.xml")

model_x.solver.interface


core_rxns_recon3d=[]

# Check if all reaction IDs in list1 are in model y
missing_reactions = []
for reaction_id in python_list:
    try:
        core_rxns_recon3d.append(model_Recon3D.reactions.get_by_id(reaction_id))
    except KeyError:
        missing_reactions.append(reaction_id)
print(f"Missing reactions: {len(missing_reactions)}")

penalties = {}
for r in model_Recon3D.exchanges:
    penalties[r.id] = 0
fc_builder = Fastcore(model_Recon3D, core_rxns_recon3d,
                      penalties=penalties,
                      default_penalty=10,
                      debug_mode=True)
print('hey1')
fc_builder.fast_core()
print('hey2')
# checking the list of reaction in the consistent network found
consistent_subnetwork = fc_builder.consistent_subnetwork
print("Consistent subnetworksize set size", len(consistent_subnetwork))
print("Context specific core:")
print(consistent_subnetwork)

# creating a cobra model for the consistent network found
print(f"Building context-specific model for {model_Recon3D.id}")
cs_model = fc_builder.build_context_specific_model()
print(cs_model.summary())

# Running and FBA using subnetwork model 
print("Running FBA on CS-model")
sol = cs_model.optimize()
print(cs_model.summary())

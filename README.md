# DecentralDC

Assessing Data Contribution under Decentralized Sharing and Exchanging BlockChain.

# Introduction of Code

We provide the codes of main experiment for two scale scenarios. Below, we illustrate the code using Scenario #1 as an example (the code structure for Scenario #2 is identical to Scenario #1):

01_create_participant.py, 02_create_behavior_paradigm.py, 03_create_bs.py, and 04_simulate_parallel processing_bs.py are scripts for dataset construction, corresponding to **Step 1** to **Step 4** in Section 5.1.1.

05.1_construct_bx_paradigm_seq_set.py and 05.2_mine_max_seq_pattern.py correspond to **Stage 1** of the proposed method, which involves mining maximal sequential patterns of behavior paradigms in two steps. Note that running 05.2_mine_max_seq_pattern.py requires the installation of the spmf algorithm package(https://pypi.org/project/spmf/) in the Python environment.

06_cal_bx_paradigm_weight.py corresponds to **Stage 2** of the proposed method, which is to calculate the importance weights of behavior paradigms.

07_cal_DBC.py corresponds to **Stage 3** of our method, which is to calculate the contribution of each database participanting in sharing and exchange combined with the amount of data.

evaluate_metrics.py is used to compute precision, recall, and F1 for the VMSP and CM-SPADE methods.

t-fcsm_evaluate_meters.py implements the t-FCSM method and calculates the precision, recall, and F1-score for this method.

# Introduction of Data

We provide the datasets of main experiment for two scale scenarios. Below, we illustrate using Scenario #1 as an example (the situation for Scenario #2 is identical to Scenario #1):

*bx_paradigm_info* contains the defined behavior paradigms for the scenario.

*bx_seq_dataset* contains the sharing and exchanging behavior metadata sequence for the scenario. For ease of subsequent processing, we replace the `provider_id` and `db_id` with `bx_paradigm_ID` in the metadata information, and omit the `data_hash` field.

*collaborative business* refers to the collaborative businesses defined within the scenario.

We provide both *txt* and *pkl* formats of the files. The former facilitates readers to inspect the contents of the dataset, while the latter is intended for actual program processing.
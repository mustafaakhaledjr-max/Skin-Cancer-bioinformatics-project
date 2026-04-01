[README.md](https://github.com/user-attachments/files/26420561/README.md)[Uploading README.md…](Skin Cancer Genomics: FASTQ Dataset Preparation

## Project Purpose
This project focuses on analyzing real-world genomic datasets for **Skin Cancer (Melanoma)** research. we utilize real high-throughput sequencing data (FASTQ) to identify biological differences between healthy skin tissue and melanoma samples. This project serves as a foundation for k-mer analysis, feature extraction, and machine learning classification in bioinformatics.

## Quick Start Guide
To set up the environment and run the project, use these commands: 

1. Create Virtual Environment:
python -m venv bioinfo_env 

2. Activate Environment:
bioinfo_env\Scripts\activate 

3. Install Dependencies:
pip install -r requirements.txt

## Project Structure

- bioinformatics_project/: Main project directory.
- data/: Stores raw FASTQ datasets (SRR samples).
- docs/: Project documentation and metadata (metadata.csv).
- results/: Output from Quality Control and analysis.
- src/: Python scripts for data processing and analysis.
- README.md: Project documentation.
- requirements.txt: Python libraries (Biopython, Pandas, etc.).

## Dataset Sources
The dataset consists of 10 real-world genomic samples retrieved from the NCBI SRA database, focusing on Skin Cancer (Melanoma) research.

| Sample ID | Condition | Label | Source Link |
| :--- | :--- | :--- | :--- |
| SRR14524074 | Skin Cancer (Melanoma) | 1 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524074) |
| SRR14524075 | Skin Cancer (Melanoma) | 1 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524075) |
| SRR14524076 | Skin Cancer (Melanoma) | 1 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524076) |
| SRR14524077 | Skin Cancer (Melanoma) | 1 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524077) |
| SRR14524078 | Skin Cancer (Melanoma) | 1 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524078) |
| SRR14524079 | Healthy Skin (Control) | 0 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524079) |
| SRR14524080 | Healthy Skin (Control) | 0 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524080) |
| SRR14524081 | Healthy Skin (Control) | 0 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524081) |
| SRR14524082 | Healthy Skin (Control) | 0 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524082) |
| SRR14524083 | Healthy Skin (Control) | 0 | [NCBI SRA](https://www.ncbi.nlm.nih.gov/sra/SRR14524083) |)

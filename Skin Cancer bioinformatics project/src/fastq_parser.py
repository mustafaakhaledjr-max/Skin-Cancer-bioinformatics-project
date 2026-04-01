from collections import namedtuple
from pathlib import Path
from Bio import SeqIO


FastqRead = namedtuple("FastqRead", ["id", "sequence", "quality_scores"])

def parse_fastq(filepath):
   
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"FASTQ file not found: {filepath}")
    
    for record in SeqIO.parse(str(filepath), "fastq"):
        yield FastqRead(
            id=record.id,
            sequence=str(record.seq),
            quality_scores=record.letter_annotations['phred_quality']
        )

def count_reads(filepath):
   
    count = 0
    for _ in parse_fastq(filepath):
        count += 1
    return count

if __name__ == "__main__":
    sample_path = r"D:\Skin Cancer bioinformatics project\data\SRR14524074_sample.fastq"
    try:
        num_reads = count_reads(sample_path)
        print(f" Total reads in {sample_path}: {num_reads}")
    except Exception as e:
        print(f" Could not process file: {e}")
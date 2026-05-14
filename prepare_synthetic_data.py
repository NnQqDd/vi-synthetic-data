import os
from tqdm import tqdm
import pandas as pd


if __name__ == "__main__":
    SELECT_PATH = 'metadatas/compact_synthetic.csv'
    METADATA_PATH = 'dataset/metadatas'
    SAVE_PATH = 'metadatas/synthetic.csv'

    df = pd.read_csv(SELECT_PATH)
    texts = []
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        path = os.path.basename(row['filepath']).split('.')[0] + '.txt'
        path = os.path.join(METADATA_PATH, path)
        with open(path, 'r') as f:
            text = f.read()
            texts.append(text.strip())
    
    df['text'] = texts
    df = df.rename(columns={"speaker": "speaker_id"})
    df.to_csv(SAVE_PATH, index=False, encoding='utf-8')
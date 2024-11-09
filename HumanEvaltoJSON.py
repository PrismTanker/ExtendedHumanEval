import pathlib

import pyarrow.parquet as pq
import json

pq_array = pq.read_table(str(pathlib.Path(__file__).parent.resolve())+"/openai_humaneval/test-00000-of-00001.parquet", memory_map=True).to_pydict()

# Standardise separators for future dataset set up
pq_array["prompt"] = list(map(lambda s: s.replace("'''", '"""'), pq_array["prompt"]))

dump =json.dumps(pq_array)

with open(str(pathlib.Path(__file__).parent.resolve())+"/openai_humaneval/HumanEvalOG.json","w+") as f:
    f.write(dump)

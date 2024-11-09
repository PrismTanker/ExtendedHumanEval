import pathlib
import json

with open(str(pathlib.Path(__file__).parent.resolve())+"/openai_humaneval/HumanEvalOG.json", 'r') as f:
    data = json.load(f)

target = str(pathlib.Path(__file__).parent.resolve())+"/openai_humaneval/EditedPrompts/reference.txt"


with open(target,"w+") as f:
    f.write("\n---\n".join(map(lambda s: s.split('"""')[-2].split('>>>')[0].strip(),data['prompt'])))

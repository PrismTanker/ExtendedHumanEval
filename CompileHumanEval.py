import pathlib
import json

fp = str(pathlib.Path(__file__).parent.resolve())+"/openai_humaneval/"

with open(fp + "HumanEvalOG.json", 'r') as f:
    data = json.load(f)

data['prompt_no_context'] = list(map(lambda s: s.split('"""')[-2],data['prompt']))

for key in ['english_only', 'with_error', 'ambiguous', 'ambiguous_with_error']:
    with open(fp + "/EditedPrompts/" + key + ".txt", 'r') as f:
        data['prompt_' + key] = f.read().split("\n---\n")

with open(fp + "HumanEval.json","w+") as f:
    f.write(json.dumps(data))
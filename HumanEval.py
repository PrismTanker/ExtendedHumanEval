import pathlib
import json

IDS = 'task_id'
PROMPTS = 'prompt'
CONTEXTLESS = 'prompt_no_context'
ENGLISH_ONLY = 'prompt_english_only'
ERROR_PROMPTS = 'prompt_with_error' 
AMB_PROMPTS = 'prompt_ambiguous'
AMB_ERROR_PROMPTS = 'prompt_ambiguous_with_error'
SOLS = 'canonical_solution'
TESTS = 'test'
EPS = 'entry_point'

with open(str(pathlib.Path(__file__).parent.resolve())+"/openai_humaneval/HumanEval.json", 'r') as f:
    HUMANEVAL = json.load(f)


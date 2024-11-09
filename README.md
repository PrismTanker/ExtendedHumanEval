# Extended HumanEval Dataset

## Table of Contents
  - [Dataset Description](#dataset-description)
  - [Dataset Example](#dataset-example-problem-73)
  - [Loading the dataset](#loading-the-dataset)
  - [Field Names](#field-names)
  - [Considerations for Using the Data](#considerations-for-using-the-data)

## Dataset Description
This is an extension of the HumanEval dataset released by OpenAI (Chen et al. 2021), compiled as
part of my honors thesis "Generative Program Correctness:
An Iterative Assistant (IA) to improve the quality of AI generated code for novice users" completed
at the University of Queensland in 2024.

For the details of the HumanEval dataset, please 
see the HumanEval [repository](https://github.com/openai/human-eval) and [paper](https://arxiv.org/abs/2107.03374).

This extended dataset adds 5 new prompt variants
for each coding problem present in the dataset.
The added variants systematically decrease the precision of the prompt, to better evaluate how agents may behave under use by a novice user.
The following additional prompt variants are provided:
- No Function signature
- No Function signature and no examples (English only)
- English only with an introduced ambiguity
- English only with an introduced error
- English only with ambiguity AND error

The ambiguities and errors were introduced by hand for each coding problem, and were intended to emulate requirement errors that are likely to occur under a novice user (Think "Non-negative" becoming "Positive").

## Dataset Example (Problem 73)
### Original Prompt
```
def smallest_change(arr):
        """
        Given an array arr of integers, find the minimum number of elements that
        need to be changed to make the array palindromic. A palindromic array 
        is an array that is read the same backwards and forwards. 
        In one change, you can change one element to any other element.

        For example:
        smallest_change([1,2,3,5,4,7,9,6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
        """
```
### No Signature
```
Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array 
    is an array that is read the same backwards and forwards. 
    In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
```
### English Only
```
Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array 
    is an array that is read the same backwards and forwards. 
    In one change, you can change one element to any other element.
```
### Ambiguous
```
Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. 
```
### With Error
```
 Given an array arr of integers, find the minimum number of elements that
    need to be swapped to make the array palindromic. A palindromic array 
    is an array that is read the same backwards and forwards. 
    In one change, you can swap one element with another element.
```
### Ambiguity + Error
```
Given an array arr of integers, find the minimum number of elements that
    need to be swapped to make the array palindromic. 
```

## Loading the dataset
```python
from HumanEval import HUMANEVAL
```
Or if you also want constants for each dataset field:
```python
from HumanEval import *
```

To access data:
```python
HUMANEVAL[<FIELD_NAME>][<PROBLEM_NUMBER>]
```

## Field Names

- `task_id`: identifier for the data sample
- `prompt`: original prompt for the model, containing function header and docstrings
- `prompt_no_context`: `prompt` with function signature removed
- `prompt_english_only`: `prompt_no_context` with examples removed
- `prompt_ambiguous`: `prompt_english_only` with an ambiguity hand-inserted
- `prompt_with_error`: `prompt_english_only` with an error hand-inserted
- `prompt_ambiguous_with_error`: `prompt_ambiguous` with the same error as `prompt_with_error` inserted
- `canonical_solution`: solution for the problem in the `prompt`
- `test`: contains function to test generated code for correctness
- `entry_point`: entry point for test


## Considerations for Using the Data
Make sure you execute generated Python code in a safe environment when evauating against this dataset as generated code could be harmful.

### Original Dataset Curators
OpenAI

### Licensing Information

MIT License
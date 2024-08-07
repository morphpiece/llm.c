from train_gpt2 import GPTConfig, GPT, write_model
from read_checkpoint import get_state
import torch
import tempfile
import pytest

def run_model_test(model, dtype):

    if dtype == 'bfloat16':
        model = model.bfloat16()

    with tempfile.NamedTemporaryFile(suffix='.bin') as tmp_file:
        tmp_file_name = tmp_file.name
        write_model(model, tmp_file_name, dtype=dtype)
        
        loaded_state_dict = get_state(tmp_file_name, dtype=dtype)

        for key in model.state_dict().keys():
            model_tensors = model.state_dict()[key]
            loaded_tensors = loaded_state_dict[key]
            assert torch.equal(model_tensors, loaded_tensors), f"Error: {key} does not match."

@pytest.mark.parametrize("dtype", ["float32", "bfloat16"])
def test_small_model(dtype):
    config = GPTConfig(n_embd=16,n_layer=2,n_head=4,block_size=128,vocab_size=50257)
    model = GPT(config)
    
    run_model_test(model,dtype)

@pytest.mark.parametrize("model_id", ["gpt2"]) # to add future model tests      
def test_hf_model(model_id):
    model = GPT.from_pretrained(model_id)
    dtype = 'float32' # 'float32'
    run_model_test(model,dtype)

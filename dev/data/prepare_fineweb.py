
from datasets import load_dataset
from huggingface_hub import snapshot_download

snapshot_download("HuggingFaceFW/fineweb-edu",repo_type="dataset",local_dir="/pfss/mlde/workspaces/mlde_wsp_MorphPiece/data/fineweb-edu/",allow_patterns="sample/100BT/*")
fw = load_dataset("/pfss/mlde/workspaces/mlde_wsp_MorphPiece/data/fineweb-edu/sample/100BT/")

#python fineweb_mod.py -t ~/data/tokenizers_50k/meta-llama-3-8b-fwedu10b-50k -f ~/data/fineweb-edu/vocab_50k/llmc_100BT_gpt2_50k/
#python fineweb_mod.py -t ~/data/tokenizers_50k/gpt2_morph15k_50k -f ~/data/fineweb-edu/vocab_50k/llmc_100BT_morph15k_50k/
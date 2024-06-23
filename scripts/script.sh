#!/bin/bash

/pfss/mlde/workspaces/mlde_wsp_MorphPiece/git/llm.c/train_gpt2cu \
-i "/pfss/mlde/workspaces/mlde_wsp_MorphPiece/data/fineweb-edu/llmc_fwedu_gpt2_50k/fineweb_train_*.bin" \
-j "/pfss/mlde/workspaces/mlde_wsp_MorphPiece/data/fineweb-edu/llmc_fwedu_gpt2_50k/fineweb_val_*.bin" \
-o /pfss/mlde/workspaces/mlde_wsp_MorphPiece/exps_llmc/log124M \
-e "d12" \
-b 64 -t 2048 \
-d 524288 \
-r 0 \
-z 1 \
-c 0.1 \
-l 0.0006 \
-q 0.0 \
-u 700 \
-n 5000 \
-v 250 -s 20000 \
-h 1 \
-x 20000
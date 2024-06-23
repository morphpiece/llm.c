#!/bin/bash

/pfss/mlde/workspaces/mlde_wsp_MorphPiece/git/llm.c/train_gpt2cu_32k_h \
-i "/pfss/mlde/workspaces/mlde_wsp_MorphPiece/data/fineweb-edu/llmc_morph15k_32k/fineweb_train_*.bin" \
-j "/pfss/mlde/workspaces/mlde_wsp_MorphPiece/data/fineweb-edu/llmc_morph15k_32k/fineweb_val_*.bin" \
-o /pfss/mlde/workspaces/mlde_wsp_MorphPiece/exps_llmc/gpt3m_morph15k_32k \
-p /pfss/mlde/workspaces/mlde_wsp_MorphPiece/git/llm.c/dev/data/hellaswag/hellaswag_val_morph15k_32k.bin \
-e "d24" \
-b 16 -t 2048 \
-d 524288 \
-r 0 \
-z 1 \
-c 0.1 \
-l 0.0003 \
-q 0.1 \
-u 700 \
-n 5000 \
-v 1000 -s 20005 \
-h 1 \
-x 10
#-x 20001
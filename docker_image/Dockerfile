# Specify the correct NVIDIA CUDA image with CUDNN and development tools
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
# FROM determinedai/genai-train

# Install system packages
RUN apt update && apt install -y \
    git wget openmpi-bin openmpi-doc libopenmpi-dev

# Install Miniconda
RUN mkdir -p ~/miniconda3 \
    && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh \
    && bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 \
    && rm ~/miniconda3/miniconda.sh \
    && ~/miniconda3/bin/conda init bash

# Setting the PATH environment variable for conda
ENV PATH /root/miniconda3/bin:$PATH
RUN conda init bash

# RUN conda install --yes pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch-nightly -c nvidia

# Install Python packages
RUN yes | pip install tqdm tiktoken requests datasets

# Clone necessary repositories to the home directory
RUN git clone https://github.com/NVIDIA/cudnn-frontend.git ~/cudnn-frontend \
    && git clone https://github.com/karpathy/llm.c.git ~/llm.c

# Set the working directory
WORKDIR /root/llm.c

# Compile llm.c with mixed precision and cuDNN flash-attention
RUN make train_gpt2cu USE_CUDNN=1

# Tokenize FineWeb dataset
RUN python dev/data/fineweb.py --version 10B

# Set entrypoint for training
ENTRYPOINT ["/root/llm.c/train_gpt2cu", \
            "-i", "dev/data/fineweb10B/fineweb_train_*.bin", \
            "-j", "dev/data/fineweb10B/fineweb_val_*.bin", \
            "-o", "log124M", \
            "-e", "d12", \
            "-b", "64", "-t", "1024", \
            "-d", "524288", \
            "-r", "1", \
            "-z", "1", \
            "-c", "0.1", \
            "-l", "0.0006", \
            "-q", "0.0", \
            "-u", "700", \
            "-n", "5000", \
            "-v", "250", "-s", "20000", \
            "-h", "1"]
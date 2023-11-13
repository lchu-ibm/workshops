import os

from dataclasses import dataclass


@dataclass
class train_config:
    # seed
    seed: int = 2023

    # model
    tokenizer: str = "/lustre/llama_weights/tokenizer.model"
    ckpt_load_path: str = "/lustre/t5/workshops/pretraining/ckpt"
    ckpt_save_path: str = "/lustre/t5/workshops/pretraining/ckpt"

    # data and dataloader
    use_dummy_dataset: bool = False
    data_path: str = "/lustre/bluepile-processing/rel0_5/tokens_llama2/"
    seq_length: int = 4096
    sep_token: int = 0
    # datasets: str = "commoncrawl,webhose,github_clean,wikipedia/lang=de,wikipedia/lang=es,wikipedia/lang=fr,wikipedia/lang=ja,wikipedia/lang=pt,wikimedia,uspto,pubmedcentral,arxiv,stackexchange,PG19"
    # weights: str = "7700,500,550,28,17,22,25,8,100,500,175,250,100,25"
    datasets: str = "lang=en/commoncrawl,lang=en/webhose,lang=en/github_clean,lang=de/wikipedia,lang=es/wikipedia,lang=fr/wikipedia,lang=ja/wikipedia/,lang=pt/wikipedia/,lang=en/wikimedia,lang=en/uspto,lang=en/pubmedcentral,lang=en/arxiv,lang=en/stackexchange,lang=en/PG19"
    weights: str = "7700,500,550,28,17,22,25,8,100,500,175,250,100,25"
    logical_shards: int = 768

    # compile
    use_torch_compile: bool = False

    # profiler
    use_profiler: bool = False

    # tp
    tp_size: int = 1

    # fsdp policies
    mixed_precision: bool = True
    fsdp_activation_checkpointing: bool = False
    selective_checkpointing: int = 1
    sharding_strategy: str = "hsdp"
    sharding_group_size: int = 8
    low_cpu_fsdp: bool = False

    # training spec
    batch_size: int = 2
    num_steps: int = 250000
    learning_rate: float = 3e-4

    # reporting
    report_interval: int = 200
    checkpoint_interval: int = 20000

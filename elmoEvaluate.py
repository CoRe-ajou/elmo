from models.sent_eval import ELMoEmbeddingEvaluator
import numpy as np

model = ELMoEmbeddingEvaluator(
	tune_model_fname="data/sentence-embeddings/elmo/tune-ckpt",
	pretrain_model_fname="data/sentence-embeddings/elmo/pretrain-ckpt/elmo.model",
	options_fname="data/sentence-embeddings/elmo/pretrain-ckpt/options.json",
	vocab_fname="data/sentence-embeddings/elmo/pretrain-ckpt/elmo-vocab.txt",
	max_characters_per_token=30, dimension=256, num_labels=2)

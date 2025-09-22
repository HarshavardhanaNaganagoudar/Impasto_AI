# Model Weights

All LoRA weights are hosted on Hugging Face:

- [impasto_painting_kontext_newest_version-lora](https://huggingface.co/nharshavardhana/impasto_painting_kontext_newest_version-lora)

You can load them directly in `generate.py`:

```python
pipeline.load_lora_weights(
    'nharshavardhana/impasto_painting_kontext_newest_version-lora',
    weight_name='impasto_painting_kontext_newest_version_000000500.safetensors'
)

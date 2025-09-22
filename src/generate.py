# generate.py
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert an image to impasto painting using FLUX.1 Kontext [dev]")
    parser.add_argument("--input_image", type=str, required=True, help="Path to input image")
    parser.add_argument("--prompt", type=str, default="Convert this image to an impasto painting", help="Text prompt for style")
    parser.add_argument("--output", type=str, default="my_image_impasto.png", help="Output file name")
    parser.add_argument("--strength", type=float, default=0.7, help="How much the output should follow the prompt (0-1)")
    args = parser.parse_args()

    # Load base model
    pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-Kontext-dev",
        torch_dtype=torch.bfloat16
    ).to("cuda")

    # Load your LoRA weights from Hugging Face
    pipeline.load_lora_weights(
        "nharshavardhana/impasto_painting_kontext_newest_version-lora",
        weight_name="impasto_painting_kontext_newest_version_000000500.safetensors"
    )

    # Load input image
    input_img = Image.open(args.input_image).convert("RGB")

    # Generate output image
    output_img = pipeline(prompt=args.prompt, image=input_img, strength=args.strength).images[0]

    # Save result
    output_img.save(args.output)
    print(f"Impasto-style image saved to {args.output}")

if __name__ == "__main__":
    main()

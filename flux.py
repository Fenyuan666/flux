import os
import requests
from huggingface_hub import InferenceClient

# 禁用代理设置
os.environ['NO_PROXY'] = '*'
os.environ['no_proxy'] = '*'

client = InferenceClient(
    provider="fal-ai",
    api_key="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",
)

# output is a PIL.Image object
image = client.text_to_image(
    "Astronaut riding a horse",
    model="black-forest-labs/FLUX.1-Krea-dev",
)

# 保存生成的图像
image.save("generated_image.png")
print("图像已保存为 generated_image.png")

# 显示图像（可选）
try:
    image.show()
except Exception as e:
    print(f"无法显示图像: {e}")
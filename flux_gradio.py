import gradio as gr
import os
from huggingface_hub import InferenceClient

# 禁用代理设置
os.environ['NO_PROXY'] = '*'
os.environ['no_proxy'] = '*'

# 初始化客户端
client = InferenceClient(
    provider="fal-ai",
    api_key="替换成你的haggingface token",
)

def generate_image(prompt):
    try:
        # 使用InferenceClient生成图像
        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-Krea-dev",
        )
        return image, f"✅ 生成成功！"
    except Exception as e:
        return None, f"❌ 生成失败: {str(e)}"

# 创建Gradio界面
iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(lines=3, placeholder="输入图像描述...(仅支持英文)", label="提示词"),
    outputs=[
        gr.Image(type="pil", label="生成的图像"),
        gr.Textbox(label="状态", interactive=False)
    ],
    title="🎨 Fy图像生成器",
    description="输入文本描述，生成相应的图像（fy出品）",
    examples=[
        
    ]
)

if __name__ == "__main__":
    iface.launch(share=True) 
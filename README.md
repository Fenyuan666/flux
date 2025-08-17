# FLUX 图像生成器

基于FLUX模型的文本到图像生成应用，使用Gradio构建的Web界面。

## 安装依赖

```bash
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## 运行应用

```bash
python gradio_app.py
```

应用将在 `http://localhost:7860` 启动，并提供一个公共链接供分享。

## 功能特性

- 🎨 文本到图像生成
- 💡 示例提示词
- 📱 响应式Web界面
- 🔄 实时状态反馈
- ⌨️ 支持回车键快速生成

## 使用方法

1. 在文本框中输入图像描述
2. 点击"生成图像"按钮或按回车键
3. 等待图像生成完成
4. 查看生成的图像和状态信息

## 注意事项

- 需要有效的Hugging Face API令牌
- 首次生成可能需要较长时间
- 建议使用详细的描述来获得更好的生成效果 
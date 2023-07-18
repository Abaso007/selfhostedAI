# **[简体中文](./README_ZH.md) | English**

# Self-Hosted AI

The API interface of this project is compatible with openai, and various open-source projects using openai can be easily
adapted. In addition, I also call on everyone to develop compatible API interfaces in a similar way, which is conducive
to the development of related applications.

Go to [release](https://github.com/josStorer/selfhostedAI/releases) to download packaged files

Use `update.bat` to update (without models)

Define the `ngrok_token` environment variable to expose the API to the internet

## Usage Example

Go to https://github.com/josStorer/chatGPTBox, and switch to the following API mode to quickly experience:

<img width=350 src="https://user-images.githubusercontent.com/13366013/230396985-5c55d8bc-55e6-4cc4-a5fa-792838d5b8ea.png"/>

## Chat

1. [RWKV](https://github.com/BlinkDL/RWKV-LM)
    - [8MB Online Installation Program](https://github.com/josStorer/RWKV-Runner/releases)
    - See more in [RWKV-Runner](https://github.com/josStorer/RWKV-Runner)

2. [ChatGLM 6B Int4](https://github.com/THUDM/ChatGLM-6B)
    - [Offline](https://github.com/josStorer/selfhostedAI/releases)
        - This package is based on ChatGLM, open-sourced under the Apache-2.0 license. The built-in model is a trimmed
          version of https://huggingface.co/silver/chatglm-6b-int4-slim.
        - After unzipping, double-click on the corresponding model file to run. For example, `llama.bat` to run
          the llama model, or `chatglm.bat` to run the chatglm model.
    - [Self-Hosted](https://huggingface.co/spaces/josStorer/ChatGLM-6B-Int4-API-OpenAI-Compatible)
        - Click the link above to go to Huggingface, copy the space, switch the CPU to the second 8-core for a fast
          experience, at this time the API address is, `[your name]-[repository name].hf.space`,
          for example, if I copy and set the name to `test`, then my URL would
          be `https://josstorer-test.hf.space/chat/completions`
    - When used with ChatGPTBox, the model name needs to be set to `chatglm-6b-int4`

3. [llama.cpp](https://github.com/ggerganov/llama.cpp)
    - [Offline](https://github.com/josStorer/selfhostedAI/releases)
        - This package is based on llama.cpp. Built-in command line interactive program
          is [the version I modified](https://github.com/josStorer/llama.cpp-unicode-windows)
          to support unicode input on windows, the built-in model is
          from [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)
        - Run `get_llama_model.sh` in WSL or Linux environment to get models. If you already have the model, directly
          replace the `models/llama.cpp/ggml-model-q4_0.bin` file.
        - After unzipping, double-click on the corresponding model file to run. For example, `llama.bat` to run
          the llama model, or `chatglm.bat` to run the chatglm model.
    - When used with ChatGPTBox, the model name needs to be set to `llama-7b-int4`

## Painting

1. [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
    - This project comes with a one-click installer, download
      link: https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/download/v1.0.0-pre/sd.webui.zip
    - Installation steps for other
      systems: https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running
    - For Windows, after downloading and unzipping the above installer, double-click `update.bat`, and then
      run `run.bat`. Subsequently, you can directly run `run.bat` for future launches (at least one model needs to be
      downloaded for normal startup).
    - You can find the model you want to use at https://civitai.com/ and download it. Place the model in
      the `webui\models\Stable-diffusion` directory and place the VAE model in the `webui\models\VAE` directory.
    - Next, open your browser and visit `http://127.0.0.1:7860/`.
    - You may need to set the VAE you downloaded in `Settings -> Stable Diffusion -> SD VAE`.

## Integrated Applications

1. [text-generation-webui](https://github.com/oobabooga/text-generation-webui)
    - This project comes with some one-click installers, download
      link: https://github.com/oobabooga/text-generation-webui#one-click-installers. Simply choose the zip file
      corresponding to your system and download it.

2. [Wenda](https://github.com/wenda-LLM/wenda)
    - This project provides a packaged program, download link: https://pan.baidu.com/s/1idvot-XhEvLLKCbjDQuhyg?pwd=wdai.
    - Steps for use: https://github.com/wenda-LLM/wenda#%E6%87%92%E4%BA%BA%E5%8C%85

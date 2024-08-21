# 책 부록 소스 프로젝트 입니다

직무 교육( OJT, On the job Training )을 위해서 클론 하였습니다.  
책 관련 링크 입니다.  

- [Mastering PyTorch 2nd [ 원서 ]](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=340789975)  

-  


## 개발 및 테스트 환경

- windows 10  
- Python 3.12.0
- pip 23.2.1
- venv  
- VS Code  
- ...  

  ```
  $ python -m venv .venv-local
  $ .venv-local/Scripts/Activate.ps1 
  $ (.venv-local) python --version
  $ (.venv-local) pip --version
  $ (.venv-local) pip install -r requirements.txt
  ```

## 사전 지식

- Python  
- pip  
- venv  
- jypyter notebook  
- ...  

---
---
---


# Mastering PyTorch, Second Edition

This is the code repository for the book [Mastering PyTorch, Second Edition](https://www.amazon.com/Mastering-PyTorch-powerful-learning-architectures-ebook/dp/1801074305), published by Packt.

<img src="https://github.com/arj7192/MasteringPyTorchV2/blob/main/MasteringPyTorch2E.jpg?raw=tru" alt="drawing" width="400"/>

# What is this book about?

PyTorch is making it easier than ever before for anyone to build deep learning applications. This PyTorch deep learning book will help you uncover expert techniques to get the most out of your data and build complex neural network models.

# What you will learn
* Implement text, vision, and music generation models using PyTorch  
* Build a deep Q-network (DQN) model in PyTorch  
* Deploy PyTorch models on mobile devices (Android and iOS)  
* Become well versed in rapid prototyping using PyTorch with fastai  
* Perform neural architecture search effectively using AutoML  
* Easily interpret machine learning models using Captum  
* Design ResNets, LSTMs, and graph neural networks (GNNs)  
* Create language and vision transformer models using Hugging Face

# Who This Book Is for?
This deep learning with PyTorch book is for data scientists, machine learning engineers, machine learning researchers, and deep learning practitioners looking to implement advanced deep learning models using PyTorch. This book is ideal for those looking to switch from TensorFlow to PyTorch. Working knowledge of deep learning with Python is required.

# Notebooks in each chapter


You can run the notebooks directly from the table below: 

| Chapter no. |Chapter title | Notebook/Utility Script (GitHub) | Open in Kaggle | Open in Colab
|:-- |:-- | :-------- | :-------- |  :-------- |
| 1 | Overview of Deep Learning Using PyTorch | [mnist_pytorch.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter01/mnist_pytorch.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter01/mnist_pytorch.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter01/mnist_pytorch.ipynb) |
| | | [mnist_tensorflow.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter01/mnist_tensorflow.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter01/mnist_tensorflow.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter01/mnist_tensorflow.ipynb) |
| 2 |  Deep CNN Architectures | [DenseNetBlock.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/DenseNetBlock.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/DenseNetBlock.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter02/DenseNetBlock.ipynb) |
|  |   | [GoogLeNet.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/GoogLeNet.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/GoogLeNet.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter02/GoogLeNet.ipynb) |
|  |   | [ResNetBlock.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/ResNetBlock.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/ResNetBlock.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter02/ResNetBlock.ipynb) |
|  |   | [lenet.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/lenet.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/lenet.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter02/lenet.ipynb) |
|  |   | [transfer_learning_alexnet.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/transfer_learning_alexnet.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/transfer_learning_alexnet.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter02/transfer_learning_alexnet.ipynb) |
|  |   | [vgg13_pretrained_run_inference.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/vgg13_pretrained_run_inference.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter02/vgg13_pretrained_run_inference.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter02/vgg13_pretrained_run_inference.ipynb) |
| 3 |  Combining CNNs and LSTMs | [image_captioning_pytorch.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter03/image_captioning_pytorch.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter03/image_captioning_pytorch.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter03/image_captioning_pytorch.ipynb) |
| 4 |  Deep Recurrent Model Architectures | [lstm.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter04/lstm.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter04/lstm.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter04/lstm.ipynb) |
|  |   | [rnn.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter04/rnn.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter04/rnn.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter04/rnn.ipynb) |
| 5 |   Advanced Hybrid Models | [out_of_the_box_transformers.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter05/out_of_the_box_transformers.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter05/out_of_the_box_transformers.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter05/out_of_the_box_transformers.ipynb) |
|  |   | [rand_wire_nn.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter05/rand_wire_nn.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter05/rand_wire_nn.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter05/rand_wire_nn.ipynb) |
|  |   | [transformer.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter05/transformer.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter05/transformer.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter05/transformer.ipynb) |
| 6 |   Graph Neural Networks | [GNN.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter06/GNN.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter06/GNN.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter06/GNN.ipynb) |
| 7 |    Music and Text Generation with PyTorch | [music_generation.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/music_generation.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/music_generation.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter07/music_generation.ipynb) |
|  |   | [text_generation.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation.ipynb) |
|  |   | [text_generation_out_of_the_box.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation_out_of_the_box.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation_out_of_the_box.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation_out_of_the_box.ipynb) |
|  |   | [text_generation_out_of_the_box_gpt3.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation_out_of_the_box_gpt3.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation_out_of_the_box_gpt3.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter07/text_generation_out_of_the_box_gpt3.ipynb) |
| 8 |    Neural Style Transfer  | [neural_style_transfer.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter08/neural_style_transfer.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter08/neural_style_transfer.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter08/neural_style_transfer.ipynb) |
| 9 |    Deep Convolutional GANs  | [dcgan.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter09/dcgan.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter09/dcgan.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter09/dcgan.ipynb) |
|  |   | [pix2pix_architecture.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter09/pix2pix_architecture.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter09/pix2pix_architecture.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter09/pix2pix_architecture.ipynb) |
| 10 |    Image Generation Using Diffusion  | [image_generation_using_diffusion.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter10/image_generation_using_diffusion.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter10/image_generation_using_diffusion.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter10/image_generation_using_diffusion.ipynb) |
|  |   | [taj_mahal_image.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter10/taj_mahal_image.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter10/taj_mahal_image.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter10/taj_mahal_image.ipynb) |
|  |   | [text_to_image_generation_using_stable_diffusion_v1_5.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter10/text_to_image_generation_using_stable_diffusion_v1_5.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter10/text_to_image_generation_using_stable_diffusion_v1_5.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter10/text_to_image_generation_using_stable_diffusion_v1_5.ipynb) |
| 11 |    Deep Reinforcement Learning  | [pong.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter11/pong.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter11/pong.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter11/pong.ipynb) |
| 13 |    Operationalizing PyTorch Models into Production  | [mnist_pytorch.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/mnist_pytorch.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/mnist_pytorch.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter13/mnist_pytorch.ipynb) |
|  |   | [model_scripting.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/model_scripting.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/model_scripting.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter13/model_scripting.ipynb) |
|  |   | [model_tracing.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/model_tracing.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/model_tracing.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter13/model_tracing.ipynb) |
|  |   | [onnx.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/onnx.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/onnx.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter13/onnx.ipynb) |
|  |   | [run_inference.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/run_inference.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter13/run_inference.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter13/run_inference.ipynb) |
| 15 |    Rapid Prototyping with PyTorch  | [fastai.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/fastai.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/fastai.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter15/fastai.ipynb) |
|  |   | [poutyne.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/poutyne.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/poutyne.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter15/poutyne.ipynb) |
|  |   | [pytorch_lightning.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/pytorch_lightning.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/pytorch_lightning.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter15/pytorch_lightning.ipynb) |
|  |   | [pytorch_profiler.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/pytorch_profiler.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter15/pytorch_profiler.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter15/pytorch_profiler.ipynb) |
| 16 |    PyTorch and AutoML  | [automl-pytorch.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter16/automl-pytorch.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter16/automl-pytorch.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter16/automl-pytorch.ipynb) |
|  |   | [optuna_pytorch.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter16/optuna_pytorch.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter16/optuna_pytorch.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter16/optuna_pytorch.ipynb) |
| 17 |    PyTorch and Explainable AI  | [captum_interpretability.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter17/captum_interpretability.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter17/captum_interpretability.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter17/captum_interpretability.ipynb) |
|  |   | [pytorch_interpretability.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter17/pytorch_interpretability.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter17/pytorch_interpretability.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter17/pytorch_interpretability.ipynb) |
| 18 |    Recommendation Systems with PyTorch  | [torch-recsys.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter18/torch-recsys.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter18/torch-recsys.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter18/torch-recsys.ipynb) |
| 19 |    PyTorch and Hugging Face  | [HuggingFaceAccelerate.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceAccelerate.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceAccelerate.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceAccelerate.ipynb) |
|  |   | [HuggingFaceDatasets.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceDatasets.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceDatasets.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceDatasets.ipynb) |
|  |   | [HuggingFaceHub.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceHub.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceHub.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceHub.ipynb) |
|  |   | [HuggingFaceOptimum.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceOptimum.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceOptimum.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFaceOptimum.ipynb) |
|  |   | [HuggingFacePyTorch.ipynb](https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFacePyTorch.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFacePyTorch.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arj7192/MasteringPyTorchV2/blob/main/Chapter19/HuggingFacePyTorch.ipynb) |


## Know more on the Discord server <img alt="Coding" height="25" width="32"  src="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_400.gif">
You can get more engaged on the discord server for more latest updates and discussions in the community at [Discord](https://packt.link/mastorch)

## Download a free PDF <img alt="Coding" height="25" width="40" src="https://emergency.com.au/wp-content/uploads/2021/03/free.gif">

_If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost. Simply click on the link to claim your free PDF._
[Free-Ebook](https://download.packt.com/free-ebook/9781801074308) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">

We also provide a PDF file that has color images of the screenshots/diagrams used in this book at [GraphicBundle](https://packt.link/gbp/9781801074308) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">


## Get to know the Author
_Ashish Ranjan Jha_ studied electrical engineering at IIT Roorkee, computer science at École Polytechnique
Fédérale de Lausanne (EPFL), and he also completed his MBA at Quantic School of Business,
with a distinction in all three degrees. He has worked for bigger tech companies like Oracle and Sony,
and recent tech unicorns – Revolut and Tractable, in the fields of data science, machine learning and
artificial intelligence. He currently works as head of ML and AI at XYZ Reality, based in London (a
construction tech start-up where construction meets AR/VR meets ML/AI to enable real-time data
driven construction intelligence). He is also an advisor to SUIND, an agritech startup that uses drones
for intelligence. Along with that, he has also authored a book, _Fight Fraud with Machine Learning_.

## Other Related Books
- [Machine Learning with PyTorch and Scikit-Learn](https://www.packtpub.com/product/machine-learning-with-pytorch-and-scikit-learn/9781801819312)
- [Python Data Cleaning Cookbook – Second Edition](https://www.packtpub.com/product/python-data-cleaning-cookbook-second-edition/9781803239873)


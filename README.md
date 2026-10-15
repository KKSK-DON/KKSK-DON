<p align="center">
  <img src="./assets/banner.svg" alt="Yang Liu, LLM inference and AI infrastructure engineer" width="100%">
</p>

## Hi, I'm Yang

I contribute to vLLM and RL-Kernel, and I have 3+ years of full-stack experience in the U.S.

<p>
  <a href="https://kksk-don.github.io"><img alt="Website" src="https://img.shields.io/badge/Website-1F2937?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIvPjxwYXRoIGQ9Ik0yIDEyaDIwTTEyIDJhMTUuMyAxNS4zIDAgMCAxIDQgMTAgMTUuMyAxNS4zIDAgMCAxLTQgMTAgMTUuMyAxNS4zIDAgMCAxLTQtMTAgMTUuMyAxNS4zIDAgMCAxIDQtMTB6Ii8+PC9zdmc+"></a>
  <a href="https://www.linkedin.com/in/YL5689"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge"></a>
  <a href="mailto:lymailforjob@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-1F2937?style=for-the-badge&logo=gmail&logoColor=EA4335"></a>
</p>

## What I work on

**Truckpedia**
- GLM-4.6V runs at W8A8C8 with calibrated FP8 KV-cache scales, on a TP4×DP2 + EP8 + SP layout chosen by measurement. Removing a CPU bottleneck under structured output raised throughput 1.86×.

**vLLM** (5 merged PRs)
- Removed 24 per-block CUDA device-to-host syncs from the GLM-4.xV vision encoder: ViT time down about 10%, multimodal prefill down about 5%.
- Computed GLM-4.xV M-RoPE positions from `mm_position`: 6.1× faster on images and 3.2× on video. Fixed video tokens being treated as text along the way.
- Co-authored support for the Isaac-0.1 multimodal model, and moved the request Processor out of `AsyncLLM`.

**RL-Kernel**
- A deterministic CUDA backward kernel for the DeepSeek-V4 MoE router, with 28 tests on H100 that include bit-for-bit comparison against a reference implementation.

**Side projects**
- INT8 KV cache in a vLLM fork: same accuracy as BF16 on GSM8K and HumanEval, twice the KV capacity.
- CUDA kernels on H100: LayerNorm and RMSNorm at about 81% of peak bandwidth, GEMM at 75% of cuBLAS.
- MoE all-to-all dispatch and combine written from scratch, with outputs matching DeepEP V2.

## Tech stack

**AI infrastructure**<br>
<img alt="CUDA" src="https://img.shields.io/badge/CUDA-1F2937?style=for-the-badge&logo=nvidia&logoColor=76B900">
<img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-1F2937?style=for-the-badge&logo=pytorch&logoColor=EE4C2C">
<img alt="Python" src="https://img.shields.io/badge/Python-1F2937?style=for-the-badge&logo=python&logoColor=FFD43B">
<img alt="C++" src="https://img.shields.io/badge/C%2B%2B-1F2937?style=for-the-badge&logo=cplusplus&logoColor=white">
<img alt="Nsight Compute" src="https://img.shields.io/badge/Nsight_Compute-1F2937?style=for-the-badge&logo=nvidia&logoColor=76B900">
<img alt="Linux" src="https://img.shields.io/badge/Linux-1F2937?style=for-the-badge&logo=linux&logoColor=FCC624">

**Backend & cloud**<br>
<img alt="Node.js" src="https://img.shields.io/badge/Node.js-1F2937?style=for-the-badge&logo=nodedotjs&logoColor=5FA04E">
<img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-1F2937?style=for-the-badge&logo=typescript&logoColor=3178C6">
<img alt="Java" src="https://img.shields.io/badge/Java-1F2937?style=for-the-badge&logo=openjdk&logoColor=white">
<img alt="Spring" src="https://img.shields.io/badge/Spring-1F2937?style=for-the-badge&logo=spring&logoColor=6DB33F">
<img alt=".NET" src="https://img.shields.io/badge/.NET-1F2937?style=for-the-badge&logo=dotnet&logoColor=white">
<img alt="Go" src="https://img.shields.io/badge/Go-1F2937?style=for-the-badge&logo=go&logoColor=00ADD8">
<img alt="MySQL" src="https://img.shields.io/badge/MySQL-1F2937?style=for-the-badge&logo=mysql&logoColor=white">
<img alt="Redis" src="https://img.shields.io/badge/Redis-1F2937?style=for-the-badge&logo=redis&logoColor=FF4438">
<img alt="AWS" src="https://img.shields.io/badge/AWS-1F2937?style=for-the-badge">
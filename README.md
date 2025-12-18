# KG-Agent

Paper: KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph
Link: http://arxiv.org/abs/2402.11163v1

Overview

KG-Agent is a minimal reference implementation and skeleton for the KG-Agent framework described in the paper. The framework integrates an LLM-based decision maker, a multifunctional toolbox, a KG-based executor, and a knowledge memory to enable autonomous multi-hop reasoning over knowledge graphs.

This repository provides a lightweight Python package structure with core interfaces and an example demonstrating how to wire components together.

Quickstart

1. Create a virtual environment with Python 3.10+
2. pip install -r requirements.txt
3. Run the example:

   python -m examples.basic

Files

- framework_name/ - core package implementing the KG-Agent skeleton
- examples/basic.py - small runnable example using dummy components
- setup.py - minimal package config
- requirements.txt - dependencies
- Dockerfile - container recipe

Notes

- This repository contains skeleton code with TODO markers: it is intended as a starting point for implementing the methods and integrating a production LLM or KG backend.
- The authors of the original paper plan to release their code and data; this repo is an independent reconstruction for research/development purposes.

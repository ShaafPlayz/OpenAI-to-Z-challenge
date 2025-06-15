# OpenAI-to-Z Challenge

This repository contains Shaaf's comprehensive exploration of OpenAI technologies, from A to Z, including integration with Google Earth Engine for geospatial AI applications.

## 🚀 Project Overview

This project demonstrates various OpenAI capabilities and integrations:
- **OpenAI API Integration**: GPT models and AI chat completions
- **Google Earth Engine Integration**: Geospatial data analysis with AI
- **Research Notebooks**: Interactive exploration and experimentation
- **Multiple AI Model Access**: Including GitHub Models integration

## 📁 Project Structure

```
OpenAI-to-Z-challenge/
├── OpenAI.py                 # Main OpenAI API implementation
├── OpenAI-o3.py             # OpenAI o3 model experiments
├── GoogleEarthEngine.py     # Google Earth Engine integration
├── Offical_OpenAI_Key.py    # API key management
├── openai-research.ipynb    # Jupyter notebook for research
├── requirements.txt         # Full environment dependencies
├── requirements-minimal.txt # Essential project dependencies
├── environment.yml          # Conda environment configuration
├── .env                     # Environment variables (not in repo)
└── README.md               # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.12.4
- Conda (Anaconda/Miniconda)
- OpenAI API Key
- Google Earth Engine Account

### Environment Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/OpenAI-to-Z-challenge.git
   cd OpenAI-to-Z-challenge
   ```

2. **Create and Activate Conda Environment**
   ```bash
   # Create the environment
   conda env create -f environment.yml
   
   # Or create manually
   conda create -n OpenAI-GoogleEngine python=3.12.4
   conda activate OpenAI-GoogleEngine
   ```

3. **Install Dependencies**
   ```bash
   # Option 1: Install minimal requirements (recommended)
   pip install -r requirements-minimal.txt
   
   # Option 2: Install full environment
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the project root:
   ```env
   GITHUB_TOKEN=your_github_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Google Earth Engine Authentication**
   ```bash
   earthengine authenticate
   ```

## 🔧 Usage

### OpenAI Integration
```python
python OpenAI.py
```

### Google Earth Engine
```python
python GoogleEarthEngine.py
```

### Jupyter Research
```bash
jupyter notebook openai-research.ipynb
```

## 📦 Key Dependencies

- **openai**: OpenAI API client
- **earthengine-api**: Google Earth Engine Python API
- **geemap**: Interactive mapping with Google Earth Engine
- **python-dotenv**: Environment variable management
- **pandas**: Data manipulation and analysis
- **jupyter**: Interactive computing environment

## 🔑 API Keys Required

1. **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/)
2. **GitHub Token**: For GitHub Models access
3. **Google Earth Engine**: Sign up at [Google Earth Engine](https://earthengine.google.com/)

## 🚀 Features

- ✅ OpenAI GPT integration
- ✅ GitHub Models access
- ✅ Google Earth Engine geospatial analysis
- ✅ Jupyter notebook research environment
- ✅ Environment management with conda
- ✅ Secure API key handling

## 🧪 Research Areas

This repository explores:
- Natural Language Processing with OpenAI
- Geospatial AI applications
- Multi-modal AI interactions
- Environmental data analysis
- AI-powered mapping solutions

## 📄 License

This project is part of the OpenAI to Z challenge educational initiative.

---
*Last updated: June 15, 2025*
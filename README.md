# OpenAI-to-Z Challenge

This repository contains Shaaf's comprehensive exploration of OpenAI technologies, from A to Z, including integration with Google Earth Engine for geospatial AI applications.

## 🚀 Project Overview

This project demonstrates various OpenAI capabilities and integrations:
- **OpenAI API Integration**: GPT models and AI chat completions
- **Google Earth Engine Integration**: Geospatial data analysis with AI
- **Research Notebooks**: Interactive exploration and experimentation
- **Multiple AI Model Access**: Including GitHub Models integration

## 🧪 Research Areas

This repository explores:
- Natural Language Processing with OpenAI
- Geospatial AI applications
- Multi-modal AI interactions
- Environmental data analysis
- AI-powered mapping solutions
- Interactive widget development for data visualization
- Jupyter notebook optimization for geospatial workflows

## 📁 Project Structure

```
OpenAI-to-Z-challenge/
├── OpenAI.py                 # Main OpenAI API implementation
├── OpenAI-o3.py             # OpenAI o3 model experiments
├── GoogleEarthEngine.py     # Google Earth Engine integration
├── Offical_OpenAI_Key.py    # API key management
├── openai-research.ipynb    # General OpenAI research notebook
├── EarthEngineResearch.ipynb # Google Earth Engine research notebook
├── test_widget.py           # Widget testing and troubleshooting
├── earth_engine_map.html    # Generated HTML map (backup display)
├── requirements.txt         # Full environment dependencies
├── requirements-minimal.txt # Essential project dependencies
├── environment.yml          # Conda environment configuration
├── sat/                     # Satellite data and analysis
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
# General OpenAI research
jupyter notebook openai-research.ipynb

# Google Earth Engine research
jupyter notebook EarthEngineResearch.ipynb
```

### Widget Troubleshooting
If widgets don't display in Jupyter notebook:
```bash
# Test widget functionality
python test_widget.py

# Upgrade ipywidgets (if needed)
pip install --upgrade ipywidgets

# Restart Jupyter server after upgrade
```

## 📦 Key Dependencies

- **openai**: OpenAI API client
- **earthengine-api**: Google Earth Engine Python API
- **geemap**: Interactive mapping with Google Earth Engine
- **ipywidgets**: Interactive widgets for Jupyter (v8.1.7+)
- **python-dotenv**: Environment variable management
- **pandas**: Data manipulation and analysis
- **jupyter**: Interactive computing environment

## 🔧 Known Issues & Solutions

### Widget Display Issues
- **Problem**: "Error displaying widget" in Jupyter notebooks
- **Solution**: Upgraded to ipywidgets 8.1.7, added widget configuration cells
- **Fallback**: HTML export available (`earth_engine_map.html`)

### Environment Setup
- **Conda Environment**: `OpenAI-GoogleEngine` 
- **Python**: 3.12.4
- **Widget Support**: Works in VS Code, configured for Jupyter notebook

## 📄 License

This project is part of the OpenAI to Z challenge educational initiative.

---
*Last updated: June 15, 2025*

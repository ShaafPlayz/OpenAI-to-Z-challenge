# 🌍 AI-Powered Amazon Rainforest Anomaly Detection

**Hackathon Submission**: Automated detection of deforestation and land-use changes in the Amazon rainforest using OpenAI GPT-4.1 vision models and satellite imagery.


## Current Problem
Modis dataset is very coarse, it has a 500m accuracy. I need to get a much sharper dataset.

## 🎯 What It Does

This system automatically detects environmental changes in the Amazon rainforest by:
1. **Fetching current satellite imagery** from Google Earth Engine (Sentinel-2)
2. **Comparing with historical data** (MODIS 2020 baseline)
3. **Using AI vision models** to identify deforestation, construction, and land-use changes
4. **Generating detailed reports** with coordinates and analysis

## ⚡ Quick Demo
![image](https://github.com/user-attachments/assets/1033fd95-0a25-473e-9f78-d2d27ef08bc7)

## 🚀 Key Features

- **AI-Powered Analysis**: GPT-4.1 vision model analyzes satellite imagery
- **Real Satellite Data**: Live Sentinel-2 imagery via Google Earth Engine
- **Automated Detection**: Identifies deforestation, roads, and urban expansion
- **Geographic Validation**: Analysis constrained to Amazon rainforest boundaries
- **Batch Processing**: Analyzes multiple locations automatically

## 🛠️ Quick Start (5 Minutes)

### Prerequisites
- Python 3.12+
- GitHub Token (free)
- Google Earth Engine account (free)

### 1. Clone & Setup
```bash
git clone https://github.com/ShaafPlayz/OpenAI-to-Z-challenge.git
cd OpenAI-to-Z-challenge
pip install -r requirements-minimal.txt
```

### 2. Configure APIs
Create `.env` file:
```env
GITHUB_TOKEN=your_github_token_here
```

### 3. Google Earth Engine Setup
```bash
earthengine authenticate
# Follow the browser authentication
```

### 4. Run the Analysis
```bash
jupyter notebook "GEE and OpenAI Research.ipynb"
# Open the notebook and run all cells
```

**That's it!** The system will automatically:
- Generate random points in the Amazon rainforest
- Fetch current satellite imagery
- Compare with historical land cover data
- Use AI to detect and report anomalies

## 📁 Project Structure

```
OpenAI-to-Z-challenge/
├── 📄 .env                                   # Environment variables (local)
├── � .gitignore                             # Git ignore rules
├── � README.md                              # Project documentation
├── � environment.yml                        # Conda environment configuration
├── � package-lock.json                      # Node.js dependencies lock file
├── �📝 requirements.txt                       # Full Python dependencies
├── 📝 requirements-minimal.txt               # Essential Python dependencies
├── 📓 GEE and OpenAI Research.ipynb          # Main research notebook
├── 📁 .git/                                 # Git repository data
├── 📁 .ipynb_checkpoints/                    # Jupyter notebook checkpoints
├── 📁 amazonia_boundary_proposal/              # Amazon boundary shapefiles
│   ├── 🗺️ amazonia_polygons.dbf              # Shapefile attribute data
│   ├── 🗺️ amazonia_polygons.prj              # Projection information
│   ├── 🗺️ amazonia_polygons.sbn              # Spatial index binary
│   ├── 🗺️ amazonia_polygons.sbx              # Spatial index
│   ├── 🗺️ amazonia_polygons.shp              # Main shapefile geometry
│   ├── 🗺️ amazonia_polygons.shp.xml          # Metadata
│   └── 🗺️ amazonia_polygons.shx              # Shapefile index
├── 📁 AppEEARS/                             # NASA AppEEARS MODIS datasets
│   ├── 🗺️ MCD12Q1.061_LC_Prop2_doy2020001_aid0001.tif  # MODIS 2020 land cover
│   ├── 🗺️ MCD12Q1.061_LC_Prop2_doy2021001_aid0001.tif  # MODIS 2021 land cover
│   ├── 🗺️ MCD12Q1.061_LC_Prop2_doy2022001_aid0001.tif  # MODIS 2022 land cover
│   ├── 🗺️ MCD12Q1.061_LC_Prop2_doy2023001_aid0001.tif  # MODIS 2023 land cover
│   ├── 🗺️ MCD12Q1.061_QC_doy2020001_aid0001.tif        # MODIS 2020 quality control
│   ├── 🗺️ MCD12Q1.061_QC_doy2021001_aid0001.tif        # MODIS 2021 quality control
│   ├── 🗺️ MCD12Q1.061_QC_doy2022001_aid0001.tif        # MODIS 2022 quality control
│   └── 🗺️ MCD12Q1.061_QC_doy2023001_aid0001.tif        # MODIS 2023 quality control
├── 📁 AppEEARSjpg/                          # Processed MODIS imagery (empty)
├── 📁 Resources/                            # Additional resources
│   ├── 🗂️ amazon_biome_border.zip          # Original biome shapefile data
│   └── 🗂️ amazonia_boundary_proposal_Eva_2005 (1).zip  # Boundary proposal data
├── 📁 satimagery/                           # Satellite imagery data
│   ├── 🖼️ sentinel_rgb.jpg                  # Processed RGB satellite image
│   └── 🗺️ sentinel_rgb.tif                  # Raw satellite data (GeoTIFF)
├── 📁 Technology Testing (Scripts)/          # Python scripts for testing
│   ├── 📄 .env                              # Local environment variables
│   ├── 🐍 GoogleEarthEngine.py              # Google Earth Engine integration
│   ├── 🔐 Offical_OpenAI_Key.py             # API key management
│   ├── 🤖 OpenAI-o3.py                      # OpenAI o3 model experiments
│   └── 🤖 OpenAI.py                         # Main OpenAI API implementation
└── 📁 WorkFlow Testing (Jupyter Notebooks)/ # Jupyter notebooks
    └── 📓 openai-research.ipynb              # Additional research notebook
```

## � How It Works

### The Analysis Pipeline
1. **Boundary Validation**: Ensures coordinates are within Amazon rainforest
2. **Satellite Data Fetch**: Downloads current Sentinel-2 imagery (10m resolution)
3. **Historical Lookup**: Retrieves MODIS 2020 land cover classification
4. **AI Analysis**: GPT-4.1 compares current vs. historical imagery
5. **Anomaly Detection**: Reports deforestation, construction, or land-use changes

### Key Functions
- `find_and_log_anomalies()`: Main detection pipeline
- `getAmazoniaAnalysisPoints()`: Generates valid Amazon coordinates
- `get_modis_class_for_point()`: Gets historical land cover data
- `promptGPT()`: Sends imagery to AI for analysis

## 📊 Sample Output
```
Footprint ID: 1 at (-2.8234, -60.1234)
Historical (MODIS) Class: Evergreen Needleleaf Trees
Status: Anomaly Found - Construction activity detected
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.12+ 
- Conda (Anaconda/Miniconda)
- GitHub Token (for GitHub Models access)
- Google Earth Engine Account
- OpenAI API Key (optional)

### Environment Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/OpenAI-to-Z-challenge.git
   cd OpenAI-to-Z-challenge
   ```

2. **Create and Activate Conda Environment**
   ```bash
   # Create the environment from YAML
   conda env create -f environment.yml
   conda activate OpenAI-GoogleEngine
   
   # Or create manually
   conda create -n OpenAI-GoogleEngine python=3.12
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
   OPENAI_API_KEY=your_openai_api_key_here  # Optional
   ```

5. **Google Earth Engine Authentication**
   ```bash
   # First time setup
   earthengine authenticate
   
   # Initialize with your project
   # Replace 'your-project-id' with your actual GEE project ID
   ```

## 🔧 Usage

### Main Research Notebook
```bash
# Launch Jupyter and open the main research notebook
jupyter notebook "GEE and OpenAI Research.ipynb"
```

### Individual Components

#### OpenAI Integration
```python
# Run OpenAI experiments
python "Technology Testing (Scripts)/OpenAI.py"
```

#### Google Earth Engine
```python
# Test GEE functionality
python "Technology Testing (Scripts)/GoogleEarthEngine.py"
```

#### Satellite Imagery Analysis
The main workflow combines both GEE and OpenAI with external datasets:
1. **Fetch Sentinel-2 satellite imagery** from Amazon region via Google Earth Engine
2. **Process and export imagery data** to local storage formats
3. **Convert to AI-readable format** with brightness enhancement
4. **Analyze using OpenAI vision models** with geospatial analyst prompting
5. **Generate natural language descriptions** of surface features
6. **Process MODIS land cover data** from NASA AppEEARS
7. **Generate statistical reports** with AI-powered insights

### Function-Based Workflow
The notebook includes modular functions for streamlined analysis:
- `getSatImageryGEE()`: Fetch satellite data from coordinates
- `downloadSatIGEE()`: Export imagery to local storage  
- `GEE_to_brightJPG()`: Convert and enhance images
- `prepareJPG_forOpenAI()`: Encode for AI model consumption
- `getGEEImagery()`: Complete pipeline from coordinates to AI-ready image
- `promptModel()`: Multi-modal AI analysis with images
- `promptONLY()`: Text-only AI analysis for reports

## 🌍 Example Analysis

The notebook demonstrates comprehensive analysis of the Amazon rainforest region near Manaus, Brazil:

### Sentinel-2 Visual Analysis
- **Coordinates**: -61.355873, -3.314660 (Manaus, Brazil)
- **Analysis Area**: 7km buffer around coordinates  
- **Data Period**: June 2023 - June 2024
- **Image Resolution**: 10m/pixel (Sentinel-2)
- **AI Model**: OpenAI GPT-4.1 via GitHub Models

### MODIS Land Cover Analysis
- **Dataset**: MCD12Q1.061 Land Cover Type (2020-2023 time series)
- **Classification**: Plant Functional Type (PFT) classes
- **Quality Control**: Dedicated QC datasets for each year
- **Analysis**: Pixel-level land cover statistics and temporal changes
- **Geospatial Context**: Amazon biome boundary integration
- **Output**: Automated markdown reports with multi-year insights

### Analysis Results
The system can identify and quantify:
- **Evergreen Needleleaf Trees**: Primary forest coverage
- **Deciduous Needleleaf Trees**: Seasonal vegetation
- **Flooded Vegetation**: Wetland and riverine areas
- **Urban Areas**: Human settlement detection
- **Unknown/No Data**: Data quality assessment

## � Tech Stack

- **AI Model**: OpenAI GPT-4.1 (via GitHub Models API)
- **Satellite Data**: Google Earth Engine (Sentinel-2)
- **Historical Data**: NASA MODIS Land Cover (2020-2023)
- **Languages**: Python, Jupyter Notebooks
- **Key Libraries**: `openai`, `earthengine-api`, `geopandas`, `rasterio`

## 🎯 Impact

This system can help:
- **Environmental Organizations**: Monitor deforestation in real-time
- **Government Agencies**: Track illegal logging and land-use violations
- **Research Institutions**: Study climate change impacts
- **Conservation Efforts**: Protect endangered ecosystems

---

**Ready to try it?** Just run the Quick Start above! 🚀

*Hackathon Submission - June, 2025*
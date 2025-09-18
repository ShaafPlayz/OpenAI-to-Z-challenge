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
![image](https://github.com/user-attachments/assets/3b4ecc0e-0709-4b1f-9f23-a86120be9847)

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

---

**Ready to try it?** Just run the Quick Start above! 🚀

*Hackathon Submission - June, 2025*

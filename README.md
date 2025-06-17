# OpenAI-to-Z Challenge

This repository contains Shaaf's comprehensive exploration of OpenAI technologies, from A to Z, including integration with Google Earth Engine for geospatial AI applications and satellite imagery analysis.

## Current CheckPoint Output
![image](https://github.com/user-attachments/assets/1033fd95-0a25-473e-9f78-d2d27ef08bc7)




## 🚀 Project Overview

This project demonstrates advanced AI capabilities combining OpenAI's vision models with satellite imagery:
- **OpenAI Vision API Integration**: Multi-modal AI for satellite image analysis
- **Google Earth Engine Integration**: Sentinel-2 satellite data processing
- **Satellite Imagery Analysis**: Automated surface feature identification
- **Research Notebooks**: Interactive exploration and experimentation
- **Multiple AI Model Access**: Including GitHub Models integration

## 🧪 Research Areas

This repository explores cutting-edge applications of AI in geospatial analysis:
- **Multi-modal AI**: Combining satellite imagery with natural language processing
- **Environmental Monitoring**: Using Sentinel-2 and MODIS data for comprehensive surface analysis
- **Land Cover Classification**: MODIS PFT (Plant Functional Type) analysis with AI interpretation
- **Cloud Computing**: Leveraging Google Earth Engine's planetary-scale data
- **Computer Vision**: Automated interpretation of satellite imagery
- **External Dataset Integration**: NASA AppEEARS data processing and analysis
- **Geospatial AI**: Location-based analysis and mapping solutions

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
├── 📁 amazon_biome_border/                   # Amazon biome shapefile data
│   ├── 🗺️ amazon_biome_border.cpg           # Character encoding info
│   ├── 🗺️ amazon_biome_border.dbf           # Attribute data
│   ├── 🗺️ amazon_biome_border.prj           # Projection information
│   ├── 🗺️ amazon_biome_border.shp           # Shapefile geometry
│   └── 🗺️ amazon_biome_border.shx           # Shapefile index
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
│   └── 🗂️ amazon_biome_border.zip          # Zipped shapefile data
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

## 🛰️ Satellite Imagery Analysis

The main research notebook (`GEE and OpenAI Research.ipynb`) demonstrates a comprehensive multi-dataset analysis workflow:

### Data Processing Pipeline
1. **Sentinel-2 Data Collection**: Automated cloud-masked satellite imagery from Amazon rainforest
2. **Image Processing**: Converting GeoTIFF to RGB format for AI analysis
3. **Multi-modal AI Analysis**: Using OpenAI's vision models to describe surface features
4. **MODIS Land Cover Analysis**: External NASA AppEEARS dataset integration
5. **Automated Interpretation**: Natural language descriptions and formatted reports

### Advanced Features
- **Modular Function Architecture**: Streamlined workflow with reusable functions
- **Multi-Dataset Integration**: Combining Google Earth Engine and NASA AppEEARS data
- **System Role Prompting**: AI configured as a geospatial analyst for domain-specific responses
- **Automated Report Generation**: Markdown-formatted analysis reports
- **Land Cover Classification**: MODIS PFT (Plant Functional Type) pixel analysis

### Key Datasets
- **Primary**: Copernicus Sentinel-2 SR Harmonized (Google Earth Engine)
- **Secondary**: MODIS MCD12Q1.061 Land Cover Type (NASA AppEEARS)
  - Multi-year time series: 2020-2023 annual land cover data
  - Quality control datasets for each year
- **Geospatial**: Amazon biome boundary shapefile data
- **Location**: Manaus, Brazil (Amazon Rainforest region)
- **Time Range**: 2023-2024 Sentinel-2 imagery with cloud filtering
- **AI Model**: GPT-4.1 vision capabilities via GitHub Models

### Analysis Capabilities
- **Surface Feature Detection**: Automated identification of vegetation, water bodies, urban areas
- **Land Cover Statistics**: Pixel-level classification and reporting
- **Multi-spectral Analysis**: RGB band processing and enhancement
- **Geospatial Context**: Location-specific analysis with coordinate-based queries

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

## 📦 Key Dependencies

### Core Libraries
- **openai**: OpenAI API client for GPT models
- **earthengine-api**: Google Earth Engine Python API
- **geemap**: Interactive mapping with Google Earth Engine
- **python-dotenv**: Environment variable management

### Data Processing
- **Pillow (PIL)**: Image processing and format conversion
- **numpy**: Numerical computing for image arrays
- **rasterio**: Geographic raster data I/O for TIFF files
- **h5py**: HDF5 file format support
- **requests**: HTTP library for data downloads

### Geospatial Analysis
- **shapely**: Geometric objects and spatial operations
- **folium**: Interactive map visualizations
- **collections.Counter**: Data counting and statistics

### Development Environment
- **jupyter**: Interactive computing environment
- **ipython**: Enhanced interactive Python shell
- **IPython.display**: Rich display capabilities for notebooks

### Satellite Data Processing
- **GDAL**: Geospatial Data Abstraction Library (via earthengine-api)
- **Rasterio**: Geographic raster data I/O (indirect dependency)

## 🚀 Features

### Core Capabilities
- **Automated Satellite Data Collection**: Fetch and process Sentinel-2 imagery
- **Multi-Dataset Integration**: Combine Google Earth Engine with NASA AppEEARS data
- **Cloud Masking**: Automatic cloud filtering for clearer imagery
- **Multi-format Export**: TIF and JPG image generation
- **AI-Powered Analysis**: Computer vision analysis of satellite imagery

### Advanced Analysis
- **MODIS Land Cover Processing**: Automated PFT classification and pixel counting
- **Interactive Mapping**: Visualize satellite data with geemap and folium
- **Base64 Encoding**: Prepare images for AI model consumption
- **System Role Configuration**: AI assistant configured as geospatial analyst
- **Modular Function Architecture**: Reusable, well-structured code organization

### Output Generation
- **Natural Language Descriptions**: Human-readable surface feature analysis
- **Formatted Reports**: Markdown-structured analysis reports
- **Statistical Summaries**: Land cover classification statistics
- **Multi-modal Responses**: Text and visual data integration

## 🔮 Future Enhancements

### Data Integration
- Time-series analysis of environmental changes
- Multi-spectral band analysis beyond RGB
- Integration with additional satellite data sources (Landsat, MODIS, etc.)
- Real-time data streaming from multiple sensors

### Analysis Capabilities  
- Automated change detection between time periods
- Machine learning classification models
- Vegetation health index calculations
- Deforestation monitoring and alerts

### User Interface
- Web interface for interactive analysis
- Dashboard for real-time monitoring
- API endpoints for programmatic access
- Mobile app for field validation

### Reporting and Visualization
- Automated PDF report generation
- Interactive web maps with time sliders
- 3D visualization of terrain and vegetation
- Export to GIS formats for further analysis

## �📄 License

This project is part of the OpenAI to Z challenge educational initiative.

---
*Last updated: June 17, 2025*
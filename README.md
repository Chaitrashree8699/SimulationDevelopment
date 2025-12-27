# 🚜 John Deere Vehicle Simulation

![Python](https://img.shields.io/badge/python-3.9+-blue)
![OpenGL](https://img.shields.io/badge/OpenGL-3.1+-green)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-Fraunhofer--IESE-lightgrey)

A **comprehensive 3D agricultural simulation** that integrates **real-world GPS data** from John Deere Operations Center with advanced vehicle dynamics, seasonal environments, and precision farming capabilities. Drive John Deere tractors with various implements across authentic field boundaries while the system generates real-time telemetry data.

---

## ✨ Key Features

### 🌍 **GPS Integration & Real Field Data**
- Connect to **John Deere Operations Center API** for authentic field boundaries
- **OAuth 2.0 authentication** with secure token management
- Select real farm fields and load actual GPS coordinates
- **0.11m precision** GPS coordinate conversion (lat/lon ↔ local x,z)
- Real-time GPS position tracking displayed in HUD
- Export telemetry data in **JSON and GeoJSON** formats

### 🚜 **Vehicle Fleet**
Four authentic John Deere tractor models:
- **JD 5075E** - Utility Tractor (75 HP)
- **JD 6120M** - Row Crop Tractor (120 HP)
- **JD 8245R** - High-Power Tractor (245 HP)
- **JD 9RX 640** - 4-Track Tractor (640 HP)

### 🔧 **Implement System** (5 Types)
- **Plow** - Soil preparation
- **Planter** - Seed planting
- **Sprayer** - Crop protection
- **Irrigator** - Water management
- **Harvester** - Crop harvesting

*Note: Implements are selected from the main menu before starting the simulation.*

### 🌦️ **Seasonal Environments**
Dynamic visual changes across **4 seasons**:
- **Spring** - Fresh green environment
- **Summer** - Vibrant growth season
- **Autumn** - Golden harvest colors
- **Winter** - Snow-covered fields

### 🤖 **Autopilot System**
- **Pure pursuit algorithm** for autonomous navigation
- Waypoint-based path following
- Configurable lookahead distance
- Toggle between manual and autonomous modes
- Visual path traces for manual driving routes

### 📊 **Advanced Features**
- **Obstacle detection** during manual driving
- **Real-time telemetry logging** (250ms intervals / 4 Hz)
- **Multiple camera modes** (Chase View, Top-Down)
- **HUD with GPS coordinates** and vehicle stats
- **Help panel** with controls and information
- **Notification system** for user feedback
- **Path tracing** visualization

---

## 🏗️ Project Structure

```
john-deere-vehicle-simulation/
│
├── farm_sim/                    # Core simulation package
│   ├── core/                    # Game engine and autopilot
│   │   ├── game.py             # Main simulation loop
│   │   └── autopilot.py        # Autonomous navigation
│   ├── entities/                # Vehicle and implement definitions
│   │   ├── tractor.py          # Tractor physics and models
│   │   └── implements.py       # Agricultural implements
│   ├── render/                  # OpenGL rendering system
│   │   ├── draw.py             # 3D drawing functions
│   │   └── camera.py           # Camera system
│   ├── ui/                      # User interface
│   │   ├── menu.py             # Main menu and selection
│   │   └── field_selector.py  # GPS field selection UI
│   ├── world/                   # Environment and terrain
│   │   ├── ground.py           # Terrain rendering
│   │   ├── crop.py             # Crop lifecycle
│   │   └── obstacles.py        # Obstacle detection
│   ├── config.py               # Global configuration
│   ├── util.py                 # Utility functions
│   └── gps_utils.py            # GPS conversion and API
│
├── operations_center/           # John Deere API integration
│   ├── auth.py                 # OAuth 2.0 authentication
│   ├── fields_service.py       # Field data retrieval
│   └── org_service.py          # Organization management
│
├── tests/                       # Comprehensive test suite (18 files)
│   ├── test_*.py               # pytest test modules
│   └── ...
│
├── logs/                        # Telemetry and log data
├── assets/                      # 3D models and textures
├── main.py                      # Application entry point
├── .env                         # API credentials (not in repo)
├── pytest.ini                   # Test configuration
├── .coveragerc                  # Coverage settings
└── README.md                    # This file
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.9 or higher**
- **OpenGL 3.1+** compatible graphics
- **John Deere Developer Account** (for GPS features)

### 1️⃣ Clone Repository
```bash
git clone https://erbenschell.iese.fraunhofer.de/TBSD/2025/john-deere/john-deere-vehicle-simulation.git
cd john-deere-vehicle-simulation
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- `pygame >= 2.5`
- `PyOpenGL >= 3.1.10`
- `PyOpenGL-accelerate >= 3.1.10`
- `requests >= 2.31`
- `pytest >= 7.4` (for testing)
- `pytest-cov` (for coverage)

### 4️⃣ Configure John Deere API Credentials

Create a `.env` file in the project root:
```bash
JD_CLIENT_ID=your_client_id_here
JD_CLIENT_SECRET=your_client_secret_here
JD_REDIRECT_URI=http://localhost:9090/callback
JD_ORG_ID=6175035
```

**Get API credentials:**
1. Visit [John Deere Developer Portal](https://developer.deere.com)
2. Create an application
3. Copy Client ID and Client Secret
4. Set redirect URI to `http://localhost:9090/callback`

### 5️⃣ Run the Simulation
```bash
python main.py
```

---

## 🎮 Controls

### **Tractor Operation**
| Key | Action |
|-----|---------|
| **W** | Accelerate forward |
| **S** | Brake / Reverse |
| **A** | Steer left |
| **D** | Steer right |
| **SPACE** | Plant crop / Activate implement |
| **E** | Harvest mature crop |

### **Camera Controls**
| Key | Action |
|-----|---------|
| **C** | Cycle camera modes (Chase View → Top-Down) |
| **Page Up / Down** | Adjust camera height |
| **+ / −** | Zoom in/out (Top-Down mode) |

### **System Controls**
| Key | Action |
|-----|---------|
| **A** (Menu) | Toggle Autopilot |
| **H** | Show/Hide help panel |
| **Q / ESC** | Quit simulation |

---

## 🌍 GPS Integration Workflow

### **9-Step Pipeline:**

1. **User Login** - OAuth 2.0 authentication with John Deere
2. **Token Generation** - Secure access token obtained
3. **Field List** - Retrieve available fields from your organization
4. **Field Selection** - Choose field via interactive UI
5. **Boundary Retrieval** - Fetch GPS coordinates (MultiPolygon format)
6. **GPS Conversion** - Transform lat/lon to local x,z coordinates
7. **Field Initialization** - Set up simulation environment
8. **Real-Time Tracking** - Display GPS position in HUD
9. **Telemetry Export** - Log data in JSON/GeoJSON formats

### **GPS Coordinate System**
- **Projection**: Equirectangular formula
- **Precision**: 0.11 meters
- **Performance**: O(1) real-time conversion
- **Earth Radius**: 6,378,137 meters

### **Conversion Equations:**
```
x = (lon - center_lon) × cos(lat) × R
z = (lat - center_lat) × R
R = 6,378,137m (Earth radius)
```

---

## 📊 Telemetry Data

### **Data Schema**
```json
{
  "timestamp": "2025-12-06T10:30:45Z",
  "latitude": 49.4521,
  "longitude": 7.7683,
  "center_lat": 49.4500,
  "center_lon": 7.7650,
  "heading": 45.2,
  "speed": 12.5,
  "field_id": "abc123",
  "field_source": "john_deere_api",
  "field_boundary_points": 24,
  "field_area_hectares": 5.2
}
```

### **Export Formats**
- **JSON** - Standard structured data
- **GeoJSON** - Geographic mapping format
- **Logging Frequency** - 250ms (4 Hz)

---

## 🧪 Testing

The project includes a comprehensive test suite with **18 test files** covering all major components.

### **Run All Tests**
```bash
pytest
```

### **Run with Coverage**
```bash
pytest --cov=farm_sim --cov-report=html
```

### **Test Categories**
- Unit tests for GPS conversion
- Field service API tests
- Autopilot algorithm tests
- Obstacle detection tests
- Telemetry validation tests
- UI component tests

### **Coverage Report**
View detailed coverage:
```bash
open htmlcov/index.html
```

---

## 🏛️ Architecture

### **System Components**

1. **Core Engine** (`farm_sim/core/`)
   - Game loop (60 FPS target)
   - Physics simulation
   - State management

2. **GPS Integration** (`operations_center/`)
   - OAuth 2.0 authentication
   - John Deere API interface
   - Coordinate conversion

3. **Rendering System** (`farm_sim/render/`)
   - OpenGL 3.1+ rendering
   - Multiple camera perspectives
   - Dynamic lighting

4. **Autopilot** (`farm_sim/core/autopilot.py`)
   - Pure pursuit algorithm
   - Waypoint navigation
   - Path planning

5. **Environment** (`farm_sim/world/`)
   - Seasonal rendering
   - Crop lifecycle
   - Obstacle system

---

## 🔧 Configuration

Key settings in `farm_sim/config.py`:

```python
# Simulation
TARGET_FPS = 60
SIMULATION_SPEED = 1.0

# Field
FIELD_SIZE_M = 100.0
GRID_CELL_SIZE_M = 2.0

# Telemetry
TELEMETRY_LOG_INTERVAL_S = 0.25  # 4 Hz

# API
JD_API_BASE_URL = "https://sandboxapi.deere.com"
JD_API_VERSION = "v3"
```

---

## 🚧 Troubleshooting

### **OpenGL Errors on macOS**
macOS has deprecated OpenGL. If you encounter issues:
```bash
pip install --upgrade --force-reinstall PyOpenGL PyOpenGL-accelerate
```

### **Authentication Issues**
- Verify `.env` file exists with correct credentials
- Check redirect URI matches exactly: `http://localhost:9090/callback`
- Ensure John Deere API application is active

### **Low FPS**
- Reduce field size in config
- Lower crop density
- Disable path tracing
- Use simpler camera mode

### **GPS Data Not Loading**
- Confirm internet connection
- Verify API credentials
- Check organization ID (default: 6175035)
- Review logs in `logs/` directory

---

## 📚 Documentation

- **Architecture Document**: `Architecture_Doc.txt` (2253 lines)
- **Graphics Guides**: 
  - `GRAPHICS_GUIDE.md`
  - `GRAPHICS_SYSTEM_OVERVIEW.md`
  - `3D_MODELS_GUIDE.md`
  - `QUICKSTART_GRAPHICS.md`
- **API Documentation**: See `operations_center/` modules

---

## 🤝 Contributing

### **Development Workflow**
1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make changes and add tests
3. Run test suite:
   ```bash
   pytest
   ```
4. Commit with descriptive message:
   ```bash
   git commit -m "feat: add new feature"
   ```
5. Push to remote:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Create Merge Request on GitLab

### **Coding Standards**
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Write tests for new features
- Update documentation as needed

---

## 📈 Project Status

### **Current Version**: 3.0
### **Last Updated**: November 23, 2025
### **Branch**: main (commit f0221c7)

### **Recent Updates** (November 2025)
- ✅ GPS Integration with John Deere Operations Center API
- ✅ Real field boundary fetching and coordinate conversion
- ✅ 5 agricultural implements (Plow, Planter, Sprayer, Irrigator, Harvester)
- ✅ 4 seasonal environments with dynamic visuals
- ✅ Autopilot system with pure pursuit algorithm
- ✅ Path tracing for manual driving
- ✅ Obstacle detection system
- ✅ Comprehensive test suite (18 test files, 27,825+ lines)
- ✅ UI improvements (Help panel, notifications)
- ✅ Enhanced telemetry logging (JSON/GeoJSON export)

---

## 📦 System Requirements

### **Minimum**
- Python 3.9+
- 4 GB RAM
- OpenGL 3.1 compatible GPU
- 500 MB disk space

### **Recommended**
- Python 3.10+
- 8 GB RAM
- Dedicated GPU with OpenGL 4.1+
- 1 GB disk space

### **Tested Platforms**
- ✅ macOS Monterey+ (Apple Silicon & Intel)
- ✅ Windows 10/11
- ✅ Ubuntu 20.04+

---

## 📜 License

This project is part of the **Fraunhofer IESE – John Deere Simulation Initiative**.

**© 2025 Fraunhofer IESE**

For questions about usage, distribution, or collaboration, please contact:
- **Project Lead**: Fraunhofer IESE
- **Partner**: John Deere

---

## 🙏 Acknowledgments

- **Fraunhofer IESE** - Research and development
- **John Deere** - API access and domain expertise
- **Python Community** - Open-source libraries and tools

---

## 📞 Support

For issues, questions, or contributions:
- **GitLab Issues**: [Create an issue](https://erbenschell.iese.fraunhofer.de/TBSD/2025/john-deere/john-deere-vehicle-simulation/-/issues)
- **Documentation**: See `docs/` folder
- **Email**: Contact project maintainers

---

**Happy Farming! 🚜🌾**

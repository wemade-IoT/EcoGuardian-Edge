# EcoGuardian Edge

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.1-green.svg)
![SQLite](https://img.shields.io/badge/sqlite-3-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

EcoGuardian Edge is a comprehensive IoT edge computing platform designed for environmental monitoring and analytics. The system provides real-time data collection, processing, and analysis capabilities for environmental sensors, enabling organizations to monitor and respond to environmental conditions effectively.

## Features

### Core Capabilities
- **Real-time Environmental Monitoring**: Collect and process sensor data in real-time
- **Device Authentication**: Secure API key-based authentication for IoT devices
- **Data Analytics**: Advanced analytics and metrics processing
- **RESTful API**: Complete REST API for device integration and data access
- **Background Processing**: Automated periodic data processing and metrics push
- **SQLite Database**: Lightweight, embedded database for edge computing scenarios

### Architecture Highlights
- **Domain-Driven Design (DDD)**: Clean architecture with separated concerns
- **Microservices Ready**: Modular design with clear service boundaries
- **Edge Computing Optimized**: Designed for deployment on edge devices
- **Scalable**: Built to handle multiple IoT devices and high-frequency data

## System Architecture

The application follows a layered architecture based on Domain-Driven Design principles:

```
├── analytics/                  # Analytics bounded context
│   ├── application/           # Application services
│   ├── domain/               # Domain entities and services
│   ├── infrastructure/       # Data persistence and external services
│   └── interfaces/           # API controllers and interfaces
├── iam/                      # Identity and Access Management
│   ├── application/         # Authentication services
│   ├── domain/             # Device entities and auth logic
│   ├── infrastructure/     # Device repositories
│   └── interfaces/         # Authentication interfaces
├── shared/                  # Shared infrastructure
│   └── infrastructure/     # Database configuration
├── app.py                  # Main application entry point
└── create_devices.py      # Device setup utility
```

## Technology Stack

- **Backend Framework**: Flask 3.1.1
- **Database**: SQLite with Peewee ORM
- **Authentication**: API Key-based authentication
- **Data Processing**: Python with real-time analytics
- **HTTP Client**: Requests library for external integrations
- **Date/Time**: Python-dateutil for enhanced date handling

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- SQLite 3

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/EcoGuardian-Edge.git
   cd EcoGuardian-Edge
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python create_devices.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

## API Documentation

### Authentication
All API requests require authentication using an API key in the header:
```
Api-Key: your-api-key-here
```

### Endpoints

#### Create Metric
**POST** `/api/v1/analytics/metrics`

Create a new environmental metric reading.

**Request Headers:**
- `Api-Key`: Device API key (required)
- `Content-Type`: application/json

**Request Body:**
```json
{
  "deviceId": 1,
  "metric_types_id": 1,
  "metric_value": 75.5
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 123,
    "metric_types_id": 1,
    "metric_value": 75.5
  }
}
```

**Metric Types:**
- `1`: Temperature
- `2`: Humidity
- `3`: Air Quality
- `4`: Light Intensity

**Validation Rules:**
- `metric_value`: Must be between 0 and 100 (percentage)
- `metric_types_id`: Must be between 1 and 4
- `deviceId`: Must be a valid registered device

### Error Responses

**400 Bad Request**
```json
{
  "error": "Missing required fields"
}
```

**401 Unauthorized**
```json
{
  "error": "Invalid device_id or API key"
}
```

## Configuration

### Environment Variables
- `FLASK_ENV`: Set to `development` for development mode
- `DATABASE_URL`: SQLite database file path (default: `ecoguardian_edge.db`)
- `API_KEY`: Default API key for device authentication

### Database Configuration
The application uses SQLite by default. The database file `ecoguardian_edge.db` is created automatically on first run.

## Usage Examples

### Register a New Device
```bash
python create_devices.py
```

### Send Sensor Data
```bash
curl -X POST http://localhost:5000/api/v1/analytics/metrics \
  -H "Content-Type: application/json" \
  -H "Api-Key: b1e2c3d4-5f6a-7b8c-9d0e-1f2a3b4c5d6e" \
  -d '{
    "deviceId": 1,
    "metric_types_id": 1,
    "metric_value": 23.5
  }'
```

### Python Client Example
```python
import requests

url = "http://localhost:5000/api/v1/analytics/metrics"
headers = {
    "Content-Type": "application/json",
    "Api-Key": "b1e2c3d4-5f6a-7b8c-9d0e-1f2a3b4c5d6e"
}
data = {
    "deviceId": 1,
    "metric_types_id": 1,
    "metric_value": 25.0
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

## Development

### Project Structure
The project follows Clean Architecture principles with clear separation of concerns:

- **Domain Layer**: Core business logic and entities
- **Application Layer**: Use cases and application services
- **Infrastructure Layer**: Data persistence and external services
- **Interface Layer**: API controllers and external interfaces

### Adding New Features

1. **New Metric Types**: Add to the domain validation rules
2. **New Endpoints**: Create in the appropriate interfaces module
3. **New Business Logic**: Implement in domain services
4. **New Data Models**: Add to infrastructure models

### Testing
```bash
# Run tests (when test suite is available)
python -m pytest tests/
```

## Deployment

### Production Deployment
1. Set environment variables for production
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure proper logging
4. Set up monitoring and alerting

### Docker Deployment
```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## Monitoring and Logging

The application includes built-in monitoring capabilities:
- Periodic metrics push to external services
- Request/response logging
- Error tracking and reporting
- Performance monitoring

## Security

- API key-based authentication
- Input validation and sanitization
- SQL injection prevention through ORM
- Rate limiting (recommended for production)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or contributions, please:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

## Changelog

### Version 1.0.0
- Initial release
- Core analytics and IAM functionality
- RESTful API implementation
- SQLite database integration
- Background processing capabilities

---

**EcoGuardian Edge** - Empowering environmental monitoring through edge computing technology.

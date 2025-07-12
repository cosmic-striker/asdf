# ExploitX Web Application

A modern Flask web application with admin panel, featuring the Neon Abyss theme.

## 🚀 Quick Start with Docker

### Prerequisites
- Docker
- Docker Compose

### Setup Instructions

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd exploitx_webpage
   ```

2. **Run the setup script**:
   ```bash
   ./setup_docker.sh
   ```

   Or manually:
   ```bash
   docker-compose up --build -d
   ```

3. **Access the application**:
   - Web Application: http://localhost:2005
   - MySQL Database: localhost:2004

## 🛠️ Manual Setup

### Using Docker Compose

1. **Build and start containers**:
   ```bash
   docker-compose up --build
   ```

2. **Run in background**:
   ```bash
   docker-compose up --build -d
   ```

3. **View logs**:
   ```bash
   docker-compose logs -f
   ```

4. **Stop containers**:
   ```bash
   docker-compose down
   ```

### Local Development Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up MySQL database**:
   ```bash
   # Start MySQL service
   sudo systemctl start mysql
   
   # Create database
   mysql -u root -p -e "CREATE DATABASE exploitx;"
   ```

3. **Initialize database**:
   ```bash
   cd exploitx
   python init_db.py
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

## 📁 Project Structure

```
exploitx_webpage/
├── exploitx/                 # Main application directory
│   ├── app.py               # Flask application
│   ├── init_db.py           # Database initialization
│   ├── templates/           # HTML templates
│   ├── static/              # Static files (CSS, JS, images)
│   └── security_config.py   # Security configurations
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker image definition
├── requirements.txt        # Python dependencies
├── setup_docker.sh        # Docker setup script
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

- `FLASK_APP`: Flask application entry point
- `FLASK_ENV`: Environment (development/production)
- `SECRET_KEY`: Secret key for sessions
- `SQLALCHEMY_DATABASE_URI`: Database connection string

### Docker Configuration

- **Web Application**: Port 2005
- **MySQL Database**: Port 2004
- **Database**: exploitx
- **Root Password**: root

## 🎨 Features

- **Neon Abyss Theme**: Dark cyberpunk aesthetic with neon colors
- **Admin Panel**: User management, content management
- **Responsive Design**: Mobile-friendly interface
- **Security Features**: Password hashing, session management
- **Database**: MySQL with SQLAlchemy ORM

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**:
   ```bash
   # Check if MySQL container is running
   docker-compose ps
   
   # Check MySQL logs
   docker-compose logs db
   
   # Restart containers
   docker-compose restart
   ```

2. **Port Already in Use**:
   ```bash
   # Check what's using the ports
   sudo netstat -tulpn | grep :2005
   sudo netstat -tulpn | grep :2004
   
   # Change ports in docker-compose.yml if needed
   ```

3. **Permission Issues**:
   ```bash
   # Fix file permissions
   chmod +x setup_docker.sh
   chmod +x wait-for-db.sh
   chmod +x start.sh
   ```

4. **Container Won't Start**:
   ```bash
   # Remove containers and rebuild
   docker-compose down
   docker-compose up --build
   
   # Check logs for specific errors
   docker-compose logs web
   ```

### Useful Commands

```bash
# View real-time logs
docker-compose logs -f

# Access container shell
docker-compose exec web bash
docker-compose exec db mysql -u root -proot

# Restart specific service
docker-compose restart web
docker-compose restart db

# Rebuild without cache
docker-compose build --no-cache

# Remove all containers and volumes
docker-compose down -v
```

## 🔒 Security Notes

- Change default passwords in production
- Update SECRET_KEY in production
- Configure proper SSL/TLS certificates
- Review security_config.py for additional settings

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs: `docker-compose logs`
3. Create an issue in the repository"# asdf" 

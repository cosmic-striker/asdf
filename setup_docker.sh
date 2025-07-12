#!/bin/bash

echo "🚀 ExploitX Docker Setup Script"
echo "================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Stop any existing containers
echo "🛑 Stopping any existing containers..."
docker-compose down

# Remove any existing volumes (optional - uncomment if you want fresh data)
# echo "🗑️  Removing existing volumes..."
# docker-compose down -v

# Build and start the containers
echo "🔨 Building and starting containers..."
docker-compose up --build -d

# Wait a moment for containers to start
echo "⏳ Waiting for containers to start..."
sleep 10

# Check container status
echo "📊 Container Status:"
docker-compose ps

# Show logs
echo "📋 Recent logs:"
docker-compose logs --tail=20

echo ""
echo "🎉 Setup complete!"
echo "🌐 Access your application at: http://localhost:2005"
echo "🗄️  MySQL is available at: localhost:2004"
echo ""
echo "📝 Useful commands:"
echo "  View logs: docker-compose logs -f"
echo "  Stop: docker-compose down"
echo "  Restart: docker-compose restart"
echo "  Rebuild: docker-compose up --build"
echo ""
echo "🔧 If you encounter issues:"
echo "  1. Check logs: docker-compose logs web"
echo "  2. Check database: docker-compose logs db"
echo "  3. Restart: docker-compose restart"
echo "  4. Rebuild: docker-compose up --build" 
FROM python:3.9-slim

WORKDIR /app

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait-for-db.sh
RUN chmod +x start.sh
RUN chmod +x manage_admin.py

ENV FLASK_APP=exploitx/app.py
ENV FLASK_ENV=development
ENV SECRET_KEY=your-secret-key-here

EXPOSE 5000

CMD ["./start.sh"] 
# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Create a folder inside the container
WORKDIR /app

# 3. Copy requirements first (to cache dependencies)
COPY requirements.txt .

# 4. Install the tools
# We use --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code (model, main.py, etc.)
COPY . .

# 6. Open the port so the outside world can talk to it
EXPOSE 5000

# 7. The command to run when the container starts
CMD ["python", "main.py"]
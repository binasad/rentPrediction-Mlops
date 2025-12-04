# Use an image that has Python + Chrome + ChromeDriver pre-installed
FROM joyzoursky/python-chromedriver:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scraper.py .

# We don't use CMD here because this isn't a server. 
# It's a script we run once.
CMD ["python", "scraper.py"]

# AutoSlideShow

## Overview
AutoSlideShow is a lightweight, automated solution for dynamically displaying PowerPoint slides as a web-based slideshow on your local network. This feature converts PowerPoint slides to images and serves them through an HTML-based slideshow that automatically updates and cycles through slides. The page refreshes every few seconds to ensure any changes to the slide content are reflected in real-time, making it ideal for live presentations, dashboards, or digital signage.

## Key Features:
- **Automated Slide Conversion:** Automatically converts PowerPoint slides into images, eliminating the need for manual conversion.
- **Dynamic Slideshow:** Displays the converted slides in a continuous, timed slideshow, cycling through each slide every minute.
- **Auto-Refresh:** The HTML page refreshes every 5-10 seconds to capture any updated content, ensuring real-time presentation updates.
- **Local Network Hosting:** Serves the slideshow on your local network, allowing you to access it from any device connected to the same network.
- **Simple Setup:** A Python script handles the entire process, from slide conversion to generating and hosting the HTML slideshow, making it easy to set up and use.

## How It Works:
- **Select Your PowerPoint File:** Choose the PowerPoint presentation you want to display.
- **Convert Slides to Images:** The script automatically converts each slide into an image format (e.g., PNG).
- **Generate and Serve HTML:** An HTML file is generated to display the slides as a timed slideshow, and it is served on your local network.
- **Access and View:** Open the slideshow on any device within your local network to view the dynamically updated presentation.

## Use Cases:
- **Live Presentations:** Automatically cycle through slides during meetings or presentations.
- **Real-Time Dashboards:** Display up-to-date information from a PowerPoint-based dashboard.
- **Digital Signage:** Use AutoSlide Server to display informational or promotional content on screens across your network.

## Prerequisites
Ensure that the following tools are installed on your system:
- **Python 3.x**
- **Docker**

## Project Structure
```
AutoSlideShow/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── upload.html
│   └── slideshow.html
├── static/
│   └── slides/  # This folder will store the converted slides
└── uploads/     # This folder will store uploaded PowerPoint files
```

## Getting Started

### 1. Clone the Repository
First, clone the project repository from GitHub:

```bash
git git@github.com:StanislavHaitov/AutoSlideShow.git
cd AutoSlideShow
```

## 2. Run the image form Docker Hub
The Docker image for this project is hosted on Docker Hub. You can pull the latest version of the image using:

```bash
docker pull stanislavhaitov/autoslideshow:latest
```
```bash
docker run -d -p 5000:5000 \
    -v "T:/Stas Haitov/AutoSlideShow/uploads:/app/uploads" \
    -v "T:/Stas Haitov/AutoSlideShow/slides:/app/static/slides" \
    --name autoslideshow autoslideshow
```

Docker Hub repository: [stanislavhaitov/autoslideshow](https://hub.docker.com/r/stanislavhaitov/autoslideshow)

## Technology Stack
- **Python & Flask**: Web application framework.
- **Docker**: Containerization of the application.
  
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, feel free to contact Stanislav Haitov at [stanislav.haitov@gmail.com](mailto:stanislav.haitov@gmail.com).

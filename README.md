
# Image Resizer and Cropper

A simple Streamlit web application to resize and crop images. 

## Features

- Upload your image in JPG, JPEG, or PNG format.
- Crop the image with easy-to-use sliders.
- Resize the image with predefined sizes or specify custom dimensions.
- Choose the output format for the resized image.
- Download the processed image.

## Live Demo

Visit the application hosted on Streamlit Share: [Image Resizer and Cropper](https://imageresizerandcrop-123.streamlit.app/)

## Installation

### Prerequisites

Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Setup

1. Clone this repository:

```bash
git clone <repository_link>
cd <repository_folder>
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

**Note**: The `requirements.txt` file should contain:

```
numpy~=1.23.5
streamlit~=1.20.0
opencv-contrib-python-headless
matplotlib
```

3. Run the application:

```bash
streamlit run <filename.py>
```

Replace `<filename.py>` with the name of the Python script containing the above code.

## Usage

1. Upload an image file (jpg, jpeg, png).
2. If desired, crop the image using the provided interface.
3. Choose a resize option. You can select from predefined sizes or specify custom dimensions.
4. Choose an output format (JPG or PNG).
5. Enter a name for the output file.
6. Click on "Download Resized Image" to get the processed image.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or feature additions.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

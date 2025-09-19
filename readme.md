# 🎨 AI-Powered Kolam Generator

This is a Streamlit web application that uses Google's Gemini generative AI model to create traditional Kolam design drawings programmatically. Users can customize Kolam designs by selecting festival themes, motifs, symmetry types, complexity levels, and grid sizes. The app then generates the Kolam drawing instructions via Gemini, parses the JSON response, and incrementally renders the Kolam step-by-step.

---

## Features

- Interactive UI with options to choose:
  - Festival: Pongal, Diwali, Daily, Unknown
  - Motif: Lotus, Peacock, Star, Abstract
  - Symmetry: Radial, Rotational, Reflectional
  - Complexity: Simple, Medium, Complex
  - Grid Size: adjustable (3 to 15)
- Uses Google Gemini 2.5 Flash generative model for Kolam instruction generation
- Incremental rendering of the Kolam including dots, curves, and motifs using Matplotlib
- Displays success message with symmetry type after generation

---

## Requirements

- Python 3.8+
- Streamlit
- google-generativeai Python SDK
- Matplotlib
- python-dotenv (for environment variable config)

Install dependencies:

---

## Setup

1. Obtain Google Gemini API key and enable access.

2. Create a `.env` file in the project root with the line:


3. Run the Streamlit app:

---

## Usage

- Select your desired options from the dropdowns and slider.
- Click the **Generate Kolam** button.
- Watch the Kolam get drawn step-by-step in the UI.
- View success confirmation once complete.

---

## Code Overview

- `genai.configure(api_key=...)` sets up Google Gemini access.
- User selections generate a prompt with Kolam design parameters.
- Gemini is called with `model.generate_content()` requesting JSON output.
- The JSON response is parsed into dot positions, curves, and motifs.
- Matplotlib plots the Kolam incrementally with short pauses for animation.
- Streamlit placeholder is used to update the same plot gradually.

---

## Notes

- Ensure your API key is valid and has sufficient quota.
- Internet connection required for API calls.
- Error handling displays parsing issues or API errors in UI.

---

## License

MIT License
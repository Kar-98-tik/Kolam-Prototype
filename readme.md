AI-Powered Kolam Generator

This project is a Streamlit web app that generates traditional Indian Kolam designs using Google’s Gemini Generative AI model. Users input design parameters, and the AI generates step-by-step instructions that are visualized in an interactive way.

Table of Contents

Technologies Used

How the Kolam Generation Works

Integration and Configuration of Gemini Model

Incremental Rendering

Error Handling

Deployment

Potential Improvements

Challenges Encountered

Key Takeaways

Technologies Used

Streamlit: For building the interactive web user interface.

Google Gemini (Generative AI): Used as the core AI model to generate Kolam drawing instructions in JSON.

Matplotlib: For incremental drawing and visualization of the Kolam.

python-dotenv: For secure storage and loading of environment variables (API keys).

Google Generative AI Python SDK: To call the Gemini API.

How the Kolam Generation Works

Users provide input parameters such as:

Festival Type

Motif

Symmetry

Complexity

Grid Size

These parameters are used to create a natural language prompt which is then sent to the Gemini AI model. Gemini returns a JSON response that specifies:

Coordinates of dots

Curves connecting dots

Motif positions

Symmetry types

The app parses this JSON and incrementally draws the Kolam:

Dots: Displayed as points on the canvas.

Curves: Connecting the dots.

Motifs: Placed at specific positions according to the design.

Each step is visualized on the same canvas, with the drawing updating progressively for an engaging user experience.

Integration and Configuration of Gemini Model

The google.generativeai Python SDK is used to interface with the Gemini API. Here's how the integration works:

The SDK is initialized with an API key, securely loaded from the .env file.

The model used is "gemini-2.5-flash".

A natural language prompt containing the Kolam parameters is sent, and the response is requested in JSON format.

The JSON response is parsed, and if there are errors, they are handled gracefully to provide feedback to the user.

Incremental Rendering

Incremental rendering is employed to make the Kolam generation process more engaging. This is achieved by:

Introducing time delays between each step (dots, curves, and motifs).

Using a Streamlit placeholder to update the canvas dynamically.

This approach avoids presenting the final result instantly and instead lets users visually experience the creation process step-by-step.

Error Handling

Error handling is implemented in the following ways:

If parsing the JSON response fails, an error message along with the raw response is displayed.

Execution stops on failure to prevent the app from crashing.

Immediate feedback is provided to the user if the AI output is malformed or incomplete.

Deployment
Local Deployment

Install the required dependencies:

pip install -r requirements.txt


Store your Google API key in a .env file.

Run the app locally:

streamlit run app.py

Cloud Deployment

For cloud deployment, ensure the following:

Environment variables, including the Google API key, are configured securely on the host.

Follow the hosting platform’s guidelines for deploying a Streamlit app.

Potential Improvements

Caching: Implement caching of Kolam instructions to avoid repeated API calls.

User Accounts: Add the ability for users to save and retrieve their favorite Kolam designs.

Export Functionality: Enable exporting the generated Kolam designs to SVG or image files.

Enhanced Prompt Engineering: Improve the prompts for more complex and context-aware designs.

UI Enhancements: Improve the user interface for better responsiveness and mobile support.

Challenges Encountered

Some challenges during the development of this project included:

Parsing JSON Safely: Handling variability in AI-generated output formatting.

UI Responsiveness: Balancing the need for incremental plotting with maintaining responsiveness of the interface.

API Key Security: Ensuring the security of the Google API key and other environment configurations.

Flexible Prompt Design: Designing prompts that can accommodate the diverse parameters of Kolam styles.

Key Takeaways

AI and Visualization: Combining LLMs (Large Language Models) with graphical visualization techniques can create engaging and creative applications.

Prompt Design and Error Handling: Crafting the right prompts and handling errors effectively is essential for AI-driven generation tasks.

Streamlit for Prototyping: Streamlit is a powerful tool for quickly building interactive machine learning-powered applications.

Bridging Tradition with Technology: This project highlights how modern AI and web technologies can bridge the gap between traditional art forms like Kolam and digital creativity.

License

This project is licensed under the MIT License - see the LICENSE
 file for details.
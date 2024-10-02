
# Socrateach - AI Socratic Teaching Assistant for Sorting Algorithms

## Tagline:
**"An AI-powered teaching assistant that uses the Socratic method to teach Sorting Algorithms through interactive questioning."**

## Problem it Solves:
Many students struggle with understanding complex computer science topics, like Sorting Algorithms, due to a lack of one-on-one guidance. The traditional teaching approach often spoon-feeds information instead of promoting critical thinking. 

Socrateach addresses this issue by using AI to engage students with the Socratic method, guiding them through thoughtful questions rather than giving direct answers. This helps students think critically and discover solutions on their own.

## Functional Prototype:
Socrateach is built using the **Google AI Python SDK** and the **Generative AI model** (`gemini-1.5-flash`). It functions as an AI-powered teaching assistant that interacts with students, asking Socratic-style questions when they input problems related to Sorting Algorithms.

### Example Use Case:
1. **Scenario**: A student’s sorting code times out on a large input case.
   - **AI Assistant**: "What do you notice about this test case compared to the others that passed?"
   - **Student**: "The input size is larger."
   - **AI Assistant**: "Great! What effect do you think the input size has on the algorithm's performance?"
   - The assistant continues asking questions, helping the student identify inefficient code sections and possible optimizations.

### Key Features:
- **Guided Questioning**: Uses Socratic questioning to help students understand Sorting Algorithms better.
- **Dynamic Interaction**: Adapts based on the student's responses, encouraging reflection and critical thinking.
- **Focus on Learning**: Guides the student without providing direct answers, ensuring a deeper learning process.

## Challenges I Ran Into:
Some of the key challenges during the project included:
- **Fine-tuning the AI model** to ask the right type of Socratic questions without giving too much information away.
- **Handling various student input types** to ensure the assistant provides helpful guidance across a range of problems.
- **UI/UX integration** to ensure a smooth interaction between the student and the AI assistant.

## Technologies I Used:
- **Google AI Python SDK**: For the generative AI model.
- **Python**: The primary language for the assistant’s logic and interaction.
- **Additional Frameworks**: Optional UI integration using tools like Flask or React (depending on implementation needs).

## Links:
- **GitHub Repository**: (Link to your repo)
- **Figma Design (if applicable)**: (Link to any Figma designs)
- **Documentation**: (Link to detailed documentation, setup, and configuration instructions in Google Drive or similar)
- **Video Demo**: (Link to a video demonstrating how the AI assistant works, hosted on Google Drive or YouTube)

## Video Demo:
- The video demo showcases how a student interacts with the assistant and how the AI uses Socratic questioning to guide the learning process.
- Use a tool like OBS Studio or Loom to capture the interaction between the AI and the student in your Python environment.

## Setup Instructions:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/socrateach.git
   ```
2. Install dependencies:
   ```bash
   pip install google-generativeai
   ```
3. Set up your API key:
   - Obtain your API key from the Google Cloud Console.
   - Export it as an environment variable:
     ```bash
     export GEMINI_API_KEY='your-api-key'
     ```
4. Run the teaching assistant:
   ```bash
   python socrateach.py
   ```

## Future Improvements:
- Add more customization for different topics beyond Sorting Algorithms.
- Expand the model to cover broader areas of data structures and algorithms.

# 🚀 Automated Content Creation Crew using CrewAI 📝

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/framework-CrewAI-orange.svg)](https://www.crewai.com/)

An autonomous multi-agent crew designed to automate the entire process of blog post creation. From a single topic, this crew researches, writes, and edits a complete, ready-to-publish article.

---

## ✨ Overview

This project demonstrates the power of the **CrewAI framework** by creating a collaborative team of AI agents. The goal is to automate the complex workflow of content creation, showcasing how specialized agents can work together to achieve a result greater than the sum of their parts.

You provide a topic, and the AI crew handles the rest, delivering a polished markdown file as the final output.

<br>

---

## 🤖 Meet the Crew

Our AI team is composed of three expert agents, each with a specific role and goal. They work sequentially to transform a simple idea into a comprehensive article.

| Agent Role | Icon | Goal | Key Responsibilities |
| :--- | :--: | :--- | :--- |
| **Research Analyst** | 🕵️‍♂️ | To gather the most relevant, up-to-date, and factual information. | - Scours the web for articles, studies, and data.<br>- Identifies key trends and statistics.<br>- Compiles a detailed research brief. |
| **Content Writer** | ✍️ | To synthesize the research into an engaging and well-structured blog post. | - Crafts a compelling narrative.<br>- Ensures the content is SEO-friendly.<br>- Organizes the information logically with clear headings. |
| **Lead Editor** | 🧐 | To review and refine the content for quality, accuracy, and style. | - Proofreads for grammar and spelling errors.<br>- Fact-checks all claims and data points.<br>- Ensures a consistent tone and voice. |

---

## 🔧 Tech Stack

This project is built with a modern, AI-focused stack:

- **Framework:** [CrewAI](https://www.crewai.com/)
- **Language:** Python 3.8+
- **Core Libraries:**
  - `crewai` & `crewai_tools` for agent and task management.
  - `langchain_community` for tool integrations.
  - `python-dotenv` for managing environment variables.
- **LLM Provider:** Compatible with OpenAI, Groq, Anthropic, and other major providers.

---

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.8 or later.
- An API key from an LLM provider (e.g., OpenAI).

### 2. Clone the Repository

```bash
git clone [https://github.com/vibhoragg16/Crew-ai-Agent.git](https://github.com/vibhoragg16/Crew-ai-Agent.git)
cd Crew-ai-Agent
```

### 3. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **On Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory by copying the example file.

```bash
cp .env.example .env
```

Now, open the `.env` file and add your API key.

```env
# .env
OPENAI_API_KEY="sk-..."
# You can also set your SERPER_API_KEY for web search capabilities
# SERPER_API_KEY="your-serper-key"
```

---

## 🚀 How to Run the Crew

Using the agent crew is simple and interactive.

1.  **Execute the Main Script**

    Run the `main.py` file from your terminal:
    ```bash
    python main.py
    ```

2.  **Provide a Topic**

    The script will prompt you to enter the topic for the blog post you want to create.
    ```
    ## Welcome to the Blog Post Generation Crew
    -------------------------------------------
    What is the topic of the blog post you want to create?
    > The Future of Renewable Energy
    ```

3.  **Watch the Magic Happen**

    The agents will begin their work. You'll see real-time updates in the console as each agent performs its tasks.

4.  **Get the Final Output**

    Once the crew has completed its mission, the final, polished blog post will be saved in the project's root directory as `blog_post.md`.

---

## 🛠️ Customization

This project is designed to be a starting point. You can easily customize and extend it:

- **Change the LLM:** Modify `src/agents.py` to use a different language model (e.g., `Groq`, `Anthropic`).
- **Add New Tools:** Equip your agents with new capabilities by defining them in a `tools` directory and assigning them to the relevant agent.
- **Modify Agent Roles:** Adjust the `goal`, `backstory`, and `tasks` in `src/agents.py` and `src/tasks.py` to alter the crew's behavior or create entirely new roles.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, create, and inspire. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

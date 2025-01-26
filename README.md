# 🏛️ Legally - Your Global Legal Advisor

**Legally** is an AI-powered virtual assistant designed to provide legal guidance tailored to your specific situation. It offers personalized legal analysis, insights, and agreement suggestions in multiple languages, making legal advice accessible to everyone.

---

## Features

- **Multilingual Support**: Available in English, Chinese, Hindi, French, Spanish, German, and Arabic.
- **Customizable Inputs**: Users can provide detailed information about their country, role in the situation and descriptions on legal situations for accurate results.
- **Secure API Integration**: Powered by secure and efficient backend services -- OpenAI GPT-4 model.
- **Disclaimer**: AI-generated legal insights are not substitutes for professional legal advice.

---

## Built With

- **[Streamlit](https://streamlit.io/):** A fast and intuitive framework for building data and AI applications with Python.
- **[OpenAI API](https://openai.com/api/):** Powering the intelligent analysis and natural language capabilities of the app.
- **[Python](https://www.python.org/):** The core programming language used for building the application.
- **[dotenv](https://pypi.org/project/python-dotenv/):** For managing environment variables securely.
- **[Requests](https://pypi.org/project/requests/):** For making HTTP requests to external APIs.
- **[Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/secrets-management):** To securely manage sensitive data such as API keys.

---


## Installation & Setup

### Prerequisites
1. Python 3.10 or above.
2. Pip package manager.

### Step 1: Clone the Repository
```bash
git clone https://github.com/hk414/legally.git
cd legally
```

### Step 2: Activate virtual environment
```bash
pip install -r requirements.txt
```

### Step 3: Setup Environment Variables in .env
```bash
OPENAI_API_KEY="your_openai_api_key_here"
```

### Step 4: Run the app
```bash
streamlit run main.py
```


## Security Best Practices

- **Environment Variables**: Store sensitive data like API keys in `.env` or Streamlit Secrets.
- **Ignore Sensitive Files**: Ensure `.env` and other sensitive files are added to `.gitignore`.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**.

---

## Contact

For questions or support, feel free to reach out:

- **Author**: hk414  
- **Email**: [hui.koh-10@student.manchester.ac.uk](mailto:hui.koh-10@student.manchester.ac.uk)  
- **GitHub**: [hk414](https://github.com/hk414)

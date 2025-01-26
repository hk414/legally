# config.py
import json, os

LANGUAGES = {
    "English": "en",
    "中文": "cn",
    "हिन्दी": "in",
    "Español": "es",
    "Français": "fr",
    "Deutsch": "de",
    "العربية": "ar"
}

TONES = {
    "Professional": "Use a formal, precise legal tone with technical language.",
    "Empathetic": "Use a compassionate and understanding tone, explaining legal concepts clearly.",
    "Direct": "Provide concise, straightforward legal advice without unnecessary elaboration.",
    "Analytical": "Offer a detailed, logical breakdown of legal considerations."
}

def load_all_language_strings(lang_folder="lang"):
    """
    Load all language JSON files into a single LANGUAGE_STRINGS dictionary.
    
    Args:
        lang_folder (str): Path to the folder containing language JSON files.
    
    Returns:
        dict: A dictionary containing all loaded language strings.
    """
    language_strings = {}
    
    try:
        # List all JSON files in the language folder
        for file_name in os.listdir(lang_folder):
            if file_name.endswith(".json"):
                # Extract the language code from the file name (e.g., "en.json" -> "en")
                lang_code = os.path.splitext(file_name)[0]
                
                # Load the content of the JSON file
                file_path = os.path.join(lang_folder, file_name)
                with open(file_path, "r", encoding="utf-8") as file:
                    language_strings[lang_code] = json.load(file)
    
    except FileNotFoundError:
        raise ValueError(f"Language folder '{lang_folder}' not found.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON file: {e}")

    return language_strings

LANGUAGE_STRINGS = load_all_language_strings()

LEGAL_CATEGORIES = {
    "Contract Law": "contract",
    "Family Law": "family",
    "Criminal Law": "criminal",
    "Property Law": "property",
    "Intellectual Property": "ip",
    "Immigration Law": "immigration",
}

import re
from typing import Optional, Dict, Any, List
import openai, os
from dotenv import load_dotenv
from config import TONES

load_dotenv()

class InputValidator:
    """Comprehensive input validation utility."""
    
    @staticmethod

    def sanitize_text(value: str, max_length: int = 500) -> str:
        """
        Sanitize and validate text input for multiple languages including Chinese, Indian (Hindi), French, German, and Arabic.
        
        Args:
            value (str): Input text to sanitize
            max_length (int): Maximum allowed length
        
        Returns:
            str: Sanitized text
        
        Raises:
            ValueError: For invalid inputs
        """
        if not value:
            raise ValueError("Input cannot be empty")
        
        # Remove potentially dangerous characters (e.g., <>&\'\" to prevent HTML injection)
        sanitized = re.sub(r'[<>&\'\"]', '', str(value).strip())
        
        # Check length
        if len(sanitized) > max_length:
            raise ValueError(f"Input exceeds maximum length of {max_length}")
        
        # Allow characters from Chinese, Hindi (Indian), French, German, Arabic, and basic punctuation
        if not re.match(r'^[\w\s.,!?()\-<>À-ÿА-Яа-я一-龯々〆〤ऀ-ॿء-يَ-ۿ]+$', sanitized):
            raise ValueError("Input contains invalid characters")
        
        return sanitized


    @staticmethod
    def validate_country(country: str) -> str:
        """
        Validate country input against a predefined list.
        
        Args:
            country (str): Country name to validate
        
        Returns:
            str: Validated country name
        
        Raises:
            ValueError: If country is not in the allowed list
        """
        ALLOWED_COUNTRIES = [
            'United States', 'United Kingdom', 'Canada', 'Australia', 
            'Germany', 'France', 'Japan', 'China', 'India', 'Brazil',
        ]
        
        sanitized_country = InputValidator.sanitize_text(country, max_length=50)
        
        if sanitized_country not in ALLOWED_COUNTRIES:
            raise ValueError(f"Invalid country: {sanitized_country}")
        
        return sanitized_country

class LegalPromptGenerator:
    """Advanced legal prompt generation utility."""
    
    @staticmethod
    def translate(text: str, target_language: str) -> str:
        try:
            openai.api_key = os.getenv("OPENAI_API_KEY")
            prompt = f"Translate the following text into {target_language}: \n{text}"

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are a highly skilled translator."},
                        {"role": "user", "content": prompt}],
                max_tokens=1000
            )

            translated_text = response['choices'][0]['message']['content']
            
            return translated_text

        except Exception as e:
            raise ValueError(f"Error during translation: {str(e)}")

    @classmethod
    def generate_prompt(
        cls,
        situation: str, 
        country: str, 
        role: Optional[str] = "Not applicable",
        tone: str = "Professional", 
        language: Optional[str] = None,
        need_agreement: bool = False
    ) -> str:
        """
        Generate a comprehensive, secure legal consultation prompt.
        
        Args:
            situation (str): Legal situation description
            country (str): Jurisdiction
            role (str, optional): Role of the user
            tone (str, optional): Consultation tone
            language (str, optional): Language considerations
            need_agreement (bool, optional): Agreement requirement
        
        Returns:
            str: Structured legal consultation prompt
        
        Raises:
            ValueError: For invalid inputs
        """
        safe_situation = situation.strip()
        safe_country = country if country else "Not specified"
        safe_role = role if role else "Not applicable"

        language_map = {
            "en": "English",
            "cn": "中文",
            "in": "हिन्दी",
            "es": "Español",
            "fr": "Français",
            "de": "Deutsch",
            "ar": "العربية"
        }

        safe_language = language_map.get(language, "Not specified")

        tone_instruction = TONES.get(tone, TONES["Professional"])

        prompt = f"""LEGAL CONSULTATION FRAMEWORK

        STRICT OUTPUT FORMAT REQUIREMENTS:
        1. Provide a structured response with EXACTLY the following sections:
        A. Legal Status Assessment
        B. Recommended Actions
        C. Potential Consequences
        D. Legal Protections
        E. Detailed Agreement Template (if applicable)
        F. References and Citations (if applicable)

        2. AGREEMENT/COMPLAINT LETTER TEMPLATE SPECIFICATIONS:
        - Include precise legal language
        - Structured with clear sections:
            a. Parties Involved
            b. Definitions
            c. Terms and Conditions
            d. Obligations
            e. Termination Clauses
            f. Signatures

        CONTEXT DETAILS:
        - Situation: {safe_situation}
        - Jurisdiction: {safe_country}
        - Role: {safe_role}
        - Language: {safe_language}
        - Agreement Required: {'Yes' if need_agreement else 'No'}

        TONE DIRECTIVE: {tone_instruction}

        COMPREHENSIVE ANALYSIS GUIDELINES:

        I. LEGAL STATUS ASSESSMENT
            - Precise legality determination
            - Specific legal statutes and precedents
            - Detailed risk identification

        II. RECOMMENDED ACTIONS
            - Immediate actions to mitigate potential legal risks, including but not limited to communication with relevant parties, securing documentation or taking protective measures. 
            - Clear, actionable, step-by-step guide to ensure full legal compliance with applicable laws and regulations
            - Straightforward advice on handling conflicts, including communication tips, when to escalate an issue, and where to find resources for resolving disputes without going to court.
            - Proactive legal strategies and safeguards to minimize future legal risks, including contractual clauses, risk-sharing mechanisms, or dispute resolution strategies.

        III. POTENTIAL CONSEQUENCES
            - Comprehensive legal implications
            - Detailed financial risk analysis
            - Quantifiable risk mitigation strategies

        IV. LEGAL PROTECTIONS
            - Exhaustive list of available legal safeguards applicable to the user's situation based on their role and jurisdiction. 
            - Clarify the legal frameworks that govern the user's case and explain their key components
            - Recommended protective documentation or evidence 
            - Comprehensive rights analysis
            - Exclusions or exceptions that may impact the users' rights or access to protection.

        V. AGREEMENT/COMPLAINT LETTER TEMPLATE
            - MUST BE FULLY DOWNLOADABLE
            - MUST USE PROFESSIONAL LEGAL FORMATTING
            - MUST INCLUDE ALL RELEVANT SECTIONS
            - MUST BE CUSTOMIZABLE TO SPECIFIC SITUATION

        VI. REFERENCES AND CITATIONS
            - Include list of references such as statutes, legal articles, or case laws, used to generate the output. The references should have proper titles, publication dates and clickable links when possible. 
            - Clearly distinguish between primary sources, like laws or regulations, and secondary sources, like legal articles or expert opinions. 
            - If no specific sources were used, explicitly state this in the response.

        OUTPUT REQUIREMENTS:
        - Based on the language implied by the **Situation**, **Role** provide the output in the language most appropriate to that context.
        - The response should be in the **native language** of the user.
        - The response should STRICTLY USE language {safe_language}.
        - Use clear, unambiguous legal language and ensure that the response is precise, actionable, and understandable in the detected language.
        - Provide specific, actionable recommendations.
        - Reference exact legal frameworks relevant to the region or jurisdiction.
        - Maintain absolute objectivity.
        - Include citations where applicable.

        CRITICAL INSTRUCTIONS:
        1. If no agreement/complaint letter is needed, clearly state 'NO AGREEMENT REQUIRED' in the inferred language.
        2. If an agreement/complaint letter is needed, provide a FULLY FORMATTED .docx COMPATIBLE TEMPLATE in the appropriate language.
        3. Ensure ALL sections are comprehensively addressed.
        4. Maintain professional legal standards of precision.
        """

        if safe_language != "English":
            translated_prompt = cls.translate(prompt, safe_language)
            return translated_prompt

        # print(translated_prompt)

        return prompt

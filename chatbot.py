#some libraries to import
#requirements.txt file

#1. loading the api ley from env file
import os
from dotenv import load_dotenv
# from langchain_google_genai import GoogleGenerativeAI
from google import genai

#Load enviroment variables from .env file
load_dotenv()

#Getting the API key from env variable
API_KEY = os.getenv('GOOGLE_API_KEY')

if API_KEY == None:
    print("API Key not found")
else:
    print("API Key loaded successfully")


#Making a function that will help us in summarizing the notes
def summarize_notes(notes):
    # Initialize the Google Generative AI model

    llm = genai.Client(api_key=API_KEY)
    prompt = f"""
    Summarize these study notes in exactly this format:

    SHORT SUMMARY:
    (4–5 lines)

    KEY POINTS:

    - Point 1
    - Point 2
    - Point 3
    - Point 4

    EXAM READY BULLETS:
    • Bullet 1
    • Bullet 2
    • Bullet 3
    • Bullet 4

    Notes to summarize:
    {notes}
    """
    response = llm.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text


summarize_notes("""**Polynomial Regression – Detailed Notes (≤250 words)**

Polynomial Regression is an extension of linear regression used to model **non-linear relationships** between the independent variable (X) and dependent variable (Y). Instead of fitting a straight line, it fits a **curve** by introducing higher-degree terms of X.

**Model Form:**
[
y = "\\beta_0 + \\beta_1 x + \\beta_2 x^2 + \\dots + \\beta_n x^n"
Here, *n* is the degree of the polynomial.
]
**Key Idea:**
Even though the equation looks non-linear, it is still **linear in parameters (β)**, which means it can be solved using linear regression techniques.

**When to Use:**

* When data shows a **curved trend**
* When linear regression underfits the data
* Common in growth patterns, physics problems, and trend modeling

**Advantages:**

* Captures complex patterns
* Flexible model fitting
* Easy to implement using feature transformation

**Disadvantages:**

* **Overfitting risk** with high degree (model memorizes noise)
* Poor extrapolation outside training data
* Computational cost increases with degree

**Important Concepts:**

* **Degree selection:** Use validation techniques (like cross-validation)
* **Bias-Variance tradeoff:** Low degree → high bias, high degree → high variance
* **Feature scaling:** Often required for stability

**Example:**
If house prices increase non-linearly with area, polynomial regression can model that curve better than a straight line.

**Conclusion:**
Polynomial Regression is powerful for modeling non-linear data but must be used carefully to avoid overfitting by choosing the right degree.""")
result = summarize_notes(...)
print(result)

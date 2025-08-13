import base64
from mistralai import Mistral
from dotenv import load_dotenv
import os

with open("document.pdf", "rb") as f:
    pdf_bytes = f.read()

b64 = base64.b64encode(pdf_bytes).decode()

# Load API key from environment (.env)
load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise RuntimeError("MISTRAL_API_KEY is not set. Create a .env with MISTRAL_API_KEY=<your_key> or set the environment variable.")

client = Mistral(api_key=api_key)

resp = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": f"data:application/pdf;base64,{b64}"
    },
    include_image_base64=True,
)

for page in resp.pages:
    print(page.markdown)

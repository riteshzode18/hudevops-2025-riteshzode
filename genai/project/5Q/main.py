import re
import pdfplumber

def parse_resume(resume_text):
    # Match the full name 
    full_name_match = re.search(r"^([A-Z][a-z]+ [A-Z][a-z]+)", resume_text, re.MULTILINE)
    full_name = full_name_match.group(1) if full_name_match else "Not Found"

    # Extract the short bio 
    bio_match = re.search(rf"^{full_name}\n([^\n]+)", resume_text, re.MULTILINE) if full_name != "Not Found" else None
    short_bio = bio_match.group(1).strip() if bio_match else "Not Found"

    details = {
        "Full Name": full_name,
        "Location": re.search(r"\d{4} Main Street, ([^•]+)", resume_text, re.MULTILINE).group(1) if re.search(r"\d{4} Main Street, ([^•]+)", resume_text, re.MULTILINE) else "Not Found",
        "Education": re.findall(r"Education\s*\n([^\n]+)", resume_text),
        "Work Experience": re.findall(r"Experience\s*\n([^\n]+)", resume_text),
        "Skills": re.findall(r"Skills\s*:\s*([\s\S]+?)(\n\n|\n[A-Z][a-z]+:|$)", resume_text),
        "Short Bio": short_bio,
    }
    return details

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.
    """
    full_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text.append(page.extract_text())
    return "\n".join(full_text)

if __name__ == "__main__":
    file_path = "resume.pdf" 
    resume_content = extract_text_from_pdf(file_path)
    
    print("Raw Resume Content:\n", resume_content)
    
    parsed_details = parse_resume(resume_content)
    print("\nParsed Candidate Details:")
    for key, value in parsed_details.items():
        print(f"{key}: {value}")
import os
import re

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def extract_mom_and_actions(transcript):
    lines = transcript.split('\n')
    mom = []
    action_items = []
    for line in lines:
        # Extract action items
        if re.search(r'action item:', line, re.IGNORECASE):
            action_items.append(line.strip())
        # Extract MOM (decisions, agreements, notes)
        if re.search(r'(noted|agreed|approved|completed|finalize|scheduled)', line, re.IGNORECASE):
            mom.append(line.strip())
    return mom, action_items

def main():
    file_path = "file.txt" 

    transcript = extract_text_from_txt(file_path)

    mom, action_items = extract_mom_and_actions(transcript)

    print("\n=== Minutes of Meeting (MOM) ===")
    for item in mom:
        print(f"- {item}")

    print("\n=== Action Items ===")
    for item in action_items:
        print(f"- {item}")

if __name__ == "__main__":
    main()

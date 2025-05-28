import random

def build_markov_chain(text):
    words = text.split()
    markov_chain = {}
    for i in range(len(words) - 1):
        curr_word = words[i]
        next_word = words[i + 1]
        if curr_word in markov_chain:
            markov_chain[curr_word].append(next_word)
        else:
            markov_chain[curr_word] = [next_word]
    return markov_chain

def generate_sentence(chain, max_length=15):
    word = random.choice(list(chain.keys()))
    sentence = [word]
    for _ in range(max_length - 1):
        next_words = chain.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        sentence.append(word)
        if word.endswith(('.', '!', '?')):
            break
    return ' '.join(sentence)

if __name__ == "__main__":

    with open('training.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    chain = build_markov_chain(text)
    # print(chain)
    for _ in range(5):
        print(generate_sentence(chain))

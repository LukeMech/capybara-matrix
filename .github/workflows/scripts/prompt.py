import g4f, json, sys, random

with open(sys.argv[1] + '/langModel.json', 'r') as file:
    data = json.load(file)

with open(sys.argv[1] + '/usedPrompts.json', 'r') as file:
    usedPrompts = json.load(file)

random_provider = random.choice(data["providers"])
random_provider_lower = random_provider.lower()


if random_provider_lower == 'liaobots': 
    provider = g4f.Provider.Liaobots
elif random_provider_lower == 'phind':
    provider = g4f.Provider.Phind
elif random_provider_lower == 'geekgpt':
    provider = g4f.Provider.GeekGpt
else:
    provider = g4f.Provider.Bing

ctx = data["prompt"] + "It must be EXACTLY AND ONLY 1 PROMPT, FORMATTED TO BE BETWEEN \" MARKS. You can get inspired (althought you better find new idea), but can't use exactly these prompts: " + '\n' + '\n'.join(usedPrompts)

print('Generating output for question: ' + ctx)
print('Using model: ' + data["model"])
print('And provider: ' + random_provider)

response = g4f.ChatCompletion.create(
    model=data["model"],
    provider=provider,
    messages=[{"role": "user", "content": ctx}]
)

# Extract text inside quotes
inside_quotes = False
result = []
for char in response:
    if char == '"':
        inside_quotes = not inside_quotes
    elif inside_quotes:
        result.append(char)
result = ''.join(result)

print('Writing to file: ' + result)

with open('./prompt.txt', 'w') as file:
    file.write(result)

print('Generated prompt.txt')
import matplotlib.pyplot as plt

res_files = {
    'Rust': 'rs_results.txt',
    'Java': 'java_results.txt',
    'C++': 'cpp_results.txt'
}

language_colors = {
    'Rust': '#dea584',
    'Java': '#b07219',
    'C++': '#f34b7d'
}

keywords = " ".join(open("keywords.txt", "r").readlines()).split()
keyword_counts = {language: {keyword: 0 for keyword in keywords} for language in res_files}

def read_keyword_counts(file_name):
    counts = {keyword: 0 for keyword in keywords}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()

            # Keyword lines
            if len(parts) == 2:
                keyword, count = parts
                if keyword in counts:
                    counts[keyword] = int(count)
    return counts

def plot_keywords():
    for keyword in keywords:
        print(f"Plotting '{keyword}' keyword...")

        counts = {language: keyword_counts[language][keyword] for language in res_files}

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.bar(counts.keys(), counts.values(), color=[language_colors[language] for language in counts])
        ax.set_title(f'Keyword: {keyword}')
        ax.set_ylabel("Occurrences")

        plt.savefig(f'plots/\'{keyword}\'.png', dpi=300)

        plt.close()

def main():
    for language, file_name in res_files.items():
        keyword_counts[language] = read_keyword_counts(file_name)

    plot_keywords()

main()

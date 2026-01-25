import os

def read_file(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]
        return int(lines[0]),int(lines[1]),lines[2:]


def smith_waterman(sequence1, window_size, match=2, mismatch=-1, gap=-2):
    m = len(sequence1)
    n = len(window_size)

    # Create a (m+1) x (n+1) matrix filled with zeros
    H = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_score = 0
    max_pos = (0, 0)

    # Fill the scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # Calculate match/mismatch score
            if sequence1[i - 1] == window_size[j - 1]:
                diag_score = H[i - 1][j - 1] + match
            else:
                diag_score = H[i - 1][j - 1] + mismatch

            # Calculate gap scores
            up_score = H[i - 1][j] + gap
            left_score = H[i][j - 1] + gap

            # Take the maximum value (including 0 for local alignment)
            H[i][j] = max(0, diag_score, up_score, left_score)

            # Track the maximum score and its position
            if H[i][j] > max_score:
                max_score = H[i][j]
                max_pos = (i, j)

    return H, max_score, max_pos


def find_motifs(sequences,window_size):
    # Generate all candidate motifs of length l from the first sequence
    windows = []
    step = 3
    for seq_idx,seq in enumerate(sequences):
        for i in range(0, len(seq) - window_size + 1, step):
            window = seq[i:i+window_size]
            windows.append((seq_idx,i, window))


    motifs = {}
    match = 2
    mismatch = -1
    gap = -2
    score_threshold = 8


    # compare all pairs of windows across *different* sequences
    for i in range(len(windows)):
        seq_i, pos_i, window1 = windows[i]
        for j in range(i + 1, len(windows)):
            seq_j, pos_j, window2 = windows[j]
            if seq_i == seq_j:
                continue  # skip comparisons within the same sequence

            _, score, _ = smith_waterman(window1, window2, match, mismatch, gap)
            if score >= score_threshold:
                if window1 not in motifs:
                    motifs[window1] = [score]  # new motif → create list of scores
                else:
                    motifs[window1].append(score)
    # frequency Rank(how many times they appeared)
    ranked_by_freq = []
    for motif in motifs:
        count = len(motifs[motif])
        ranked_by_freq.append((motif, count))
    ranked_by_freq.sort(key=lambda x: x[1], reverse=True)

    # maximum score Rank
    ranked_by_score = []
    for motif in motifs:
        max_score = max(motifs[motif])
        ranked_by_score.append((motif, max_score))
    ranked_by_score.sort(key=lambda x: x[1], reverse=True)

    return ranked_by_freq,ranked_by_score

def main():
    os.makedirs('output', exist_ok=True)
    datasets = ["dataset1", "dataset2", "dataset3"]
    for dataset in datasets:
     with open(f"output/output_{dataset}.txt", "w") as f:
        lines,length,sequences = read_file(dataset)
        ranked_by_freq,ranked_by_score = find_motifs(sequences,length)

        header = f"\n=== RESULTS FOR {dataset.upper()} ===\n"
        print(header)
        f.write(header)
        
        print("Top 10 motifs by Score:")
        f.write(f"Top 10 motifs by Score:\n")
        if ranked_by_score:
            for motif in ranked_by_score[:10]:
                motif, score = motif[0], motif[1]
                line = f"Motif: {motif}, Score: {score}\n"
                print(line.strip())
                f.write(line)
        else:
            print("No motifs found by score")
            f.write(f"No motifs found by score:\n")

        print("\nTop 10 motifs by Frequency:")
        f.write(f"Top 10 motifs by Frequency:\n")
        if ranked_by_freq:
            for motif, count in ranked_by_freq[:10]:
                line = f"Motif: {motif}, Count: {count}\n"
                print(line.strip())
                f.write(line)
        else:
            print("No motifs found by frequency")
        f.write("\n" + "=" * 40 + "\n\n")
if __name__ == "__main__":
    main()
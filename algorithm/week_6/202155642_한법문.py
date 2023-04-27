#알고리즘: dna를 전사 후 1~6 번째 오픈리딩프레임에서 M ~ _ 사이 최대 길이들을 비교

def make_triplet_code():
    first_base = second_base = third_base = ['U', 'C', 'A', 'G']
    code = []
    for f in first_base:
        for s in second_base:
            for t in third_base:
                code.append(f + s + t)
                
    triplet_code = {'_': []}
    for i in range(ord('A'), ord('Z') + 1):
        triplet_code[chr(i)] = []
    for c in range(1, len(code) + 1):
        if (1 <= c <= 2):
            triplet_code['F'].append(code[c - 1])
        elif (3 <= c <= 4) or (17 <= c <= 20):
            triplet_code['L'].append(code[c - 1])
        elif (5 <= c <= 8) or (45 <= c <= 46):
            triplet_code['S'].append(code[c - 1])
        elif (9 <= c <= 10):
            triplet_code['Y'].append(code[c - 1])
        elif (13 <= c <= 14):
            triplet_code['C'].append(code[c - 1])
        elif (16 == c):
            triplet_code['W'].append(code[c - 1])
        elif (21 <= c <= 24):
            triplet_code['P'].append(code[c - 1])
        elif (25 <= c <= 26):
            triplet_code['H'].append(code[c - 1])
        elif (27 <= c <= 28):
            triplet_code['Q'].append(code[c - 1])
        elif (29 <= c <= 32) or (47 <= c <= 48):
            triplet_code['R'].append(code[c - 1])
        elif (33 <= c <= 35):
            triplet_code['I'].append(code[c - 1])
        elif (c == 36):
            triplet_code['M'].append(code[c - 1])
        elif (37 <= c <= 40):
            triplet_code['T'].append(code[c - 1])
        elif (41 <= c <= 42):
            triplet_code['N'].append(code[c - 1])
        elif (43 <= c <= 44):
            triplet_code['K'].append(code[c - 1])
        elif (49 <= c <= 52):
            triplet_code['V'].append(code[c - 1])
        elif (53 <= c <= 56):
            triplet_code['A'].append(code[c - 1])
        elif (57 <= c <= 58):
            triplet_code['D'].append(code[c - 1])
        elif (59 <= c <= 60):
            triplet_code['E'].append(code[c - 1])
        elif (61 <= c <= 64):
            triplet_code['G'].append(code[c - 1])
        else:
            triplet_code['_'].append(code[c - 1])
    delete_key = []
    for key, value in triplet_code.items():
        if not (len(value)):
            delete_key.append(key)
    for k in delete_key:
        del triplet_code[k]

    return (triplet_code)

def transcription(dna_seq):
    rna = ""
    for c in dna_seq:
        if (c == "T"):
            rna += "A"
        elif (c == "A"):
            rna += "U"
        elif (c == "G"):
            rna += "C"
        elif (c == "C"):
            rna += "G"
        else:               # dna_seq에 T A G C 외의 것이 있으면 예외 처리
            return ("")
    return (rna[::-1])

def open_reading_frame(rna, triplet_code, start):
    amino_acid = ""
    start_codon = False
    stop_codon = False
    for i in range(start, len(rna), 3):
        code = rna[i: i + 3]
        for key, val in triplet_code.items():
            if (code in val):
                amino_acid += key
                if key == 'M': 
                    start_codon = True
                elif key == '_': 
                    if (start_codon): stop_codon = True
                break
    if (start_codon and stop_codon):
        return (amino_acid)
    else:                               # amino_acid 에 M~~~_가 없으면 예외처리
        return ""

def protein_len(amino_acid):
    protein_len = -1
    s = 0

    while (s < len(amino_acid)):
        if (amino_acid[s] == 'M'):
            for e in range(s + 1, len(amino_acid)):
                if (amino_acid[e] == '_'):
                    if (protein_len < e - s):
                        protein_len = e - s
                    s = e
                    break
        s += 1
    return (protein_len)

def solution(dna_seq):
    triplet_code = make_triplet_code()
    rna = transcription(dna_seq.upper())
    answer = -1
    if not (len(rna)):
        return (answer)

    for i in range(0, 6):
        amino_acid = open_reading_frame(rna, triplet_code, i)
        if not (len(amino_acid)): continue
        max_len = protein_len(amino_acid)
        if (answer < max_len):
            answer = max_len
    
    return (answer)
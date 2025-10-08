print("***Fun with Word***")
words_input, mode = input("Enter Input : ").split("/")
words = words_input.split()

# สร้าง dictionary ให้ค่าตัวอักษร a-z
alphabet_score = {chr(i + 96): i for i in range(1, 27)}

def word_weight(word):
    """คำนวณน้ำหนักของคำจากค่า a=1, b=2, ... z=26"""
    return sum(alphabet_score.get(ch, 0) for ch in word.lower())

def insert_by_weight(sorted_list, word, index=None):
    """ใส่คำลงใน list ที่เรียงตามน้ำหนักคำ"""
    if index is None:
        index = len(sorted_list)
    if index == 0:
        sorted_list.insert(0, word)
        return
    if word_weight(word) > word_weight(sorted_list[index-1]):
        sorted_list.insert(index, word)
        return
    insert_by_weight(sorted_list, word, index-1)

# สำหรับโหมดจัดลำดับตามสระ
vowel_priority = {'a':5, 'e':4, 'i':3, 'o':2, 'u':1}

def word_vowel_score(word):
    """คืน tuple (จำนวนสระ, -ค่าสูงสุดของสระ)"""
    count = 0
    max_priority = 0
    for ch in word.lower():
        if ch in vowel_priority:
            count += 1
            if vowel_priority[ch] > max_priority:
                max_priority = vowel_priority[ch]
    return (count, -max_priority)

def insert_by_vowel(sorted_list, word, index=None):
    if index is None:
        index = len(sorted_list)
    if index == 0:
        sorted_list.insert(0, word)
        return
    if word_vowel_score(word) >= word_vowel_score(sorted_list[index-1]):
        sorted_list.insert(index, word)
        return
    insert_by_vowel(sorted_list, word, index-1)

# --- main ---
result = []

if mode.upper() == 'W':
    for w in words:
        insert_by_weight(result, w)
elif mode.upper() == 'V':
    for w in words:
        insert_by_vowel(result, w)

print(" ".join(result))
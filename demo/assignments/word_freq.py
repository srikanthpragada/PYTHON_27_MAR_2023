st = "how do you do how did you do"
words = st.split(" ")

for w in set(words):
    print(f"{w} - {words.count(w)}")



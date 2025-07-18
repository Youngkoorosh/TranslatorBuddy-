# دریافت تعداد کلمات دیکشنری
n = int(input())

# دیکشنری برای ذخیره ترجمه‌ها
dictionary = {}

# خواندن دیکشنری
for _ in range(n):
    words = input().split()
    word_ref = words[0]  # کلمه مرجع
    eng, fr, ger = words[1], words[2], words[3]
    # ذخیره ترجمه‌ها (انگلیسی، فرانسوی، آلمانی به مرجع)
    dictionary[eng] = word_ref
    dictionary[fr] = word_ref
    dictionary[ger] = word_ref
    # مدیریت کلمات چندبخشی (مثل la programmation)
    if ' ' in fr:
        dictionary[fr.replace(' ', '')] = word_ref

# دریافت جمله ورودی
sentence = input().split()

# ترجمه جمله
translated = []
for word in sentence:
    # اگر کلمه در دیکشنری باشد، ترجمه را اضافه کن، وگرنه خود کلمه
    translated.append(dictionary.get(word, word))

# چاپ خروجی
print(' '.join(translated))

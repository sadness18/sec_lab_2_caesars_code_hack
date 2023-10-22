import string

anls = ""; # текст для анализа
anls_arr = []; # массив кол-ва символов в тексте для анализа
decod = ""; # зашифрованный текст
decod_arr = []; # массив кол-ва символов в тексте для расшифровки
count = 0; # счетчик
count_arr = []; # массив разности кол-ва символов при всех сдвигах
minimum = 0; # переменная для определения минимальной разности
key = 0; # предполагаемый ключ
a = ord('а');
rus_arr = [];
rus_arr_h = [];
#eng_arr = [];
#eng_arr_h = [];

#for i in (string.ascii_lowercase):
#    eng_arr.append(i);

#for i in (string.ascii_uppercase):
#    eng_arr_h.append(i);

for i in ([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]):
    rus_arr.append(i);

for i in ([chr(i) for i in range(a,a+6)] + [chr(a+33)] + [chr(i) for i in range(a+6,a+32)]):
    rus_arr_h.append(i.upper());

for i in range(0, 33):
    anls_arr.append(0);
    decod_arr.append(0);
    count_arr.append(0);

# функцйия подсчета кол-ва символов в тексте
def text(string, arr):
    for i in range(0, len(string)):
        for j in range(0, 33):
            if ((string[i] == rus_arr[j]) or (string[i] == rus_arr_h[j])):
                arr[j] += 1;

print("Введите текст для анализа: ");
anls = input();
text(anls, anls_arr);

print("Введите текст для расшифровки: ");
decod = input();
text(decod, decod_arr);

# величина сдвига
for i in range(0, 33):
    count = 0;
    for j in range(0, 33):
        ind = j + i; # сдвиг
        if (ind > 32):
            ind -= 33;
        count += abs(anls_arr[j] - decod_arr[ind]);
        count_arr[i] = count;
print(count_arr);
for i in range(0, 33):
    if (i == 0):
        minimum = count_arr[i];
        key = i;
    else:
        if (count_arr[i] < minimum):
            minimum = count_arr[i];
            key = i;

print("Предполагаемый ключ: ", key);

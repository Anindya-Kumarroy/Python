# একটি মূল লিস্ট তৈরি করা হলো
numbers = [2, 1, 3]

# ১. append(): লিস্টের একদম শেষে নতুন উপাদান যোগ করে
numbers.append(4)  # Output: [2, 1, 3, 4]
print(numbers)

# ২. sort(): ছোট থেকে বড় (Ascending order) সাজায়
numbers.sort()  # Output: [1, 2, 3, 4]
print(numbers)

# ৩. sort(reverse=True): বড় থেকে ছোট (Descending order) সাজায়
numbers.sort(reverse=True)  # Output: [4, 3, 2, 1]
print(numbers)

# ৪. reverse(): লিস্টের উপাদানগুলোর ক্রম উল্টে দেয়
numbers.reverse()  # Output: [1, 2, 3, 4]
print(numbers)

# ৫. insert(index, element): নির্দিষ্ট ইনডেক্সে নতুন উপাদান বসায়
# উদাহরণস্বরূপ: 3 নম্বর ইনডেক্সে 9 বসানো হলো
numbers.insert(3, 9)  # Output: [1, 2, 3, 9, 4]
print(numbers)

# remove(val): মান (value) দেখে প্রথমবার পাওয়া উপাদানটি লিস্ট থেকে সরিয়ে দেয়
# নোট: লিস্টে না থাকা মান দিলে ValueError আসবে
numbers.remove(9)
print(numbers)  # Output: [5, 2, 9, 4]

# pop(2) মেথডটি 2 নম্বর ইনডেক্সের উপাদানটিকে (যেটি হলো 3) মুছে ফেলবে
numbers.pop(2)
print(numbers)  # Output: [5, 2, 4]
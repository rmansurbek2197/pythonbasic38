class PalindromChecker:
    def __init__(self):
        self.text = input("Matn kiriting: ")
        self.text = self.text.replace(" ", "").lower()

    def is_palindrom(self):
        return self.text == self.text[::-1]

    def check(self):
        if self.is_palindrom():
            print("Matn palindrom")
        else:
            print("Matn palindrom emas")

    def get_statistics(self):
        print("Matn uzunligi: ", len(self.text))
        print("Matn ichidagi belgi soni: ", len(self.text.replace(" ", "")))

    def start(self):
        self.check()
        self.get_statistics()

def main():
    checker = PalindromChecker()
    checker.start()
    while True:
        javob = input("Dasturni qayta ishga tushirishni istaysizmi? (ha/yo'q): ")
        if javob.lower() == "ha":
            checker = PalindromChecker()
            checker.start()
        elif javob.lower() == "yo'q":
            break
        else:
            print("Noto'g'ri javob. Iltimos, qayta urinib ko'ring.")

if __name__ == "__main__":
    main()
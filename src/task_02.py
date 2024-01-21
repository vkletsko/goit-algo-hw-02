from collections import deque


def check_palindrome(text):
    if len(text) == 0:
        return "Empty text"

    cleaned_phrase = text.lower().replace(" ", "")

    chars_dq = deque(cleaned_phrase)
    if chars_dq == deque(reversed(chars_dq)):
        return f"{text} is a palindrome"

    return f"{text} is not a palindrome"


def is_palindrome(text):
    if len(text) == 0:
        return "Empty text"

    cleaned_phrase = text.lower().replace(" ", "")

    chars_dq = deque(cleaned_phrase)
    while len(chars_dq) > 1:
        if chars_dq.popleft() != chars_dq.pop():
            return f"{text} is not a palindrome"

    return f"{text} is a palindrome"


def main():
    txt = input("Enter a phrase: ")
    res = check_palindrome(txt)
    print("res: ", res)

    res2 = is_palindrome(txt)
    print("res2: ", res2)


if __name__ == "__main__":
    main()

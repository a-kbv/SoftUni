# def reverse_string(text):
#     st = []
#     for ch in text:
#         st.append(ch)
#
#     reversed_text = []
#     while st:
#         ch = st.pop()
#         reversed_text.append(ch)
#     return ''.join(reversed_text)
#
# print(reverse_string(input()))

def reverse_string(text):
    return text[::-1]

print(reverse_string(input()))
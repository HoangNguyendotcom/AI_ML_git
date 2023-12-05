import gensim.downloader as api
import numpy as np

# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
model = api.load("glove-twitter-25")
# 25 ~ Runtime: 30s
# 50 ~ Runtime: 1m
# 100 ~ Runtime: 2m
# 200 ~ Runtime: 3.5m

"""
word = "beautiful"
print(model[word])
"""

"""
print("1----------")
result = model.most_similar(word, topn=10)
print(result)
"""

"""
print("2----------")
result = model.most_similar(positive=["january", "february"], topn=10)
print(result)
"""

"""
print("3----------")
result = model.similarity("man", "woman")
print(result)
"""

"""
print("4----------")
result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
print(result)
"""

"""
print("5----------")
result = model.most_similar(positive=["berlin", "vietnam"], negative=["hanoi"], topn=1)
print(result)
"""

"""
print("6----------")
result = model.similarity("marriage", "happiness")
print(result)
"""

#TODO: Các bạn thử viết 2 cách khác nhau để tính cosine similarity
# giữa 2 vector nhé. Kết quả giống với khi dùng model.similarity() là được
# 1 cách là dùng numpy, 1 cách là không dùng numpy nhé
def Np_cosine(word1: str, word2: str) -> float:
    #Get the word vectors using the model:
    vector_word1 = model[word1]
    vector_word2 = model[word2]

    # Calculate the dot product:
    dot_product = np.dot(vector_word1, vector_word2)

    #Calculate magnitudes of the vectors:
    mag_word1 = np.linalg.norm(vector_word1)
    mag_word2 = np.linalg.norm(vector_word2)

    #Calculate the cosine similarity:
    cosine_similarity = dot_product / (mag_word1 * mag_word2)

    return cosine_similarity

def NotNp_cosine(word1: str, word2: str) -> float:
    #Get the word vectors using the model:
    vector_word1 = model[word1]
    vector_word2 = model[word2]

    size = vector_word1.shape[0]

    # Calculate the dot product:
    # A * B = A1*B1 + A2*B2 + .. + An*Bn
    dot_product = 0

    #Calculate the magnitudes of the vectors:
    # ||V|| = sqrt(V1^2 + ... + Vn^2)
    mag_word1_sq = 0
    mag_word2_sq = 0

    for n in range(size):
        dot_product += vector_word1[n] * vector_word2[n]
        mag_word1_sq += vector_word1[n] ** 2
        mag_word2_sq += vector_word2[n] ** 2
    mag_word1 = np.sqrt(mag_word1_sq)
    mag_word2 = np.sqrt(mag_word2_sq)

    #Calculate the cosine similarity:
    cosine_similarity = dot_product / (mag_word1 * mag_word2)
    
    return cosine_similarity


def main():
    while True:
        word1 = input("Please input the word1: ").lower().strip()
        word2 = input("Please input the word2: ").lower().strip()
        result1 = Np_cosine(word1, word2)
        result2 = NotNp_cosine(word1, word2)
        result3 = model.similarity(word1, word2)
        print("Cosine Similarity (Numpy): {}".format(result1))
        print("Cosine Similarity (No Numpy): {}".format(result2))
        print("Cosine Similarity (GenSim): {}".format(result3))

main()
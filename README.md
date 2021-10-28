# Flipkart-product-reviews
NLP - Machine learning

<img align="left" alt="Visual Studio Code" width="1080px" src="https://feedcheck.co/blog/wp-content/uploads/2017/11/Skeptical-about-Amazon-Product-Reviews-Here-is-How-to-Find-the-Truth1.jpg" />

# About

---

Product reviews is an essential part of an online store like Flipkart’s branding and marketing. They help to build trust and loyalty and typically describe what sets your product apart from others. Savvy shoppers almost never purchase a product without knowing how it’s going to work for them. The more reviews a platform has, the more convinced a user will be that he/she is making the right decision.

Online reviews are very important to e-commerce businesses because they ultimately increase sales by giving the consumers the information they need to make the decision to purchase the product. One other important factor in elevating the reputation, standard, and evaluation of an e-commerce store is product rating. 

# NLP

---

Natural Language Processing (NLP) helps machines “read” text by simulating the human ability to understand language. It is a field of Artificial Intelligence that gives machines the ability to read, understand and derive meaning from human languages.

<img align="left" alt="Visual Studio Code" width="1080px" src="https://cdn.searchenginejournal.com/wp-content/uploads/2020/08/an-introduction-to-natural-language-processing-with-python-for-seos-5f3519eeb8368.png" />

# #1 Tokenization

---

Tokenization is the process of breaking down sentence or paragraphs into smaller chunks of words called tokens.

# #2 Stop Words Removal

---

On removal of some words, the meaning of the sentence doesn't change, like and, am. Those words are called stop-words and should be removed before feeding to any algorithm. In datasets, some non-stop words repeat very frequently. Those words too should be removed to get an unbiased result from the algorithm.

# #3 Vectorization

---

After tokenization, and stop words removal, our "content" are still in string format. We need to convert those strings to numbers based on their importance (features). We use TF-IDF vectorization to convert those text to vector of importance. With TF-IDF we can extract important words in our data. It assign rarely occurring words a high number, and frequently occurring words a very low number.

# Topic Modelling - LDA

<img align="left" alt="Visual Studio Code" width="720px" src="https://www.slideteam.net/media/catalog/product/cache/960x720/p/r/product_review_summary_Slide01.jpg" />

---
Topic modeling in python involves counting words and grouping similar word patterns to infer topics within unstructured data. Let’s take the example of Flipkart where you might want to know what customers are saying about a particular product from x seller. Instead of spending hours to find out the best-reviewed product through heaps of feedback, you can analyze them with a topic modeling algorithm.

By detecting patterns such as word frequency and distance between words, a topic model clusters feedback that is similar, and words and expressions that appear most often. With this information, you can quickly deduce what each set of texts are talking about.

There are various topic in modelling algorithms, we will be using the Latent Dirichlet Allocation algorithm(LDA).


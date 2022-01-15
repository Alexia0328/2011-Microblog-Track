## [2011-Microblog-Track](https://trec.nist.gov/data/microblog2011.html)

#### Xinyi HE

## Task 1

Implement an Information Retrieval (IR) system based for a collection of documents (Twitter messages)

**Step 1**. Preprocessing: Implement preprocessing functions for tokenization and stopword removal. The index terms will be all the words left after filtering out punctuation tokens, numbers, stopwords, etc. Optionally, use the Porter stemmer to stem the index words. 

•       Input: Documents that are read one by one from the collection

•       Output: Tokens to be added to the index (vocabulary)

 

**Step 2**. Indexing:  Build an inverted index, with an entry for each word in the vocabulary. Use any appropriate data structure (hash table, linked lists, Access database, etc.). 

•       Input: Tokens obtained from the preprocessing module

•       Output: An inverted index for fast access

For weighting, use the tf-idf weighting scheme (w_ij = tf_ij x idf_i). For each query, the system will produce a ranked list of documents, starting with the most similar to the query and ending with the least similar. For the query terms, use a modified tf-idf weighting scheme w_iq = (0.5 + 0.5 tf_iq)∙idf_i

 

**Step 3**. Retrieval and Ranking:  Use the inverted index (from step 2) to find the limited set of documents that contain at least one of the query words. Compute the similarity scores between a query and each document (using cosine or other method). 

 

•       Input: One query and the Inverted Index (from Step2)

•       Output: Similarity values between the query and each of the documents. Rank the documents in decreasing order of similarity scores.

 
**Step 4**. Results file: Run the system on the set of test queries.  Include the output as a file named Results. 

The file should have the following TREC format. Include the top-1000 results for each query (the queries should be ordered in ascending order): topic_id Q0 docno rank score tag where: topic_id is the topic/query number (use the numbers, such a 1 instead of MB001), Q0 is an unused field (the literal 'Q0'), docno is the tweet id, rank is the rank assigned by the system to the segment (1 is the highest rank), score is the computed degree of match between the segment and the topic, and tag is a unique identifier the chose for this run (same for every topic).

**Step 5**. Evaluation: For evaluation, use the trec_eval script. The main evaluation measures will be MAP (mean average precision) and P@10 (precision in the first 10 documents retrieved). Compare the results with the expected results, from the relevance feedback file, available here, in the following format:

Q_no 0     tweet_id         Relevance

where Q_no is the query number and Relevance can be 0 (not relevant) or 1 (relevant). 

### Task 2

The goals of this assignment is to explore recent neural information retrieval methods (based on deep learning, transformers, BERT-like models) in order to achieve better evaluation scores than in Task 1.

1. Query vector modification or query expansion based on pretrained word embeddings or other methods. For example, add synonyms to the query if there is similarity with more than one word in the query (or with the whole query vector). Use pre-trained word embeddings (such as FastText, word2vec, GloVe, and others), preferably some build on a Twitter corpus, to be closer to the collection of documents.

2.  Use BERT or other neural models from the beginning, without the need on an initial classical IR system, to compute the similarity between the query and every document in the collection. For example, use a simple boolean index to restrict the calculations only to documents that have at least one query word.




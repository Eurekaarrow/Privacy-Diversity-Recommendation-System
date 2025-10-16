# Privacy-Diversity-Recommendation-System

## 1. Preparing Dataset - MovieLens 25M Dataset Summary

### Summary

This dataset (**ml-25m**) describes 5-star rating and free-text tagging activity from [MovieLens](https://movielens.org), a movie recommendation service.  
It contains **25,000,095 ratings** and **1,093,360 tag applications** across **62,423 movies**.  
These data were created by **162,541 users** between **January 9, 1995** and **November 21, 2019**.  
The dataset was generated on **November 21, 2019**.

- Users were selected at random, and all had rated at least 20 movies.
- No demographic information is included.
- Each user is represented by an anonymized ID.
- The dataset files include:  
  `genome-scores.csv`, `genome-tags.csv`, `links.csv`, `movies.csv`, `ratings.csv`, and `tags.csv`.

All datasets are publicly available for download at:  
👉 [http://grouplens.org/datasets/](http://grouplens.org/datasets/)

---

### Usage License

The dataset may be used for research purposes under the following conditions:

- You **may not** state or imply any endorsement from the University of Minnesota or the GroupLens Research Group.  
- You **must acknowledge** the dataset in any publication using it.  
- You **may not redistribute** the dataset without permission.  
- You **may not use** it for commercial purposes without prior authorization from a GroupLens faculty member.  
- The software scripts are provided **“as is”**, without any warranty.  
- The University of Minnesota and its affiliates are **not liable** for any damages resulting from use of the dataset.

For questions or comments, contact:  
📧 **grouplens-info@umn.edu**

---

### Citation

If you use this dataset, please cite:

> F. Maxwell Harper and Joseph A. Konstan. 2015.  
> *The MovieLens Datasets: History and Context.*  
> ACM Transactions on Interactive Intelligent Systems (TiiS) 5(4): 19:1–19:19.  
> [https://doi.org/10.1145/2827872](https://doi.org/10.1145/2827872)

---

### About GroupLens

GroupLens is a research group in the **Department of Computer Science and Engineering** at the **University of Minnesota**.  
Since 1992, its projects have explored:

- Recommender systems  
- Online communities  
- Mobile and ubiquitous technologies  
- Digital libraries  
- Local geographic information systems  

GroupLens operates the MovieLens recommender system based on collaborative filtering — the source of these data.

Visit: [http://movielens.org](http://movielens.org)

If you have ideas for experimental work using MovieLens, email **grouplens-info@cs.umn.edu**.

---

### ✅ Verifying Dataset Contents

To verify the dataset integrity (check MD5 checksum):

#### On Linux
```bash
md5sum ml-25m.zip; cat ml-25m.zip.md5

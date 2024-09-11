**PROJECT OVERVIEW**
This project is using K-Means algorithm and RFM Analysis technique to build Machine learning model to segment customers based on their RFM Score (Recency, Frequency, Monetary Value).
Based on the clusters created we will recommend personalized and effective marketing campaigns to increase customer retention and incrase revenue.

**Objective**
1. Identifying distinct customer segments/group.
2. Visualizing and Interpreting segments.
3. Provide recommendations for marketing strategies.

**Dataset**: We are using Online Retail dataset as a sample to train our model.

**Methodology**
1. Data Preprocessing: Explore and Clean the dataset to remove missing values or inconsistent entries.
2. Feature Selection: Select key features like InvoiceNo, Quantity, InvoiceDate, UnitPrice, CustomerID for clustering.
3. Compute RFM score: Calculate Recency(R), Frequency(F) and Monetory value(M)
4. K-Means Algorithm: Apply the K-Means algorithm on RFM score to segment customers into different clusters.
5. Evaluation: Elbow method to determine the optimal number of clusters.
6. Visualization: Interpret and visualize the clusters using bar plots and pie charts.

**Conclusion**

Model divided customers into 4 clusters:

1. _Power Shoppers_ : Highest highest recency, frequency, and monetary score.
2. _Loyal customers_:  Moderate recency, frequency, and monetary values. These customers still spend more and purchase more frequently than clusters 2 and 3.
3. _Inactive/ At-risk customers_: Lowest RFM score. These customers spend less, don’t buy often, and haven’t made a purchase recently.
4. _Recent Customers_: High Recency,  relatively lower frequency and moderate monetary values. Potential long-term customers.

_Personalized Recommendation_
 1. Power Shoppers: Offer personalized special discounts, early access, and other perks to make them feel valued and appreciated.
 2. Loyal Customers: Appreciation campaigns, referral bonuses, and rewards for loyalty.
 3. At-Risk Customers: Re-engagement efforts including discounts or promotions to encourage buying.
 4. Recent Customers: Targeted campaigns educating about the brand and discounts on subsequent purchases.

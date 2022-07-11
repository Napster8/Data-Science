# Customer Segmentation Based on Recency, Frequency and Monetary Values(RFM) 

Just because you can use Ensemble of Machine Learning Technique, use Grid or Randomized search to identify the best performing Machine Learning Model, doesn't `ALWAYS` mean you have to take that route! 

Some times simple statistical procedures such as quartile segmentation and little bit of programming can fetch you the results!

Here is an illustration of E-Commerce Purchase History from a Retail Store and how the Customers are classified into different segments or classes!


1. Data Pre-Processing Techniques such as cleaning, null values removal.
2. Feature Creation
  * First Feature name: Recency: Number of days since the last purchase by the customer.
  * Second Feature name: Total Number of Purchases by each customer.
  * Third Feature name: Monetary Value.
3. Segmentation Processing using `if-else` statements:
    * Customer Segmentation into 4 `quartiles` based on `Recency` value:

        * High recency indicates that customer has not returned back. This indicates, customer is not happy with the purchases they made or has shifted their house to some other location.

    * Customer Segmentation based on `Frequency` value:
        * High Frequency indicates that customer is happy with the purchases he makes and is more likely to return than other customers.

    * Customer Segmentation based on `Monetary` value:
        * High Monetary Value indicates that the customer was willing to spend more money than other customers.

4. Metrics to track:
    * Who are our Best Customers, Loyal Customers, Big Spenders, Almost Lost, Lost Cheap Customers.

5. References:
    * Link : https://www.blastanalytics.com/blog/rfm-analysis-boosts-sales

This article clearly explains how RFM is performed.

6. Actions to take:

From what I could think of on top of my head at the time:

**Best Customers** : Reward them. They can be early adopters to new products. Suggest them "Refer a friend".

**At Risk or Almost Lost**: Send them personalized emails to encourage them to shop.

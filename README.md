# Customer Affinity Modelling

## Introduction

This project is aimed at modeling customer affinity for car insurance. The goal of this project is to predict which customers are most likely to be interested in purchasing a new insurance policy. The results of this project can help the insurance company to focus their marketing efforts and resources on the customers who are most likely to buy, thereby increasing their conversion rate and overall revenue.

## Data

The dataset used for this project contains information about customers, such as age, car age, the presence of damage to the car, etc. The target variable indicates whether the customer is interested in purchasing a new insurance policy or not.

## Methodology

Modelling customer affinity is a binary classification problem. Three machine learning algorithms were trained for this project: logistic regression, random forest, and SDGClassifier. The performance of each model was evaluated using the precision, recall, and F1-score metrics. The weighted average was also taken into consideration.

## Results

The random forest model achieved the best results, with a recall score of 0.94, precision score of 0.77, and weighted average of 0.85. This model was selected as the final model for this project.

## Limitations

The SMOTE technique used to balance the target classes may cause overfitting. It is important to be cautious when using SMOTE and to try other techniques such as undersampling the majority class and oversampling the minority class.

One potential limitation of the model is that it may not be fully optimized. There is still room for improvement and it may be necessary to continue to fine-tune the model in order to increase its accuracy and performance. Further optimization may involve adjusting hyperparameters, using different techniques for feature selection and preprocessing, and exploring alternative algorithms. It is important to continually assess the model and make updates as necessary in order to achieve the best results.

## Future Work

There is potential for further fine-tuning of the models. Additionally, other algorithms such as SVM or K-nearest neighbors could also be explored.
## Conclusion

This project demonstrates the use of machine learning algorithms for predicting customer affinity. The results of the random forest model show that it is possible to accurately predict which customers are most likely to be interested in purchasing a new insurance policy. This information can help the company to focus their marketing efforts and resources on the customers who are most likely to buy, thereby increasing their conversion rate and overall revenue.

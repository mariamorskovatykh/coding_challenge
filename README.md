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

_________________________________________________________________________________________________________________________________________

# Modellierung der Kundenaffinität
## Einführung

Dieses Projekt zielt darauf ab, die Kundenaffinität für Kfz-Versicherungen zu modellieren. Ziel dieses Projekts ist es, ein Machine Learning Modell zu entwickeln, das die Kundenaffinität vorhersagen kann. Das Verständnis der Kundenaffinität ist für Unternehmen wichtig, da es hilft, die wertvollsten Kunden zu identifizieren und Strategien zu entwickeln, um ähnliche Kunden zu halten und anzuziehen.

## Daten

Der Datensatz enthält Informationen über Kunden, wie z. B. Alter, Alter von Fahrzeug, Vorschaden usw. Die Zielvariable gibt an, ob die Kunden Intesesse am Angebot haben.

## Methodik

Die Modellierung der Kundenaffinität ist ein binäres Klassifikationsproblem. Für dieses Projekt wurden drei Machine Learning Modelle trainiert: logistische Regression, Random Forest und SDGClassifier. Die Leistung jedes Modells wurde anhand der Metriken Recall, Precision und F1-Score bewertet.

## Ergebnisse

Das Random-Forest-Modell erzielte die besten Ergebnisse mit einem Recall-Score von 0,94, einem Precision-Score von 0,77 und einem gewichteten Durchschnitt von 0,85. Dieses Modell wurde als endgültiges Modell für dieses Projekt ausgewählt.

## Einschränkungen

Die SMOTE-Technik kann zu einer Overfitting führen. Es ist wichtig, bei der Verwendung von SMOTE vorsichtig zu sein und andere Techniken auszuprobieren, z. B. gleichzeitige Undersampling der Mehrheitsklasse und Oversampling der Minderheitsklasse.

Eine mögliche Einschränkung des Modells besteht darin, dass es möglicherweise nicht vollständig optimiert ist. Es gibt noch Raum für Verbesserungen, und es kann notwendig sein, das Modell weiter zu verfeinern, um seine Leistung zu erhöhen. 

## Zukünftige Arbeit

Es besteht Potenzial für eine weitere Feinabstimmung der Modelle. Darüber hinaus könnten auch andere Algorithmen wie SVM oder K-nächste Nachbarn untersucht werden.

## Abschluss

Dieses Projekt demonstriert die Verwendung von Machine Learning Algorithmen zur Vorhersage der Kundenaffinität. Die Ergebnisse des Random-Forest-Modells zeigen, dass es möglich ist, genau vorherzusagen, welche Kunden am wahrscheinlichsten am Kauf einer neuen Versicherung interessiert sind. Diese Informationen können dem Unternehmen helfen, seine Marketingbemühungen und -ressourcen auf die Kunden zu konzentrieren, die am ehesten kaufen werden, wodurch seine Konversionsrate und sein Gesamtumsatz gesteigert werden.

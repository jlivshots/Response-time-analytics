# Police Response Time Analytics
Dataset: [Police Incidents in Champaign County since 1988](https://data.ccrpc.org/dataset/police-incidents-since-1988/resource/6e3d7e45-eccf-4e84-9d4e-65d9c455cf49)

## Contents
- [Running the Project](#running-the-project)
- [Understanding the Dataset](#understanding-the-dataset)
- [CatBoost](#catboost)
- [SAHP](#shap)
- [Findings](#findings)
- [Summaries](#summaries)


## Running the Project
* Use [environment.yml](environment.yml) to install dependencies
* Download the dataset into the [data](data/) folder
* Run [Clean_data.ipynb](Clean_data.ipynb) (only needs to be done once)
* Run [Catboost.ipynb](Catboost.ipynb)

## Understanding the Dataset
Pre-processed data has the following columns:
* Response time: minutes between time arrived and time reported
* Crime Category Description: directly from dataset
* Mins of Day: minutes since midnight of time reported
* Geo Code: directly from dataset, see [here](https://www.urbanaillinois.us/sites/default/files/attachments/04-upd-geocode-map.pdf) for an example
* Day of Week: 0-6, Monday-Sunday
* Month Occurred: 1-12, Jan-Dec
* Day of Year
* Day of Month
* Year Occurred

## CatBoost
I used [CatBoost](https://catboost.ai/) to quickly and accurately analyze the dataset because of its support for categorical data (Crime Category Description and Geo Code)

## SHAP
My main data analysis comes from SHAP visualizations to assess feature importance on the model. In this project I trained a model to predict police response time in Champaign county given various feature values, and SHAP visualizations help us better undestand each feature's relationship with response time. For the following visuals, the magnitude of the SHAP value indicates how significant that feature is in predicting response time. A positive SHAP value represents an increased response time, and a negative SHAP value indicates a decreased response time. You can learn more about SHAP [here](https://github.com/slundberg/shap).

## Findings
Below is data from modelling response times over 0 mins and within an hour. Response time of 0 mins is ommitted to avoid incidents initiated by an officer, rather than called in by somebody.
<p align="center">
  <img src="https://user-images.githubusercontent.com/60240640/129144035-293cd93f-981a-47c8-a17f-d1df81ef1a6d.png">
</p>

  
<p align="center">
  <img src="https://user-images.githubusercontent.com/60240640/129143564-cb592d2c-b7be-43b0-a0d4-d94eef8b3110.jpg">
</p>

## Summaries
* [All Categories (200282 entries)](SHAP-plots/All_categories.pdf)
* [Traffic Offenses (10870 entries)](SHAP-plots/traffic_offenses.pdf)
* [Theft (21087 entries)](SHAP-plots/theft.pdf)
* [Accident (14128 entries)](SHAP-plots/accident.pdf)
* [Battery (22899 entries)](SHAP-plots/battery.pdf)
* [Domestic Dispute (18808 entries)](SHAP-plots/domestic_dispute.pdf)
* [Criminal Damage (14261 entries)](SHAP-plots/criminal_damage.pdf)
* [Assist Other Agency/Business (16355 entries)](SHAP-plots/assist_other_agencyBusiness.pdf)
* [Disorderly Conduct (9921 entries)](SHAP-plots/disorderly_conduct.pdf)
* [Burglary (10757 entries)](SHAP-plots/burglary.pdf)
* [Interfering w/Public Officers (5625 entries)](SHAP-plots/interfering_wPublic_officers.pdf)
* [Deception & Fraud (4845 entries)](SHAP-plots/deception_fraud.pdf)
* [Crisis Intervention (5108 entries)](SHAP-plots/crisis_intervention.pdf)
* [Burglary from Motor Vehicle (4757 entries)](SHAP-plots/burglary_from_motor_vehicle.pdf)
* [Suicide, Attempts, and Threats (2537 entries)](SHAP-plots/suicide_attempts_threats.pdf)
* [Assault (3350 entries)](SHAP-plots/assault.pdf)
* [Offenses Involving Children (2488 entries)](SHAP-plots/offenses_involving_children.pdf)
* [Robbery (1668 entries)](SHAP-plots/robbery.pdf)
* [Kidnapping (1003 entries)](SHAP-plots/kidnapping.pdf)
* [Sex Offenses (779 entries)](SHAP-plots/sex_offenses.pdf)
* [Criminal Sexual Assault (707 entries)](SHAP-plots/criminal_sexual_assault.pdf)

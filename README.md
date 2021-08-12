# Police Response Time Analytics
Dataset: [Police Incidents in Champaign County since 1988](https://data.ccrpc.org/dataset/police-incidents-since-1988/resource/6e3d7e45-eccf-4e84-9d4e-65d9c455cf49)

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

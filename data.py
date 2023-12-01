import pandas as pd

def average_age_modal_age_median_age_death(data):
    death_data = [entry['age'] for entry in data.values() if entry['DEATH_EVENT'] == 1]

    if not death_data:
        return None, None, None

    average_age = sum(death_data) / len(death_data)
    modal_age = pd.Series(death_data).mode()[0]
    median_age = pd.Series(death_data).median()
    items = [{
        "name":"average_age", "value": average_age},
        {"name":"modal_age", "value": modal_age},
        {"name":"median_age", "value": median_age}]
    return items

def average_time_no_death(data):
    no_death_data = [entry['time'] for entry in data.values() if entry['DEATH_EVENT'] == 0]

    if not no_death_data:
        return None

    average_time = sum(no_death_data) / len(no_death_data)
    items = [{
        "name":"average_time", "value": average_time}]
    return items

def age_stats_high_blood_pressure(data):
    high_bp_data = [entry['age'] for entry in data.values() if entry['high_blood_pressure'] == 1]

    if not high_bp_data:
        return None, None, None

    modal_age = pd.Series(high_bp_data).mode()[0]
    average_age = sum(high_bp_data) / len(high_bp_data)
    median_age = pd.Series(high_bp_data).median()
    items = [{
        "name":"average_age", "value": average_age},
        {"name":"modal_age", "value": modal_age},
        {"name":"median_age", "value": median_age}]
    return items

def age_stats_diabetes(data):
    diabetes_data = [entry['age'] for entry in data.values() if entry['diabetes'] == 1]

    if not diabetes_data:
        return None, None, None

    modal_age = pd.Series(diabetes_data).mode()[0]
    average_age = sum(diabetes_data) / len(diabetes_data)
    median_age = pd.Series(diabetes_data).median()
    items = [{
        "name":"average_age", "value": average_age},
        {"name":"modal_age", "value": modal_age},
        {"name":"median_age", "value": median_age}]
    return items

def diabetes_linked_to_smoking_and_hbp(data):
    # Check if diabetes is linked to smoking and high blood pressure
    diabetes_smoking_hbp_data = [entry for entry in data.values() if entry['diabetes'] == 1 and entry['smoking'] == 1 and entry['high_blood_pressure'] == 1]
    items = [{
        "name":"Is Diabetes linked to Smoking and High Blood Pressure?", "value": len(diabetes_smoking_hbp_data)>0
        }]
    return items

def average_serum_sodium_diabetes(data):
    diabetes_data = [entry['serum_sodium'] for entry in data.values() if entry['diabetes'] == 1]

    if not diabetes_data:
        return None

    average_sodium = sum(diabetes_data) / len(diabetes_data)
    items = [{
        "name":"average_sodium", "value": average_sodium
        }]
    return items

def anaemia_linked_to_smoking(data):
    # Check if anaemia is linked to smoking
    anaemia_smoking_data = [entry for entry in data.values() if entry['anaemia'] == 1 and entry['smoking'] == 1]
    items = [{
        "name":"Is Anaemia linked to Smoking?", "value": len(anaemia_smoking_data)>0
        }]
    return items

def no_hbp_died_of_heart_failure(data):
    # Find anyone without high blood pressure that died of heart failure
    no_hbp_died_data = [entry for entry in data.values() if entry['DEATH_EVENT'] == 1 and entry['high_blood_pressure'] == 0]
    items = [{
        "name":"no_hbp_died_data", "value": len(no_hbp_died_data)
        }]
    return items

def iqr_ejection_fraction_serum_creatinine(data):
    # Compute the interquartile ranges (IQRs) of ejection fraction and serum creatinine
    iqr_ef = pd.Series([entry['ejection_fraction'] for entry in data.values()]).quantile(0.75) - pd.Series([entry['ejection_fraction'] for entry in data.values()]).quantile(0.25)
    iqr_creatinine = pd.Series([entry['serum_creatinine'] for entry in data.values()]).quantile(0.75) - pd.Series([entry['serum_creatinine'] for entry in data.values()]).quantile(0.25)
    items = [{
        "name":"iqr_ef", "value": iqr_ef},
        {"name":"iqr_creatinine", "value": iqr_creatinine
        }]
    return items

def sample_variance_cpk_serum_sodium(data):
    # Compute the sample variance of creatinine phosphokinase and serum sodium
    variance_cpk = pd.Series([entry['creatinine_phosphokinase'] for entry in data.values()]).var()
    variance_sodium = pd.Series([entry['serum_sodium'] for entry in data.values()]).var()
    items = [{
        "name":"variance_cpk", "value": variance_cpk},
        {"name":"variance_sodium", "value": variance_sodium
        }]
    return items

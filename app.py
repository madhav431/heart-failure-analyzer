import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

from data import average_age_modal_age_median_age_death, average_time_no_death, age_stats_high_blood_pressure, age_stats_diabetes, diabetes_linked_to_smoking_and_hbp, average_serum_sodium_diabetes, anaemia_linked_to_smoking, no_hbp_died_of_heart_failure, iqr_ejection_fraction_serum_creatinine, sample_variance_cpk_serum_sodium

app = Flask(__name__)
CORS(app)


def load_data(file_path):
  """
  Load the heart failure clinical record dataset from a CSV file into a nested dictionary.

  Parameters:
  - file_path: str, the path to the CSV file.

  Returns:
  - data_dict: dict, a nested dictionary containing the dataset.
  """
  df = pd.read_csv(file_path)
  data_dict = df.to_dict(orient='index')
  return data_dict


# Example usage:
file_path = 'dataset.csv'

heart_failure_data = load_data(file_path)

@app.route('/avgnodeath')
def avgnodeath():
    data = average_time_no_death(heart_failure_data)
    return jsonify(data)

@app.route('/agestatsofdeath')
def agestatsofdeath():
    data = average_age_modal_age_median_age_death(heart_failure_data)
    return jsonify(data)

@app.route('/agestatsofhighbp')
def agestatsofhighbp():
    data = age_stats_high_blood_pressure(heart_failure_data)
    return jsonify(data)

@app.route('/agestatsofdiabetes')
def agestatsofdiabetes():
    data = age_stats_diabetes(heart_failure_data)
    return jsonify(data)

@app.route('/diabetessmokehbp')
def diabetessmokehbp():
    data = diabetes_linked_to_smoking_and_hbp(heart_failure_data)
    return jsonify(data)

@app.route('/avgserumsdiabetes')
def avgserumsdiabetes():
    data = average_serum_sodium_diabetes(heart_failure_data)
    return jsonify(data)

@app.route('/anaemialinktosmoking')
def anaemialinktosmoking():
    data = anaemia_linked_to_smoking(heart_failure_data)
    return jsonify(data)

@app.route('/nohbpdiedofheartfailure')
def nohbpdiedofheartfailure():
    data = no_hbp_died_of_heart_failure(heart_failure_data)
    return data

@app.route('/iqrefserumcreatinine')
def iqrefserumcreatinine():
    data = iqr_ejection_fraction_serum_creatinine(heart_failure_data)
    return data

@app.route('/svcpkserumsodium')
def svcpkserumsodium():
    data = sample_variance_cpk_serum_sodium(heart_failure_data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

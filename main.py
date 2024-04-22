from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('heart.html')


@app.route('/test')
def test():
    return render_template('heart.html')

@app.route('/get_data', methods = ['POST'])
def model_prediction():
    data = request.form 
    print(data)

    load_model = pickle.load(open(r'C:\Users\gauri\Documents\Heart_project\artifacts\model.pkl','rb'))
    print(load_model)

    user_data = [[float(data['age']),
                  float(data['sex']),
                  float(data['cp']),
                  float(data['trestbps']),
                  float(data['chol']),
                  float(data['fbs']),
                  float(data['restecg']),
                  float(data['thalach']),
                  float(data['exang']),
                  float(data['oldpeak']),
                  float(data['slope']),
                  float(data['ca']),
                  float(data['tha'])
                  ]]
    
    print(user_data)


    result = load_model.predict(user_data)

    print(result)

    target = ['no', 'yes']

    print(f"prediction = {target[result[0]]}")


    return target[result[0]]


if __name__ == "__main__":
    app.run(debug=True)
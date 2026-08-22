from flask import Flask, render_template, request

app = Flask(__name__)

# Логика расчета (наша "бизнес-логика")
def calculate_cost(project_type, hours, express):
    # Базовые ставки
    rates = {
        'landing': 5000,
        'store': 15000,
        'portal': 30000
    }
    
    base_price = rates.get(project_type, 0)
    total = base_price + (int(hours) * 1000) # 1000 руб за час работы
    
    if express: # Если стоит галочка "Срочно"
        total *= 1.5
        
    return total

@app.route('/', methods=['GET', 'POST'])
def index():
    cost = None
    if request.method == 'POST':
        # Получаем данные из формы
        p_type = request.form.get('project_type')
        p_hours = request.form.get('hours', 0)
        p_express = request.form.get('express') == 'on'
        
        # Считаем
        cost = calculate_cost(p_type, p_hours, p_express)
        
    return render_template('index.html', cost=cost)

if __name__ == '__main__':
    app.run(debug=True)

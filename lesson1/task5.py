'''5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

turnover = int(input('Turnover \n'))
costs = int(input('Costs \n'))
margin = turnover - costs


if turnover > costs:
    print(f'Plus margin is {margin}')
else:
    print(f'Minus margin {margin}')


profitability = margin / turnover
workers = int(input('Workers \n'))
profit_on_one = margin/workers
print(f'Your profit on one is {int(profit_on_one)}')


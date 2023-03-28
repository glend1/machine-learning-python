import pandas as pd

dataFrame = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
                          'Sue': ['Pretty good.', 'Bland.']},
                         index=['Product A', 'Product B'])
# print(dataFrame)
series = pd.Series([1, 2, 3, 4, 5])
# print(series)
sales = pd.Series([30, 35, 40], index=['2015 Sales',
                  '2016 Sales', '2017 Sales'], name='Product A')
# print(sales)
wine_reviews = pd.read_csv("melb_data.csv", index_col=0)
# print(wine_reviews.shape)
# print(wine_reviews.head())
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
# print(fruits)
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                           index=['2017 Sales', '2018 Sales'])
# print(fruit_sales)
quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')
print(recipe)

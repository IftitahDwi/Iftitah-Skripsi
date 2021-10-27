import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def call_calc(data_set, support, confidence):
  te = TransactionEncoder()
  te_ary = te.fit(data_set).transform(data_set)
  df = pd.DataFrame(te_ary, columns=te.columns_)
  frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)
  rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
  rules["antecedents"] = rules["antecedents"].apply(lambda x: ','.join(list(x))).astype("unicode")
  rules["consequents"] = rules["consequents"].apply(lambda x: ','.join(list(x))).astype("unicode")
  result = rules.to_dict('records')
  return result
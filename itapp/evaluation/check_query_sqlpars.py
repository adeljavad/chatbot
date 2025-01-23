import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML

def analyze_query(query):
    parsed = sqlparse.parse(query)
    stmt = parsed[0]

    join_count = 0
    groupby_count = 0
    where_count = 0
    nested_query_count = 0
    hallucination = False

    for token in stmt.tokens:
        if token.ttype is DML and token.value.upper() == 'SELECT':
            continue
        if token.ttype is Keyword and token.value.upper() == 'JOIN':
            join_count += 1
        if token.ttype is Keyword and token.value.upper() == 'GROUP BY':
            groupby_count += 1
        if token.ttype is Keyword and token.value.upper() == 'WHERE':
            where_count += 1
        if token.ttype is Keyword and token.value.upper() == 'SELECT':
            nested_query_count += 1

    # Check for hallucination (non-existent tables or columns)
    # This part requires a connection to the database to verify table and column names
    # For simplicity, we assume a list of valid tables and columns
    valid_tables = ['table1', 'table2']
    valid_columns = ['column1', 'column2']

    for token in stmt.tokens:
        if isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                if identifier.get_real_name() not in valid_columns:
                    hallucination = True
        elif isinstance(token, Identifier):
            if token.get_real_name() not in valid_tables and token.get_real_name() not in valid_columns:
                hallucination = True

    return {
        'parsed' : parsed,
        'join_count': join_count,
        'groupby_count': groupby_count,
        'where_count': where_count,
        'nested_query_count': nested_query_count,
        'hallucination': hallucination
    }

query = "SELECT  FROM table3 JOIN table2 ON table1.id = table2.id WHERE table1.column1 = 'value' GROUP BY table1.column1"
result = analyze_query(query)
print(result)

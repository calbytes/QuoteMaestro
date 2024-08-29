class PSQL_QUERIES:

    SELECT_ALL_QUOTES = '''
        SELECT * 
        FROM quotes;
    '''
    
    PSQL_RESET_SELECTED = '''
        UPDATE your_table
        SET selected = TRUE
        WHERE selected = FALSE;
    '''

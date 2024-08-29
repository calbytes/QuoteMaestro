class PSQL_QUERIES:

    SELECT_ALL_QUOTES = '''
        SELECT * 
        FROM quotes;
    '''

    UPDATE_QUOTE = '''
        UPDATE quotes
        SET quote = %s, selected = false
        WHERE id = %s; 
    '''
    
    PSQL_RESET_SELECTED = '''
        UPDATE your_table
        SET selected = TRUE
        WHERE selected = FALSE;
    '''

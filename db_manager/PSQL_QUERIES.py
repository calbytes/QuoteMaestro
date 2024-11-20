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

    INSERT_QUOTE = '''
        INSERT INTO quotes
        (quote, author, title, page, selected)
        VALUES
        (%s, %s, %s, %s, %s)
    '''
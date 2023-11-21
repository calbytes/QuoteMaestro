import quote_updater.update_selected_quote as qu

def generate_selected_quote():
    id = qu.select_quote_id()
    qu.update_selected_quotes(id)


if __name__ == '__main__':
    generate_selected_quote()

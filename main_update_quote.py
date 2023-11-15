import quote_updater.quote_selector as qs

def get_random_quote_entry():
    quote_entry = qs.select_quote_entry()


if __name__ == '__main__':
    get_random_quote_entry()
    print('qm_app() finished')